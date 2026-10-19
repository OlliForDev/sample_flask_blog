import sqlite3
from contextlib import closing
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


def init_db(app):
    with closing(get_connection(app)) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )
            """
        )
        connection.commit()
