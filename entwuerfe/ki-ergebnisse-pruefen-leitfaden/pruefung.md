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

## Runde 3 – 23.10.2026 (Prüfer, Express-Lauf, Überarbeitung mit Tills drei Fällen)

**Ergebnis: NICHT BESTANDEN** (zwei kleine Autor-Mängel; Grafik ohne Mangel)

Geprüft: beitrag.md, quellen.md, alle PNGs (g1–g5, g4/g5-social, vorschaubild.png angesehen), g4.html/g5.html,
`redaktion/eingang/2026-10-23-till-eigene-ki-fehler.md`, Board-Vorgaben, `git diff` gegen die bestandene Fassung,
Vergleich mit `redaktion/referenz/ki-agenten-was-nach-dem-chatbot-kommt-und-was-kmu-davon-haben.html`,
`python3 tools/lexical.py` (fehlerfrei, rc 0, auch nach meiner Korrektur).

**Quellen:** Erneuter WebFetch der vier Originale (OpenAI Blog, OpenAI Help, OWASP LLM09, Anthropic-Doku) war in diesem Lauf
gesperrt (Berechtigungsanfrage nicht beantwortet). Laut `git diff` sind alle quellengestützten Sätze inhaltlich unverändert
gegenüber der in Runde 1 gegen die Originale geprüften Fassung (nur umgestellt; „KI-Anwendungen“ → „Anwendungen mit
Sprachmodellen“ = Hinweis aus Runde 1 umgesetzt). Regel 2 hält die korrigierte Anthropic-Formulierung (A2). A1–A4, G1–G4
nicht zurückgekehrt – außer dem Muster von A1 (veralteter INTERN-Absatz), siehe A5.

**Rechnungen nachgerechnet:** 10 − 6 − 1 = 3 € Deckungsbeitrag; 3 × 100 × 0,95 = 285 €; (3 ÷ 10) × 100 × 0,95 = 28,50;
100.000 × 1,1 = 110.000; × 1,1 = 121.000; linear 120.000. Text Z. 64/68, Box „Zum Ausprobieren“ und g4 stimmen überein.

**Ich-Aussagen gegen Tills Eingang:** alle belegt (Einstieg Z. 12, Z. 38, Fall 1–3, Regel 2 „Wenn ich heute …“, Prompt-Zusatz
wörtlich, „Meine Einschätzung“). Abschwächungen („unglaublich“, „enorm“, „begeistert“) und Streichung „Einzelhändler“ im
INTERN-Absatz offengelegt. Steckachse: nirgends behauptet, die Achse habe nicht gepasst – ok. „Beruflich“ nicht übernommen – ok.
**Ich-Form in den Fallabschnitten:** vertretbar. Es sind Tills echte, von ihm freigegebene Erfahrungen (Eingang: „dürfen in
Ich-Form verwendet werden“); auch der veröffentlichte KI-Agenten-Beitrag hat Ich-Form außerhalb der Einschätzung
(„Vier Beispiele, die ich für KMU spannend finde“). Rubrik bleibt Leitfäden: Die Fälle sind Anlass, kein Test mit ermittelten Ergebnissen.

### Checkliste

| # | Punkt | Ergebnis |
|---|---|---|
| 1 | Zahlen/Namen/Daten | ok (Quellen s. o., Rechnungen nachgerechnet) |
| 2 | Einschränkungen | ok – Beispielzahlen „nicht die Originaldaten“, Schwund „vereinfacht“, ausgedachte Beispiele gekennzeichnet |
| 3 | Originale verlinkt | ok |
| 4 | Nichts erfunden | ok (s. o.) |
| 5 | Platzhalter | ok – keine `[TILL]`/`[GRAFIK]` mehr. **Mangel A5:** INTERN-Absatz nennt noch einen Grafik-Platzhalter |
| 6 | Format, Länge, Teaser | ok – Einleitung 2 Absätze, Box 5 Punkte, H2 als Aussagen/Fragen, Zum Ausprobieren, Meine Einschätzung · Gedanke · Quellen; Teaser 141 Zeichen ≠ Titel. Länge ca. 2.100 Wörter inkl. Boxen (Hinweis) |
| 7 | Rubrik/Tags | ok – Wissen / Leitfäden + `#wissen` |
| 8 | Für KMU | entfällt |
| 9 | Ton/Verbote | ok – kein Handel, kein Arbeitgeber, kein CTA, Steigerungen entschärft |
| 10 | KMU-Bezug | ok – Handwerksbetrieb, Bäckerei/Gastronom, Betrieb mit 30 Leuten, Bürokraft/Küchenchefin |
| 11 | Grafiken | ok – g4 `g-vergleich` + `g-box--dunkel` aus dem Baukasten, Werte = Text, Titel als Aussage, Fußzeile mit Stand, Bildunterschrift ein Satz, Alt-Text vollständig; g5 neu passt zu Regeln 3/4 |
| 12 | Vorschaubild | ok – drei Zeilen, Logo, Lime-Kante |
| 13 | Ghost-Vorschau | nicht geprüft – Ghost enthält noch die alte Fassung; nach Korrektur neu hochladen |
| 14 | Wie bisher | ok – Aufbau wie KI-Agenten-Beitrag, 5 Schaubilder (Rahmen 4–5), `kmk-errors`/`kmk-prompt` aus `kaesten.html` |
| – | Inhaltliche Genauigkeit „Zum Ausprobieren“ | **Mangel A6** |

### Mängel Autor

**A5 – INTERN-Absatz veraltet** (Z. 10, letzter Satz: „Grafiken: g1, g2, g3, g5 bleiben; neu ein Grafik-Platzhalter für die Excel-Rechnung (Fall 2).“)
g4 ist eingebunden, g5 wurde geändert. → „Grafiken: fünf Schaubilder eingebunden; neu g4 (Excel-Rechnung 28,50 vs. 285 €), g5 an die neuen Regeln 3 und 4 angepasst.“

**A6 – Schritt 4 in „Zum Ausprobieren“ kann eine richtige Tabelle als falsch erscheinen lassen** (Z. 133, Schritt 4)
Im Text (Z. 64) ist 285 € ausdrücklich an die Vereinfachung „Schwund mindert die Absatzmenge“ gebunden. In der Box fehlt das.
Rechnet die Tabelle des Lesers den Schwund anders (z. B. als Aufschlag auf den Wareneinsatz), kommt korrekt ein anderer Wert
heraus, und „Sonst such die vertauschte Zelle“ schickt ihn auf Fehlersuche.
→ Schritt 4 ersetzen durch: „Rechne von Hand nach: Behandelt die Tabelle den Schwund als weniger verkaufte Stück, sind es
3 € × 100 × 0,95 = 285 €. Zeigt sie 28,50, wird wahrscheinlich durch den Verkaufspreis geteilt. Bei anderen Werten prüf, wie
die Tabelle den Schwund rechnet und ob Zellen vertauscht sind.“

### Mängel Grafik

Keine.

### Selbst korrigiert

- Z. 14: „Hier geht es um die Frage danach:“ → „Hier geht es um die Frage, die daraus folgt:“ (missverständlich). lexical.py danach fehlerfrei.

### Hinweise (kein Mangel)

- Länge ca. 2.100 Wörter inkl. Boxen, knapp über 1.900–2.000; begründet durch Tills drei Fälle. Falls kürzen: Z. 74 letzter Satz
  doppelt sich mit Regel 4 und „Meine Einschätzung“.
- g5 Regel 2 „Die KI markiert, was nicht aus deinen Unterlagen stammt“ – der Fließtext sagt das nicht mehr wörtlich (jetzt „weiß ich
  nicht“ + Prompt „Trenne Fakten von Annahmen“); passt sinngemäß. Fußzeile „u. a. nach OWASP, OpenAI, Anthropic“, Text nennt für
  die Regeln nur OWASP und Anthropic – durch „u. a.“ gedeckt.
- Z. 46 „ChatGPT hatte nicht alle nötigen Informationen“: Till schrieb „nicht zwingend alle“; durch seinen Satz „Für diese
  Sicherheit fehlten entscheidende Informationen“ gedeckt.
- Unverändert aus Runde 1: OLG-Hamm-Link erst nach dessen Veröffentlichung; Social-Kacheln mit großem Leerraum (Werkzeugverhalten).
- Ghost-Entwurf nach Umsetzung neu laden (g4 hochladen, g5 ersetzen).

## Runde 4 – 23.10.2026 (Prüfer, Express-Lauf, nur Nachprüfung A5/A6)

**Ergebnis: BESTANDEN**

| Mangel | Prüfung |
|---|---|
| A5 INTERN-Absatz | ok – „Grafiken: fünf Schaubilder eingebunden; neu g4 (Excel-Rechnung 28,50 vs. 285 €), g5 an die neuen Regeln 3 und 4 angepasst.“ Zusätzlich ist die Überschrift des Prompt-Kastens („Mein Zusatz für technische Fragen“) unter (2) als redaktionell markiert, wie es sein soll. |
| A6 Schritt 4 | ok – wörtlich nach Vorschlag, die Schwund-Annahme steht jetzt auch in der Box |

Z. 74 bleibt bewusst stehen (Pointe von Fall 3), das war nur ein Hinweis. Die Korrektur aus Runde 3 in Z. 14 ist erhalten.
`python3 tools/lexical.py` läuft fehlerfrei (rc 0). Der Ghost-Entwurf muss neu hochgeladen werden: g4 neu, g5 ersetzt.
