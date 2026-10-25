# Routinen der KMK-Redaktion

Geplante Claude-Läufe in der Cloud. Sie laufen, auch wenn Tills Rechner aus ist. Die Regeln stehen im Repo
(`CLAUDE.md`, `.claude/agents/chefredakteur.md`, Skills) – die Prompts der Routinen sind bewusst kurz.

## Wie Till mitarbeitet

Donnerstags gegen 8:20 Uhr kommt das **Redaktionsbriefing** an `till.zehnle@gmail.com` (seit 24.10.2026, vorher Mo/Mi/Fr):
oben die Empfehlung, darunter höchstens 4 Themen (Nummern), jedes gleich aufgebaut – Worum geht es? · Warum für KMU? ·
Unsere Idee (Arbeitstitel) · Rubrik · Quelle. Nie aufgefüllt; schon gemailte Themen kommen nicht wieder.
Fertige Entwürfe warten nicht auf Donnerstag: Sobald einer bereit ist, kommt eine kurze Mail „Vorschau bereit“ (Buchstaben).
Till antwortet einfach, z. B. „1 und 3. Zu 1: … · 2 nein, zu technisch · A ja“.
Sonntags kommt der Newsletter-Vorschlag für Dienstag als **echte Testmail von Ghost** (seit 25.10.2026): genau so, wie ihn
die Leser bekommen, nur an Till. Dazu ein kurzer Begleitzettel der Redaktion (was neu ist, was Vorschlag ist). Ablauf: Sonntags-Lauf
schreibt und prüft, startet den Ghost-Lauf, der legt den Newsletter als Entwurf an und schickt die Testmail (`ghost.py testmail`).
Till schreibt Änderungen zurück (Antworten um 12:17, 15:17, 18:17, 21:17; jede neue Fassung kommt wieder als Testmail) und gibt mit
„N ja“ frei – dann wird er für Dienstag 7:05 eingeplant, fünf Minuten nach dem Hauptbeitrag, damit dessen Link schon geht.
Eigene Ideen: jederzeit eine Mail an sich selbst mit Betreff „KMK Idee: …“ (Satz, Link, weitergeleitete Mail, Foto).
Der nächste Mail-Lauf nimmt sie auf, der Scout prüft die Quelle, die Idee kommt geprüft als I1 … ins Briefing am Donnerstag.
Mit „ausarbeiten“ im Text wird sie direkt geschrieben.
Ergebnisse anderer Recherche-Werkzeuge (z. B. ChatGPT-Aufgabe): an sich selbst weiterleiten mit Betreff „KMK Recherche“.
Der Mail-Lauf legt sie in `redaktion/eingang/` ab, der Scout prüft jeden Hinweis an der Originalquelle und führt ihn mit den eigenen Funden zusammen.
Takt (seit 25.10.2026, Tills Entscheidung): gleichmäßig veröffentlichen statt viel an einem Tag. Dienstag 7:00 Hauptbeitrag plus
Newsletter, Donnerstag 7:00 ein kürzerer Beitrag, höchstens zwei pro Woche. „A ja“ heißt: zum nächsten freien Termin aus
`redaktion/fahrplan.md` (die Vorschau-Mail nennt ihn). „A sofort“ oder ein eigener Termin („A Dienstag“) weicht davon ab.
Express: Sobald Till ein Thema freigibt, startet der Mail-Lauf sofort einen Redaktions-Lauf (ohne Scout). Der startet nach der Prüfung
den Ghost-Lauf (Entwurf) und danach den Mail-Lauf (Mail „Vorschau bereit“). Vorschau-Link meist nach etwa einer Stunde.
Ausfall-Check: Fehlt donnerstags um 8:17 der Bericht des Redaktions-Laufs, startet der Mail-Lauf ihn nach; das Briefing kommt dann um 12:17.
Die Redaktion bestätigt im selben Verlauf und arbeitet weiter. Antworten werden Mo–Fr um 12:17 und 18:17 gelesen
(und um 8:17); Veröffentlichungen laufen eine halbe Stunde später.

## Die Läufe

| Name | Zeitplan | Umgebung | Connectors |
|---|---|---|---|
| KMK Redaktions-Lauf | Do 6:47 (mit Scout) + Express nach Tills Ja | Standard (Websuche + Webabruf) | – |
| KMK Ghost-Lauf | So–Fr 7:47, 12:47, 18:47, 21:47 + bei Bedarf | KMK-Ghost | keine |
| KMK Mail-Lauf | Mo–Fr 8:17, 12:17, 18:17 | Standard | Gmail |
| KMK Mail-Lauf Sonntag | So 10:17, 12:17, 15:17, 18:17, 21:17 | Standard | Gmail |
| KMK Sonntags-Lauf | So 9:47 | Standard (Websuche + Webabruf) | – |

Stand 19.10.2026: Der erste Testlauf zeigte, dass Redaktions- und Sonntags-Lauf in der Ghost-Umgebung liefen und
kein Internet hatten (DNS-Fehler, keine Originalquelle lesbar). Beide sind deshalb neu angelegt und laufen in der
Standard-Umgebung; Recherche über WebSearch und WebFetch. Die alten Versionen sind pausiert („alt, ohne Internet“).
Die Shell dort erreicht das Internet nicht – das Logo liegt deshalb als `assets/logo.png` im Repo.

## Ein Beispiel-Durchlauf

- Do 6:47 Scout findet 3 Themen der Woche → Do 8:17 Redaktionsbriefing an Till
- Do 10:00 Till antwortet „1 und 3“ → Do 12:17 Mail-Lauf trägt ein, bestätigt, startet den Express-Lauf
- Do ~12:30 Redaktion schreibt 1 und 3 mit Grafiken, Prüfer prüft → Ghost-Lauf legt Entwürfe an → Mail „Vorschau bereit“
- Do 15:00 Till: „A ja“ → Do 18:17 Freigabe mit dem nächsten freien Termin (z. B. Di 7:00) eingetragen, Bestätigung nennt den Termin → Do 18:47 A ist in Ghost eingeplant → Di 7:00 online

## Sicherheit

- Ghost-Schlüssel nur in „KMK-Ghost“. Diese Umgebung erreicht nur den Blog und liest keine Mails.
- Der Mail-Lauf hat keinen Ghost-Zugang. Er trägt Freigaben nur ein, wenn die Antwort aus Tills eigenem Gmail kommt
  (`till.zehnle@gmail.com`, Label „Gesendet“) und im Verlauf einer Redaktions-Mail steht – mit Zitat und Gmail-ID.
- `tools/ghost.py` veröffentlicht nur mit einer Freigabe, die zum Stand passt, den Till in der Vorschau gesehen hat.
- Beitragsbild ist immer das Titelbild (`tools/titelbild.py`), nie die Titel-Kachel; `draft` und `publish` blockieren sonst.
  Ein Titelbild an einem veröffentlichten Beitrag tauscht der Ghost-Lauf nur mit Tills Freigabe der Art `titelbild`.
- `tools/sperre.py` blockiert direkte Ghost-Aufrufe, Änderungen an der Sperre und Löschen im Gedächtnis.
- Ehrlich: Das sind feste Regeln im Code, keine kryptografische Sicherung.
