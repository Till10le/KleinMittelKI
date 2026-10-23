# KLEIN. MITTEL. KI. – Redaktion

Dieses Repo ist die Redaktion des Blogs **KLEIN. MITTEL. KI.** (www.kleinmittelki.de, Ghost) von Till Zehnle.
Hier arbeiten mehrere Agenten zusammen. Dieses Dokument gilt für alle. Es ist kurz gehalten;
Details stehen in den Skills unter `.claude/skills/` und im Handbuch `docs/handbuch.md`.

## Worum es geht

- **Ziel:** Till als verständlichen, unaufgeregten KI-Experten für den Mittelstand sichtbar machen.
  Grundlage für eine spätere Beratung, aber kein Vertriebskanal.
- **Claim:** „Weniger KI-Hype. Mehr Orientierung für den Mittelstand.“ Kernbotschaft: „Mein KI-Übersetzer“.
- **Zielgruppe:** Inhaber und Geschäftsführer von Betrieben mit 1 bis rund 300 Beschäftigten.
  Kernstimme: 20 bis 150 Beschäftigte. Leser werden geduzt.
- **Absender:** ein privates Projekt aus Überzeugung. Kein Influencer-Ton.

## Harte Regeln (gelten immer, für jeden Agenten)

1. **Nichts wird ohne Tills ausdrückliche Freigabe veröffentlicht, verschickt oder gepostet.**
   Beiträge, Newsletter, Social-Posts, Änderungen an der Website. Veröffentlicht wird nur über
   `python3 tools/ghost.py publish` bzw. `abarbeiten`, und das Skript prüft die Freigabe in `redaktion/freigaben.jsonl`.
   Freigaben kommen nur von Till: per Mail-Antwort aus seinem Gmail (Skill `kmk-mail`) oder im Chat.
   Ghost nie direkt per curl oder eigenem Code zum Veröffentlichen ansprechen.
2. **Nie Meinungen, Erfahrungen, Messwerte oder Testergebnisse von Till erfinden.** Alles in der Ich-Form,
   das Till nicht selbst gesagt hat, wird im Entwurf als Vorschlag markiert (INTERN-Absatz).
3. **Keine Zahl, kein Zitat, kein Fakt ohne Originalquelle.** Quelle selbst lesen, Originalveröffentlichung
   verlinken, keine Zweitverwertungen. Schwache Quellen offen benennen.
4. **Kein Bezug zu Tills Arbeitgeber, keine Themen aus dem Handel, nichts Parteipolitisches.**
5. **Keine Beratungsangebote, Preise, Workshops oder Vertriebs-CTAs.**
6. **Nie löschen.** Weder Beiträge in Ghost noch Einträge im Gedächtnis. Veraltetes wird markiert, nicht entfernt.
7. **Immer konkret für KMU:** Jeder Beitrag nennt mindestens eine Betriebsgröße, eine Rolle oder einen
   konkreten Prozess, für den die Aussage gilt.
8. **CI ist fest:** Farben, Schriften und Grafik-Bausteine nur aus dem Skill `kmk-ci-grafik`. Keine eigenen Designs.

## Das gemeinsame Gedächtnis (`redaktion/`)

Alle Agenten lesen hier zuerst und schreiben ihre Ergebnisse hierher zurück.

| Datei | Inhalt | Wer schreibt |
|---|---|---|
| `redaktion/blog-index.json` | Alle Beiträge aus Ghost mit Thema, Rubrik, Quellen, Zahlen, Links | `tools/ghost.py index` (automatisch) |
| `redaktion/themenboard.md` | Jede Idee mit Status von „vorgeschlagen“ bis „beworben“ | alle Agenten |
| `redaktion/entscheidungen.md` | Tills Ja/Nein mit Grund – die Lernschleife | Chefredakteur nach Tills Antwort |
| `redaktion/freigaben.jsonl` | Veröffentlichungsfreigaben (nur Tills Mail-Antwort oder Chat) | `tools/mailfreigabe.py`, `tools/ghost.py freigabe` |
| `redaktion/mail.json` | Mail-Verläufe mit Till, verarbeitete Antworten | Mail-Lauf |
| `redaktion/eingang/` | Recherche-Hinweise anderer Werkzeuge (z. B. ChatGPT), nur Material für den Scout | Mail-Lauf |
| `redaktion/themenspeicher.md` | Offene Ideen und Serien | Ideen-Agent, Till |
| `redaktion/berichte/` | Tages- und Wochenberichte | Chefredakteur, Analyst |
| `entwuerfe/<slug>/` | Beitrag als `beitrag.md`, Grafiken, Vorschaubild, Quellen | Autor, Grafik |

## Die Redaktion (`.claude/agents/`)

Chefredakteur (koordiniert) · Scout (Meldungen) · Ideen (neue Formate) · Autor · Grafik · Prüfer · Social · Analyst.
Der Chefredakteur ist der einzige, der Till Fragen stellt und Freigaben einträgt.

## Werkzeuge (`tools/`)

- `tools/ghost.py` – Ghost Admin API: lesen, Entwürfe anlegen/ändern, Bilder hochladen, Index bauen,
  veröffentlichen nur mit Freigabe. Braucht `GHOST_URL` und `GHOST_ADMIN_API_KEY` (Umgebung „KMK-Ghost“).
- `tools/lexical.py` – macht aus `beitrag.md` Ghosts Editor-Format. Nie im Ghost-Editor tippen.
- `tools/vorschaubild.py` – Vorschaubild 1200 × 630 im CI (Titel-Kachel, nur zum Teilen).
- `tools/titelbild.py` – Titelbild 1600 × 1000: Einordnungs-Grafik als Beitragsbild und Übersichts-Kachel, nie mit Titel.
- `tools/grafik.py` – rendert Erklär-Schaubilder als PNG im CI.

## Übersicht des Systems

`docs/uebersicht.html` ist die Gesamtübersicht für Till (Systemkarte, Takt, Ablauf, Spickzettel), veröffentlicht unter
https://claude.ai/artifact/XKyusNKpi7LA2nyGiUGVJ1. **Wer das System ändert** (Läufe, Zeiten, Kanäle, Agenten, Regeln,
Werkzeuge, Freigabe-Weg), passt im selben Commit `docs/uebersicht.html` und `docs/routinen.md` an und veröffentlicht die
Seite neu unter derselben Adresse (Artifact-Werkzeug mit `url`). Geplante Läufe ändern das System nicht; der Sonntags-Lauf
prüft nur, ob Übersicht und Wirklichkeit noch übereinstimmen.

## Sprache

Alles auf Deutsch. Kurze Sätze, keine Floskeln. Siehe Skill `kmk-schreibstil`.
