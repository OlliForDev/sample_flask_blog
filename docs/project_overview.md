# Projektübersicht

## Metadaten

- projekt_pfad: `/Users/rechenzentrum/Dev/bsc_SWE/DLBSEPDOCD01_D/sample_flask_blog`
- erstellt_am: 2026-10-22 22:59:08
- anzahl_dateien: 21
- anzahl_zeilen_gesamt: 1262

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
│   ├── workflows
│   │   └── ci.yml
│   └── .DS_Store
├── migrations
│   ├── 001_create_posts.py
│   └── 002_add_created_at.py
├── src
│   ├── blog
│   │   ├── templates
│   │   │   ├── index.html
│   │   │   └── new.html
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── db.py
│   │   └── validation.py
│   ├── instance
│   └── .DS_Store
├── tests
│   ├── conftest.py
│   ├── test_app.py
│   ├── test_migrations.py
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

9 directories, 26 files
```

## Dateibeschreibungen

### `.dockerignore`

- **Typ:** Datei (ohne Erweiterung)
- **Zeilen:** 0

### `.gitignore`

- **Typ:** Datei (ohne Erweiterung)
- **Zeilen:** 17
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
- **Zeilen:** 25
- **Erste Inhaltszeile:** FROM python:3.13-slim

### `README.md`

- **Typ:** Markdown-Dokumentation
- **Zeilen:** 94
- **Erste Inhaltszeile:** # Sample Flask Blog

### `migrations/001_create_posts.py`

- **Typ:** Python-Modul
- **Zeilen:** 14
- **Imports:** from yoyo import step

### `migrations/002_add_created_at.py`

- **Typ:** Python-Modul
- **Zeilen:** 11
- **Imports:** from yoyo import step

### `pyproject.toml`

- **Typ:** TOML-Konfiguration
- **Zeilen:** 44
- **Erste Inhaltszeile:** [project]

### `src/blog/__init__.py`

- **Typ:** Python-Modul
- **Zeilen:** 3
- **Imports:** from app import create_app

### `src/blog/app.py`

- **Typ:** Python-Modul
- **Zeilen:** 62
- **Imports:** os, from contextlib import closing, from flask import Flask, redirect, render_template, request, url_for, from db import get_connection, from validation import validate_post
- **Funktionen:** create_app, main, index, new_post, create_post

### `src/blog/db.py`

- **Typ:** Python-Modul
- **Zeilen:** 18
- **Imports:** sqlite3, from pathlib import Path
- **Funktionen:** get_db_path, get_connection

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
- **Zeilen:** 34
- **Imports:** pytest, from yoyo import get_backend, read_migrations, from blog.app import create_app
- **Funktionen:** apply_migrations, app, client

### `tests/test_app.py`

- **Typ:** Python-Modul
- **Zeilen:** 18
- **Funktionen:** test_startseite, test_neuer_post, test_post_erstellen

### `tests/test_migrations.py`

- **Typ:** Python-Modul
- **Zeilen:** 38
- **Imports:** from contextlib import closing, from yoyo import get_backend, read_migrations, from blog.db import get_connection
- **Funktionen:** test_leere_datenbank_kann_migriert_werden, test_erneute_migration_erhaelt_daten

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
- **Zeilen:** 571
- **Erste Inhaltszeile:** version = 1
