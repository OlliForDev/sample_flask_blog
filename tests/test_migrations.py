from contextlib import closing

from yoyo import get_backend, read_migrations

from blog.db import get_connection


def test_leere_datenbank_kann_migriert_werden(app):
    with closing(get_connection(app)) as connection:
        tables = {
            row["name"]
            for row in connection.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table'"
            ).fetchall()
        }

    assert "posts" in tables


def test_erneute_migration_erhaelt_daten(app):
    with closing(get_connection(app)) as connection:
        connection.execute(
            "INSERT INTO posts (title, content) VALUES (?, ?)",
            ("Bleibender Beitrag", "Inhalt"),
        )
        connection.commit()

    database_url = f"sqlite:///{app.config['DATABASE']}"
    backend = get_backend(database_url)
    migrations = read_migrations("migrations")

    backend.apply_migrations(backend.to_apply(migrations))

    with closing(get_connection(app)) as connection:
        posts = connection.execute("SELECT title, content FROM posts").fetchall()

    assert len(posts) == 1
    assert posts[0]["title"] == "Bleibender Beitrag"
