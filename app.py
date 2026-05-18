from __future__ import annotations

import mimetypes
import os
import sys

from flask import Flask

from config import get_config
from database.extensions import db
from routes.api import api_bp
from routes.pages import pages_bp
from services.model_service import ModelService
from utils.error_handlers import register_error_handlers
from utils.logging_config import configure_logging
from utils.security import apply_security_headers


def create_app() -> Flask:
    mimetypes.add_type("application/javascript", ".js")
    mimetypes.add_type("text/css", ".css")

    app = Flask(__name__)
    app.config.from_object(get_config())

    configure_logging(app)
    app.config["UPLOAD_FOLDER"].mkdir(parents=True, exist_ok=True)
    app.config["GRADCAM_FOLDER"].mkdir(parents=True, exist_ok=True)
    app.config["LOG_FOLDER"].mkdir(parents=True, exist_ok=True)
    app.config["DATABASE_FOLDER"].mkdir(parents=True, exist_ok=True)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        app.extensions["model_service"] = ModelService(app.config)

    app.register_blueprint(pages_bp)
    app.register_blueprint(api_bp)
    register_error_handlers(app)
    apply_security_headers(app)

    return app


app = create_app()


if __name__ == "__main__":
    # macOS often binds AirPlay to 5000; local dev defaults to 5001 there.
    default_port = 5001 if sys.platform == "darwin" else 5000
    port = int(os.environ.get("PORT", str(default_port)))
    app.run(host="0.0.0.0", port=port, debug=app.config["DEBUG"])
