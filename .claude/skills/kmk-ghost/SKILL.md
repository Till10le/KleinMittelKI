---
name: kmk-ghost
description: Wie die KMK-Redaktion mit Ghost arbeitet – tools/ghost.py, Entwürfe aus beitrag.md, Bilder, Blog-Index, Freigabe-Sperre und Veröffentlichung. Laden vor jeder Arbeit mit Ghost.
---

# Arbeiten mit Ghost

Blog: www.kleinmittelki.de (Ghost(Pro), Admin klein-mittel-ki.ghost.io). Alles läuft über `tools/ghost.py` –
nie über den Ghost-Editor, nie per curl. Die Werkzeuge brauchen die Umgebung **„KMK-Ghost“**
(Variablen `GHOST_URL`, `GHOST_ADMIN_API_KEY`; erlaubte Domains klein-mittel-ki.ghost.io, www.kleinmittelki.de, storage.ghost.io).

## Befehle

| Zweck | Befehl |
|---|---|
| Verbindung prüfen | `python3 tools/ghost.py check` |
| Blog-Index neu bauen | `python3 tools/ghost.py index` |
| Beiträge auflisten | `python3 tools/ghost.py list --status draft` |
| Beitrag lesen | `python3 tools/ghost.py get <slug>` (`--raw` für alle Felder) |
| Bild hochladen | `python3 tools/ghost.py upload <datei>` |
| Entwurf anlegen/aktualisieren | `python3 tools/ghost.py draft entwuerfe/<slug>` |
| Freigabe eintragen | `python3 tools/ghost.py freigabe <slug> --art beitrag --zitat "<Tills Worte>"` |
| Veröffentlichen | `python3 tools/ghost.py publish <slug>` (optional `--zeitpunkt 2026-10-20T05:00:00Z`) |
| Newsletter einplanen | `python3 tools/ghost.py newsletter <slug> --newsletter <newsletter-slug> --zeitpunkt …` |
| Newsletter-Testmail an Till | `python3 tools/ghost.py testmail entwuerfe/<newsletter-slug>` (nur Newsletter, nur an till.zehnle@gmail.com, bleibt Entwurf) |

## Was die Werkzeuge garantieren

- `draft` legt immer nur **Entwürfe** an, setzt den Tag `#zur-freigabe`, lädt die Titel-Kachel `vorschaubild.png`
  als `og_image`/`twitter_image` und das Titelbild `titel-<slug>.jpg` als `feature_image` hoch und schreibt Vorschau-Link
  und Ghost-ID nach `entwuerfe/<slug>/ghost.json`. Ohne Titelbild (oder wenn es die Titel-Kachel ist) bricht `draft` ab.
- `publish` blockiert, wenn das Beitragsbild in Ghost die Titel-Kachel ist (doppelte Überschrift). Dann `draft` neu.
- Titelbild an einem **veröffentlichten** Beitrag tauschen: nur mit Tills Freigabe der Art `titelbild`
  (`ghost.py freigabe <slug> --art titelbild --zitat "…"`, gebunden an die Bilddatei). `abarbeiten` tauscht dann nur
  `feature_image`, sonst nichts. Ändert sich die Bilddatei danach, blockiert es.
  Ein bereits veröffentlichter Beitrag wird nie überschrieben. Gleicher Slug schon vorhanden → Abbruch (Dublette?).
- `publish` und `newsletter` laufen nur mit einer Freigabe aus `redaktion/freigaben.jsonl`, die **zum aktuellen Stand**
  des Beitrags passt. Jede Änderung nach der Freigabe macht sie ungültig. Der INTERN-Absatz wird beim Veröffentlichen
  entfernt, `#zur-freigabe` ebenso. Offene Platzhalter (`[TILL: …]`, `{{…}}`) blockieren.
- Beiträge gehen **nie** per E-Mail raus. Nur `newsletter` verschickt, und nur mit Freigabe der Art `newsletter`.
- Es gibt keinen Löschbefehl. Ein Hook (`tools/sperre.py`) blockiert direkte API-Aufrufe und Änderungen an der Sperre.

## Zeiten

Ghost speichert in UTC. Dienstag 7:00 Uhr deutscher Zeit = 05:00Z (Sommerzeit) bzw. 06:00Z (Winterzeit, ab 25.10.2026).

## Vorschau

Entwürfe sind unter `https://www.kleinmittelki.de/p/<uuid>/` sichtbar (steht in `ghost.json`). Ist die Seite
passwortgeschützt, nie ein Passwort eingeben – Till fragen.

## Bekannte offene Punkte

- Die „Für KMU“-Zeile steht in `twitter_description` (siehe `kmk-formate`). `draft` überträgt das
  Frontmatter-Feld `fuer_kmu` dorthin (seit 18.10.2026, mit Tills Freigabe).
- Änderungen an Code-Injection oder Theme (z. B. „Eine Zahl, genau gelesen“) kann die Admin-API mit Integrations-Key
  nicht vornehmen. Solche Änderungen als Vorschlag an Till.
