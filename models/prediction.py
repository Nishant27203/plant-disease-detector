from __future__ import annotations

from datetime import datetime, timezone

from database.extensions import db
from services.disease_service import get_disease_details, normalize_lang, resolve_disease_key


class Prediction(db.Model):
    __tablename__ = "predictions"

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(64), unique=True, nullable=False, index=True)
    image_path = db.Column(db.String(255), nullable=False)
    gradcam_path = db.Column(db.String(255), nullable=True)
    disease_key = db.Column(db.String(120), nullable=True)
    disease_name = db.Column(db.String(120), nullable=False)
    confidence_score = db.Column(db.Float, nullable=False)
    severity = db.Column(db.String(32), nullable=False)
    treatment = db.Column(db.Text, nullable=False)
    solution = db.Column(db.Text, nullable=False)
    recommendation_snapshot = db.Column(db.JSON, nullable=True)
    top_predictions = db.Column(db.JSON, nullable=False, default=list)
    prediction_time = db.Column(db.Float, nullable=False)
    created_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    def to_dict(self, lang: str = "en") -> dict:
        lang = normalize_lang(lang)
        details = self._localized_details(lang)

        return {
            "id": self.id,
            "session_id": self.session_id,
            "image_path": self.image_path,
            "gradcam_image": self.gradcam_path,
            "disease_key": self.disease_key,
            "disease": details.get("name", self.disease_name),
            "disease_name": details.get("name", self.disease_name),
            "confidence": round(self.confidence_score, 2),
            "confidence_score": round(self.confidence_score, 2),
            "severity": details.get("severity", self.severity),
            "treatment": details.get("treatment", self.treatment),
            "solution": details.get("solution", self.solution),
            "symptoms": details.get("symptoms", ""),
            "medicines": details.get("medicines", []),
            "organic": details.get("organic", []),
            "prevention": details.get("prevention", []),
            "when_to_apply": details.get("when_to_apply", ""),
            "safety": details.get("safety", ""),
            "expert_note": details.get("expert_note", ""),
            "lang": lang,
            "top_predictions": self.top_predictions or [],
            "prediction_time": round(self.prediction_time, 4),
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }

    def _localized_details(self, lang: str) -> dict:
        if self.recommendation_snapshot and lang in self.recommendation_snapshot:
            return self.recommendation_snapshot[lang]
        if self.disease_key:
            return get_disease_details(self.disease_key, lang)
        resolved = resolve_disease_key(self.disease_name)
        if resolved:
            return get_disease_details(resolved, lang)
        return {
            "name": self.disease_name,
            "severity": self.severity,
            "treatment": self.treatment,
            "solution": self.solution,
        }
