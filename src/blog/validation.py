def validate_post(title: str, content: str) -> tuple[str, str]:
    """Normalisiert Eingaben und lehnt leere Pflichtfelder ab."""
    title = title.strip()
    content = content.strip()

    if not title or not content:
        raise ValueError("Titel und Inhalt dürfen nicht leer sein.")

    return title, content
