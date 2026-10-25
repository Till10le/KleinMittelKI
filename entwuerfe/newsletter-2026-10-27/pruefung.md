# Prüfung: newsletter-2026-10-27 (Ausgabe #4, Di 27.10.2026, 7:00)

## Runde 1 – 25.10.2026 (Prüfer, Sonntags-Lauf)

**Ergebnis: NICHT BESTANDEN** (3 Mängel am Text, 4 Mängel am INTERN-Absatz bzw. an der Bedingung für Abschnitt 01; alle mit kleinen Textänderungen lösbar, Aufbau, Zahlenblock und Fakten tragen)

Geprüft: `beitrag.md` gegen die Skills `kmk-newsletter`, `kmk-schreibstil`, `kmk-formate` und gegen CLAUDE.md. Aufbau verglichen mit
`redaktion/referenz/3-was-ki-agenten-konnen-und-warum-gepflegtes-wissen-zahlt.html` (Ausgabe #3). Fakten gegen
`entwuerfe/ki-ergebnisse-pruefen-leitfaden/beitrag.md` + `quellen.md` + `pruefung.md` (Runde 7 BESTANDEN) und
`entwuerfe/olg-hamm-chatbot-haftung/beitrag.md` + `quellen.md` + `pruefung.md` geprüft, dazu `redaktion/blog-index.json`.
`python3 tools/lexical.py` lief fehlerfrei (rc 0). Ghost, Mail und Commit nicht angefasst.

**Originalquellen nicht selbst abrufbar:** WebFetch auf https://openai.com/index/why-language-models-hallucinate/ und
https://nrwe.justiz.nrw.de/olgs/hamm/j2026/4_UKl_3_25_Urteil_20260512.html wurde blockiert (Freigabe-Anfrage nicht beantwortet).
Abgleich deshalb nur gegen die bereits geprüften `quellen.md` (OpenAI: Leitfaden-quellen.md Abschnitt 1, am Original gelesen; OLG Hamm:
Volltext NRWE und Pressemitteilung, laut quellen.md/pruefung.md am Original gelesen, Rn. 70, 93 gegengelesen).

### Was stimmt

- Aufbau exakt wie Vorlage: INTERN, „Hallo,“, Einstieg „in dieser Ausgabe geht es um …“, `## 01 · Neu im Blog: …`,
  `## 02 · Aktuell eingeordnet: …`, `## 03 · Eine Zahl, genau gelesen`, `## 04 · Ein Gedanke zum Mitnehmen`, Button, `---`,
  Schluss wörtlich, „Bis bald“, „Till“. Je Abschnitt 3 Absätze, dann Bookmark-Karte im Format `URL | Titel | KLEIN. MITTEL. KI. | Teaser`.
  Titel und Teaser der Karten stimmen mit den Beiträgen überein. Art-Zuordnung richtig (Leitfaden = „Neu im Blog“, OLG-Nachricht = „Aktuell eingeordnet“).
- Zahlenblock: per Regex gegen die Vorlage im Skill geprüft, HTML wörtlich identisch, nur die vier Platzhalter ersetzt
  (`OpenAI · September 2025` / `1 zu 365` / Aussage / Lesart). Kein `>` im Text. „Quelle: [OpenAI, Why language models hallucinate](…)“ direkt darunter, Original verlinkt.
- Titel 55 Zeichen (≤ 60), Teaser 128 Zeichen (105–130), Gedanke 26 Wörter (≤ 40), endet mit prüfbarer Frage an die Teamrunde.
- Frontmatter: Tag `#newsletter`, Kategorie leer. Nummer #4 = letzte Ausgabe im Index (#3, 20.10.) + 1. Keine Wiederholung von #3 (KI-Agenten, Wissensmanagement).
- Fakten: „1 zu 365“ und „Ich weiß es nicht“ = sicher null Punkte, „Tests zählen meist nur richtige Antworten“, Datum September 2025 (05.09.2025),
  Einordnung als Rechenbeispiel, nicht Messwert: gedeckt durch quellen.md Abschnitt 1. OLG Hamm: Anbieter ästhetischer Behandlungen,
  nicht existierende Facharzttitel, Mai 2026 (12.05.), irreführende geschäftliche Handlung, Zurechnung, „kein Dritter“, „(lediglich) ein technisches Mittel“ (Rn. 70),
  Gesundheitswesen (Rn. 93), keine Aussage zu anderen Branchen: gedeckt. Leitfaden: Excel-Fall, 28,50 statt 285, drei Fälle, drei Stufen, Leitfrage wörtlich,
  fünf Regeln, Instagram-Entwurf bis Allergene: gedeckt. „kann … genauso sicher klingen“ entspricht der Korrektur F5 im Leitfaden.
- OLG-Beitrag laut Index seit 23.10.2026 veröffentlicht, URL stimmt. Leitfaden im Index `draft`, geplanter Slug stimmt mit Entwurf überein.
- KMU-Bezug: Handwerksbetrieb mit 20 bis 150 Leuten, Teamrunde, Speisekarte. Hinweis „keine Rechtsberatung“ vorhanden.
- Keine Hype- oder Gefühlswörter, keine Rhythmus-Versprechen, keine Vertriebs-CTAs, kein Arbeitgeber-/Handelsbezug.
  Ich-Form nur in „Im Beitrag zeige ich …“, im INTERN-Absatz als Vorschlag markiert, ebenso Einstieg, Haken, Lesart und Gedanke.
- `python3 tools/lexical.py`: 23 Knoten, Reihenfolge paragraph(INTERN) · Hallo · Einstieg · H2 · 3× p · bookmark · H2 · 3× p · bookmark · H2 · html · p(Quelle) · H2 · p · button · horizontalrule · 3× p. Fehlerfrei.

### Mängel am Text

**T1 – „Er ersetzt keine Rechtsberatung.“ ist mehrdeutig** (Abschnitt 02, 3. Absatz, letzter Satz)
Bezugswort im Satz davor ist grammatisch „den Chatbot“, gemeint ist der Beitrag. So liest es sich, als ersetze der Chatbot keine Rechtsberatung.
→ „Der Beitrag ersetzt keine Rechtsberatung.“

**T2 – „dort gelten besonders strenge Maßstäbe“ ohne Zuschreibung** (Abschnitt 02, 2. Absatz, 1. Satz)
Im OLG-Beitrag wurde genau diese Stelle in der Prüfung auf „laut Gericht“ korrigiert (Rn. 93 ist eine Aussage des Senats, keine allgemeine Rechtslage).
→ „Der Haken: Es ging um das Gesundheitswesen, dort gelten laut Gericht besonders strenge Maßstäbe.“

**T3 – „Je fertiger ein Ergebnis aussieht, desto seltener schaut jemand nach.“ ist unbelegt** (Abschnitt 01, 2. Absatz, letzter Satz)
Eine Verhaltensaussage ohne Quelle. Der Leitfaden sagt nur: „Je professioneller ein Ergebnis aussieht, desto fertiger wirkt es.“ (OWASP spricht von übermäßigem Vertrauen, ohne diesen Zusammenhang.)
→ „Je professioneller ein Ergebnis aussieht, desto fertiger wirkt es.“ (oder als Tills Einschätzung im INTERN-Absatz zur Freigabe markieren)

### Mängel am INTERN-Absatz und an der Bedingung für Abschnitt 01

**I1 – Gedanke zum Mitnehmen fehlt für den Fall ohne Abschnitt 01** (INTERN, Abschnitt „BEDINGTER ABSCHNITT“; betrifft `## 04`)
„Ob Kalkulation oder Chatbot“ greift die Excel-Kalkulation aus Abschnitt 01 auf. Entfällt 01, verweist der Gedanke auf etwas, das in der Mail nicht vorkommt
(der Zahlenblock handelt nicht von Kalkulationen). Skill: Der Gedanke „greift die Themen der Ausgabe auf“.
→ Im INTERN-Absatz eine Ersatzfassung nennen, z. B. „Die KI formuliert, die Verantwortung bleibt im Betrieb. Frag in der nächsten Teamrunde, welche KI-Ergebnisse bei euch rausgehen, ohne dass jemand draufschaut.“ (21 Wörter)

**I2 – Ersatz-Einstieg nicht ausformuliert** (INTERN, „Einstieg ohne den Satz zur Excel-Kalkulation“)
Der betroffene Satz („Was das für deinen Betrieb heißt, zeigen eine Excel-Kalkulation und ein Urteil zu einem Website-Chatbot.“) nennt auch das Urteil.
Wird er gestrichen, fehlt der Bezug zum einzigen verbleibenden Beitrag; umformulieren müsste dann jemand ungeprüft beim Einplanen.
→ Ersatzsatz wörtlich in den INTERN-Absatz, z. B. „Was das für deinen Betrieb heißt, zeigt ein Urteil zu einem Website-Chatbot.“

**I3 – Freigabe-Reihenfolge nicht geregelt** (INTERN, Bedingung und CHECKLISTE)
Die Newsletter-Freigabe ist an den Fingerabdruck der zuletzt gemailten Fassung gebunden (`--text-hash`, Skill `kmk-newsletter` Schritt 4).
Fällt Abschnitt 01 nach Tills „N ja“ weg, ist der eingeplante Text nicht mehr der freigegebene. Gibt Till den Newsletter frei, den Leitfaden aber nicht,
geht ein toter Link raus.
→ Ergänzen: „Bitte über den Leitfaden entscheiden, bevor du den Newsletter freigibst. Entfällt Abschnitt 01, schicken wir dir die gekürzte Fassung neu zur Freigabe.“

**I4 – Alternativ-Teaser (A) zu lang** (INTERN, „ALTERNATIVE TITEL UND TEASER“, (A))
„Warum KI sicher klingt, obwohl sie irrt, was das OLG Hamm zu Chatbots sagt, eine Zahl zum Raten und ein Gedanke für deinen Betrieb.“ = 131 Zeichen (Rahmen 105–130).
→ z. B. „Warum KI sicher klingt, obwohl sie irrt, was das OLG Hamm zu Chatbots sagt, eine Zahl und ein Gedanke für deinen Betrieb.“ (122)
Übrige Varianten im Rahmen: (B) 52/123, Ersatz ohne 01: 48/107.

### Hinweise (kein Mangel)

- H1 „eine Zahl zum Raten“ im Teaser kann als „eine Zahl, die du raten sollst“ gelesen werden. Klarer wäre „eine Zahl von OpenAI“ (wie im Ersatz-Teaser). Till entscheidet.
- H2 Die Zahl 1 zu 365 steht auch im Leitfaden (Grafik g1). Mit Abschnitt 01 wiederholt der Zahlenblock also Inhalt aus 01; als Vertiefung vertretbar, im INTERN-Absatz ist die Alternative (88 %, IAB) mit Begründung genannt.
- H3 Der Leitfaden liegt in Ghost laut Leitfaden-Prüfung (H15) noch in der Fassung vom 23.10. Vor einer Freigabe muss der aktuelle Stand in Ghost sein, sonst passt die Bookmark-Karte (Titel, Teaser) nicht.
- H4 Originalquellen OpenAI und NRWE in diesem Lauf nicht selbst abrufbar (s. o.). Die Abgleiche beruhen auf den am Original geprüften quellen.md; vor dem Einplanen genügt ein Blick, ob die OpenAI-Seite noch erreichbar ist.

### Zum Nachprüfen in Runde 2

T1–T3 im Text, I1–I4 im INTERN-Absatz. Danach Zeichen- und Wortzahlen erneut messen und `python3 tools/lexical.py` laufen lassen.

---

## Runde 2 – 25.10.2026 (Prüfer, Nachprüfung, ca. 09:05 UTC)

**Ergebnis: BESTANDEN**

`beitrag.md` noch einmal vollständig geprüft (Aufbau, Zahlenblock, Schluss, Längen, Fakten, Verbote, INTERN-Absatz), nicht nur die geänderten Stellen.

- T1 behoben: „Der Beitrag ersetzt keine Rechtsberatung.“
- T2 behoben: „… dort gelten laut Gericht besonders strenge Maßstäbe.“
- T3 behoben: „Je professioneller ein Ergebnis aussieht, desto fertiger wirkt es.“ (wörtlich wie im Leitfaden)
- I1 behoben: Ersatz-Gedanke steht im INTERN-Absatz, greift nur Themen auf, die auch ohne Abschnitt 01 vorkommen.
- I2 behoben: Ersatz-Einstieg wörtlich: „Was das für deinen Betrieb heißt, zeigt ein Urteil zu einem Website-Chatbot.“
- I3 behoben: Abschnitt „REIHENFOLGE DER FREIGABE“ (erst Leitfaden, dann „N ja“; gekürzte Fassung geht neu zur Freigabe).
- I4 behoben: Alternativ-Teaser (A) jetzt 121 Zeichen.
- H1 umgesetzt: Teaser „… eine Zahl von OpenAI …“.
- H3 erledigt laut Chefredakteur; `entwuerfe/ki-ergebnisse-pruefen-leitfaden/ghost.json` bestätigt das: updated_at 2026-10-25T06:48 UTC,
  Titel in Ghost = Titel der Bookmark-Karte, Status draft.

Neu gemessen: Titel 55 Zeichen · Teaser 129 (105–130) · Gedanke 26 Wörter · Ersatz: Titel 48, Teaser 110, Gedanke 22 Wörter ·
Alternativen (A) 46/121, (B) 52/123. Zahlenblock weiter wörtlich gleich der Skill-Vorlage (Regex-Abgleich), Quelle-Zeile darunter,
Schluss wörtlich. Durch die Änderungen keine neuen Fakten, keine neuen Ich-Sätze, keine Verbotswörter.
`python3 tools/lexical.py` fehlerfrei (rc 0).

Hinweise (kein Mangel):
- Der INTERN-Absatz nennt beim Ersatz-Gedanken „21 Wörter“, es sind 22 (der Fehler stammt aus meinem Vorschlag in Runde 1). Liegt im Rahmen, wird mit dem INTERN-Absatz entfernt.
- Originalquellen (OpenAI, NRWE) waren in diesem Lauf weiterhin nicht selbst abrufbar; der Abgleich beruht auf den am Original geprüften quellen.md (siehe Runde 1).
- Vor dem Einplanen gilt die CHECKLISTE im INTERN-Absatz, vor allem: Leitfaden-Link erst nach Veröffentlichung gültig.

---

## Runde 3 – 25.10.2026 (Prüfer, Fassung 2)

**Ergebnis: NICHT BESTANDEN** (ein Mangel, schnell behebbar)

Geprüft: `git diff HEAD` (INTERN, Einstieg, Abschnitt 01, Bookmark) gegen den freigegebenen Leitfaden
`entwuerfe/ki-ergebnisse-pruefen-leitfaden/beitrag.md` (Freigabe in `redaktion/freigaben.jsonl`, 25.10., Zeitpunkt 27.10. 06:00 UTC).

### Mangel

**M1 – Tiger im Indikativ, schärfer als der Leitfaden** (Abschnitt 01, erster Absatz, Sätze 3 und 4)
Newsletter: „Sie erkennt das Muster, aber nicht den Zusammenhang. Und sie zweifelt nicht.“
Leitfaden: „Die KI würde das Muster erkennen, aber nicht den Zusammenhang … Und sie würde nicht zweifeln.“
Das Bild ist ein mit KI nachgestelltes Beispiel, kein Messergebnis; der Satz davor steht korrekt im Konjunktiv („könnte sagen: Tiger“).
→ Ersatz: „Sie würde das Muster erkennen, aber nicht den Zusammenhang. Und sie würde nicht zweifeln.“

### Ok

- Einstieg: „ein Hund, den eine KI für einen Tiger halten könnte“ – Konjunktiv, gedeckt.
- Steckachse: „100 %“, Länge und Gewinde nicht geprüft – gedeckt.
- Excel: „sah professionell aus, rechnete die jährliche Steigerung aber zunächst falsch“ – gedeckt („sieht professionell aus und rechnet trotzdem falsch“, „rechnete das zunächst anders“).
- Drei Stufen mit Leitfrage wörtlich, drei Regeln, Kundenantwort (Stufe 2), Allergenangabe/Speisekarte (Stufe 3) – gedeckt. Keine 28,50/285 €, keine fünf Regeln, kein Instagram mehr.
- Bookmark-Karte: Titel und Teaser zeichengleich mit dem Frontmatter des Leitfadens.
- Format `kmk-newsletter`: Einstieg 2 Sätze, Abschnitt 01 drei Absätze plus Karte, Titel 55 Zeichen, Teaser 129, Gedanke 26 Wörter.
- Teaser passt weiter. Gedanke „Ob Kalkulation oder Chatbot“ passt weiter, die Excel-Kalkulation steht noch in 01.
- Ich-Sätze („Mir hat ChatGPT …“, „Im Beitrag zeige ich …“) im INTERN-Absatz als Vorschlag markiert, Inhalt aus Tills freigegebenem Leitfaden.
- Keine Floskeln, kein Hype, keine CTAs, kein Arbeitgeber-/Handelsbezug.
- `python3 tools/lexical.py entwuerfe/newsletter-2026-10-27/beitrag.md` fehlerfrei (rc 0).

### Hinweise (kein Mangel)

- H1 „drei Regeln, mit denen du der KI den Zusammenhang mitgibst“: genau genommen tun das Regel 1 und 2, Regel 3 ist Selbst-Nachrechnen. Gedeckt durch die Leitfaden-Überschrift „Drei Regeln: Gib der KI den Zusammenhang“.
- H2 Der Leitfaden-Teaser in der Bookmark-Karte („Eine KI hält einen Hund für einen Tiger.“) steht im Indikativ; er ist von Till freigegeben und muss gleich bleiben. M1 gilt trotzdem für den eigenen Text.
- H3 Lokale `ghost.json` des Leitfadens zeigt `status: draft` (updated_at 17:39 UTC). Vor dem Einplanen des Newsletters prüfen, dass der Leitfaden in Ghost für 27.10. 7:00 geplant ist.
