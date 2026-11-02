# Routinen der KMK-Redaktion

Geplante Claude-Läufe in der Cloud. Sie laufen, auch wenn Tills Rechner aus ist. Die Regeln stehen im Repo
(`CLAUDE.md`, `.claude/agents/chefredakteur.md`, Skills) – die Prompts der Routinen sind bewusst kurz.

## Wie Till mitarbeitet

Donnerstags gegen 8:20 Uhr kommt das **Redaktionsbriefing** an `till.zehnle@gmail.com` (seit 24.10.2026, vorher Mo/Mi/Fr):
oben die Empfehlung, darunter höchstens 4 Themen (Nummern), jedes gleich aufgebaut – Worum geht es? · Warum für KMU? ·
Unsere Idee (Arbeitstitel) · Rubrik · Quelle. Nie aufgefüllt; schon gemailte Themen kommen nicht wieder.
Fertige Entwürfe warten nicht auf Donnerstag: Sobald einer bereit ist, kommt eine kurze Mail „Vorschau bereit“ (Buchstaben).
Till antwortet einfach, z. B. „1 und 3. Zu 1: … · 2 nein, zu technisch · A ja“.
Sonntags gegen 8:30 kommt der Newsletter-Vorschlag für Dienstag mit Vorschau-Link und, wenn Ghost mitspielt, als **echte Testmail**
(nur an Till, so wie ihn die Leser bekommen). Die Testmail ist Zusatz, kein Muss (02.11.2026). Dazu steht in der Mail des Laufs, was neu und was Vorschlag ist.
Till schreibt Änderungen zurück (gelesen um 12:47 und 18:47; jede neue Fassung kommt wieder als Testmail) und gibt mit
„N ja“ frei – dann wird er für Dienstag 7:05 eingeplant, fünf Minuten nach dem Hauptbeitrag, damit dessen Link schon geht.
Eigene Ideen: jederzeit eine Mail an sich selbst mit Betreff „KMK Idee: …“ (Satz, Link, weitergeleitete Mail, Foto).
Der nächste Lauf nimmt sie auf, der Scout prüft die Quelle, die Idee kommt geprüft als I1 … ins Briefing am Donnerstag.
Mit „ausarbeiten“ im Text wird sie direkt geschrieben.
Ergebnisse anderer Recherche-Werkzeuge (z. B. ChatGPT-Aufgabe): an sich selbst weiterleiten mit Betreff „KMK Recherche“.
Der Lauf legt sie in `redaktion/eingang/` ab, der Scout prüft jeden Hinweis an der Originalquelle und führt ihn mit den eigenen Funden zusammen.
Takt (seit 25.10.2026, Tills Entscheidung): gleichmäßig veröffentlichen statt viel an einem Tag. Dienstag 7:00 Hauptbeitrag plus
Newsletter, Donnerstag 7:00 ein kürzerer Beitrag, höchstens zwei pro Woche. „A ja“ heißt: zum nächsten freien Termin aus
`redaktion/fahrplan.md` (die Vorschau-Mail nennt ihn). „A sofort“ oder ein eigener Termin („A Dienstag“) weicht davon ab.
Gibt Till ein Thema frei, arbeitet derselbe Lauf es aus und schickt die Vorschau in seiner Mail; sonst der nächste Lauf.
Antworten werden So–Fr um 7:47, 12:47 und 18:47 gelesen, Freigaben im selben Lauf ausgeführt.

## Der Lauf (seit 01.11.2026)

Ein einziger geplanter Lauf ersetzt die fünf früheren (Tills Entscheidung 01.11.2026: schlanker, weniger Eingriffe).

| Name | Zeitplan | Umgebung | Connectors | Prompt |
|---|---|---|---|---|
| KMK Redaktion | So–Fr 7:47, 12:47, 18:47 | KMK-Ghost | Gmail | „Lies docs/lauf.md und führe es aus.“ |

Ablauf: `docs/lauf.md`. Do 7:47 mit Scout und Briefing, So 7:47 mit Ideen, Wochenbericht, Newsletter (Testmail im selben Lauf), Social.
Höchstens eine Mail pro Lauf mit Statuszeile. Ein Fehler steht immer im Bericht; tritt er zweimal hintereinander auf, steht er in der Mail.
Die alten Läufe (Redaktions-, Ghost-, Mail-, Mail-Sonntag-, Sonntags-Lauf) sind pausiert, nicht gelöscht.

Warum: Bis 01.11. gaben fünf Läufe Arbeit über das Repo weiter und starteten sich per `fire_trigger` – das wird in geplanten
Läufen abgelehnt. Mail- und Ghost-Lauf waren getrennt, Fehler blieben still, Prompts und Repo-Regeln liefen auseinander.

Stand 19.10.2026: Der erste Testlauf zeigte, dass Redaktions- und Sonntags-Lauf in der Ghost-Umgebung liefen und
kein Internet hatten (DNS-Fehler, keine Originalquelle lesbar). Beide sind deshalb neu angelegt und laufen in der
Standard-Umgebung; Recherche über WebSearch und WebFetch. Die alten Versionen sind pausiert („alt, ohne Internet“).
Die Shell dort erreicht das Internet nicht – das Logo liegt deshalb als `assets/logo.png` im Repo.

Stand 01.11.2026: Die Newsletter-Testmail kam nicht, weil der Prompt des Ghost-Laufs den Testmail-Schritt nicht nannte (der Lauf
um 12:47 fand nichts zu tun und endete ohne Spur). Der Prompt nennt jetzt alle Schritte (abarbeiten, Entwürfe, Testmail, Index) und
verlangt, jeden Fehler in den Bericht zu schreiben und zu committen. Ein Lauf kann einen anderen per `fire_trigger` oft nicht starten
(Berechtigung, zuletzt 27.10. und 01.11.); dann holt der nächste geplante Lauf es nach.

Stand 02.11.2026: Die automatische Testmail ist seit 27.10. in fünf Versuchen gescheitert (Ghost antwortet auf `email_previews`
mit der Admin-Seite statt mit Daten; Ursache offen, `ghost.py` meldet jetzt eine Umleitung mit). Till: Testmail ist nur noch Zusatz,
der Begleitzettel kommt mit Vorschau-Link. Außerdem fiel der Redaktions-Lauf am 29.10. wegen des Nutzungslimits aus – ein Lauf statt fünf
(18 statt rund 46 Starts pro Woche) entlastet das Kontingent. Umbau am 02.11. aktiviert.

## Ein Beispiel-Durchlauf

- Do 7:47 Scout findet 3 Themen der Woche → Mail des Laufs mit Briefing (~8:30)
- Do 10:00 Till antwortet „1 und 3“ → Do 12:47 Lauf trägt ein, schreibt 1 und 3 mit Grafiken, Prüfer prüft, legt Entwürfe in Ghost an → Mail mit Vorschau A, B
- Do 15:00 Till: „A ja“ → Do 18:47 Lauf trägt die Freigabe mit dem nächsten freien Termin ein und plant A in Ghost ein → Mail nennt den Termin → Di 7:00 online

## Sicherheit

- Ghost-Schlüssel nur in „KMK-Ghost“.
- Seit 01.11.2026 hat der eine Lauf Gmail und Ghost (Tills Entscheidung). Er trägt Freigaben nur ein, wenn die Antwort aus Tills eigenem Gmail kommt
  (`till.zehnle@gmail.com`, Label „Gesendet“) und im Verlauf einer Redaktions-Mail steht – mit Zitat und Gmail-ID.
- `tools/ghost.py` veröffentlicht nur mit einer Freigabe, die zum Stand passt, den Till in der Vorschau gesehen hat.
- Beitragsbild ist immer das Titelbild (`tools/titelbild.py`), nie die Titel-Kachel; `draft` und `publish` blockieren sonst.
  Ein Titelbild an einem veröffentlichten Beitrag tauscht der Lauf nur mit Tills Freigabe der Art `titelbild`.
- `tools/sperre.py` blockiert direkte Ghost-Aufrufe, Änderungen an der Sperre und Löschen im Gedächtnis.
- Ehrlich: Das sind feste Regeln im Code, keine kryptografische Sicherung.
