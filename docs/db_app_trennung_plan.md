# Umstellungsplan: Datenbankmigrationen für die Flask-Blog-App

## Ziel

Die bestehende Flask-App wird schrittweise auf versionierte Datenbankmigrationen und persistente Datenhaltung umgestellt. Migrationen werden getrennt vom normalen Webserverstart ausgeführt. Die bestehende Blog-Funktionalität bleibt erhalten; ein vollständiger Umbau der Datenzugriffsschicht ist zunächst nicht vorgesehen.

## Ausgangslage

- Die Anwendung verwendet Flask und SQLite.
- Im frisch gestarteten Container fehlt die Tabelle `posts`.
- Anwendungsstart und Datenbankaufbau sind noch nicht zuverlässig aufeinander abgestimmt.
- Lokale Entwicklung, CI und Container verwenden künftig `pyproject.toml` und `uv.lock` als gemeinsame Abhängigkeitsgrundlage.
- Die tatsächlichen aktuellen Dateiinhalte müssen vor der Umsetzung geprüft werden.

## Zielbild

```text
Versionierter Anwendungscode einschließlich Migrationen
        │
        ├─ Separater Migrationslauf
        │       └─ Aktualisiert das Schema im persistenten Datenbankspeicher
        │
        └─ Webserver
                └─ Verwendet denselben Datenbankspeicher
```

## Grundsätze

- Keine unkoordinierten Schemaänderungen beim Start jeder Anwendungsinstanz.
- Keine Datenbankinitialisierung während des Image-Builds.
- Keine produktiven Nutzdaten im Anwendungsimage.
- Anwendung und Migrationsprozess verwenden dieselbe Datenbankkonfiguration.
- Tests verwenden isolierte temporäre Datenbanken.
- Bereits angewendete Migrationen werden nicht nachträglich verändert.
- Vorhandene Daten werden nicht ungeprüft gelöscht oder zurückgesetzt.
- Die Auswahl einer Migrationslösung erfolgt nach Sichtung des Quellcodes.

## Schritt 1: Bestehenden Datenbankablauf analysieren

### Aufgaben

- [ ] Datenbankpfad und Konfigurationsquelle ermitteln.
- [ ] Aufrufe von `init_db()` nachvollziehen.
- [ ] Prüfen, ob `init_db()` vorhandene Daten oder Tabellen löscht.
- [ ] Unterschiede zwischen `main()`, App-Factory und Container-Start untersuchen.
- [ ] Aufbau der Testdatenbanken prüfen.
- [ ] Konfiguration von Anwendung, Tests und Initialisierung vergleichen.

### Ergebnis

Dokumentierte Ausgangslage mit einer Entscheidung, welche bestehende Logik beibehalten, verschoben oder ersetzt wird.

## Schritt 2: Datenbankkonfiguration vereinheitlichen

### Aufgaben

- [ ] Einen eindeutigen, konfigurierbaren Datenbankpfad festlegen.
- [ ] Anwendung und Migrationsprozess an dieselbe Konfiguration anbinden.
- [ ] Erstellung des benötigten Datenbankverzeichnisses und Zugriffsrechte berücksichtigen.
- [ ] Für Tests einen separaten temporären Datenbankpfad vorsehen.

### Aufgabenverteilung

```text
Anwendungskonfiguration → bestimmt den Datenbankpfad
Datenbankzugriff        → öffnet Verbindungen zu diesem Pfad
Migrationsprozess      → aktualisiert das Schema an diesem Pfad
```

### Ergebnis

Ein einheitlicher Datenbankzugriff unabhängig davon, wie die Anwendung gestartet wird.

## Schritt 3: Versionierte Migrationen einführen

### Aufgaben

- [ ] Geeignete Migrationslösung anhand von `db.py` und `pyproject.toml` auswählen.
- [ ] Das aktuelle Schema als erste Migration erfassen.
- [ ] Eine Historie angewendeter Migrationen vorsehen.
- [ ] Den Neuaufbau auf einer leeren Datenbank sicherstellen.
- [ ] Umgang mit einer bereits vorhandenen lokalen Datenbank festlegen.

### Erste Migration

```text
Migration 001
└─ Tabelle posts mit dem tatsächlich vorhandenen Schema anlegen
```

### Umgang mit Bestandsdaten

- Vor Änderungen klären, ob bisherige Blogbeiträge erhalten bleiben müssen.
- Vorhandenes Schema prüfen und bei Bedarf eine Sicherung erstellen.
- Eine bestehende Datenbank nicht pauschal zurücksetzen.
- Einen Migrationsstand nur nach bestätigter Schemaübereinstimmung übernehmen.

### Ergebnis

Nachvollziehbarer Aufbau einer neuen Datenbank und ein kontrollierter Übernahmeweg für bestehende Daten.

## Schritt 4: Separaten Migrationsbefehl bereitstellen

### Ablauf

```text
Konfiguration laden
        ↓
Datenbankstand feststellen
        ↓
Ausstehende Migrationen ausführen
        ↓
Ergebnis melden und Prozess beenden
```

### Aufgaben

- [ ] Einen expliziten Migrationsbefehl implementieren.
- [ ] Fehler mit einem nicht erfolgreichen Prozessstatus melden.
- [ ] Bereits angewendete Migrationen anhand der Historie überspringen.
- [ ] Automatische Schemaänderungen aus dem normalen Webserverstart entfernen.
- [ ] Koordination gegen parallele Migrationsläufe für spätere Deployments berücksichtigen.

### Ergebnis

Ein gemeinsamer Migrationsweg für lokale Entwicklung, Tests und spätere Deployments.

## Schritt 5: Tests auf den tatsächlichen Aufbauprozess umstellen

### Testfälle

- [ ] Leere Datenbank vollständig migrieren.
- [ ] Migrationsbefehl erneut ausführen, ohne abgeschlossene Migrationen erneut anzuwenden.
- [ ] Vorhandene Beiträge bei erneutem Migrationslauf erhalten.
- [ ] Upgrade eines früheren Schemas testen, sobald eine Folgemigration existiert.
- [ ] Startseite nach der Migration erfolgreich aufrufen.
- [ ] Beitrag erstellen und anschließend wieder anzeigen.
- [ ] Bestehende Routen- und Validierungstests weiterhin erfolgreich ausführen.

### Aufgaben

- [ ] Test-Fixtures auf den gemeinsamen Migrationsweg umstellen.
- [ ] Eine zweite, unabhängig gepflegte Testschema-Definition vermeiden.
- [ ] Tests weiterhin voneinander isolieren.

### Ergebnis

Automatisierte Absicherung des Datenbankaufbaus und der bestehenden Fachfunktionen.

## Schritt 6: Containerbetrieb und Persistenz ergänzen

### Aufgaben

- [ ] Migrationen und benötigte Konfiguration in das Image aufnehmen.
- [ ] Einen persistenten Speicherort für die SQLite-Datenbank festlegen.
- [ ] Migrationslauf und Webserver an denselben Speicher anbinden.
- [ ] Migration vor der Bereitstellung des Webservers ausführen.
- [ ] Bei fehlgeschlagener Migration den weiteren Bereitstellungsablauf stoppen.
- [ ] Nachweisen, dass Beiträge nach einem Containerwechsel erhalten bleiben.

### Ergebnis

Ein austauschbarer Anwendungscontainer mit unabhängig gespeicherten Nutzdaten.

## Schritt 7: CI erweitern und CD vorbereiten

### Phase 2: CI

- [ ] Migrationstests ausführen.
- [ ] Bestehende Anwendungstests ausführen.
- [ ] Container-Image bauen.
- [ ] Container-Funktionstest gegen eine frische Testdatenbank ergänzen.
- [ ] Im Funktionstest zuerst migrieren, anschließend die Anwendung starten und die Startseite prüfen.
- [ ] Temporäre Testressourcen nach dem Lauf aufräumen.

```text
Qualitätsprüfung und Tests
        ↓
Container-Build
        ↓
Testdatenbank migrieren
        ↓
Container starten
        ↓
HTTP-Funktionsprüfung
```

### Phase 3: CD

```text
Staging: Migration → Bereitstellung → Funktionsprüfung
        ↓
Produktionsfreigabe
        ↓
Production: Migration → Bereitstellung → Funktionsprüfung
```

- [ ] Migrationsschritt in die jeweilige Zielumgebung integrieren.
- [ ] Freigaben, Sicherung und Fehlerbehandlung festlegen.
- [ ] Parallele Bereitstellungen koordinieren.
- [ ] Bei späteren inkompatiblen Änderungen Erweiterung, Umstellung und Bereinigung auf mehrere Releases verteilen.

### Ergebnis

Ein durchgängiger Prozess von der automatisierten Prüfung bis zur kontrollierten Datenbankänderung in der Zielumgebung.

## Benötigte Dateien für die konkrete Umsetzung

Bitte die vollständigen aktuellen Inhalte bereitstellen, nicht nur eine Strukturübersicht.

| Datei | Zweck |
|---|---|
| `src/blog/app.py` | App-Factory, Konfiguration, Routen und bisheriger Initialisierungsaufruf |
| `src/blog/db.py` | Datenbankpfad, Verbindungen und aktuelles Schema |
| `src/blog/__init__.py` | Paketstruktur und Import der App-Factory |
| `pyproject.toml` | Abhängigkeiten, Paketkonfiguration und Testeinstellungen |
| `tests/conftest.py` | Aufbau und Isolation der Testdatenbank |
| `tests/test_app.py` | Bestehende Startseiten- und Beitragstests |
| `tests/test_post_routes.py` | Erwartungen an Datenbankzugriffe und Beitragserstellung |
| `Dockerfile` | Aktueller Image-Aufbau und Startkommando |
| `.dockerignore` | Ausschlüsse für den Container-Build |
| `.github/workflows/ci.yml` | CI-Ablauf und Einbindung zusätzlicher Prüfungen |

### Zusätzlich hilfreich

- Konfigurationsdatei oder bereinigte `.env.example`, falls vorhanden.
- Container-Orchestrierungsdatei, falls vorhanden.
- README-Abschnitt mit aktuellen Start- und Testbefehlen.
- `uv.lock` für den exakten Abhängigkeitsstand.

### Nicht erforderlich

- Templates, solange keine Änderung an der Darstellung nötig ist.
- Lokale `.venv`.
- SQLite-Datei mit Nutzdaten.
- Echte Zugangsdaten, Tokens oder sonstige Geheimnisse.

## Erste Arbeitseinheit und Abnahmekriterien

Zunächst wird folgender Ablauf umgesetzt und nachgewiesen:

```text
Leere Datenbank
        ↓
Migrationsbefehl ausführen
        ↓
Anwendung starten
        ↓
Beitrag anlegen und anzeigen
        ↓
Container ersetzen und denselben Speicher erneut anbinden
        ↓
Beitrag weiterhin vorhanden
```

### Abnahme

- [ ] Eine frische Umgebung benötigt keine manuell vorbereitete lokale Datenbank.
- [ ] Die Tabelle `posts` wird über die erste Migration erstellt.
- [ ] Wiederholte Migrationsläufe lassen bestehende Daten unverändert.
- [ ] Der Webserver startet ohne eigene Schemaänderungen.
- [ ] Startseite und Beitragserstellung funktionieren.
- [ ] Beiträge bleiben bei einem Containerwechsel erhalten.
- [ ] Bestehende und neue Tests sind erfolgreich.

## Noch zu klären

- Müssen bisherige lokale Blogbeiträge erhalten bleiben?
- Welche Datenbankkonfiguration und Initialisierung existieren tatsächlich im aktuellen Code?
- Welche Migrationslösung passt zur bestehenden Datenzugriffsschicht?
- Welcher persistente Datenbankpfad soll für den Containerbetrieb verwendet werden?

## Nächster Schritt

Die zehn Dateien aus der Tabelle bereitstellen und angeben, ob vorhandene Blogbeiträge erhalten bleiben sollen. Anschließend wird Schritt 1 anhand des tatsächlichen Codes durchgeführt und die konkrete Umsetzung festgelegt.
