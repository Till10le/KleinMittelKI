# Routinen der KMK-Redaktion

Geplante Claude-Läufe in der Cloud. Sie laufen, auch wenn Tills Rechner aus ist. Die Regeln stehen im Repo
(`CLAUDE.md`, `.claude/agents/chefredakteur.md`, Skills) – die Prompts der Routinen sind bewusst kurz.

## Wie Till mitarbeitet

Montags, mittwochs und freitags gegen 8:20 Uhr kommt eine Mail an `till.zehnle@gmail.com`:
neue Themen (Nummern), fertige Entwürfe mit Vorschau-Link (Buchstaben), ggf. der Newsletter (N).
Till antwortet einfach, z. B. „1 und 3. Zu 1: … · 2 nein, zu technisch · A ja · N ja“.
Sonntags gegen 10:20 Uhr kommt der Newsletter-Vorschlag für Dienstag mit vollem Text. Till schreibt Änderungen
zurück (Antworten um 12:17, 15:17, 18:17, 21:17) und gibt mit „N ja“ frei – dann wird er angelegt und für Dienstag 7:00 eingeplant.
Eigene Ideen: jederzeit eine Mail an sich selbst mit Betreff „KMK Idee: …“ (Satz, Link, weitergeleitete Mail, Foto).
Der nächste Mail-Lauf nimmt sie auf, der Scout prüft die Quelle, die Idee kommt geprüft als I1 … in die nächste Redaktions-Mail.
Mit „ausarbeiten“ im Text wird sie direkt geschrieben.
Ergebnisse anderer Recherche-Werkzeuge (z. B. ChatGPT-Aufgabe): an sich selbst weiterleiten mit Betreff „KMK Recherche“.
Der Mail-Lauf legt sie in `redaktion/eingang/` ab, der Scout prüft jeden Hinweis an der Originalquelle und führt ihn mit den eigenen Funden zusammen.
Express: Sobald Till ein Thema freigibt, startet der Mail-Lauf sofort einen Redaktions-Lauf (ohne Scout). Der startet nach der Prüfung
den Ghost-Lauf (Entwurf) und danach den Mail-Lauf (Mail „Vorschau bereit“). Vorschau-Link meist nach etwa einer Stunde.
Ausfall-Check: Fehlt um 8:17 (Mo/Mi/Fr) der Bericht des Redaktions-Laufs, startet der Mail-Lauf ihn nach und sagt es Till in der Mail.
Die Redaktion bestätigt im selben Verlauf und arbeitet weiter. Antworten werden Mo–Fr um 12:17 und 18:17 gelesen
(und um 8:17); Veröffentlichungen laufen eine halbe Stunde später.

## Die Läufe

| Name | Zeitplan | Umgebung | Connectors |
|---|---|---|---|
| KMK Redaktions-Lauf | Mo, Mi, Fr 6:47 + Express nach Tills Ja | Standard (Websuche + Webabruf) | – |
| KMK Ghost-Lauf | So–Fr 7:47, 12:47, 18:47, 21:47 + bei Bedarf | KMK-Ghost | keine |
| KMK Mail-Lauf | Mo–Fr 8:17, 12:17, 18:17 | Standard | Gmail |
| KMK Mail-Lauf Sonntag | So 10:17, 12:17, 15:17, 18:17, 21:17 | Standard | Gmail |
| KMK Sonntags-Lauf | So 9:47 | Standard (Websuche + Webabruf) | – |

Stand 19.10.2026: Der erste Testlauf zeigte, dass Redaktions- und Sonntags-Lauf in der Ghost-Umgebung liefen und
kein Internet hatten (DNS-Fehler, keine Originalquelle lesbar). Beide sind deshalb neu angelegt und laufen in der
Standard-Umgebung; Recherche über WebSearch und WebFetch. Die alten Versionen sind pausiert („alt, ohne Internet“).
Die Shell dort erreicht das Internet nicht – das Logo liegt deshalb als `assets/logo.png` im Repo.

## Ein Beispiel-Durchlauf

- Mo 6:47 Scout findet 3 Themen → Mo 8:17 Mail an Till
- Mo 10:00 Till antwortet „1 und 3“ → Mo 12:17 Mail-Lauf trägt ein, bestätigt
- Mi 6:47 Redaktion schreibt 1 und 3 mit Grafiken, Prüfer prüft → Mi 7:47 Entwürfe in Ghost → Mi 8:17 Mail mit Vorschau-Links
- Mi 9:00 Till: „A ja, B Dienstag“ → Mi 12:17 Freigaben eingetragen → Mi 12:47 A ist online, B eingeplant → Mi 18:17 Bestätigung mit Link

## Sicherheit

- Ghost-Schlüssel nur in „KMK-Ghost“. Diese Umgebung erreicht nur den Blog und liest keine Mails.
- Der Mail-Lauf hat keinen Ghost-Zugang. Er trägt Freigaben nur ein, wenn die Antwort aus Tills eigenem Gmail kommt
  (`till.zehnle@gmail.com`, Label „Gesendet“) und im Verlauf einer Redaktions-Mail steht – mit Zitat und Gmail-ID.
- `tools/ghost.py` veröffentlicht nur mit einer Freigabe, die zum Stand passt, den Till in der Vorschau gesehen hat.
- `tools/sperre.py` blockiert direkte Ghost-Aufrufe, Änderungen an der Sperre und Löschen im Gedächtnis.
- Ehrlich: Das sind feste Regeln im Code, keine kryptografische Sicherung.
