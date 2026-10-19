import pytest

from blog.validation import validate_post


@pytest.mark.parametrize(
    ("title", "content", "expected"),
    [
        pytest.param(
            "Titel",
            "Inhalt",
            ("Titel", "Inhalt"),
            id="gueltige-eingabe",
        ),
        pytest.param(
            "  Titel  ",
            "  Inhalt  ",
            ("Titel", "Inhalt"),
            id="aeussere-leerzeichen",
        ),
        pytest.param(
            "\tTitel\n",
            "\nInhalt\t",
            ("Titel", "Inhalt"),
            id="tabs-und-zeilenumbrueche",
        ),
        pytest.param(
            "Mein erster Post",
            "Ein Text\nmit zweiter Zeile.",
            ("Mein erster Post", "Ein Text\nmit zweiter Zeile."),
            id="innere-formatierung-bleibt-erhalten",
        ),
        pytest.param(
            "Grüße",
            "Äpfel, Öl und überraschende Neuigkeiten.",
            ("Grüße", "Äpfel, Öl und überraschende Neuigkeiten."),
            id="umlaute",
        ),
    ],
)
def test_validate_post_normalisiert_gueltige_eingaben(title, content, expected):
    result = validate_post(title, content)

    assert result == expected


@pytest.mark.parametrize(
    ("title", "content"),
    [
        pytest.param("", "Inhalt", id="titel-fehlt"),
        pytest.param("Titel", "", id="inhalt-fehlt"),
        pytest.param("", "", id="beide-felder-fehlen"),
        pytest.param("   ", "Inhalt", id="titel-nur-leerzeichen"),
        pytest.param("Titel", "   ", id="inhalt-nur-leerzeichen"),
        pytest.param("\t\n", "Inhalt", id="titel-nur-whitespace"),
        pytest.param("Titel", "\t\n", id="inhalt-nur-whitespace"),
    ],
)
def test_validate_post_lehnt_leere_pflichtfelder_ab(title, content):
    with pytest.raises(ValueError, match="Titel und Inhalt"):
        validate_post(title, content)
