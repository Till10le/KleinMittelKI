# Prüfung: eu-eurobarometer-ki-unternehmen

Datum: 19.10.2026 · Prüfer (unabhängig)

## Ergebnis: NICHT BESTANDEN

Ein Mangel bleibt offen (Titel, Punkt 1). Alle übrigen Mängel habe ich direkt in `beitrag.md` behoben (siehe unten).

## Gegengelesene Quellen (selbst abgerufen am 19.10.2026)

- Pressemitteilung IP/26/2160 (DE) über die Presscorner-Schnittstelle: 14.10.2026, 42 %, 21 %, 47/36/30 %, 61 %, 75 %, 90 % / 2 %, 50/49/48 %, 49 % kein Vertrauen. Keine Stichprobengröße und keine Feldzeit genannt.
- DG-EMPL-Meldung vom 14.10.2026 (https://employment-social-affairs.ec.europa.eu/news/growing-use-ai-european-companies-2026-10-14_en) und die offizielle Infografik als PDF darin: 12.826 Interviews, CATI, 1 bis 749 Beschäftigte, 27 Staaten, Feldzeit 20.03. bis 13.04.2026, 90 % = 52 + 38 (bei den Nutzern). **Keine Werte nach Größenklassen.**
- Bericht als Original-PDF bei europa.eu: nicht gefunden. Die Eurobarometer-Seite 3696 liefert ohne JavaScript nur Metadaten, eine Suche auf europa.eu ergab keinen direkten PDF-Link.
- Spiegel-PDF (bollettinoadapt.it): 41/49/56/64 % wörtlich bestätigt. Ebenfalls bestätigt: die Hürden nach Größe, die Definition „can be powered by Artificial Intelligence or not“, „the term 'AI' is sometimes used alone in this report“ und Q3 nur an Nutzer. Katalognummer KE-01-26-085-EN-N und ISBN stehen im PDF.

## Checkliste

| Nr. | Punkt | Ergebnis |
|---|---|---|
| 1 | Zahlen, Daten, Namen | Alle Zahlen im Text stimmen mit dem Original überein. **Mangel Titel**, siehe unten. Die Basis der 90 % fehlte (behoben). |
| 2 | Grundgesamtheit und Einschränkungen | ok: 1 bis 749 Beschäftigte, private Betriebe, 27 Staaten, Selbstauskunft (Bildunterschrift und Fußzeile), keine reine KI-Quote |
| 3 | Originalveröffentlichung verlinkt | ok: Eurobarometer-Seite 3696 und IP/26/2160. Der Spiegel ist nicht verlinkt (richtig so). |
| 4 | Ich-Aussagen | ok: Die Einordnung ist komplett als Vorschlag im INTERN-Absatz markiert, die Frage an Till ist gestellt (F1). |
| 5 | Platzhalter | ok, keine |
| 6 | Format und Längen | ok: H2 exakt, Abschnitte 92/99/98/19 Wörter, insgesamt ca. 330 plus Grafiksatz. Teaser 154 Zeichen, Für KMU 109 Zeichen. Der Einstieg vor „Was ist passiert?“ war ein Mangel (behoben). |
| 7 | Rubrik, Kategorie, Tags | ok: Aktuell / Studien & Zahlen + #empfehlung |
| 8 | Zeile „Für KMU“ | ok |
| 9 | Ton und Verbote | ok |
| 10 | KMU-Bezug | ok: Größenklassen, 20 bis 150 Beschäftigte, Geschäftsführung, Schicht- und Einsatzplanung |
| 11 | Grafik | ok: Balken-Karte im CI, Werte = Spiegel-PDF, Titel ist eine Aussage, Fußzeile mit Quelle, Stand und Selbstauskunft, Alt-Text vorhanden, Bildunterschrift als Datenkarte. Der Satz „Was die Grafik zeigt“ fehlte (behoben). Die Social-Kachel ist ok. |
| 12 | Vorschaubild | ok: drei Zeilen, Logo, Lime-Kante. **Muss nach der Titeländerung neu gerendert werden.** |
| 13 | Ghost-Vorschau | entfällt in diesem Lauf |
| 14 | Vergleich mit Referenz (bitkom, kfw) | Aufbau gleich, nachdem ich den Einstieg entfernt habe. lexical.py läuft: 5 H2, 14 Knoten. |

## Offener Mangel

**Titel „KI bei Arbeit und Personal: Warum kleine Betriebe noch zögern“** (Frontmatter `titel`, Vorschaubild)

1. „KI“ allein ist falsch. Gezählt sind KI **oder** automatisierte Systeme. Text, Teaser, Grafik und Bildunterschrift sagen das korrekt, nur der Titel nicht. Ausgerechnet der Titel wird aber geteilt.
2. „Warum kleine Betriebe noch zögern“ trägt die Umfrage nicht. Die Hürden-Frage ging an alle, und kleine Betriebe nennen die Hürden *seltener* als große (Rechtsunsicherheit 49 % bei 1–9 gegenüber 61 % bei 250–749). Der Beitrag sagt das selbst („Auffällig ist …“). Der Titel verspricht eine Erklärung, die die Daten für kleine Betriebe nicht liefern. Den Fehler der Mail-Headline hat die Titeländerung damit nur zur Hälfte behoben.

Vorschlag (bitte Till vorlegen, danach das Vorschaubild neu erzeugen):
„KI und Automatik bei Schichtplan und Personal: Was Betriebe in der EU bremst“
oder kürzer: „Software für Arbeit und Personal: Was Betriebe in der EU bremst“.

## Direkt korrigiert in beitrag.md

1. Den Einstieg vor „Was ist passiert?“ entfernt. Keine veröffentlichte Nachricht hat einen Einstieg vor dem ersten H2 (bitkom, kfw, schatten-ki, werbung-chatgpt u. a.). Den INTERN-Hinweis dazu habe ich angepasst.
2. „90 Prozent lassen am Ende Menschen entscheiden“ geändert in „90 Prozent **der Nutzer** …“. Frage 3 ging nur an Nutzer.
3. Den Satz „Was die Grafik zeigt: …“ nach der Grafik ergänzt. Er ist Pflicht bei Daten-Karten aus Studien (Skill `kmk-ci-grafik`, Regel 5).
4. „Größere Betriebe nennen diese Hürden häufiger“ geändert in „meist häufiger“. Bei den Kosten liegen die Betriebe mit 250–749 Beschäftigten bei 54 % und damit unter denen mit 50–249 (56 %). Für fehlendes Fachwissen gibt es nur zwei Werte.
5. INTERN-Absatz präzisiert: Die Größenklassen-Werte 41/49/56/64 und die Aussage zu den Hürden nach Größe stammen **nur aus dem Spiegel-PDF**. Sie stehen nicht in der Pressemitteilung und nicht in der Infografik. Vorher hieß es pauschal „Zahlen decken sich mit der Pressemitteilung“, das stimmte für diese Werte nicht.

## Hinweis für Till

Die Werte nach Betriebsgröße sind plausibel (Katalognummer und ISBN der Kommission im PDF). Sie sind aber nicht bei europa.eu selbst gegengelesen. Vor der Freigabe einmal die Eurobarometer-Seite 3696 im Browser öffnen und im Bericht nach „Adoption rises steadily with company size“ suchen.

---

## Runde 2 – 19.10.2026

## Ergebnis: BESTANDEN

- **Titel** „Kosten, Recht, Wissen: Was EU-Betriebe bei KI und Personalsoftware bremst“ ist von den Daten gedeckt:
  - Kosten 50 %, Recht 49 % und Wissen 48 % sind die drei häufigsten Hürden. Die Frage ging an alle Befragten.
  - „KI und Personalsoftware“ trifft die Frage nach „AI or automated systems“ im Bereich Arbeit und Personal.
  - Der Titel stellt keine Behauptung mehr über kleine Betriebe auf.
- **Teaser:** 144 Zeichen, wiederholt den Titel nicht, „solche Systeme“ ist sauber. Die INTERN-Notiz „Titel von der Redaktion geändert, Till entscheidet“ ist vorhanden.
- **Vorschaubild** (png und jpg) angesehen: Titel in drei Zeilen, nichts abgeschnitten, Kategorie mit Lime-Strich, Logo, kleinmittelki.de und Lime-Kante sind da.
- **Nichts zurückgedreht:**
  - Der Einstieg ist weiterhin entfernt.
  - Die Stellen „90 Prozent der Nutzer“, „Was die Grafik zeigt“, „meist häufiger“ und der Spiegel-Hinweis im INTERN-Absatz stehen noch.
- **lexical.py** läuft: 5 Zwischenüberschriften in richtiger Reihenfolge, 14 Knoten.
- **Kleinkorrektur:** Im INTERN-Absatz „JavaScript; Die“ zu „JavaScript. Die“ korrigiert.
- **Hinweis für Till**, kein Mangel: Die Werte nach Betriebsgröße (41/49/56/64 %) sind nur am Spiegel-PDF geprüft. Vor der Freigabe bitte auf der Eurobarometer-Seite gegenlesen (steht so im INTERN-Absatz).
