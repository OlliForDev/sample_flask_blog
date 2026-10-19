from contextlib import closing
from urllib.parse import urlsplit

import pytest

from blog.db import get_connection


@pytest.mark.parametrize(
    "form_data",
    [
        pytest.param(
            {"title": "", "content": "Inhalt"},
            id="leerer-titel",
        ),
        pytest.param(
            {"title": "Titel", "content": ""},
            id="leerer-inhalt",
        ),
        pytest.param(
            {"title": "   ", "content": "Inhalt"},
            id="titel-nur-leerzeichen",
        ),
        pytest.param(
            {"title": "Titel", "content": "\t\n"},
            id="inhalt-nur-whitespace",
        ),
        pytest.param(
            {"content": "Inhalt"},
            id="titelfeld-fehlt",
        ),
        pytest.param(
            {"title": "Titel"},
            id="inhaltsfeld-fehlt",
        ),
        pytest.param(
            {},
            id="beide-felder-fehlen",
        ),
    ],
)
def test_create_lehnt_ungueltige_eingaben_ohne_db_aenderung_ab(app, client, form_data):
    with closing(get_connection(app)) as connection:
        connection.execute(
            "INSERT INTO posts (title, content) VALUES (?, ?)",
            ("Vorhandener Post", "Dieser Inhalt bleibt erhalten."),
        )
        connection.commit()

        posts_before = [
            tuple(row)
            for row in connection.execute(
                "SELECT id, title, content FROM posts ORDER BY id"
            ).fetchall()
        ]

    response = client.post(
        "/create",
        data=form_data,
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert urlsplit(response.headers["Location"]).path == "/new"

    with closing(get_connection(app)) as connection:
        posts_after = [
            tuple(row)
            for row in connection.execute(
                "SELECT id, title, content FROM posts ORDER BY id"
            ).fetchall()
        ]

    assert posts_after == posts_before


def test_create_speichert_normalisierte_eingaben(app, client):
    response = client.post(
        "/create",
        data={
            "title": "  Mein Titel  ",
            "content": "\nMein Inhalt\t",
        },
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert urlsplit(response.headers["Location"]).path == "/"

    with closing(get_connection(app)) as connection:
        posts = [
            tuple(row)
            for row in connection.execute(
                "SELECT title, content FROM posts ORDER BY id"
            ).fetchall()
        ]

    assert posts == [("Mein Titel", "Mein Inhalt")]
