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

Interne Tags (mit `#`, nicht öffentlich): `#empfehlung` (jede Nachricht mit Originalquelle), `#notiz` (eigene Texte,
Anleitungen, Praxistests), `#newsletter` (Newsletter-Ausgaben), `#zur-freigabe` (Entwurf wartet auf Till).

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
  OFFEN: In welchem Ghost-Feld sie steht, ist noch nicht dokumentiert. Vor dem ersten Aktuell-Beitrag einen bestehenden
  Beitrag mit `python3 tools/ghost.py get <slug> --raw` lesen, das Feld finden und hier eintragen.

## Format 1: Nachricht (Aktuell)

Zwischenüberschriften (H2) exakt so – das Theme erzeugt daraus Nummerierung 01–04 und die hervorgehobene Box:

1. `Was ist passiert?` – 60–100 Wörter, W-Fragen, sachlich.
2. `Meine Einordnung` – 80–120 Wörter, Ich-Form: Relevanz, Chancen, Grenzen, was übersehen wird.
3. `Was bedeutet das für den Mittelstand?` – 60–100 Wörter, konkrete Prozesse, Rollen, Entscheidungen, Betriebsgrößen.
   Gibt es keinen sinnvollen Bezug: offen sagen.
4. `Ein Gedanke zum Mitnehmen` – höchstens 40 Wörter, genau ein Gedanke, gern als Frage.
5. `Zum Originalartikel` – danach eine Bookmark-Karte mit der echten Quelle,
   Beschreibung „Originalveröffentlichung vom TT.MM.JJJJ“.

Tags: Kategorie + `#empfehlung`. Umfang ca. 300 Wörter.

## Format 2: Anleitung (Wissen / Leitfäden)

H2: `Warum das gerade jetzt zählt` · `So machst du den Test` · `Worauf du bei den Antworten achtest` · `Ein Gedanke zum Mitnehmen`.
Tags: Kategorie + `#notiz`. Kein Quellenabschnitt nötig, Quellen im Text verlinken.

## Format 3: Langtext (Wissen / Grundlagen, Leitfäden)

- Einleitung (2 Absätze) mit konkreter Alltagsszene.
- Box „Das Wichtigste in 30 Sekunden“ (Baustein `kurz`) mit fünf Punkten direkt nach der Einleitung.
- Eigene H2-Abschnitte, 3–4 Grafiken.
- Endet mit `Was das für den Mittelstand bedeutet` (mit „**Meine Einordnung:**“-Absatz) · `Ein Gedanke zum Mitnehmen` · `Quellen`
  (mit Abrufdatum „Abgerufen am …, zuletzt geprüft am …“).
- 8–9 Minuten Lesezeit.

## Format 4: Lagebericht (Wissen / Lageberichte)

- Serienkopf „Status Quo“ mit „Ausgabe <Monat Jahr> · erscheint vierteljährlich“ (Baustein `serie`).
  OFFEN: Rhythmus (monatlich oder vierteljährlich) ist mit Till zu klären.
- Nummerierte Abschnitte (Baustein `abschnitt`): 01 Verbreitung · 02 Anwendungen · 03 Integration · 04 Hürden · 05 Wirkung.
- Je Abschnitt mindestens eine Balkengrafik oder Kennzahl.
- Box „Meine Einordnung“ (Baustein `einordnung`), dann „Quellen & Datenbasis“ (Baustein `quellen`) mit nummerierten Quellen [1]–[n]
  und Hinweis zur Vergleichbarkeit der Erhebungen.

## Format 5: Praxistest (Praxistests)

- Serienkopf „Selbst ausprobiert“ mit Untertitel, z. B. „Erfahrungsbericht · Generalversammlung am 18. September 2026“.
- H2: `Welches Problem soll gelöst werden?` · `Wie lief der Test ab?` · `Was ist dabei herausgekommen?` · `Wo sind die Grenzen?` · `Mein Fazit`.
- Pflicht: Prompt-Kasten „Mein Prompt an Claude“ (Baustein `prompt`), Grenzen- oder Fehler-Kasten (`hinweis`), Transparenz-Absatz.
- Nie Ergebnisse eintragen, die Till nicht selbst ermittelt hat. Fehlen sie: Platzhalter `[TILL: Ergebnis eintragen]` und im Board vermerken.
- Tags: `KI in der Praxis` + `#notiz`. Vorlage in Ghost: Entwurf „KI in der Praxis – Beitragsvorlage“.

## Vorschaubild

Jeder Beitrag bekommt ein eigenes Vorschaubild (Skill `kmk-ci-grafik`, `tools/vorschaubild.py`).
