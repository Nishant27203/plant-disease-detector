from __future__ import annotations

from sqlalchemy import inspect, text

from database.extensions import db


def ensure_prediction_schema() -> None:
    """Add newer columns on existing SQLite databases without a full migration tool."""
    inspector = inspect(db.engine)
    if "predictions" not in inspector.get_table_names():
        return

    columns = {column["name"] for column in inspector.get_columns("predictions")}
    statements: list[str] = []

    if "disease_key" not in columns:
        statements.append("ALTER TABLE predictions ADD COLUMN disease_key VARCHAR(120)")
    if "recommendation_snapshot" not in columns:
        statements.append("ALTER TABLE predictions ADD COLUMN recommendation_snapshot JSON")

    for statement in statements:
        db.session.execute(text(statement))
    if statements:
        db.session.commit()
