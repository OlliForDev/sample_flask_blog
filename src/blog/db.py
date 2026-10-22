import sqlite3
from pathlib import Path


def get_db_path(app):
    db_path = app.config.get("DATABASE")

    if not db_path:
        db_path = Path(app.instance_path) / "blog.db"

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    return db_path


def get_connection(app):
    connection = sqlite3.connect(get_db_path(app))
    connection.row_factory = sqlite3.Row
    return connection
