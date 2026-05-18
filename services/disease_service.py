from __future__ import annotations

from services.disease_data import DISEASE_LIBRARY


SUPPORTED_LANGS = {"en", "hi"}


def normalize_lang(lang: str | None) -> str:
    if not lang:
        return "en"
    code = lang.lower().strip().split("-")[0]
    return code if code in SUPPORTED_LANGS else "en"


def resolve_disease_key(label_or_name: str | None) -> str | None:
    if not label_or_name:
        return None
    if label_or_name in DISEASE_LIBRARY:
        return label_or_name
    normalized = label_or_name.strip().lower()
    for key, entry in DISEASE_LIBRARY.items():
        for lang in SUPPORTED_LANGS:
            if entry[lang]["name"].strip().lower() == normalized:
                return key
    return None


def get_disease_details(label: str, lang: str = "en") -> dict:
    lang = normalize_lang(lang)
    resolved = resolve_disease_key(label) or label
    entry = DISEASE_LIBRARY.get(resolved)

    if not entry:
        readable = label.replace("Tomato___", "").replace("_", " ").strip().title()
        fallback = {
            "name": readable or "Unknown Tomato Condition",
            "severity": "Medium" if lang == "en" else "मध्यम",
            "treatment": "Consult local extension guidance" if lang == "en" else "स्थानीय कृषि विभाग से सलाह लें",
            "solution": (
                "Isolate the plant, monitor symptom spread, and consult a local agriculture expert for confirmation."
                if lang == "en"
                else "पौधे को अलग रखें, लक्षण देखें, और स्थानीय कृषि विशेषज्ञ से पुष्टि कराएँ।"
            ),
            "symptoms": "",
            "medicines": [],
            "organic": [],
            "prevention": [],
            "when_to_apply": "",
            "safety": "",
            "expert_note": "",
        }
        return _pack_details(label, lang, fallback)

    localized = entry[lang]
    severity = entry["severity"][lang]
    payload = {**localized, "severity": severity}
    return _pack_details(resolved, lang, payload)


def get_bilingual_snapshot(label: str) -> dict:
    resolved = resolve_disease_key(label) or label
    return {
        "en": get_disease_details(resolved, "en"),
        "hi": get_disease_details(resolved, "hi"),
    }


def _pack_details(label: str, lang: str, payload: dict) -> dict:
    return {
        "disease_key": label,
        "lang": lang,
        "name": payload.get("name", ""),
        "severity": payload.get("severity", ""),
        "treatment": payload.get("treatment", ""),
        "solution": payload.get("solution", ""),
        "symptoms": payload.get("symptoms", ""),
        "medicines": payload.get("medicines", []),
        "organic": payload.get("organic", []),
        "prevention": payload.get("prevention", []),
        "when_to_apply": payload.get("when_to_apply", ""),
        "safety": payload.get("safety", ""),
        "expert_note": payload.get("expert_note", ""),
    }
