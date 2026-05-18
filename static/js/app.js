const imageInput = document.querySelector("#imageInput");
const dropZone = document.querySelector("#dropZone");
const browseButton = document.querySelector("#browseButton");
const cameraButton = document.querySelector("#cameraButton");
const previewPanel = document.querySelector("#previewPanel");
const previewImage = document.querySelector("#previewImage");
const validationMessage = document.querySelector("#validationMessage");
const detectButton = document.querySelector("#detectButton");
const detectButtonText = document.querySelector("#detectButtonText");
const clearButton = document.querySelector("#clearButton");
const inlineResult = document.querySelector("#inlineResult");
const siteHeader = document.querySelector(".site-header");

const cameraModal = document.querySelector("#cameraModal");
const cameraVideo = document.querySelector("#cameraVideo");
const cameraCanvas = document.querySelector("#cameraCanvas");
const cameraStatus = document.querySelector("#cameraStatus");
const captureButton = document.querySelector("#captureButton");

let selectedFile = null;
let cameraStream = null;

const allowedTypes = ["image/jpeg", "image/png", "image/webp"];

function setMessage(message) {
  validationMessage.textContent = message || "";
}

function setLoading(isLoading) {
  detectButton.disabled = isLoading || !selectedFile;
  detectButton.classList.toggle("loading", isLoading);
  detectButtonText.textContent = isLoading ? t("upload.analyzing") : t("upload.analyze");
}

function validateFile(file) {
  if (!file) {
    return t("upload.err.choose");
  }
  if (!allowedTypes.includes(file.type)) {
    return t("upload.err.type");
  }
  if (file.size > 8 * 1024 * 1024) {
    return t("upload.err.size");
  }
  return "";
}

function showPreview(file) {
  const reader = new FileReader();
  reader.onload = () => {
    previewImage.src = reader.result;
    previewPanel.classList.remove("hidden");
  };
  reader.readAsDataURL(file);
}

function selectFile(file) {
  const error = validateFile(file);
  if (error) {
    setMessage(error);
    return;
  }

  selectedFile = file;
  setMessage("");
  showPreview(file);
  detectButton.disabled = false;
  clearButton.disabled = false;
  inlineResult.classList.add("hidden");
}

function clearSelection() {
  selectedFile = null;
  imageInput.value = "";
  previewImage.src = "";
  previewPanel.classList.add("hidden");
  detectButton.disabled = true;
  clearButton.disabled = true;
  inlineResult.classList.add("hidden");
  setMessage("");
}

function setCameraStatus(key) {
  if (cameraStatus) {
    cameraStatus.textContent = t(key);
    cameraStatus.classList.remove("hidden");
  }
}

async function openCameraModal() {
  if (!cameraModal || !navigator.mediaDevices?.getUserMedia) {
    setMessage(t("camera.err.unavailable"));
    return;
  }

  cameraModal.classList.remove("hidden");
  document.body.classList.add("modal-open");
  captureButton.disabled = true;
  cameraVideo.classList.add("hidden");
  setCameraStatus("camera.requesting");

  try {
    cameraStream = await navigator.mediaDevices.getUserMedia({
      video: {
        facingMode: { ideal: "environment" },
        width: { ideal: 1280 },
        height: { ideal: 720 },
      },
      audio: false,
    });

    cameraVideo.srcObject = cameraStream;
    await cameraVideo.play();
    cameraVideo.classList.remove("hidden");
    cameraStatus.classList.add("hidden");
    captureButton.disabled = false;
  } catch (error) {
    cameraVideo.classList.add("hidden");
    captureButton.disabled = true;

    if (error.name === "NotAllowedError" || error.name === "PermissionDeniedError") {
      setCameraStatus("camera.err.denied");
    } else if (error.name === "NotFoundError" || error.name === "DevicesNotFoundError") {
      setCameraStatus("camera.err.unavailable");
    } else {
      setCameraStatus("camera.err.failed");
    }
  }
}

function closeCameraModal() {
  if (cameraStream) {
    cameraStream.getTracks().forEach((track) => track.stop());
    cameraStream = null;
  }
  if (cameraVideo) {
    cameraVideo.srcObject = null;
  }
  if (cameraModal) {
    cameraModal.classList.add("hidden");
  }
  document.body.classList.remove("modal-open");
}

function captureFromCamera() {
  if (!cameraVideo.videoWidth) {
    return;
  }

  const context = cameraCanvas.getContext("2d");
  cameraCanvas.width = cameraVideo.videoWidth;
  cameraCanvas.height = cameraVideo.videoHeight;
  context.drawImage(cameraVideo, 0, 0);

  cameraCanvas.toBlob(
    (blob) => {
      if (!blob) {
        setMessage(t("camera.err.failed"));
        closeCameraModal();
        return;
      }
      const file = new File([blob], `leaf-${Date.now()}.jpg`, { type: "image/jpeg" });
      closeCameraModal();
      selectFile(file);
    },
    "image/jpeg",
    0.92,
  );
}

imageInput.addEventListener("change", (event) => {
  selectFile(event.target.files[0]);
});

browseButton.addEventListener("click", (event) => {
  event.preventDefault();
  event.stopPropagation();
  imageInput.click();
});

cameraButton.addEventListener("click", (event) => {
  event.preventDefault();
  event.stopPropagation();
  openCameraModal();
});

captureButton?.addEventListener("click", captureFromCamera);

cameraModal?.querySelectorAll("[data-camera-close]").forEach((element) => {
  element.addEventListener("click", closeCameraModal);
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && cameraModal && !cameraModal.classList.contains("hidden")) {
    closeCameraModal();
  }
});

dropZone.addEventListener("click", (event) => {
  if (event.target.closest("button")) {
    return;
  }
  imageInput.click();
});

["dragenter", "dragover"].forEach((eventName) => {
  dropZone.addEventListener(eventName, (event) => {
    event.preventDefault();
    dropZone.classList.add("dragging");
  });
});

["dragleave", "drop"].forEach((eventName) => {
  dropZone.addEventListener(eventName, (event) => {
    event.preventDefault();
    dropZone.classList.remove("dragging");
  });
});

dropZone.addEventListener("drop", (event) => {
  selectFile(event.dataTransfer.files[0]);
});

clearButton.addEventListener("click", (event) => {
  event.preventDefault();
  event.stopPropagation();
  clearSelection();
});

detectButton.addEventListener("click", async (event) => {
  event.preventDefault();
  event.stopPropagation();

  const error = validateFile(selectedFile);
  if (error) {
    setMessage(error);
    return;
  }

  const formData = new FormData();
  formData.append("image", selectedFile);
  setLoading(true);
  setMessage("");

  try {
    const response = await fetch(`/api/detect?${apiLangQuery()}`, {
      method: "POST",
      body: formData,
    });
    const data = await response.json();

    if (!response.ok || !data.success) {
      setMessage(data.error || t("upload.err.fail"));
      return;
    }

    renderInlineResult(data);
    window.setTimeout(() => {
      window.location.href = `/result/${data.session_id}`;
    }, 900);
  } catch (error) {
    setMessage(t("upload.err.network"));
  } finally {
    setLoading(false);
  }
});

function renderInlineResult(data) {
  inlineResult.classList.remove("hidden");
  inlineResult.innerHTML = `
    <p class="eyebrow">${escapeHtml(t("upload.ready"))}</p>
    <h3>${escapeHtml(data.disease)}</h3>
    <p>${Number(data.confidence).toFixed(2)}% ${escapeHtml(t("result.confidence"))} — ${escapeHtml(data.severity)} ${escapeHtml(t("result.severity"))}</p>
    <div class="confidence-list">
      ${renderConfidenceRows(data.top_predictions)}
    </div>
  `;
  inlineResult.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

function renderConfidenceRows(items) {
  return (items || []).map((item) => `
    <div class="confidence-row">
      <strong>${escapeHtml(cleanLabel(item.label))}</strong>
      <div class="bar"><span style="width:${Number(item.confidence).toFixed(2)}%"></span></div>
      <span>${Number(item.confidence).toFixed(2)}%</span>
    </div>
  `).join("");
}

function cleanLabel(label) {
  return String(label || "").replace("Tomato___", "").replaceAll("_", " ");
}

function escapeHtml(value) {
  return String(value || "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

if (siteHeader && document.body.classList.contains("page-home")) {
  const onScroll = () => {
    siteHeader.classList.toggle("scrolled", window.scrollY > 48);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
}

document.addEventListener("leafscan:langchange", () => {
  if (detectButton && !detectButton.classList.contains("loading")) {
    detectButtonText.textContent = t("upload.analyze");
  }
  if (cameraModal && !cameraModal.classList.contains("hidden") && cameraStream && cameraStatus?.classList.contains("hidden")) {
    /* live camera — no status text */
  } else if (cameraModal && !cameraModal.classList.contains("hidden") && cameraStatus && !cameraStatus.classList.contains("hidden")) {
    const text = cameraStatus.textContent;
    const keys = ["camera.requesting", "camera.err.denied", "camera.err.unavailable", "camera.err.failed"];
    const match = keys.find((key) => text === I18N.en[key] || text === I18N.hi[key]);
    if (match) {
      setCameraStatus(match);
    }
  }
});
