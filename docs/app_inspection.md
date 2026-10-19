# Dateiinspektion

## Dateidetails

## `/Users/rechenzentrum/Dev/bsc_SWE/DLBSEPDOCD01_D/sample_flask_blog/app.py`

- **Typ:** Python-Modul
- **Zeilen:** 111
- **Pfad:** `/Users/rechenzentrum/Dev/bsc_SWE/DLBSEPDOCD01_D/sample_flask_blog/app.py`
- **Modulbeschreibung:** Einfache Flask-Blog-Anwendung mit SQLite.  Bietet: - Startseite mit Liste aller Blogposts (neueste zuerst) - Formularseite zum Erstellen neuer Posts - Speicherung der Posts in einer SQLite-Datenbank (blog.db)
- **Imports:** from flask import Flask, render_template, request, redirect, sqlite3
- **Funktionen:** init_db, index, new_post, create_post

### Inhaltsvorschau

```py
"""
Einfache Flask-Blog-Anwendung mit SQLite.

Bietet:
- Startseite mit Liste aller Blogposts (neueste zuerst)
- Formularseite zum Erstellen neuer Posts
- Speicherung der Posts in einer SQLite-Datenbank (blog.db)
"""

from flask import Flask, render_template, request, redirect
import sqlite3


# Flask-Anwendung initialisieren
app = Flask(__name__)


def init_db():
    """
    Initialisiert die SQLite-Datenbank für den Blog.

    Legt die Tabelle 'posts' an, falls sie noch nicht existiert.
    Die Tabelle enthält:
    - id: INTEGER PRIMARY KEY AUTOINCREMENT
    - title: TEXT NOT NULL
    - content: TEXT NOT NULL

    Die Datenbankdatei 'blog.db' wird im aktuellen Verzeichnis erstellt,
    falls sie nicht existiert.
    """
    conn = sqlite3.connect("blog.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()


# Datenbank beim Start der Anwendung einmalig initialisieren
init_db()


@app.route("/")
def index():
    """
    Rendert die Startseite des Blogs.

    Ruft alle Blogposts aus der Datenbank ab (sortiert nach id absteigend)
    und übergibt sie an das Template 'index.html'.

    Returns:
        Gerendertes HTML der Startseite mit der Liste der Posts.
    """
    conn = sqlite3.connect("blog.db")
    cur = conn.cursor()
    cur.execute("SELECT id, title, content FROM posts ORDER BY id DESC")
    posts = cur.fetchall()
    conn.close()

    return render_template("index.html", posts=posts)


@app.route("/new")
def new_post():
    """
    Rendert die Seite zum Erstellen eines neuen Blogposts.

    Zeigt ein Formular mit Feldern für Titel und Inhalt an.

    Returns:
        Gerendertes HTML der 'new.html'-Seite mit dem Erstellungsformular.
    """
    return render_template("new.html")


@app.route("/create", methods=["POST"])
def create_post():
    """
    Verarbeitet das Absenden des Formulars zum Erstellen eines neuen Posts.

    Liest die Felder 'title' und 'content' aus dem POST-Request,
    fügt einen neuen Eintrag in die Tabelle 'posts' ein und leitet
    anschließend auf die Startseite weiter.

    Returns:
        HTTP-Redirect auf die Startseite ("/").
    """
    title = request.form["title"]
    content = request.form["content"]

    conn = sqlite3.connect("blog.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO posts (title, content) VALU
```

---
