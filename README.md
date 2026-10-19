# Sample Flask Blog

Mini-Blog-Anwendung als Grundlage für die CI/CD-Fallstudie.

## Teststrategie

Die Testsuite umfasst 23 Testfälle und orientiert sich an der Testpyramide:
Isolierte Unit-Tests prüfen die Validierungslogik, Integrationstests sichern
das Zusammenspiel von Flask-Routen, Validierung und SQLite ab. Ergänzend
prüfen anwendungsnahe Tests zentrale Nutzerabläufe über den Flask-Testclient.

| Testdatei | Testfälle | Schwerpunkt |
|---|---:|---|
| `tests/test_validation.py` | 12 | Validierung und Normalisierung ohne Flask oder Datenbank |
| `tests/test_post_routes.py` | 8 | Formularverarbeitung, Weiterleitungen und Speicherung |
| `tests/test_app.py` | 3 | Startseite, Formular und Erstellen eines Posts |
| Gesamt | 23 | |

Parametrisierte Testfunktionen zählen je Eingabekonstellation als eigener Testfall.

### Unit-Tests

Die Tests für `validate_post()` prüfen:

- Gültige Eingaben sowie den Erhalt von Umlauten und innerer Textformatierung.
- Das Entfernen äußerer Leerzeichen, Tabs und Zeilenumbrüche.
- Die Ablehnung leerer oder ausschließlich aus Whitespace bestehender
  Pflichtfelder durch eine `ValueError`-Exception.

### Integrations- und anwendungsnahe Tests

Die Route-Tests prüfen `POST /create` mit einer echten temporären SQLite-Datenbank:

- Sieben ungültige Eingabekonstellationen: leere oder nur aus Whitespace
  bestehende Felder sowie fehlende Formularfelder.
- Bei Ablehnung: HTTP 302, Weiterleitung nach `/new` und unveränderter
  Datenbestand einschließlich bereits vorhandener Posts.
- Bei gültigen Eingaben: normalisierte Speicherung und Weiterleitung
  auf die Startseite.

Die drei weiteren Anwendungstests prüfen Startseite, Formular und
Post-Erstellung über den Flask-Testclient. Sie sind keine isolierten
Unit-Tests und verwenden keinen echten Browser. Vollständige Nutzerabläufe
können zugleich als automatisierte Akzeptanztests eingeordnet werden.

### Testisolation

Die Fixtures in `tests/conftest.py` erzeugen pro Test eine eigene Anwendung
mit temporärer SQLite-Datenbank. Dadurch bleiben die reguläre Datenbank
und andere Tests unbeeinflusst. Verbindungen werden explizit geschlossen,
Schreiboperationen mit `commit()` gespeichert.

## Tests und Codequalität prüfen

Gesamte Testsuite mit Coverage sowie Ruff ausführen:

```bash
uv run pytest
uv run ruff check .
```

Einzelne Testbereiche ohne projektweite Coverage-Prüfung ausführen:

```bash
uv run pytest tests/test_validation.py --no-cov
uv run pytest tests/test_post_routes.py --no-cov
uv run pytest tests/test_app.py --no-cov
```

Mit `uv run pytest -v` werden alle Testfälle mit ihren Namen angezeigt.

## Testabdeckung und Qualitätskriterien

Die Mindestabdeckung beträgt 70 %. Gemessen werden Anweisungen und
Verzweigungen.

Stand des lokalen Testlaufs vom 18.10.2026:

| Bereich | Coverage |
|---|---:|
| `src/blog/__init__.py` | 100 % |
| `src/blog/app.py` | 85 % |
| `src/blog/db.py` | 89 % |
| `src/blog/validation.py` | 100 % |
| Gesamt | 88,57 % |

Alle 23 Testfälle bestehen ohne Ressourcenwarnungen. Die Werte sind eine
Momentaufnahme und können sich durch Code- oder Teständerungen verändern.

Für die spätere CI-Pipeline gelten folgende Qualitätskriterien:

- Alle automatisierten Tests bestehen.
- Die Mindestabdeckung von 70 % wird erreicht.
- Ruff meldet keine Verstöße gegen die konfigurierten Regeln.