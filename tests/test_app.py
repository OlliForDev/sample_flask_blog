def test_startseite(client):
    response = client.get("/")
    assert response.status_code == 200


def test_neuer_post(client):
    response = client.get("/new")
    assert response.status_code == 200


def test_post_erstellen(client):
    response = client.post(
        "/create",
        data={"title": "Test", "content": "Inhalt"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Test" in response.data
