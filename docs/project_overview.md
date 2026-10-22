# Projektübersicht

## Metadaten

- projekt_pfad: `/Users/rechenzentrum/Dev/bsc_SWE/DLBSEPDOCD01_D/sample_flask_blog`
- erstellt_am: 2026-10-21 09:29:49
- anzahl_dateien: 18
- anzahl_zeilen_gesamt: 1136

## Einstiegspunkte

- `src/blog/app.py`

## Konfigurationsdateien

- `Dockerfile`
- `README.md`
- `pyproject.toml`

## Dokumentation

- `README.md`

## Projektstruktur

```text
/Users/rechenzentrum/Dev/bsc_SWE/DLBSEPDOCD01_D/sample_flask_blog
├── .github
│   └── workflows
│       └── ci.yml
├── src
│   ├── blog
│   │   ├── templates
│   │   │   ├── index.html
│   │   │   └── new.html
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── db.py
│   │   └── validation.py
│   └── instance
├── tests
│   ├── conftest.py
│   ├── test_app.py
│   ├── test_post_routes.py
│   └── test_validation.py
├── .coverage
├── .dockerignore
├── .DS_Store
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── Dockerfile
├── pyproject.toml
├── README.md
└── uv.lock

8 directories, 21 files
```

## Dateibeschreibungen

### `.dockerignore`

- **Typ:** Datei (ohne Erweiterung)
- **Zeilen:** 0

### `.gitignore`

- **Typ:** Datei (ohne Erweiterung)
- **Zeilen:** 13
- **Erste Inhaltszeile:** .venv/

### `.pre-commit-config.yaml`

- **Typ:** YAML-Konfiguration
- **Zeilen:** 16
- **Erste Inhaltszeile:** repos:

### `.python-version`

- **Typ:** Datei (ohne Erweiterung)
- **Zeilen:** 1
- **Erste Inhaltszeile:** 3.13

### `Dockerfile`

- **Typ:** Docker-Konfiguration
- **Zeilen:** 24
- **Erste Inhaltszeile:** FROM python:3.13-slim

### `README.md`

- **Typ:** Markdown-Dokumentation
- **Zeilen:** 94
- **Erste Inhaltszeile:** # Sample Flask Blog

### `pyproject.toml`

- **Typ:** TOML-Konfiguration
- **Zeilen:** 40
- **Erste Inhaltszeile:** [project]

### `src/blog/__init__.py`

- **Typ:** Python-Modul
- **Zeilen:** 3
- **Imports:** from app import create_app

### `src/blog/app.py`

- **Typ:** Python-Modul
- **Zeilen:** 63
- **Imports:** from contextlib import closing, from flask import Flask, redirect, render_template, request, url_for, from db import get_connection, init_db, from validation import validate_post
- **Funktionen:** create_app, main, index, new_post, create_post

### `src/blog/db.py`

- **Typ:** Python-Modul
- **Zeilen:** 33
- **Imports:** sqlite3, from contextlib import closing, from pathlib import Path
- **Funktionen:** get_db_path, get_connection, init_db

### `src/blog/templates/index.html`

- **Typ:** HTML-Datei
- **Zeilen:** 74
- **Kommentare:** 1 gefunden
  - Startseiten Template für den Mini-Blog mit Region für Posts

### `src/blog/templates/new.html`

- **Typ:** HTML-Datei
- **Zeilen:** 54
- **Kommentare:** 1 gefunden
  - Seite um neue Posts zu erstellen

### `src/blog/validation.py`

- **Typ:** Python-Modul
- **Zeilen:** 9
- **Funktionen:** validate_post
  - `validate_post`: Normalisiert Eingaben und lehnt leere Pflichtfelder ab.

### `tests/conftest.py`

- **Typ:** Python-Modul
- **Zeilen:** 20
- **Imports:** pytest, from blog.app import create_app
- **Funktionen:** app, client

### `tests/test_app.py`

- **Typ:** Python-Modul
- **Zeilen:** 18
- **Funktionen:** test_startseite, test_neuer_post, test_post_erstellen

### `tests/test_post_routes.py`

- **Typ:** Python-Modul
- **Zeilen:** 98
- **Imports:** from contextlib import closing, from urllib.parse import urlsplit, pytest, from blog.db import get_connection
- **Funktionen:** test_create_lehnt_ungueltige_eingaben_ohne_db_aenderung_ab, test_create_speichert_normalisierte_eingaben

### `tests/test_validation.py`

- **Typ:** Python-Modul
- **Zeilen:** 61
- **Imports:** pytest, from blog.validation import validate_post
- **Funktionen:** test_validate_post_normalisiert_gueltige_eingaben, test_validate_post_lehnt_leere_pflichtfelder_ab

### `uv.lock`

- **Typ:** Datei (.lock)
- **Zeilen:** 515
- **Erste Inhaltszeile:** version = 1
