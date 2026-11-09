# Prüfung: newsletter-2026-11-10 (Fassung 1, mit Fassung 2 im INTERN-Absatz)

Datum: 08.11.2026 (Lauf So 7:47) · Prüfer · Maßstab: `.claude/agents/pruefer.md`, Skills kmk-newsletter, kmk-schreibstil, kmk-themen, CLAUDE.md.
Gelesen: `redaktion/referenz/powerpoint-mit-ki-im-eigenen-design.html` (veröffentlicht 06.11.), `entwuerfe/ki-recherche-assistent-selbstversuch/beitrag.md` (Stand Ghost-Entwurf 25.10.), Original https://www.anthropic.com/research/agents-judgment-calls (am 08.11.2026 selbst abgerufen, HTTP 200), Newsletter #4 und #5, `redaktion/blog-index.json`, Board-Einträge A und ki-agent-beeinflusst-entscheidungen. `python3 tools/lexical.py` gelaufen.

## Ergebnis: NICHT BESTANDEN

Zwei inhaltliche Mängel im Zahlenblock bzw. Gedanken (Abschnitt 03/04). Alles andere ist ok. Nichts korrigiert, weil beide Punkte inhaltlich sind.

## Mängel

1. **03 und 04 · Rat widerspricht der eigenen Quelle.**
   Fundstelle: Zahlenblock „Für deinen Betrieb heißt das: Bevor du eine Preis- oder Personalfrage mit der KI vorbereitest, schreib deine eigene Einschätzung auf.“ und Gedanke „Schreib deine eigene Einschätzung deshalb auf, bevor du ihre liest.“
   Problem: Die Studie zeigt gerade, dass eine vorher geäußerte eigene Meinung wenig schützt: „When analysts had already expressed their own preference before the agent weighed in, they switched away from it 60% of the time if the agent disagreed, compared to 6% if it agreed.“ (38 Fälle, 95-%-KI 24–82 Prozentpunkte, laut Autoren unpräzise). „Erst die Meinung des Menschen erfragen“ nennen die Autoren nur als Idee für das Design von Agenten, die erst noch erforscht werden soll, nicht als belegtes Gegenmittel. Ein Leser, der die Quelle öffnet, findet also das Gegenteil des Rats. Dazu steht derselbe Rat zweimal (03 und 04).
   Korrekturvorschlag: Der Rat sollte zu dem passen, was die Quelle stützt, z. B. im Zahlenblock: „Für deinen Betrieb heißt das: Lass dir bei einer Preis- oder Personalfrage von der KI für jede Option das stärkste Argument geben, nicht nur für eine.“ (Die Quelle: „they rarely made a strong case for why an expert might prefer the other option“.) Oder: „Leg vorher fest, welche Entscheidungen du selbst triffst.“ („Organizations will need to decide deliberately which decisions need a person’s own informed judgment“.) Der Gedanke in 04 sollte dann einen anderen Satz bekommen als der Zahlenblock, z. B. „… Frag sie deshalb bei wichtigen Entscheidungen auch nach den Gründen für die andere Option.“ Wer „eigene Einschätzung aufschreiben“ behalten will, muss den 60-%-Befund ehrlich mitnennen. Beides sind Vorschläge in Tills Namen und bleiben im INTERN-Absatz markiert.

2. **03 · „verdeckt nahelegte“ ist ungenau.**
   Fundstelle: „der Analyseentscheidungen fielen so aus, wie ein KI-Agent es verdeckt nahelegte.“
   Problem: Verdeckt war nur, dass die Tendenz per Münzwurf vorgegeben war („which the analysts weren’t told about“). Der Agent hat seine Tendenz offen vertreten („to raise it when the decision came up, and to make the strongest case for it“). „Verdeckt nahelegen“ klingt nach heimlicher Manipulation.
   Korrekturvorschlag: „der Analyseentscheidungen fielen so aus, wie ein KI-Agent es empfahl. Seine Tendenz war per Münzwurf vorgegeben, ohne dass die Analysten es wussten. Ohne seinen Einfluss wären etwa 50 Prozent zu erwarten.“

## Checkliste

- **Fakten 86 %:** ok. Original wörtlich: „Across the four analytical choices, analysts went with their agent’s lean 86% of the time. If the agent’s input made no difference, we’d expect about 50%.“ 50 Analysten (61 rekrutiert, 11 ohne Agent ausgeschlossen), fiktiver Fall („fictional organization, the Greenfields Farming Cooperative“), „We deliberately strengthened the agents’ lean“, „only 15% credited the agent“, veröffentlicht „Oct 27, 2026“. Kopfzeile „Anthropic · Oktober 2026“ und Datum 27.10.2026 stimmen. Bezug „Entscheidungen, nicht Personen“ und „Herstellerstudie über das eigene Produkt“ korrekt genannt. Einschränkungen: ok, außer den Mängeln 1 und 2.
- **Originalquelle verlinkt:** ok (anthropic.com/research, keine Zweitverwertung; the-decoder nicht genutzt).
- **01 gegen veröffentlichten Beitrag:** ok, nichts geht über den Beitrag hinaus. Petrol/Dunkelblau, Symbole in Kreisen, abgerundete Kästen, „nach zwei Sekunden“, drei Versuche mit sechs Folien in Claude, B nach der Marke, C wie aus einem Guss mit Logo und Seitenzahlen, Widerspruch Brandbook/Vorlage („Die KI muss sich entscheiden“), Folien zum Durchklicken, Design-Steckbrief, Auftrag zum Kopieren, Schreiner/Küchenentwurf, Immobilienbüro/Eigentümerpräsentation: alles im Beitrag. Die Bookmark-Karte stimmt wörtlich mit Titel und Teaser im Index überein.
- **02 gegen Ghost-Entwurf:** ok. Vorarbeit (Studien, Urteile, Funktionen, Originalquelle, Lärm), feste Kriterien, donnerstags, höchstens vier Themen, „entscheide ich“, Internetzugang im ersten Test, Protokoll, „Ein Knopfdruck war die Einrichtung nicht“, fünf Schritte, Malerbetrieb/Ausschreibungen, Hausverwaltung/Gesetzesänderungen, drei Beispiel-Anfragen, drei Wege: alles im Entwurf. Die Bookmark-Karte ist wörtlich. Hinweis 1 beachten.
- **Ich-Form markiert:** ok. Einstieg, Ich-Zusammenfassungen in 01/02, Haken-Sätze, Lesart und Gedanke stehen als VORGESCHLAGEN im INTERN-Absatz. Nichts erfunden: Die Ich-Aussagen geben Tills veröffentlichte bzw. eingereichte Texte sinngemäß wieder.
- **Platzhalter:** ok, keine `[TILL: …]`/`[GRAFIK: …]`.
- **Aufbau nach Vorlage:** ok. INTERN, „Hallo,“, Einstieg mit 2 Sätzen, 01/02 mit „Selbst ausprobiert:“ (beide Praxistests), je drei Absätze plus Bookmark, 03 Zahl mit Quelle-Zeile, 04 Gedanke (30 Wörter, ≤ 40), Button, `---`, Schluss **wörtlich** wie Vorlage, „Bis bald“, „Till“. Das Zahlenblock-HTML ist wörtlich nach Vorlage.
- **Frontmatter:** ok. Titel 51 Zeichen (≤ 60), Teaser 123 Zeichen (Rahmen 105–130), Teaser ungleich Titel, Tag `#newsletter`, Kategorie leer. Alternativen: (A) Titel 58 / Teaser 133, (B) 47 / 129, Fassung 2: Titel 40 / Teaser 126. Alt-Teaser A liegt mit 133 knapp über dem Rahmen (Hinweis 3).
- **Wiederholung #4/#5:** ok. Andere Beiträge und Zahlen (#4: 1 zu 365, OpenAI; #5: 90 %, EU-Kommission). Die Vorlagen-Wendungen „Der Haken:“, „Im Beitrag stehen …“, „Für deinen Betrieb heißt das:“ stammen aus der festen Vorlage. Siehe Hinweis 2.
- **Ton/Verbote:** ok. Keine Floskeln, kein Hype, keine Gefühlswörter, keine CTAs, kein Handel oder Arbeitgeber. „donnerstags“ beschreibt den Agenten, ist kein Rhythmus-Versprechen.
- **KMU-Bezug:** ok (Schreiner, Immobilienbüro, Malerbetrieb, Hausverwaltung, Preis-/Personalfrage). Keine Betriebsgröße genannt, Rolle und Prozess reichen nach CLAUDE.md Regel 7.
- **lexical.py:** ok. Läuft ohne Fehler, 23 Knoten (wie #4), Zwischenüberschriften `01 · Selbst ausprobiert: Dreimal dieselbe Präsentation mit KI`, `02 · Selbst ausprobiert: Ein KI-Assistent, der sucht, aber nicht entscheidet`, `03 · Eine Zahl, genau gelesen`, `04 · Ein Gedanke zum Mitnehmen`. Frontmatter wird korrekt gelesen.
- **Ghost-Vorschau / Grafiken / Vorschaubild:** entfällt (Newsletter, noch nicht in Ghost, keine Grafiken außer Zahlenblock).

## Hinweise (kein Mangel, zur Entscheidung)

1. **02 hängt an einem Beitrag, dessen Review offen ist.** Laut Board hat sich „der Prozess geändert“ (Till, 02.11.). Das Review vom 03.11. ist nicht dokumentiert. Der INTERN-Absatz sagt das und bietet Fassung 2 an. Vor dem Einplanen muss 02 mit der freigegebenen Fassung von A abgeglichen werden, sonst gilt Fassung 2.
2. **„Der Haken“ zweimal in einer Ausgabe** (01: „Der Haken steckte …“, 02: „Der Haken: …“). In #4 und #5 kam es je einmal vor. Vorschlag für 01: „Überrascht hat mich etwas anderes: Brandbook und Vorlage widersprachen sich …“ (wieder als Vorschlag markieren). Außerdem kommt „entscheiden“ im Einstieg, in 02 und im Gedanken vor. Das ist gewollt als roter Faden, wirkt aber etwas dicht.
3. **Alternativ-Teaser A** hat 133 Zeichen, also knapp über 130. Er lässt sich kürzen, z. B. „Dreimal dieselbe Präsentation mit KI, ein Assistent, der sucht, aber nicht entscheidet, eine Zahl und ein Gedanke.“
4. **02, „Ein grüner Status heißt nur …“:** Im Beitrag steht das als Hinweis von Anthropic, im Newsletter als eigene Feststellung. Das ist inhaltlich richtig. Wer genau sein will, schreibt: „Ein grüner Status heißt nur, dass der Lauf ohne technischen Fehler endete, so steht es auch bei Anthropic.“
5. Mit der Zahl 86 % ist die Kennzahl des offenen Themas ki-agent-beeinflusst-entscheidungen schon einmal genannt. Der INTERN-Absatz weist Till darauf hin. Ok.

---

# Runde 2 (08.11.2026, Lauf So 7:47)

Neu gelesen: überarbeiteter Entwurf `beitrag.md`. Original https://www.anthropic.com/research/agents-judgment-calls am 08.11.2026 erneut abgerufen (HTTP 200), die neuen Belegstellen selbst geprüft. `python3 tools/lexical.py` erneut gelaufen.

## Ergebnis: BESTANDEN

## Mängel aus Runde 1

1. **Rat 03/04: behoben.**
   - 03: „Lass dir bei einer Preis- oder Personalfrage von der KI für jede Option das stärkste Argument geben, nicht nur für eine.“ Im Original steht: „But they rarely made a strong case for why an expert might prefer the other option, which might have helped analysts make a better-informed choice. With only one side argued well, the analysts could adopt the agent’s assumptions …“ Dazu: „Agents could make the best case for each option“. Der Rat ist eine Ableitung, die der Befund stützt. Er widerspricht der Quelle nicht.
   - 04: „Leg deshalb fest, welche Entscheidungen im Betrieb bei dir bleiben, und nimm dir dafür Zeit.“ Im Original steht: „Organizations will need to decide deliberately which decisions need a person’s own informed judgment, and give people the time and resources to form one.“ Das passt.
   - Der Rat steht nicht mehr doppelt. Der Gedanke hat 35 Wörter (≤ 40).
   - Die Streichung des alten Rats und der Grund (60 % Wechsel bei 38 Fällen) stehen im INTERN-Absatz. Die neuen Sätze sind als VORGESCHLAGEN markiert.
2. **„verdeckt nahelegte“: behoben.** Neu steht da: „wie ein KI-Agent es empfahl. Seine Tendenz war per Münzwurf vorgegeben, ohne dass die Analysten es wussten.“ Im Original: „set up each analyst’s agent to favor one option on each decision, which the analysts weren’t told about. Which way the agents would ‚lean‘ would be decided by coin flip.“ Das stimmt.

## Hinweise aus Runde 1

- **„Der Haken“** kommt nur noch einmal vor (02). In 01 steht jetzt „Überrascht hat mich etwas anderes …“. Das deckt der veröffentlichte Beitrag („Mit dieser Stelle hatte ich nicht gerechnet … Mir war das nicht aufgefallen.“), und der Satz ist im INTERN als Vorschlag aufgeführt. Ok.
- **Grüner Status:** steht jetzt als Hinweis von Anthropic („so steht es auch bei Anthropic“), wie im Beitrag A. Ok.
- **Alternativ-Teaser A:** 114 Zeichen. Ok.
- **Abhängigkeit von 02 vom offenen Review von A:** bleibt bestehen. Der INTERN-Absatz und die Checkliste regeln das (sonst Fassung 2). Das ist kein Mangel des Textes.

## Erneut geprüft, unverändert ok

- 86 %, etwa 50 %, 15 %, 50 Analysten, fiktiver Fall, bewusst verstärkte Tendenz, 27.10.2026: wörtlich im Original. Die Kopfzeile „Anthropic · Oktober 2026“ stimmt.
- Titel 51 Zeichen, Teaser 123 Zeichen, Tag `#newsletter`, Kategorie leer. Keine Platzhalter. Schluss wörtlich.
- lexical.py: 23 Knoten, vier Zwischenüberschriften wie in Runde 1, Frontmatter korrekt.

## Hinweis (kein Mangel)

- Der Rat „für jede Option das stärkste Argument“ ist bei den Autoren ein Gestaltungsvorschlag für Agenten, den sie selbst noch nicht getestet haben. Sie warnen, das könne Nutzer überfordern. Im Zahlenblock steht er als Folgerung „Für deinen Betrieb heißt das“, nicht als Studienergebnis. Das ist vertretbar. Till sollte nur wissen, dass es eine Ableitung ist.

---

# Fassung 2 (09.11.2026, Chat)

Geprüft wurden nur die Änderungen gegenüber Runde 2: Abschnitt 02 (Recherche-Assistent) ist auf Tills Wunsch gestrichen, dazu kommen neuer Titel, Teaser, Einstieg und der INTERN-Absatz. Die Fakten der Zahl wurden nicht erneut am Original geprüft, das ist in Runde 2 geschehen.

## Ergebnis: BESTANDEN

## Geprüft

- **Aufbau und Nummerierung:** Einstieg, dann 01 · Selbst ausprobiert, 02 · Eine Zahl, genau gelesen, 03 · Ein Gedanke zum Mitnehmen. Danach folgen Button, Trennlinie und der wörtliche Schluss. Das entspricht kmk-newsletter. Keine Nummer fehlt.
- **Titel:** „#6: Dreimal dieselbe Präsentation mit KI“ hat 40 Zeichen (höchstens 60), ist sachlich und hält die Form `#<Nummer>: <Thema>` ein.
- **Teaser:** 126 Zeichen, also im Rahmen von 105–130. Er zählt auf, was drinsteht, und erwähnt den Recherche-Assistenten nicht mehr.
- **Einstieg:** „Hallo,“ steht als eigener Absatz, dann folgt ein Absatz „in dieser Ausgabe geht es um …“ mit zwei Sätzen. Er passt zu 01. Im INTERN-Absatz ist er als Vorschlag markiert.
- **Gedanke ohne 02:** Er trägt weiter. „Vorlage“ greift 01 auf, „Umgekehrt richtest du dich leicht nach ihr“ greift die Zahl auf. Er hat 35 Wörter (höchstens 40).
- **Verwaiste Bezüge:** Im sichtbaren Text kommt der Recherche-Assistent nicht mehr vor. Die Ausgabe von lexical.py habe ich danach durchsucht. Der einzige Treffer ist der Slug (siehe unten).
- **lexical.py:** läuft fehlerfrei. Es entstehen 18 Knoten und drei Zwischenüberschriften (01–03). Das Frontmatter ist korrekt: Tag `#newsletter`, Kategorie leer.

## Direkt korrigiert (formal, nur INTERN-Absatz)

1. Die Liste VORGESCHLAGEN verwies noch auf den alten Einstieg („zwei Selbstversuche …“) und auf Sätze aus 02. Für Fassung 2 steht jetzt eine eigene, aktuelle Liste am Anfang. Der Vermerk zu Fassung 1 bleibt darunter stehen und ist als nicht mehr gültig gekennzeichnet.
2. Die Alternativ-Titel und -Teaser A und B erwähnten den Assistenten bzw. die Vorauswahl. Für Fassung 2 gibt es jetzt zwei neue Alternativen. Die Teaser haben 126 und 130 Zeichen, die Titel 23 und 51 Zeichen.
3. Die Checkliste hing noch an Beitrag A. Für Fassung 2 gibt es jetzt eine eigene Checkliste.

## Hinweis (kein Mangel)

- Der Slug `6-folien-ohne-ki-look-und-ein-recherche-assistent` nennt noch den Assistenten. Er bleibt bewusst so: `ghost.py draft` findet den bestehenden Entwurf über den Slug (ghost.json, id 6af01d6a…). Mit einem neuen Slug entstünde ein zweiter Entwurf. Der Newsletter geht nur per E-Mail, deshalb sieht kein Leser den Slug.
- „Kriterien, Fragen“ im Gedanken stammte ursprünglich aus 02. Allgemein gelesen bleibt die Aussage richtig. Wer straffen will, schreibt: „Die KI richtet sich nach dem, was du ihr vorgibst.“
- ghost.json zeigt noch den alten Titel. Der Entwurf in Ghost muss mit `ghost.py draft` aktualisiert werden, bevor die neue Testmail und der Begleitzettel rausgehen.
