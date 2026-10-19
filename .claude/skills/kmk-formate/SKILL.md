---
name: kmk-formate
description: Die festen Beitragsformate von KLEIN. MITTEL. KI. (Nachricht, Anleitung, Langtext, Lagebericht, Praxistest) mit exakten Zwischenüberschriften, Längen, Tags und Rubrik-Regel. Laden, bevor ein Beitrag geschrieben, eingeordnet oder geprüft wird.
---

# Beitragsformate und Rubriken

## Rubriken und Kategorien (Ghost-Tags)

| Rubrik | Kategorie (öffentlicher Tag) | Was hineingehört | Format |
|---|---|---|---|
| 01 · Aktuell | `Entwicklungen` | Neue Funktionen, Produkte, Regeln, Ereignisse mit KMU-Bezug | Nachricht |
| 01 · Aktuell | `Studien & Zahlen` | Neue Studien, Umfragen, Statistiken | Nachricht |
| 02 · Wissen | `Grundlagen` | Begriffe und Zusammenhänge erklärt | Langtext |
| 02 · Wissen | `Leitfäden` | Anleitung, Selbsttest, Rechtslage einfach erklärt | Anleitung oder Langtext |
| 02 · Wissen | `Lageberichte` | Eigene Analyse mehrerer Quellen: Wo steht der Mittelstand? | Lagebericht |
| 03 · Praxistests | `KI in der Praxis` | Nur eigene Tests von Till mit echten Ergebnissen | Praxistest |

Interne Tags (mit `#`, nicht öffentlich) – so in allen veröffentlichten Beiträgen (geprüft 19.10.2026):
`#empfehlung` (jede Nachricht in Aktuell), `#wissen` (jeder Beitrag in Wissen: Grundlagen, Leitfäden, Lageberichte),
`#status-quo` (zusätzlich beim Lagebericht), `#notiz` (Praxistests), `#newsletter` (Newsletter-Ausgaben),
`#zur-freigabe` (Entwurf wartet auf Till, wird beim Veröffentlichen entfernt).

**Entscheidungsregel:**
1. Hat Till es selbst ausprobiert und Ergebnisse ermittelt? → Praxistests.
2. Konkreter Anlass mit Datum und Originalquelle? → Aktuell. Studie/Umfrage/Statistik → `Studien & Zahlen`, sonst `Entwicklungen`.
3. Bleibt der Text in sechs Monaten gültig? → Wissen. Erklärt Begriffe → `Grundlagen`. Sagt, was zu tun ist → `Leitfäden`.
   Wertet mehrere Quellen zur Lage aus → `Lageberichte`.
4. Passt nichts: nicht schreiben, im Themenboard als Frage an Till markieren. Neue öffentliche Kategorien legt nur Till an.

## Titel und Teaser

- Titel: eine Frage oder klare Aussage, oft mit Doppelpunkt. Beispiel: „Schatten-KI: Deine Mitarbeiter nutzen KI vielleicht längst. Weißt du, wofür?“
- Teaser (`custom_excerpt`): höchstens zwei Sätze, sachlich, wiederholt nicht die Überschrift, 90–160 Zeichen,
  ähnlich lang wie die bestehenden Teaser (sonst werden die Karten ungleich hoch).
- Aktuell-Beiträge brauchen zusätzlich die Zeile „**Für KMU:** …“ (ein konkreter Satz für Betriebe).
  Im Frontmatter als `fuer_kmu: …` (ohne „Für KMU:“ davor). In Ghost steht der Satz im Feld **`twitter_description`**;
  das Theme zeigt ihn auf der Startseite als „**Für KMU:** …“ unter der Aktuell-Karte (geprüft am 18.10.2026 an sechs
  Beiträgen). Länge wie bei den bestehenden: ein Satz, 50–120 Zeichen. Achtung: Dasselbe Feld ist auch die
  Vorschau-Beschreibung beim Teilen auf X – der Satz muss also ohne den Beitrag verständlich sein.

## Format 1: Nachricht (Aktuell)

Zwischenüberschriften (H2) exakt so – das Theme erzeugt daraus Nummerierung 01–04 und die hervorgehobene Box:

1. `Was ist passiert?` – 60–100 Wörter, W-Fragen, sachlich.
2. `Meine Einordnung` – 80–120 Wörter, Ich-Form: Relevanz, Chancen, Grenzen, was übersehen wird.
3. `Was bedeutet das für den Mittelstand?` – 60–100 Wörter, konkrete Prozesse, Rollen, Entscheidungen, Betriebsgrößen.
   Gibt es keinen sinnvollen Bezug: offen sagen.
4. `Ein Gedanke zum Mitnehmen` – höchstens 40 Wörter, genau ein Gedanke, gern als Frage.
5. `Zum Originalartikel` – danach eine Bookmark-Karte mit der echten Quelle,
   Beschreibung „Originalveröffentlichung vom TT.MM.JJJJ“.

Tags: Kategorie + `#empfehlung`. Umfang 260–330 Wörter; mit Schaubild bis ca. 460 Wörter.
Höchstens eine Grafik, nur wenn sie den Kern klarer macht – Vorbild: „Wenn der Meister in Rente geht“.
Neu (Till, 19.10.2026): Hat die Meldung eine starke, belegte Zahl, bekommt sie eine Kennzahl-Grafik nach `Was ist passiert?`.

## Format 2: Anleitung (Wissen / Leitfäden)

H2: `Warum das gerade jetzt zählt` · `So machst du den Test` · `Worauf du bei den Antworten achtest` · `Ein Gedanke zum Mitnehmen`.
Tags: `Leitfäden` + `#wissen`. Kein Quellenabschnitt nötig, Quellen im Text verlinken. Umfang ca. 550 Wörter.

**Variante Rechtslage einfach erklärt** (Vorbild „Muss ich KI-Bilder jetzt kennzeichnen?“): Einstieg mit Alltagsszene in Du-Form,
dann die Nachricht-Gliederung (`Was ist passiert?` … `Zum Originalartikel`), ca. 1.800 Wörter, zwei HTML-Karten
(Rollen/Fälle und Prüfliste aus `urteil-und-pruefliste`), Bildunterschrift „Vereinfachte Orientierung, keine Rechtsberatung …“.
Tags `Leitfäden` + `#wissen`.
Neu (Till, 19.10.2026): Ab ca. 1.000 Wörtern auch hier die Box „Das Wichtigste in 30 Sekunden“ (Baustein `kurz`) nach dem Einstieg.

## Format 3: Langtext (Wissen / Grundlagen, Leitfäden)

- Einleitung (2 Absätze) mit konkreter Alltagsszene.
- Box „Das Wichtigste in 30 Sekunden“ (Baustein `kurz`) mit fünf Punkten direkt nach der Einleitung.
- Eigene H2-Abschnitte, 3–4 Grafiken.
- H2 als Fragen oder klare Aussagen aus Lesersicht („Was ist überhaupt ein KI-Agent?“, „Warum Zugriff das eigentliche Risiko ist“).
- Gern ein praktischer Abschnitt `Zum Ausprobieren: …` mit nummerierten Schritten und Beispiel-Prompt (Vorbild Agenten-Beitrag).
- Endet mit `Was das für den Mittelstand bedeutet` **oder** `Meine Einschätzung` (Ich-Form, nur mit Tills Worten, sonst INTERN-Vorschlag)
  · `Ein Gedanke zum Mitnehmen` · `Quellen` (verlinkte Originale mit Datum; „Abgerufen am …, zuletzt geprüft am …“).
- 1.900–2.000 Wörter (8–9 Minuten Lesezeit), 4–5 PNG-Schaubilder im Karten-System. Tags `Grundlagen`/`Leitfäden` + `#wissen`.

## Format 4: Lagebericht (Wissen / Lageberichte)

- Serienkopf „Status Quo“ mit „Ausgabe <Monat Jahr> · erscheint vierteljährlich“ (Baustein `serie`).
  OFFEN: Rhythmus (monatlich oder vierteljährlich) ist mit Till zu klären.
- Nummerierte Abschnitte (Baustein `abschnitt`): 01 Verbreitung · 02 Anwendungen · 03 Integration · 04 Hürden · 05 Wirkung.
- Je Abschnitt mindestens eine Balkengrafik oder Kennzahl.
- Ca. 900 Wörter. Tags `Lageberichte` + `#wissen` + `#status-quo`.
- Box „Meine Einordnung“ (Baustein `einordnung`), dann „Quellen & Datenbasis“ (Baustein `quellen`) mit nummerierten Quellen [1]–[n]
  und Hinweis zur Vergleichbarkeit der Erhebungen.

## Format 5: Praxistest (Praxistests)

- Serienkopf „Selbst ausprobiert“ mit Untertitel, z. B. „Erfahrungsbericht · Generalversammlung am 18. September 2026“.
- H2: `Welches Problem soll gelöst werden?` · `Wie lief der Test ab?` · `Was ist dabei herausgekommen?` · `Wo sind die Grenzen?` · `Mein Fazit`.
- Pflicht: Prompt-Kasten „Mein Prompt an Claude“ (Baustein `prompt`), Grenzen- oder Fehler-Kasten (`hinweis`), Transparenz-Absatz.
- Erlaubt: ein zusätzlicher Nutzwert-Abschnitt vor `Wo sind die Grenzen?`, z. B. „Sechs Regeln für dein nächstes Werbemittel“.
- Bilder: echte Fotos und anonymisierte Screenshots aus dem Test, Bildunterschrift erklärt, was man sieht.
- 700–1.200 Wörter.
- Nie Ergebnisse eintragen, die Till nicht selbst ermittelt hat. Fehlen sie: Platzhalter `[TILL: Ergebnis eintragen]` und im Board vermerken.
- Tags: `KI in der Praxis` + `#notiz`. Vorlage in Ghost: Entwurf „KI in der Praxis – Beitragsvorlage“.

## Vorschaubild

Jeder Beitrag bekommt ein eigenes Vorschaubild (Skill `kmk-ci-grafik`, `tools/vorschaubild.py`).
