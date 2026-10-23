# Prüfung: ki-ergebnisse-pruefen-leitfaden

## Runde 1 – 23.10.2026 (Prüfer, Express-Lauf)

**Ergebnis: NICHT BESTANDEN** (sechs kleine Mängel, alle in wenigen Minuten zu beheben; inhaltlich und strukturell trägt der Beitrag)

Geprüft: beitrag.md, quellen.md, kmk-ki-pruefen-g1/g2/g3/g5.png (+ g2/g5-social angesehen), vorschaubild.png,
`python3 tools/lexical.py` (läuft fehlerfrei, rc 0), Vergleich mit `redaktion/referenz/ki-agenten-was-nach-dem-chatbot-kommt-und-was-kmu-davon-haben.html`,
Board-Vorgaben von Till. Ghost-Vorschau in diesem Lauf nicht vorgesehen (Punkt 13 entfällt).

### Quellen selbst gelesen (WebFetch, 23.10.2026)

| Quelle | Ergebnis |
|---|---|
| OpenAI „Why language models hallucinate“ (05.09.2025) | Definition, Mitautor Kalai, drei falsche Titel, Geburtstag dreimal falsch, „1-in-365“, „widely used chatbot“, Accuracy nie 100 %, Halluzinationen nicht unvermeidbar: alles korrekt wiedergegeben. |
| OpenAI Help „Does ChatGPT tell the truth?“ | „sound confident—even when it’s wrong“, falsche Daten/Fakten, erfundene Zitate/Studien/Quellen, „first draft, not a final source“: korrekt. Seite ohne festes Datum („Updated: 19 hours ago“), im Beitrag richtig als „abgerufen“ angegeben. |
| OWASP LLM09:2025 Misinformation (Stand 17.04.2025) | Halluzination, Overreliance, Folgen Reputationsschaden/rechtliche Haftung, RAG mit verifizierten Quellen, menschliche Gegenprüfung: korrekt. |
| Anthropic „Reduce hallucinations“ | „can drastically reduce false information“, Zitat-Beleg/Retract, „don’t eliminate them entirely … always validate critical information“: korrekt. **Ausnahme:** „in einem neuen Chat“ steht dort nicht (siehe A2). |
| Eigene Beiträge | Protokoll-Selbstversuch: „Einige Namen waren falsch geschrieben, und bei den Kassenprüfern stimmte die Amtszeit nicht.“ – passt. KI-Agenten-Beitrag: Stufen Beobachten/Vorbereiten/Ausführen – passt. OLG Hamm laut blog-index weiter `draft` → INTERN-Hinweis richtig. |

Ungeprüft (vom Autor korrekt als nicht verwendet markiert): OpenAI-Paper-PDF, BSI-PDF, OWASP-Beispielfälle, LinkedIn-Beitrag Lichtenberger, OLG-Hamm-Volltext.

### Checkliste

| # | Punkt | Ergebnis |
|---|---|---|
| 1 | Zahlen/Namen/Daten wie in Quelle | Mangel A2 (Zuschreibung „neuer Chat“), A3 („stützen sich auf“), G2 (Fußzeile g5) |
| 2 | Grundgesamtheit/Einschränkungen | ok – Herstellerangaben als solche benannt (OpenAI-Forschung, Hilfeseite), Beispiele als ausgedacht gekennzeichnet |
| 3 | Originalveröffentlichung verlinkt | ok – alle vier Quellen sind Originale |
| 4 | Nichts in Tills Namen erfunden | ok – „Meine Einschätzung“ und Gedanke im INTERN-Absatz als Vorschlag markiert, Protokoll-Bezug zur Bestätigung |
| 5 | Platzhalter | `[TILL: …]` bewusst offen, korrekt markiert. **Mangel A1:** INTERN-Absatz behauptet noch „fünf Platzhalter [GRAFIK: …]“ |
| 6 | Format, Längen, Teaser | ok – Einleitung 2 Absätze, Box 5 Punkte, H2 als Aussagen/Fragen, „Zum Ausprobieren“ als nummerierte Box mit Prompt (wie Vorbild), Meine Einschätzung · Gedanke · Quellen; ca. 1.916 Wörter; Teaser 134 Zeichen, ≠ Titel |
| 7 | Rubrik/Kategorie/Tags | ok – Wissen / Leitfäden (sagt, was zu tun ist) + `#wissen` |
| 8 | Für-KMU-Zeile | entfällt (kein Aktuell-Beitrag) |
| 9 | Ton und Verbote | Mangel A4 („ehrlich gesagt“). Kein Handel, kein Hype, kein CTA, kein Meme, keine Ampelfarben – ok |
| 10 | KMU-Bezug | ok – Malerbetrieb mit zwölf Leuten, Betrieb mit 30 Leuten, Rollen Bürokraft/Küchenchefin, Prozesse Angebot/Exposé/Speisekarte |
| 11 | Grafiken | Mangel G1 (g2 widerspricht sich), G2 (Fußzeile g5), G3 (g2 ohne Stand), G4 (Bildunterschrift g1 zwei Sätze). Sonst: Baukasten, Kicker, Titel als Aussage, Alt-Texte vorhanden, nur Schwarz/Lime |
| 12 | Vorschaubild | ok – Kategorie „Leitfäden“, Titel drei Zeilen lesbar, Logo, Lime-Kante |
| 13 | Ghost-Vorschau | entfällt in diesem Lauf |
| 14 | Wie bisher auf der Seite | ok – Aufbau, Box-Bausteine, „Abgerufen und geprüft am …“ und Grafikanzahl (4, Rahmen 4–5) wie im KI-Agenten-Beitrag |

### Mängel Autor

**A1 – INTERN-Absatz veraltet** (beitrag.md Z. 10, letzter Satz „Grafiken: fünf Platzhalter [GRAFIK: …] für die Grafik-Agentin.“)
Till liest den Absatz vor der Freigabe; die Angabe ist falsch (vier Schaubilder sind eingebunden).
→ Ersetzen durch: „Grafiken: vier Schaubilder eingebunden (g1, g2, g3, g5); die optionale Beispiele-Tabelle wurde weggelassen.“

**A2 – Zuschreibung an Anthropic ungenau** (Z. 90: „Ein weiterer Trick aus derselben Dokumentation: Stell dieselbe Frage zweimal in einem neuen Chat.“)
Die Doku sagt „Run Claude through the same prompt multiple times and compare the outputs“ – von „neuem Chat“ und „zweimal“ steht dort nichts.
→ „Ein weiterer Tipp aus derselben Dokumentation: Stell dieselbe Frage mehrmals, am besten jeweils in einem neuen Chat, und vergleiche die Antworten.“ (Der Zusatz „neuer Chat“ ist dann als eigene Empfehlung lesbar.)

**A3 – „Sie stützen sich auf …“ überdehnt** (Z. 84)
Regel 5 (fehlende Angabe testen) und die benannte Person in Regel 4 stehen so in keiner der Quellen.
→ „Die ersten drei stützen sich auf die Empfehlungen von OWASP und auf die Hinweise von OpenAI und Anthropic selbst. Regel 4 und 5 sind praktische Ergänzungen für den Betriebsalltag.“

**A4 – Floskel im sachlichen Teil** (Z. 62: „Das ist ehrlich gesagt nicht realistisch.“)
„Ehrlich gesagt“ ist Ich-Stimme außerhalb der Einschätzung und Füllwort.
→ „Das ist nicht realistisch.“

### Mängel Grafik

**G1 – g2 widerspricht sich selbst** (kmk-ki-pruefen-g2.png und g2.html, auch -social)
Merksatz: „Die KI hat nichts erfunden. Sie hat nur die Unsicherheit weggelassen.“ Gleichzeitig ist „komplett saniert“ hervorgehoben – „komplett“ und „saniert“ statt „erneuert“ sind gerade hinzugefügt. Ein aufmerksamer Leser stolpert genau hier.
→ Merksatz ändern in: „**Niemand hat gelogen.** Die KI hat die Unsicherheit gestrichen und ‚komplett‘ ergänzt.“ – oder KI-Text auf „Dach 2010 erneuert.“ ändern und „2010 erneuert“ hervorheben (dann passt der bestehende Merksatz). Text Z. 54 bei Variante 2 mit anpassen.

**G2 – Fußzeile g5 schreibt alle fünf Regeln den Quellen zu** („Quellen: OWASP, OpenAI, Anthropic“)
→ „Vereinfachte Darstellung · Stand: 23.10.2026 · Eigene Zusammenstellung, u. a. nach OWASP, OpenAI, Anthropic“ (passend zu A3). Auch -social neu rendern.

**G3 – g2 ohne Stand** (Fußzeile „Vereinfachte Darstellung · ausgedachtes Beispiel“)
CI-Regel: Fußzeile mit „Stand: TT.MM.JJJJ“.
→ „Vereinfachte Darstellung · Stand: 23.10.2026 · ausgedachtes Beispiel“.

**G4 – Bildunterschrift g1 hat zwei Sätze** (beitrag.md Z. 30: „Vereinfacht: Wer raten darf, rät. Das gilt auch für Sprachmodelle.“)
CI-Regel: ein Satz.
→ „Wer raten darf, rät – das gilt auch für Sprachmodelle.“

### Hinweise (kein Mangel, Entscheidung beim Chefredakteur/Till)

- Z. 40 „Das passt zu einer Beobachtung, die viele kennen: Je besser ein Text klingt, desto weniger genau liest man ihn.“ – unbelegte Allgemeinaussage, als Alltagsbeobachtung vertretbar. Ggf. als Frage an den Leser formulieren.
- Z. 38 „Liste der zehn wichtigsten Risiken für KI-Anwendungen“ – genauer wäre „für Anwendungen mit Sprachmodellen“.
- Z. 42 „Was ein Chatbot auf der Website deines Betriebs sagt, sagst am Ende du.“ – trägt erst mit dem OLG-Hamm-Link richtig; erscheint dieser Beitrag vor dem OLG-Beitrag, bleibt die Aussage ohne Beleg. Reihenfolge der Veröffentlichung bedenken.
- Social-Kacheln g2/g5: großer Leerraum zwischen Titel und Inhalt (Werkzeugverhalten von `--social`), nicht Teil des Beitrags.

## Runde 2 – 23.10.2026 (Prüfer, Express-Lauf)

**Ergebnis: BESTANDEN**

Nachgeprüft: beitrag.md, kmk-ki-pruefen-g2.png/-social, kmk-ki-pruefen-g5.png/-social (neu gerendert, angesehen), `python3 tools/lexical.py` (fehlerfrei, rc 0).

| Mangel | Prüfung |
|---|---|
| A1 INTERN-Absatz | ok – „Grafiken: vier Schaubilder eingebunden (g1, g2, g3, g5); die optionale Beispiele-Tabelle wurde weggelassen.“ |
| A2 Anthropic-Zuschreibung | ok – „Stell dieselbe Frage mehrmals, am besten jeweils in einem neuen Chat, und vergleiche die Antworten.“ deckt sich mit „same prompt multiple times … compare“ |
| A3 „stützen sich auf“ | ok – „Die ersten drei stützen sich auf …; Regel 4 und 5 sind praktische Ergänzungen für den Betriebsalltag.“ |
| A4 „ehrlich gesagt“ | ok – gestrichen |
| G1 g2-Merksatz | ok – „Niemand hat gelogen. Die KI hat die Unsicherheit gestrichen und ‚komplett‘ ergänzt.“ passt zur Hervorhebung und zu Z. 54 |
| G2 g5-Fußzeile | ok – „Eigene Zusammenstellung, u. a. nach OWASP, OpenAI, Anthropic · Stand: 23.10.2026“ |
| G3 g2-Stand | ok – „… · ausgedachtes Beispiel · Stand: 23.10.2026“ |
| G4 Bildunterschrift g1 | ok – „Wer raten darf, rät – das gilt auch für Sprachmodelle.“ |

Keine neuen Mängel. Offen bleiben bewusst für Till: `[TILL: …]` in „Meine Einschätzung“, INTERN-Vorschläge (Einschätzung, Gedanke, Protokoll-Bezug), LinkedIn-Anlass bestätigen, OLG-Hamm-Link nach dessen Veröffentlichung. Die Hinweise aus Runde 1 (Z. 38, 40, 42; Social-Leerraum) bleiben Hinweise, kein Mangel.
