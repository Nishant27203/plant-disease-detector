from __future__ import annotations

import cv2
import numpy as np

from services.image_service import ImageInput, ImageService


class GradCAMService:
    """Occlusion-based class saliency (Grad-CAM–style overlay) for ONNX classifiers."""

    def __init__(self, config: dict):
        self.gradcam_folder = config["GRADCAM_FOLDER"]
        self.grid_size = max(4, int(config["GRADCAM_GRID_SIZE"]))
        self.max_patches = max(64, int(config["GRADCAM_MAX_PATCHES"]))
        self.batch_chunk = max(8, int(config["GRADCAM_BATCH_CHUNK"]))
        self.image_service = ImageService(config)

    def generate(self, model_service, image_input: ImageInput, target_index: int, session_id: str) -> str:
        heatmap = self._occlusion_heatmap(model_service, image_input.processed_rgb, target_index)
        heatmap = cv2.resize(heatmap, (image_input.original_rgb.shape[1], image_input.original_rgb.shape[0]))
        heatmap_uint8 = np.uint8(255 * heatmap)
        color_map = cv2.applyColorMap(heatmap_uint8, cv2.COLORMAP_JET)
        color_map = cv2.cvtColor(color_map, cv2.COLOR_BGR2RGB)
        overlay = cv2.addWeighted(image_input.original_rgb, 0.62, color_map, 0.38, 0)

        output_name = f"{session_id}_gradcam.jpg"
        output_path = self.gradcam_folder / output_name
        cv2.imwrite(str(output_path), cv2.cvtColor(overlay, cv2.COLOR_RGB2BGR), [cv2.IMWRITE_JPEG_QUALITY, 92])
        return f"gradcam/{output_name}"

    @staticmethod
    def _cover_positions(dim: int, patch: int, stride: int) -> list[int]:
        if dim <= patch:
            return [0]
        positions: list[int] = []
        p = 0
        last = dim - patch
        while p <= last:
            positions.append(p)
            p += stride
        if not positions:
            return [0]
        if positions[-1] != last:
            positions.append(last)
        # collapse duplicates while preserving order
        deduped: list[int] = []
        for x in positions:
            if not deduped or x > deduped[-1]:
                deduped.append(x)
        return deduped

    def _patch_stride_for_budget(self, height: int, width: int, patch_h: int, patch_w: int) -> tuple[int, int]:
        stride_h = max(4, patch_h // 2)
        stride_w = max(4, patch_w // 2)

        def count() -> int:
            return len(self._cover_positions(height, patch_h, stride_h)) * len(
                self._cover_positions(width, patch_w, stride_w)
            )

        while count() > self.max_patches and (stride_h < patch_h - 2 or stride_w < patch_w - 2):
            stride_h = min(patch_h - 1, stride_h + max(2, patch_h // 10))
            stride_w = min(patch_w - 1, stride_w + max(2, patch_w // 10))
        # If still too many (very large images), grow stride more aggressively
        while count() > self.max_patches * 2:
            stride_h = min(patch_h - 1, stride_h + 4)
            stride_w = min(patch_w - 1, stride_w + 4)
            if stride_h >= patch_h - 1 and stride_w >= patch_w - 1:
                break
        return stride_h, stride_w

    def _blur_occlusion_canvas(self, processed_rgb: np.ndarray) -> np.ndarray:
        h, w = processed_rgb.shape[:2]
        sigma = float(max(5.0, min(h, w) / 20.0))
        return cv2.GaussianBlur(processed_rgb, (0, 0), sigmaX=sigma, sigmaY=sigma)

    def _occlusion_heatmap(self, model_service, processed_rgb: np.ndarray, target_index: int) -> np.ndarray:
        height, width, _ = processed_rgb.shape
        baseline_prob = float(model_service.predict_probabilities(self.image_service.to_model_tensor(processed_rgb))[target_index])
        baseline_prob = max(baseline_prob, 1e-9)
        log_baseline = float(np.log(baseline_prob))

        # Patch size from grid fineness; overlapping windows sharpen attribution on all leaf sizes.
        patch_h = max(12, height // max(6, min(self.grid_size, 16)))
        patch_w = max(12, width // max(6, min(self.grid_size, 16)))
        patch_h = min(patch_h, height)
        patch_w = min(patch_w, width)

        stride_h, stride_w = self._patch_stride_for_budget(height, width, patch_h, patch_w)
        ys = self._cover_positions(height, patch_h, stride_h)
        xs = self._cover_positions(width, patch_w, stride_w)

        blurred = self._blur_occlusion_canvas(processed_rgb)

        locations: list[tuple[int, int, int, int]] = []
        for y in ys:
            y2 = min(y + patch_h, height)
            y1 = y2 - patch_h
            for x in xs:
                x2 = min(x + patch_w, width)
                x1 = x2 - patch_w
                locations.append((y1, y2, x1, x2))

        occluded_tensors: list[np.ndarray] = []
        for y1, y2, x1, x2 in locations:
            modified = processed_rgb.copy()
            modified[y1:y2, x1:x2] = blurred[y1:y2, x1:x2]
            occluded_tensors.append(self.image_service.to_model_tensor(modified)[0])

        scores = self._run_batched(model_service, occluded_tensors, target_index)

        # Positive when occlusion lowers confidence for the predicted class (region matters).
        log_scores = np.log(np.maximum(scores.astype(np.float64), 1e-12))
        importance = np.maximum(0.0, log_baseline - log_scores)

        acc = np.zeros((height, width), dtype=np.float32)
        wsum = np.zeros((height, width), dtype=np.float32)
        for value, (y1, y2, x1, x2) in zip(importance, locations):
            acc[y1:y2, x1:x2] += float(value)
            wsum[y1:y2, x1:x2] += 1.0

        coarse = np.divide(acc, np.maximum(wsum, 1e-6))

        if float(np.max(coarse)) <= 1e-10:
            gray = cv2.cvtColor(processed_rgb, cv2.COLOR_RGB2GRAY).astype(np.float32)
            gx = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
            gy = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)
            coarse = np.sqrt(gx * gx + gy * gy)
            coarse -= float(np.min(coarse))
            m = float(np.max(coarse))
            if m > 0:
                coarse /= m
            return coarse

        # Light edge-preserving smooth before contrast stretch (scale-adaptive, not fixed sigma=9).
        sigma = float(max(1.2, min(height, width) / 42.0))
        coarse = cv2.GaussianBlur(coarse, (0, 0), sigmaX=sigma, sigmaY=sigma)

        lo, hi = np.percentile(coarse, [1.5, 98.5])
        coarse = np.clip((coarse - lo) / (hi - lo + 1e-8), 0.0, 1.0)
        return coarse.astype(np.float32)

    def _run_batched(self, model_service, occluded_tensors: list[np.ndarray], target_index: int) -> np.ndarray:
        if not occluded_tensors:
            return np.array([], dtype=np.float32)
        chunk = self.batch_chunk
        parts: list[np.ndarray] = []
        for i in range(0, len(occluded_tensors), chunk):
            batch = np.stack(occluded_tensors[i : i + chunk], axis=0)
            try:
                probs = model_service.predict_batch_probabilities(batch)[:, target_index]
            except Exception:
                probs = np.array(
                    [
                        model_service.predict_probabilities(np.expand_dims(t, axis=0))[target_index]
                        for t in occluded_tensors[i : i + chunk]
                    ],
                    dtype=np.float32,
                )
            parts.append(np.asarray(probs, dtype=np.float32))
        return np.concatenate(parts, axis=0)
