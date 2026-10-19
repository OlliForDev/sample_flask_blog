import pytest

from blog.app import create_app


@pytest.fixture
def app(tmp_path):
    app = create_app(
        test_config={
            "DATABASE": str(tmp_path / "test_blog.db"),
            "TESTING": True,
        }
    )

    yield app


@pytest.fixture
def client(app):
    return app.test_client()
