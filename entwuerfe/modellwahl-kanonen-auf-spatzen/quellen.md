# Quellen: modellwahl-kanonen-auf-spatzen

Angelegt im Chat mit Till am 10.11.2026 (Recherche vor der Themenfreigabe). Alle Quellen unten selbst gelesen
(WebFetch/WebSearch, Abruf 10.11.2026), außer wo „ungeprüft“ oder „Zweitquelle“ steht. Zahlen exakt wie in der Quelle.
Der Autor liest die Primärquellen vor dem Schreiben noch einmal (Preise und Modellnamen ändern sich schnell).

## Wichtig vorab: Was wir NICHT belegen können

- Tills Ausgangsthese („viele Unternehmen schießen mit Kanonen auf Spatzen, Mitarbeiter nutzen für alles das größte Modell“)
  ist **nicht durch eine Studie belegt**. Gesucht wurde nach Nutzungsdaten (Anteil der Anfragen an Spitzenmodelle bei
  einfachen Aufgaben) – nichts Belastbares gefunden.
- Nahe dran, aber nicht dasselbe:
  - Harmonic Security, AI Usage Index (Mai 2026, ca. 1,9 Mio. Nutzungsminuten, sechs KI-Werkzeuge): Beschäftigte bringen
    dieselben Aufgaben in jedes Werkzeug, das gerade offen ist – egal ob Firmen- oder Privatkonto, kostenlos oder bezahlt.
    Das betrifft das **Werkzeug**, nicht die Modellgröße. Anbieter ist Sicherheitsfirma (Eigenstudie).
    https://www.businesswire.com/news/home/20260520319293/en/ (Pressemitteilung, Original-Report ungeprüft)
  - Perplexity, „Inside the rise of enterprise AI model-switching“ (03.02.2026): Firmenkunden wechseln zunehmend zwischen
    Modellen; 43,6 % der Organisationen nutzten 2025 mehr als ein Modell. Herstellerangabe, eigene Plattform.
    https://www.perplexity.ai/hub/blog/inside-the-rise-of-enterprise-ai-model-switching
- **Folge für den Text:** Die These als Beobachtung bzw. Frage formulieren („Wer seinem Team ChatGPT oder Claude gibt,
  lässt oft jede Aufgabe über dasselbe Modell laufen“), nicht als Statistik. Wenn Till eigene Erfahrung hat → INTERN-Absatz,
  Till bestätigt.

## 1. Anthropic: Preise der Claude-Modelle (Hersteller-Doku)

URL: https://platform.claude.com/docs/en/about-claude/pricing (Abruf 10.11.2026). Preise in US-Dollar je 1 Mio. Tokens.

| Modell | Eingabe | Ausgabe | Einsatz laut Anthropic |
|---|---|---|---|
| Claude Haiku 5.5 (Prompt bis 100.000 Tokens) | 0,10 $ | 0,50 $ | viele, zeitkritische Aufgaben wie Einordnen, Herausziehen, Weiterleiten |
| Claude Sonnet 5.5 | 2 $ | 10 $ | beste Mischung aus Tempo und Intelligenz |
| Claude Opus 5.5 | 4 $ | 20 $ | lang laufende Agenten-Programmierung und Wissensarbeit |
| Claude Fable 5.2 | 8 $ | 40 $ | anspruchsvolles Denken, lange Agenten-Aufgaben |

- Haiku 5.5 über 100.000 Tokens Prompt: 0,50 $ / 2,50 $.
- Eigene Rechnung aus der Liste: Sonnet kostet je Token das **20-Fache** von Haiku, Opus das **40-Fache**, Fable das **80-Fache**.
- Eigene Rechnung, Beispielanfrage 2.000 Tokens rein / 300 raus: Haiku 5.5 ≈ 0,00035 $, Sonnet 5.5 ≈ 0,007 $,
  Opus 5.5 ≈ 0,014 $, Fable 5.2 ≈ 0,028 $. Je 1.000 Anfragen: 0,35 $ / 7 $ / 14 $ / 28 $.
  (Annahme 2.000/300 aus reflektlab.ai, Zweitquelle; die Rechnung selbst nur mit den offiziellen Preisen.)
- Aus derselben Seite, „Cost optimization strategies“: Haiku für einfache Aufgaben, Sonnet für die meisten Anwendungen,
  Opus für das komplexeste Denken.
- Batch-Verarbeitung (Antwort innerhalb 24 h): 50 % Rabatt. Neuere Modelle zählen ca. 30 % mehr Tokens für denselben Text.

## 2. Anthropic: „Choosing the right model“ (Hersteller-Doku)

URL: https://platform.claude.com/docs/en/about-claude/models/choosing-a-model (Abruf 10.11.2026)

- Zwei gleichwertige Wege (NICHT „immer klein anfangen“ – Fehler aus dem Modelle-Beitrag vom 08.10. nicht wiederholen):
  1. „Efficiency-first“: mit Haiku 5.5 starten, testen, nur bei konkreten Lücken hochstufen. Gut für viele einfache,
     gleichartige Aufgaben und knappe Budgets.
  2. „Capability-first“: mit Opus 5.5 starten, dann prüfen, ob Denkaufwand („effort“) oder ein kleineres Modell reichen.
     Gut für komplexes Denken, Fälle, in denen Genauigkeit wichtiger ist als Kosten.
- Matrix: Haiku 5.5 für niedrigste Wartezeit und niedrigsten Preis; Sonnet 5.5 für Alltagsarbeit (Texte, Datenanalyse);
  Opus 5.5 für komplexe Agenten- und Unternehmensaufgaben; Fable 5.2 für höchste Fähigkeit.
- Hinweis: Der Denkaufwand („effort“) innerhalb eines Modells sei oft ein besserer Hebel als der Modellwechsel.
- Für Tests empfiehlt Anthropic eigene Prüffälle mit echten Daten statt allgemeiner Ranglisten.

## 3. Anthropic: „Optimizing for cost and intelligence“ (Hersteller-Doku mit Messungen)

URL: https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence
(Abruf 10.11.2026; nur die ersten 100.000 von 172.000 Zeichen gelesen.)
**Schwäche:** Alles Anthropic-interne Messungen, laut Seite selbst „richtungsweisend, keine Garantie“. Benchmark-Namen im
Text nicht nennen (Themenregel: keine Benchmark-Rennen), nur als Größenordnung nutzen.

- Grundsatz: Modelle nach **Kosten je erledigter Aufgabe** vergleichen, nicht nach Preis je Token. Ein günstiges Modell,
  das scheitert, kostet den Versuch, die Wiederholung und die Folgen.
- Prüfungsfragen-Test (GPQA Diamond): Haiku 5.5 85 % richtig, Opus 5.5 und Sonnet 5.5 je 91 %. Haiku kostete je
  richtiger Antwort etwa **ein Zwanzigstel** von Opus 5.5 und etwa ein Zehntel von Sonnet 5.5.
- Recherche-Test (DeepResearch Bench II, 44 Aufgaben): Fable 5.2 kostete das **4,3-Fache** von Sonnet 5.5 ohne messbar
  besseres Ergebnis; Opus 5.5 lag 2,4 Punkte über Sonnet 5.5 bei 1,5-fachen Kosten.
- Programmier-Test: Opus 5.5 auf niedriger Stufe löste etwa so viele Aufgaben wie Sonnet 5.5 auf Standardstufe, für etwa
  7 % mehr je gelöster Aufgabe → das größere Modell ist nicht automatisch teurer pro Ergebnis. **Gegenpunkt für den Text.**
- Antwortlänge: gleicher Agent, nur die Vorgabe fürs Ergebnis geändert – eine Zeile 0,49 $, zwei Zeilen 0,57 $,
  ausführliches Memo 1,40 $ (2,8-fach), Genauigkeit im Rahmen der Messschwankung gleich (Claude Sonnet 5).
  → Tipp für jeden: „Frag nach der Antwort, die du liest, nicht nach der, die gründlich aussieht.“
- Tabelle als Datei statt eingefügt (Sonnet 5, 25 Fragen zu 1.862 Zeilen): eingefügt 7 von 25 richtig, 5,01 $;
  hochgeladen und per Code ausgewertet 25 von 25 richtig, 0,40 $ (etwa ein Zwölftel). Gilt für die API;
  Übertragung auf die Chat-Apps (Datei hochladen statt Tabelle reinkopieren) ist plausibel, aber nicht gemessen → so schreiben.
- Größter Hebel in der API laut Anthropic meist das Zwischenspeichern (Prompt Caching), nicht der Modellwechsel.
  Modell mitten im Gespräch zu wechseln, bricht diesen Speicher. → Für Betriebe mit eigener Anwendung erwähnen.

## 4. Anthropic Help Center: Nutzungsgrenzen in den Abos

- https://support.claude.com/en/articles/9797557-usage-limit-best-practices (Abruf 10.11.2026, Ausschnitt aus Suche; laut Prüfer 10.11.: nennt Modellwahl als Faktor, aber weder Opus noch Sonnet und keine Alltagsempfehlung): Die Nutzungsgrenze hängt u. a.
  von Nachrichtenlänge, Dateigröße, Gesprächslänge, Werkzeugen (Recherche, Websuche) **und der Modellwahl** ab.
- **VERALTET (Prüfrunde 1, 10.11.2026): Seite liefert HTTP 404, Aussage im Beitrag gestrichen.**
  https://support.claude.com/en/articles/9267304-about-team-and-enterprise-plan-usage (Abruf 10.11.2026): Für Team- und
  Enterprise-Plätze (Standard) verbraucht Opus das Wochenlimit schneller als Sonnet; Anthropic empfiehlt Sonnet für den Alltag.
  **Achtung:** Seite nennt noch Opus 4.5 / Sonnet 4.5 („Updated this week“, kein Datum) → nur den Grundsatz verwenden,
  keine Modellnamen daraus.
- https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan (Abruf 10.11.2026, Prüfer und Autor):
  Fable-Modelle zählen auf Max, Ultra und Premium-Plätzen in Team/Enterprise gegen das Wochenlimit, verbrauchen es schneller als
  andere Claude-Modelle, höchstens 50 % des Wochenlimits für Fable ohne Aufpreis. Auf Pro und Standard-Team-Plätzen sind
  Fable-Modelle nicht in den Limits enthalten und laufen von Anfang an über nutzungsabhängiges Guthaben (usage credits).
- Zweitquellen (nicht verwenden): Faktor „Opus ca. 5x schneller am Limit“ (usagebar.com) – nicht von Anthropic belegt.

## 5. OpenAI: Automatische Modellwahl in ChatGPT („Auto“)

**Nachtrag 12.11.2026 (Prüfrunde 3, Tills Screenshots im Chat):** Die Einträge unten zu „Auto“ und zur Admin-Umleitung
sind **VERALTET** (nicht gelöscht). Laut Suchergebnissen hat OpenAI das automatische Umschalten für Enterprise/Edu am
28.10.2026 eingestellt; Original (help.openai.com) in der Lauf-Umgebung gesperrt, deshalb im Text nicht verwendet.
Stand laut Tills eigenem ChatGPT-Konto (Screenshots 12.11.2026, Annahme Business): Chat – zwei Modelle (GPT-6, GPT-5.6 Sol)
und Regler „Denkaufwand“ (bis „Hoch“); Work – „Standard · Empfohlene Modellauswahl“ plus GPT-6.1 Sol, GPT-6.1 Terra,
GPT-6 Astra, GPT-6 Sol, GPT-6 Luna, GPT-5.6 Sol, GPT-5.6 Terra. Keine sichtbare „Auto“-Weiche. Modellnamen im Text nicht genannt.

- ChatGPT Enterprise/Edu Release Notes, https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes
  (Ausschnitt aus Suche, Abruf 10.11.2026): 26.06.2026 vereinfachte Modellauswahl („Balance aus Tempo und Denkaufwand“);
  Admin-Einstellung „Redirect Auto Router to Thinking mini“ – die automatische Weiterleitung kann auf ein kleineres
  Denkmodell gelenkt werden. 18.03.2026: Enterprise kann „Auto“ standardmäßig auf GPT-5.4 mini leiten.
- ChatGPT Release Notes https://help.openai.com/en/articles/6825453-chatgpt-release-notes: 28.04.2026 Modellwahl und
  Denkstufe direkt im Eingabefeld (Plus, Pro, Business).
- TechCrunch 12.08.2025 (Zweitquelle, nur Hintergrund): Mit GPT-5 führte OpenAI einen Router ein, der pro Anfrage
  zwischen schnellem und denkendem Modell wählt; danach kamen „Auto“, „Fast“, „Thinking“ als Auswahl zurück.
- **Für den Text:** „Die Technik davor gibt es in ChatGPT schon – sie heißt Auto.“ Vor Veröffentlichung im eigenen
  Business-Konto prüfen, wie die Auswahl heute heißt (Till oder Autor per Help Center). Aktuelle Modellnamen (GPT-6 …)
  nur aus OpenAI-Seiten, nicht aus Zweitquellen.
- Kontingente für Pro-Modelle in ChatGPT Business („15 Nachrichten/Monat auf Standard-Plätzen“) nur aus Zweitquelle
  (ai-toolbox.co) → **nicht verwenden**, außer OpenAI-Seite bestätigt.

## 6. RouteLLM (LMSYS / UC Berkeley, 01.07.2024)

URL: https://www.lmsys.org/blog/2024-07-01-routellm (Abruf 10.11.2026), Paper https://arxiv.org/abs/2406.18665,
Code (Open Source) https://github.com/lm-sys/RouteLLM. Autoren: Ong, Almahairi, Wu, Chiang, Wu, Gonzalez, Kadous, Stoica.

- Ein „Router“ entscheidet je Anfrage zwischen starkem, teurem und schwächerem, günstigem Modell.
- Ergebnis: Kosten **über 85 % niedriger** (MT Bench), **45 %** (MMLU), **35 %** (GSM8K) im Vergleich zu „alles an GPT-4“,
  bei **95 % der GPT-4-Qualität**.
- Auf MT Bench reichten dafür 26 % der Anfragen an GPT-4, nach zusätzlichem Training 14 %.
- **Einordnung:** Forschung von 2024 mit damaligen Modellen und Preisen; die Ersparnis hängt stark davon ab, wie leicht die
  eigenen Aufgaben sind (Spanne 35–85 % zeigt das). Für KMU: Prinzip zeigen, nicht die Zahl versprechen.

## 7. FrugalGPT (Stanford, Chen/Zaharia/Zou, Mai 2023)

URL: https://arxiv.org/abs/2305.05176 (Abstract gelesen, Abruf 10.11.2026)

- Preise der KI-Schnittstellen unterscheiden sich um **zwei Größenordnungen** (Faktor bis 100).
- „Kaskade“: erst das günstige Modell, nur wenn die Antwort nicht reicht, das nächstgrößere.
- Ergebnis: gleiche Leistung wie das beste Einzelmodell (GPT-4) mit **bis zu 98 %** weniger Kosten – oder 4 % genauer
  bei gleichen Kosten.
- **Einordnung:** „bis zu“ = bester Fall in Laborbedingungen, ältere Modelle. Nur als Beleg für das Prinzip.

## 8. Hochschule München: Energie- und CO₂-Kosten von KI-Antworten (Juni 2025)

Studie: Maximilian Dauner, Gudrun Socher, „Energy costs of communicating with AI“, Frontiers in Communication 10 (2025),
DOI 10.3389/fcomm.2025.1572947. Pressemitteilung Frontiers 19.06.2025:
https://www.frontiersin.org/news/2025/06/19/ai-prompts-50-times-more-co2-emissions (Abruf 10.11.2026; Paper selbst ungeprüft)

- 14 offene Modelle (7 bis 72 Mrd. Parameter), 1.000 Fragen, gemessen auf eigener Hardware.
- Denkende Modelle („Reasoning“) erzeugten **bis zu 50-mal** mehr CO₂ als knapp antwortende Modelle.
- Im Schnitt 543,5 „Denk“-Tokens je Frage gegenüber 37,7 Tokens bei knappen Modellen.
- Beispiel: Qwen 2.5 (72 Mrd.) beantwortet bei ähnlicher Genauigkeit gut dreimal so viele Fragen wie DeepSeek R1 (70 Mrd.)
  für dieselben Emissionen.
- Dauners Rat sinngemäß: knapp antworten lassen und große Modelle nur für Aufgaben nutzen, die sie wirklich brauchen.
- **Einordnung:** offene Modelle auf eigener Hardware, nicht ChatGPT/Claude selbst. Deutsche Hochschule → gut für KMU-Leser.
  Für Größenordnung je Anfrage (0,3 Wh, Epoch AI / OpenAI) nur Zweitquellen gelesen → nicht verwenden oder vorher Original lesen.

## 9. Interne Verlinkung

- „ChatGPT ist nicht das KI-Modell. Was hinter ChatGPT, Claude und Gemini steckt“ (08.10.2026)
  https://www.kleinmittelki.de/chatgpt-claude-gemini-ki-modelle-erklaert/ – enthält Auto-Bild (Marke/Fahrzeug/Motor) und
  den Namens-Decoder (Opus/Sonnet/Haiku, Pro/Flash). Neuer Beitrag baut darauf auf: gleiche Motoren, jetzt mit PS und Verbrauch.
  Bewerben: früh im Text verlinken und im Newsletter/Social als „Grundlage“ mitnennen (Tills Wunsch, Chat 10.11.2026).
- Passend auch: „Nicht jedes Problem braucht KI“ (gleiche Denkrichtung: einfachste ausreichende Lösung).
