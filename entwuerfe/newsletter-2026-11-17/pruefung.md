# Prüfung: newsletter-2026-11-17 (#7, Fassung 1)

Datum: 15.11.2026 (Lauf So, Sonntags-Teil) · Prüfer · Maßstab: `.claude/agents/pruefer.md`, Skills kmk-newsletter, kmk-schreibstil, CLAUDE.md.
Gelesen: Original https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence (am 15.11.2026 selbst abgerufen, erreichbar; erste 100.000 von rund 216.000 Zeichen, die Stelle liegt darin), `entwuerfe/modellwahl-kanonen-auf-spatzen/beitrag.md` und `quellen.md`, `redaktion/referenz/modellwahl-kanonen-auf-spatzen.html`, `redaktion/referenz/chatgpt-claude-gemini-ki-modelle-erklaert.html` und `.json`, Newsletter #5 (11-03) und #6 (11-10), `redaktion/blog-index.json`. `python3 tools/lexical.py` läuft durch (rc 0).

## Ergebnis: NICHT BESTANDEN

Ein inhaltlicher Mangel (Grundlage-Absatz). Ein Zeichenzahl-Mangel im INTERN-Absatz ist direkt behoben. Alles andere ist ok.

## Mängel

1. **01, Grundlage-Absatz · „wofür Namen wie Opus, Sonnet und Haiku stehen“ steht so nicht im Oktober-Beitrag.**
   Fundstelle: „Im Beitrag vom Oktober steht, warum ChatGPT das Fahrzeug ist und das Modell der Motor, und wofür Namen wie Opus, Sonnet und Haiku stehen.“
   Problem: Im Text des veröffentlichten Beitrags (Referenz-HTML und Lexical aus Ghost) kommen Opus, Sonnet und Haiku nicht vor. Es gibt nur die Grafik „Übersicht: große, mittlere und kleine Modelle von OpenAI, Anthropic und Google“ (kmk-ki-modelle-g3-v2.png). Die konnte ich nicht ansehen, weil der Ghost-Speicher gesperrt ist. Belegt ist nur der Teil mit Fahrzeug und Motor („ChatGPT, Claude und Gemini sind die Fahrzeuge. Das Modell ist der Motor.“) und „Jeder Anbieter staffelt seine Modelle.“ Die Angabe in quellen.md („Namens-Decoder“) ist eine Notiz aus der Recherche, kein Beleg.
   Korrekturvorschlag: „… warum ChatGPT das Fahrzeug ist und das Modell der Motor, und warum jeder Anbieter seine Modelle in große, mittlere und kleine staffelt.“ Oder Till bestätigt, dass die Grafik die Claude-Namen nennt.

## Direkt behoben

- INTERN, Alternative A: Der Teaser hatte 131 Zeichen, erlaubt sind 105 bis 130. „eine Zahl zu Tabellen in der KI“ ist jetzt „eine Zahl zu Tabellen“ (121 Zeichen).

## Checkliste

- **Fakten 7 von 25 / 25 von 25 / Zwölftel:** ok. Original wörtlich: „Anthropic asked 25 aggregate questions … over a 1,862-row public CSV“, „Pasted into the prompt … Claude Sonnet 5 answered 7 of 25 questions correctly. Uploaded, with code execution, it answered all 25, and the run cost about a twelfth as much.“ Die Grafik nennt 5,01 $ gegenüber 0,40 $. „directional, not guarantees“ ist im Block als „richtungsweisend, keine Garantie“ wiedergegeben. Schnittstelle statt Chat-App ist genannt, ebenso der Hinweis „plausibel, aber nicht gemessen“. Grundgesamtheit (25 Fragen, eine Tabelle, ein Modell) ist genannt.
- **Originalquelle verlinkt:** ok, Hersteller-Doku. Keine Zweitverwertung.
- **Kopfzeile „Anthropic · November 2026“:** ok, mit Hinweis. Die Seite hat kein Datum, deshalb steht dort der Abrufmonat. Das steht im INTERN-Absatz und in der Quellenzeile („abgerufen 15.11.2026“).
- **01 gegen veröffentlichten Beitrag:** ok bis auf Mangel 1. Diese Punkte stehen alle im Beitrag: Ingenieurbüro mit 40 Leuten und Terminbestätigung, drei Sätze, „Im Firmenkonto ist das stärkste Modell eingestellt“, Rechtschreibung bis Vertragsprüfung, „Billig ist nicht immer günstig“, Nacharbeit, Limits/Wartezeit/Strom im Abo, Geld erst über die Schnittstelle, Hausverwaltung mit Mieteranfragen, Preisliste, Faustregel in drei Stufen, „Die eigene Faustregel in einer halben Stunde“ mit drei Aufgaben.
- **Bookmark-Karten:** ok. Titel und Teaser beider Karten sind wörtlich wie im Blog-Index, die URLs stimmen.
- **Wiederholung:** ok. #6 (Powerpoint, IAB, 86 %) und #5 (Eurobarometer, Nicht jedes Problem, 90 %) werden nicht wiederholt. Hinweis: Den Oktober-Beitrag hatte schon #2 (13.10.) verlinkt. Er ist jetzt bewusst als Grundlage gesetzt (Tills Wunsch, quellen.md Abschnitt 9). Das ist keine Wiederholung aus der Vorwoche.
- **Kandidat ki-recherche-assistent-selbstversuch:** ok, er steht nicht im Lesertext, nur im INTERN-Absatz.
- **Ich-Form / Vorschläge:** ok. Die Ausgabe hat keine Ich-Sätze. Alle redaktionellen Stellen stehen als VORGESCHLAGEN im INTERN-Absatz.
- **Platzhalter:** ok, es gibt keine.
- **Aufbau nach Vorlage:** ok. INTERN, „Hallo,“, Einstieg mit zwei Sätzen, 01 „Neu im Blog:“ mit drei Absätzen und Karte (plus Grundlage-Absatz mit zweiter Karte), 02 Zahl mit Quellenzeile, 03 Gedanke, Button, `---`, Schluss **wörtlich**, „Bis bald“, „Till“. Das Zahlenblock-HTML ist wörtlich nach Vorlage.
- **Längen:** ok. Titel 41 Zeichen (höchstens 60), Teaser 121 Zeichen (105–130), Gedanke 31 Wörter (höchstens 40). Alternativen: Titel 27 und 49 Zeichen, Teaser 121 (nach der Korrektur) und 116 Zeichen.
- **Frontmatter:** ok. Tag `#newsletter`, Kategorie leer, Nummer #7 (letzte im Index #6).
- **Ton / Verbote:** ok. Keine Floskeln, kein Hype, keine Gefühlswörter, keine Rhythmus-Versprechen, keine Vertriebs-CTAs, kein Bezug zu Arbeitgeber oder Handel.
- **KMU-Bezug:** ok. Ingenieurbüro mit 40 Leuten, Hausverwaltung, Auftragsliste und Stundentabelle, Teamrunde.
- **lexical.py:** ok, läuft durch.
