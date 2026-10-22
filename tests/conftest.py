import pytest
from yoyo import get_backend, read_migrations

from blog.app import create_app


def apply_migrations(database_url: str) -> None:
    backend = get_backend(database_url)
    migrations = read_migrations("migrations")

    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))


@pytest.fixture
def app(tmp_path):
    database_path = tmp_path / "test_blog.db"
    database_url = f"sqlite:///{database_path}"

    apply_migrations(database_url)

    app = create_app(
        test_config={
            "DATABASE": str(database_path),
            "TESTING": True,
        }
    )

    yield app


@pytest.fixture
def client(app):
    return app.test_client()
