# Projektübersicht

## Metadaten

- projekt_pfad: `/Users/rechenzentrum/Dev/bsc_SWE/DLBSEPDOCD01_D/sample_flask_blog`
- erstellt_am: 2026-10-18 13:25:43
- anzahl_dateien: 13
- anzahl_zeilen_gesamt: 608

## Einstiegspunkte

- `src/blog/app.py`

## Konfigurationsdateien

- `README.md`
- `pyproject.toml`
- `requirements.txt`

## Dokumentation

- `README.md`

## Projektstruktur

```text
/Users/rechenzentrum/Dev/bsc_SWE/DLBSEPDOCD01_D/sample_flask_blog
├── src
│   └── blog
│       ├── templates
│       │   ├── index.html
│       │   └── new.html
│       ├── __init__.py
│       ├── app.py
│       └── db.py
├── tests
│   ├── conftest.py
│   └── test_app.py
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
├── requirements.txt
└── uv.lock

5 directories, 13 files
```

## Dateibeschreibungen

### `.gitignore`

- **Typ:** Datei (ohne Erweiterung)
- **Zeilen:** 11
- **Erste Inhaltszeile:** .venv/

### `.python-version`

- **Typ:** Datei (ohne Erweiterung)
- **Zeilen:** 1
- **Erste Inhaltszeile:** 3.13

### `README.md`

- **Typ:** Markdown-Dokumentation
- **Zeilen:** 16
- **Erste Inhaltszeile:** # Sample Flask Blog

### `pyproject.toml`

- **Typ:** TOML-Konfiguration
- **Zeilen:** 25
- **Erste Inhaltszeile:** [project]

### `requirements.txt`

- **Typ:** Datei (.txt)
- **Zeilen:** 4
- **Erste Inhaltszeile:** Flask>=3.0,<4.0

### `src/blog/__init__.py`

- **Typ:** Python-Modul
- **Zeilen:** 3
- **Imports:** from app import create_app

### `src/blog/app.py`

- **Typ:** Python-Modul
- **Zeilen:** 60
- **Imports:** from flask import Flask, redirect, render_template, request, url_for, from db import init_db
- **Funktionen:** create_app, main, index, new_post, create_post, before_request

### `src/blog/db.py`

- **Typ:** Python-Modul
- **Zeilen:** 29
- **Imports:** sqlite3, from pathlib import Path
- **Funktionen:** get_db_path, init_db, get_connection

### `src/blog/templates/index.html`

- **Typ:** HTML-Datei
- **Zeilen:** 49
- **Kommentare:** 1 gefunden
  - Startseiten Template für den Mini-Blog mit Region für Posts

### `src/blog/templates/new.html`

- **Typ:** HTML-Datei
- **Zeilen:** 54
- **Kommentare:** 1 gefunden
  - Seite um neue Posts zu erstellen

### `tests/conftest.py`

- **Typ:** Python-Modul
- **Zeilen:** 30
- **Imports:** pytest, from blog.app import create_app
- **Funktionen:** app, client

### `tests/test_app.py`

- **Typ:** Python-Modul
- **Zeilen:** 18
- **Funktionen:** test_startseite, test_neuer_post, test_post_erstellen

### `uv.lock`

- **Typ:** Datei (.lock)
- **Zeilen:** 308
- **Erste Inhaltszeile:** version = 1
