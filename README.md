# KLEIN. MITTEL. KI. – Redaktion

Hier arbeitet die Agenten-Redaktion des Blogs [kleinmittelki.de](https://www.kleinmittelki.de).
Das Repo ist ihr gemeinsames Gedächtnis: Regeln, Wissen über den Blog, Arbeitsstand und Werkzeuge.

**Grundsatz:** Agenten recherchieren, schlagen vor und bereiten fertig vor. Veröffentlicht, verschickt oder gepostet
wird nur, wenn Till ausdrücklich zustimmt.

## Was wo liegt

| Ordner/Datei | Inhalt |
|---|---|
| `CLAUDE.md` | Kurze Grundregeln für alle Agenten |
| `.claude/agents/` | Die Redaktion: Chefredakteur, Scout, Ideen, Autor, Grafik, Prüfer, Social, Analyst |
| `.claude/skills/` | Das Handbuch in Teilen: Stil, Formate, Themen, CI und Grafik, Ghost, Newsletter, Social |
| `redaktion/` | Gemeinsames Gedächtnis: Themenboard, Entscheidungen, Freigaben, Blog-Index, Berichte |
| `entwuerfe/` | Ein Ordner je Beitrag: Text, Quellen, Grafiken, Vorschaubild, Prüfbericht |
| `tools/` | Ghost-Werkzeug mit Freigabe-Sperre, Lexical-Umwandlung, Vorschaubild, Schaubilder, Sperr-Hook |
| `assets/` | Schriften (SIL OFL) und Logo |
| `docs/` | Überblick, offene Entscheidungen, Routinen, Muster-Beitrag |

## So geht es los

1. Cloud-Umgebungen „KMK-Recherche“ und „KMK-Ghost“ anlegen (siehe Anleitung im Chat).
2. Auf claude.ai/code eine Sitzung mit diesem Repo und der Umgebung **KMK-Ghost** starten und schreiben:
   `Lies .claude/agents/chefredakteur.md. Prüfe mit python3 tools/ghost.py check die Verbindung, baue den Index
   und kläre die offenen Punkte zur „Für KMU“-Zeile und zur Newsletter-Vorlage.`
3. Danach die Routinen aus `docs/routinen.md` anlegen.
