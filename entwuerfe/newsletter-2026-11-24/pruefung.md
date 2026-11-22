# Prüfung – Newsletter #8 (Di 24.11.2026)

Datum: So 22.11.2026, Redaktions-Lauf 7:47 · Prüfer (unabhängig)
Geprüft: `entwuerfe/newsletter-2026-11-24/beitrag.md` gegen Skill `kmk-newsletter`, `kmk-schreibstil`, CLAUDE.md, Originalquellen.

## Ergebnis: BESTANDEN

Eine kleine Korrektur direkt vorgenommen (siehe unten). Keine offenen Mängel.

## Checkliste

**Fakten**
1. ok – Bitkom-Presseinformation „Internet-Suche im Wandel: Die Hälfte nutzt bereits KI-Chats“ (Berlin, 20. November 2025) am 22.11.2026 selbst geladen und gelesen. Stimmen wörtlich bzw. sinngemäß korrekt: 50 Prozent „zumindest gelegentlich“, zwei Drittel bei 16- bis 29-Jährigen (5+11+20+30 = 66), überwiegend 7 %, ausschließlich 5 %, nur klassisch 47 %, telefonisch, 1.156 Personen ab 16 Jahren, KW 39–43 2025 („Herbst 2025“ passt). Kopfzeile „Bitkom · November 2025“ stimmt.
   Handwerksblatt-Original „Mit KI leichter Fachkräfte für den Handwerksbetrieb finden“ (1. Oktober 2026) selbst gelesen: Dachdeckerbetriebe in Düsseldorf, „die modern ausbilden“, Betrieb „ganz weit oben“; Website, Bewertungen, Presseberichte als Grundlage (HWK-Beraterin Sarah Eichhorn); Arbeitszeiten, Vergütungsrahmen, Ansprechpartner. „im Oktober“ stimmt.
   Leitfaden (veröffentlicht 20.09.) gelesen: fünf Fragen, vier Prüfpunkte, „Bei einer einzigen Antwort übernimmt er meistens, was dort steht“, Fehler „von der eigenen Website“ – korrekt wiedergegeben.
2. ok – Grundgesamtheit (Internetnutzer ab 16 in Deutschland), Methode, Alter der Zahl, Zählweise („zumindest gelegentlich“) und Grenze (Suche allgemein, nicht Betriebe/Lehrstellen) stehen im Block.
3. ok – Quelle verlinkt auf die Bitkom-Originalveröffentlichung (HTTP 200). YouGov als schwächere Quelle begründet verworfen (quellen.md).

**Ehrlichkeit**
4. ok – Keine Ich-Sätze. Einstieg, Abschnitt 01, Lesart im Zahlenblock und Gedanke im INTERN-Absatz als Vorschlag markiert.
5. ok – Keine `[TILL: …]`- oder `[GRAFIK: …]`-Platzhalter.

**Format (kmk-newsletter)**
6. ok – Titel „#8: Was die KI über deinen Betrieb erzählt“ 42 Zeichen (≤ 60); Teaser 119 Zeichen (105–130), Aufzählung, nicht gleich dem Titel; zwei Alternativen im INTERN. Nummer #8 = letzte Ausgabe im Index (#7, 17.11.) + 1; kein anderer Entwurf für den 24.11. im Index oder in `entwuerfe/`. „Hallo,“ eigener Absatz, Einstieg 2 Sätze. Zahlenblock-HTML zeichengenau gegen die Vorlage im Skill abgeglichen (nur Platzhalter ersetzt). „Quelle: […](…)“ darunter. Gedanke 30 Wörter (≤ 40), greift das Thema auf. Button, Trennlinie, Schluss wörtlich, „Bis bald“, „Till“.
7. ok – Tag `#newsletter`, Kategorie leer.
8. entfällt (kein Aktuell-Beitrag).
   Bookmark-Karten: URL, Titel und Teaser beider Karten wörtlich identisch mit `redaktion/blog-index.json` (Stand 22.11.2026 06:50); alle drei Links liefern HTTP 200. Beide Beiträge sind veröffentlicht (status „published“); kein unveröffentlichter Beitrag im Text.

**Wiederholung**
- ok – Gegen `entwuerfe/newsletter-2026-10-27` bis `-11-17` und die Ausgaben #1–#7 in `redaktion/referenz/` geprüft: keiner der beiden Beiträge war verlinkt, die Bitkom-Zahl zur Internet-Suche kommt weder in einem Newsletter noch im Blog-Index vor.

**Ton und Verbote**
9. ok – Keine Floskeln, kein Hype, keine Gefühlswörter, keine Rhythmus-Versprechen, keine CTAs außer dem festen Schluss, kein Arbeitgeber-/Handelsbezug.
10. ok – KMU-Bezug: Dachdeckerbetrieb, Ausbildungsbetriebe, Bewerbersuche/Website als Prozess.

**Darstellung / Technik**
11.–13. Für den Newsletter nur Zahlenblock (Vorlage wörtlich); kein Vorschau- oder Titelbild vorgesehen. Ghost-Vorschau noch nicht vorhanden (Entwurf noch nicht in Ghost).
- `python3 tools/lexical.py entwuerfe/newsletter-2026-11-24/beitrag.md` läuft durch (Exit 0; Zwischenüberschriften 01–03 erkannt; INTERN nicht im Ergebnis).
14. ok mit Hinweis – Aufbau wie #7 (ein Abschnitt mit zwei Karten, dann Zahl und Gedanke). Neu ist nur die Überschrift-Art „Aus dem Archiv“, die der Skill nicht kennt; Grund (kein neuer Beitrag freigegeben) steht im INTERN-Absatz. Till entscheidet.

## Direkt behoben

- Einstieg, Satz 2: „eine Zahl dazu, wie viele …“ nach „Dazu zwei Beiträge …“ – doppeltes „dazu“ gestrichen: „Dazu zwei Beiträge aus dem Archiv und eine Zahl, wie viele Menschen inzwischen so suchen.“ lexical.py danach erneut erfolgreich.

## Hinweise (kein Mangel, für Till sichtbar)

- Abschnitt 01, Satz 1 („Wer eine KI … fragt, bekommt einen bestimmten Betrieb ganz weit oben genannt“) klingt allgemeingültig; das Handwerksblatt beschreibt eine einzelne Beobachtung zu einer konkreten Anfrage. Wortgleich zum veröffentlichten Azubi-Beitrag, daher vertretbar. Präziser wäre: „… bekam laut Handwerksblatt einen bestimmten Betrieb ganz weit oben genannt.“
- Azubi-Beitrag wurde am 12.10. aus Ausgabe 2 herausgenommen (entscheidungen.md: „auf zwei Beiträge reduziert“); der INTERN-Absatz weist offen darauf hin.
- Kommt bis Mo 18:47 eine Freigabe für einen Hauptbeitrag, muss die neue Fassung erneut geprüft werden (Titel, Teaser, Nummerierung, Karte aus dem dann aktuellen Index).
