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

## Runde 5 – 25.10.2026 (Prüfer, Überarbeitung „100 % fachlich richtig, für KMU verständlich“)

**Ergebnis: NICHT BESTANDEN** (8 Fakten-Mängel, davon 3 inhaltlich ernst: F1 OWASP, F3 „neuer Chat“, F5 „genauso sicher“; 5 Verständlichkeits-Mängel; 1 Mangel an `quellen.md`. Alles mit Textänderungen lösbar, Grafiken ohne Mangel.)

Geprüft: beitrag.md (Stand 25.10.2026, 00:38 Uhr), quellen.md, alle eingebundenen PNGs angesehen (g6, g1, g4, g3, g5), dazu g4/g6-social,
vorschaubild.png, titel-ki-ergebnisse-pruefen-leitfaden.jpg, `redaktion/eingang/2026-10-23-till-eigene-ki-fehler.md`, Themenboard,
entscheidungen.md, blog-index.json, `redaktion/referenz/protokoll-per-ki-selbstversuch.html`, `entwuerfe/olg-hamm-chatbot-haftung/beitrag.md`,
Vergleich mit `redaktion/referenz/ki-agenten-…html`. `python3 tools/lexical.py` läuft fehlerfrei (rc 0). Ghost nicht angefasst.

### Quellen selbst gelesen (WebFetch, 25.10.2026)

| Quelle | Ergebnis |
|---|---|
| OpenAI „Why language models hallucinate“ (05.09.2025) | Definition, Pretraining/Rechtschreibung („errors there disappear with scale“), Geburtstag eines Haustiers („cannot be predicted from patterns alone and hence lead to hallucinations“), 1 zu 365, null Punkte, „accuracy will never reach 100 %“, „not inevitable … can abstain“: richtig wiedergegeben. Überdehnt: „Genau dort“ (F6). Kalai-Passage: „asked a widely used chatbot … produced three different answers—none of them correct“, Geburtstag „three different dates, likewise all wrong“ → Präsens-Verallgemeinerung (F7). |
| OpenAI Help „Does ChatGPT tell the truth?“ | „might sound confident—even when it’s wrong“, „Incorrect definitions, dates, or facts“, „Fabricated quotes, studies, citations or references to non-existent sources“, „first draft, not a final source“: richtig. „Datumsangaben“ korrekt. Seite heute „Updated: yesterday“, Inhalt unverändert passend. Sie sagt „kann“, nicht „genauso sicher wie bei richtigen Antworten“ (F5). |
| OWASP LLM09:2025 Misinformation (Stand 17.04.2025) | Halluzination als „one of the major causes“, dazu Bias und unvollständige Informationen. **Overreliance ist „a related issue“, das „exacerbates the impact“ – ausdrücklich keine Ursache** (F1). Folgen „security breaches, reputational damage, and legal liability“: richtig. Gegenmaßnahmen RAG, „cross-check LLM outputs with trusted external sources“, „human oversight and fact-checking … for critical or sensitive information“: deckt Regel 1. „Gemeinnützig“ steht weder hier noch auf der Charta-Seite (genai.owasp.org/project-mission-and-charter: „a global, open-source initiative“, „community-driven“) (F2). |
| Anthropic „Reduce hallucinations“ | „Explicitly give Claude permission to admit uncertainty. This technique can drastically reduce false information.“ – kein „allein“, und es geht um Claude (F4). Best-of-N: „Run Claude through the same prompt multiple times and compare the outputs. Inconsistencies … could indicate hallucinations.“ Neue Chats werden nicht erwähnt → Zusatz ist eigener Tipp, korrekt so gekennzeichnet, aber fachlich unvollständig (F3). „significantly reduce … don’t eliminate them entirely“: richtig. |
| Zusätzlich für F3: OpenAI Help 8983136 (Memory) und 8914046 (Temporary Chat) | „Chat history allows ChatGPT to reference past conversations when responding“; Temporary Chat „won’t reference or update memory“. Ein normaler neuer Chat ist also nicht zwingend unbeeinflusst. |
| Eigene Beiträge | Protokoll-Selbstversuch: „Einige Namen waren falsch geschrieben, und bei den Kassenprüfern stimmte die Amtszeit nicht.“ – Satz in Z. 89 passt. Schatten-KI- und KI-Agenten-Slug existieren (published). OLG Hamm: im blog-index (Stand 23.10. 05:48) noch `draft`, laut `berichte/2026-10-23.md` Z. 61/66 live unter /olg-hamm-chatbot-haftung/; Seite selbst für mich nicht abrufbar (WebFetch-Freigabe nicht beantwortet, curl 403 am Proxy). Inhalt laut Entwurf: Urteil 12.05.2026, 4 UKl 3/25, Falschangaben des Chatbots dem Betreiber zugerechnet (§ 5 UWG), Gesundheitsbereich. |

### Nachgerechnet

(10 − 6 − 1) = 3 € · 3 / 10 = 0,3 · 0,3 × 100 × 0,95 = **28,50** · 3 × 100 × 0,95 = **285 €** · 285 / 28,50 = 10 (= Verkaufspreis, also genau der Einheitenfehler) ·
Kontrolle: 0,3 × (10 × 100) × 0,95 = 285 € (Marge × Umsatz) · 100.000 × 1,1 = 110.000 · × 1,1 = 121.000 · linear 120.000.
Text Z. 71–77, Formelkasten, g4 und Box „Zum Ausprobieren“ (Schritte 3–5) stimmen überein.

### Fachlich ohne Quelle geprüft

- **Steckachse / 148 mm:** richtig. 148 mm ist die Einbaubreite der Hinterradnabe (Boost). Länge der Steckachse hängt zusätzlich vom Rahmen ab, das Gewinde (Steigung) ist rahmenabhängig. Aussage deckt sich mit Tills Text; nirgends behauptet, die Achse habe nicht gepasst. Ok – aber für Laien unverständlich (V1).
- **Bilderkennung vs. Halluzination:** Abgrenzung richtig (Fehlklassifikation ≠ Halluzination). „Und sie zweifelt nicht“ ist als Illustration vertretbar; echte Bilderkennungen geben meist einen Wahrscheinlichkeitswert aus (H8).
- **„Neuer Chat“-Tipp:** fachlich unvollständig, siehe F3. Fall 3 im eigenen Text belegt das Gegenteil: ChatGPT hat dort frühere Chats ausgewertet.
- **Deckungsbeitrag:** 3 € pro Stück = Preis minus variable Kosten (Einkauf, Material) – richtig. **Marge** als „Anteil am Preis“ – richtig (30 %). „Bruttogewinn“ (Tills Zellbezeichnung, g4) und „Deckungsbeitrag“ (Text) meinen hier dasselbe – fachlich vertretbar, für Laien zwei Namen für eine Zahl (H3).
- **Schwund-Vereinfachung:** offen benannt („vereinfacht“, „verdorbene Ware trotzdem eingekauft“) – ok. Sprachlich holpert „100 Verkäufe“ vs. „weniger verkaufte Stück“ (V4).
- **Wachstum:** richtig; „nicht 120.000“ steht so in Tills Text.

### Checkliste

| # | Punkt | Ergebnis |
|---|---|---|
| 1 | Zahlen/Namen/Daten wie in Quelle | **Mangel** F1–F8 |
| 2 | Einschränkungen | ok – Herstellerangaben benannt, Beispielzahlen und Vereinfachung genannt, Bild-Beispiel als Illustration markiert |
| 3 | Originale verlinkt | ok – vier Originale; für F3 ggf. OpenAI-Hilfeseite „Temporary Chat“ ergänzen |
| 4 | Nichts erfunden | ok – alle Ich-Sätze aus Tills Eingang (Z. 13, 47, 51–55, 59, 77, 81–83, 125 „Wenn ich heute …“, 145–149); redaktionelle Stellen im INTERN-Absatz unter (2) |
| 5 | Platzhalter | ok – keine |
| 6 | Format, Länge, Teaser | ok mit Hinweis – Einleitung 2 Absätze, Box 5 Punkte, H2 als Aussagen, Zum Ausprobieren, Meine Einschätzung · Gedanke · Quellen; Teaser 123 Zeichen ≠ Titel. **Länge ca. 2.060 Wörter Fließtext + 290 in Boxen ≈ 2.350** (Format 1.900–2.000) → H10. H2 Z. 117 → F8 |
| 7 | Rubrik/Tags | ok – Wissen / Leitfäden + `#wissen` |
| 8 | Für KMU | entfällt |
| 9 | Ton/Verbote | ok – kein Hype, kein CTA, kein Handel; H13 (Nähe Bilderkennung) |
| 10 | KMU-Bezug | ok – Handwerksbetrieb, Bäckerei/Gastronom, Betrieb mit 30 Leuten, Bürokraft/Küchenchefin, Teamrunde |
| 11 | Grafiken | ok – g6/g1/g4/g3/g5 aus dem Baukasten, Kicker, Titel als Aussage, Fußzeile mit Stand, Bildunterschrift je ein Satz, Alt-Texte vollständig, Werte = Text. Hinweise H3, H6, H8 |
| 12 | Vorschaubild | ok – „LEITFÄDEN“, neuer Titel in drei Zeilen lesbar, Logo, Lime-Kante |
| 12a | Titelbild | ok – Einordnung, drei Stufen, ein Merksatz, ohne Titel, keine Zahl, `titelbild:` im Frontmatter |
| 13 | Ghost-Vorschau | nicht prüfbar – Ghost hat noch die alte Fassung (ghost.json: alter Titel, kein g6). Nach Korrektur neu laden (g4, g6, Vorschaubild); danach Vorschau auf doppelten Titel prüfen |
| 14 | Wie bisher | ok – Aufbau wie KI-Agenten-Beitrag, 5 Schaubilder (Rahmen 4–5), Kästen aus `kaesten.html`/`kurz.html` |

### Mängel – Fakten

**F1 – OWASP: übermäßiges Vertrauen ist keine Ursache** (Z. 87, Satz 2 und 3)
Text: „Als Ursache nennt es neben den Halluzinationen ausdrücklich das übermäßige Vertrauen … Erst dadurch wird aus einem Fehler ein Schaden.“
Quelle: „A related issue is overreliance … This overreliance exacerbates the impact of misinformation“. Ursachen sind laut OWASP Halluzination, Verzerrungen in Trainingsdaten, unvollständige Informationen. „Erst dadurch“ ist stärker als „verstärkt“.
→ „Dazu nennt OWASP ein verwandtes Problem: übermäßiges Vertrauen. Menschen prüfen die Antworten nicht genug und übernehmen falsche Angaben in Entscheidungen und Abläufe. Das verstärkt den Schaden.“

**F2 – OWASP „gemeinnützige Gemeinschaft“ nicht belegt** (Z. 87, Satz 1)
Weder die verlinkte Seite noch die Projekt-Charta sagt „gemeinnützig“. Die Charta sagt „global, open-source initiative“, „community-driven“. Außerdem kennt der Bäcker „OWASP“ nicht.
→ „Das OWASP Gen AI Security Project, eine weltweite, offene Initiative von Fachleuten für IT-Sicherheit, führt Fehlinformation durch Sprachmodelle in seiner Liste der zehn wichtigsten Risiken für KI-Anwendungen wie Chatbots (Stand 2025).“

**F3 – „neuer Chat“-Tipp fachlich unvollständig** (Z. 125: „Praktisch heißt das: Frag am besten jeweils in einem neuen Chat, damit die erste Antwort die nächste nicht beeinflusst.“)
ChatGPT kann über die Erinnerungsfunktion auf frühere Chats zurückgreifen (OpenAI-Hilfe: „Chat history allows ChatGPT to reference past conversations“); Fall 3 im Beitrag zeigt genau das. Ein normaler neuer Chat ist also nicht sicher unabhängig.
→ „Unser Tipp dazu: Frag jeweils in einem neuen Chat, bei ChatGPT am besten in einem temporären Chat. Ein normaler neuer Chat kann über die Erinnerungsfunktion frühere Gespräche einbeziehen.“
Quelle ergänzen: [OpenAI Help Center: Temporary Chat FAQ](https://help.openai.com/en/articles/8914046) (abgerufen 25.10.2026). Vorher die deutsche Bezeichnung in der ChatGPT-Oberfläche („Temporärer Chat“) einmal selbst nachsehen.

**F4 – Anthropic „allein“ überdehnt, und die Doku gilt für Claude** (Z. 125: „Anthropic schreibt in seiner Dokumentation, dass allein diese Erlaubnis falsche Angaben deutlich verringern kann.“)
Quelle: „This technique can drastically reduce false information“ – ohne „allein“, bezogen auf Claude.
→ „Anthropic schreibt in der Dokumentation zu seinem Modell Claude, dass diese Erlaubnis falsche Angaben deutlich verringern kann.“

**F5 – „genauso sicher wie bei richtigen Antworten“ stärker als die Quelle** (Z. 15 und Box „30 Sekunden“, Punkt 1)
OpenAI: „might sound confident—even when it’s wrong“ / „may express high confidence even in incorrect answers“. Das ist ein „kann“, keine Regel.
→ Z. 15: „Sie liegt falsch und kann dabei genauso sicher klingen wie bei richtigen Antworten.“ · Box Punkt 1: „KI liegt manchmal falsch und kann dabei genauso sicher klingen wie bei richtigen Antworten.“

**F6 – „Genau dort entstehen Halluzinationen“ klingt ausschließlich** (Z. 31, letzter Satz)
OpenAI: Solche Fakten „cannot be predicted from patterns alone and hence lead to hallucinations“ – nicht: nur dort. Außerdem trennt ein Komma zwei Hauptsätze.
→ „Rechtschreibung folgt festen Mustern. Solche Fehler verschwinden, je größer die Modelle werden. Seltene Einzelfakten wie der Geburtstag eines Haustiers folgen keinem Muster. Bei solchen Fakten entstehen Halluzinationen.“

**F7 – Kalai-Beispiel als allgemeine Regel im Präsens** (Z. 33)
„Fragt man einen verbreiteten Chatbot …, nennt er drei verschiedene Titel“ liest sich, als passiere das immer. OpenAI berichtet einen einzelnen Versuch. „An einem eigenen Mitautor“ versteht ein Laie nicht.
→ „Wie das aussieht, zeigt OpenAI an einem der Autoren des Forschungsbeitrags. Als das Team einen verbreiteten Chatbot nach dem Titel seiner Doktorarbeit fragte, gab er drei verschiedene Antworten. Keine davon stimmte. Beim Geburtstag war es genauso.“

**F8 – Zwischenüberschrift „die meisten Fehler“ ohne Beleg** (Z. 117)
Mengenaussage ohne Quelle. → „Fünf Regeln, die viele Fehler abfangen“

### Mängel – Verständlichkeit (Leser: Bäckerei-Inhaber, 12 Leute, ohne Technikwissen)

**V1 – Fall 1 voller Fachwörter** (Z. 51–53: Steckachse, Gewindesteigung, Hinterrad-Einbaubreite, Nabe)
Ohne Fahrradwissen versteht man nicht, was das Problem war.
→ Z. 51 nach „Steckachse“: „…, also die Achse, die das Hinterrad im Rahmen hält und an der der Anhänger befestigt wird.“
→ Z. 53 Satz 2–3 ersetzen: „ChatGPT hatte aus einem einzigen Maß, der Breite der Hinterradnabe von 148 Millimetern, auf die passende Achse geschlossen. Wie lang die Achse sein muss und welches Gewinde der Rahmen hat, folgt daraus aber nicht. Beides war nicht geprüft.“

**V2 – Doppelte Verneinung** (Z. 37: „Halluzinationen sind trotzdem nicht unvermeidbar, denn …“)
→ „Halluzinationen sind trotzdem kein Naturgesetz: Ein Modell kann bei Unsicherheit auch sagen, dass es etwas nicht weiß.“

**V3 – Sprung vom Tiger zur Halluzination** (Z. 29: „Bei Texten heißt das **Halluzination**.“)
Direkt davor steht, der Tiger sei keine Halluzination. „Das“ bezieht sich für den Leser auf den Tiger.
→ „Wenn ein Sprachmodell wie ChatGPT auf diese Weise etwas Falsches behauptet, heißt das **Halluzination**.“ (Den Erklärsatz zu Sprachmodellen dann direkt dahinter setzen.)

**V4 – „100 Verkäufe“ und „weniger verkaufte Stück“ widersprechen sich scheinbar** (Z. 73, Box Schritt 3/4)
Erst sind es 100 Verkäufe, dann wird mit 0,95 gerechnet. Der Bäcker fragt: Wurden 100 oder 95 verkauft?
→ Z. 73: „Rechnet man den Schwund so wie die Tabelle, also vereinfacht als weniger verkaufte Stück (von 100 geplanten werden 95 verkauft), ergibt sich …“ Box Schritt 4 analog: „… als weniger verkaufte Stück (95 statt 100), sind es …“

**V5 – „bewertet“ bleibt unklar** (Z. 35: „Sprachmodelle werden so trainiert und bewertet, …“)
Wer bewertet? → „Dazu kommt: Die Tests, mit denen Sprachmodelle trainiert und verglichen werden, zählen meist nur richtige Antworten. Raten lohnt sich dort mehr als ein ehrliches ‚Ich weiß es nicht‘.“ (OpenAI: Bewertungen „reward guessing over acknowledging uncertainty“.)

### Mangel – Unterlagen

**Q1 – `quellen.md` veraltet** (nicht im Beitrag sichtbar, aber Arbeitsgrundlage)
Steht noch: „Verworfen gemäß Tills Vorgaben: Hund-Tiger-Meme“ und „OLG Hamm: noch nicht online“. Es fehlen: die neue OpenAI-Passage (Pretraining, Rechtschreibung, Haustier-Geburtstag) und Tills Wunsch vom 25.10. zum Bild-Beispiel.
→ Abschnitt „Stand 25.10.2026“ ergänzen; Meme-Zeile als „überholt am 25.10.2026 (Till, Chat): als eigene Illustration erlaubt“ markieren, nicht löschen.

### Hinweise (kein Mangel, für Autor/Chefredakteur/Till)

- **H1** Z. 71: Marge greifbar machen: „… eine Marge, also einen Anteil am Preis (hier 3 von 10 Euro, also 30 Prozent).“
- **H2** Z. 73: „Einheitenfehler“ ist neu für Laien → „Schon dieser Fehler, Anteil statt Euro, macht aus 285 Euro 28,50.“
- **H3** g4 rechts „Bruttogewinn pro Jahr in Euro“, Text sagt „Deckungsbeitrag“. Entweder im Text einmal gleichsetzen („der Bruttogewinn, hier also Deckungsbeitrag mal verkaufte Stück“) oder g4-Label lassen – fachlich nicht falsch.
- **H4** Z. 115: „Schatten-KI“ kurz erklären: „(also KI-Nutzung, von der die Leitung nichts weiß, siehe [Schatten-KI](…))“.
- **H5** Z. 133: „Absatzmenge“ → „verkaufte Stückzahl“; „Passt eine unabhängig gerechnete Stichprobe?“ → „Stimmt eine Beispielrechnung von Hand mit der Tabelle überein?“
- **H6** g1 steht hinter dem Absatz zu OpenAIs Folgerung (Z. 37), zeigt aber das Raten aus Z. 35. Besser direkt nach Z. 35 („Also rät das Modell.“).
- **H7** Z. 43: „Eine falsch zugeordnete Zelle in einer Excel-Tabelle (siehe Fall 2) …“ – sonst Vorgriff ohne Anker.
- **H8** g6: „nachgestelltes Beispiel“ (Fußzeile, Bildunterschrift Z. 25) klingt nach einem echten, nachgespielten Vorfall. Die Herkunft des Bildes ist unklar → „ausgedachtes Beispiel“ bzw. Bildunterschrift „Ein ausgedachtes Beispiel: Die KI erkennt das Muster, nicht das Tier.“ Z. 27 „Und sie zweifelt nicht.“ genauer: „Und sie meldet keinen Zweifel.“
- **H9** Z. 93 „ausgedachte, aber typische Beispiele“ und Box Punkt 2 „typische Muster“: „typisch“ ist nicht belegt → „naheliegende Beispiele“ / „wiederkehrende Muster“.
- **H10** Länge ≈ 2.350 Wörter inkl. Boxen (Runde 3: ≈ 2.100). Zuwachs kommt von Tills Wunsch nach Erklärungen – vertretbar, aber über dem Rahmen. Wenn kürzen: Z. 43 (Halluzination vs. Logikfehler) und Z. 89 Satz 1 doppeln sich mit Fall 2/Fall 3; Z. 135 letzter Satz doppelt sich mit „Meine Einschätzung“.
- **H11** Überschrift: selbsterklärend, ja – Problem und Nutzen stehen drin, 78 Zeichen, drei Zeilen im Vorschaubild. Ganz genau wäre „KI kann sich irren und trotzdem sicher klingen: So prüfst du KI-Ergebnisse im Betrieb“ (passt zu F5). Als Überschrift ist die Zuspitzung vertretbar; Till entscheidet.
- **H12** Z. 123 „OWASP empfiehlt genau das“ → „Das entspricht der Empfehlung von OWASP“ (OWASP spricht über technische Anwendungen; der Abgleich durch Nutzer steht dort aber ausdrücklich).
- **H13** Bild-Beispiel: Bilderkennung liegt nah an Tills beruflichem Feld. Im Text kein Bezug zu Arbeitgeber oder Handel → kein Verstoß. Themenboard und `entscheidungen.md` sagen noch „ohne Meme“; Tills neuen Wunsch vom 25.10. trägt der Chefredakteur dort ein.
- **H14** Z. 91 OLG Hamm: Der Satz verallgemeinert ein Urteil aus dem Gesundheitsbereich. Der verlinkte Beitrag ordnet das ein; genauer wäre „… sagst am Ende du. So hat das OLG Hamm die Falschangaben eines Website-Chatbots dem Betreiber zugerechnet.“
- **H15** Ghost hat noch die Fassung vom 23.10. (alter Titel, g2 statt g6). Nach Korrektur `ghost.py draft` neu, g4/g6/Vorschaubild hochladen, dann Punkt 13 nachholen.
- **H16** Social-Kacheln g4/g6: großer Leerraum (Werkzeugverhalten, bekannt), nicht Teil des Beitrags.

## Runde 6 – 25.10.2026 (Prüfer, Nachprüfung Runde 5)

**Ergebnis: NICHT BESTANDEN** (ein neuer Mangel aus der Umsetzung von V1, ein Satz; sonst alles sauber)

Geprüft: beitrag.md (neu), quellen.md (Nachtrag 25.10.), g4/g6 und ihre Social-Kacheln (neu gerendert 22:53, angesehen),
`python3 tools/lexical.py` (rc 0). Quellen für die neuen Aussagen: OpenAI Help 8914046 und 8983136 (am 25.10. gelesen, siehe Runde 5),
`entwuerfe/olg-hamm-chatbot-haftung/beitrag.md`, Tills Eingang `redaktion/eingang/2026-10-23-till-eigene-ki-fehler.md`.

### Mängel aus Runde 5

| Mangel | Prüfung |
|---|---|
| F1 OWASP | ok – Z. 87 „Dazu nennt es ein verwandtes Problem: übermäßiges Vertrauen … Das verstärkt den Schaden.“ = „related issue … exacerbates the impact“ |
| F2 „gemeinnützig“ | ok – „eine weltweite, offene Initiative von Fachleuten für IT-Sicherheit“ = Charta „global, open-source initiative“, „community-driven“ |
| F3 neuer Chat | ok – siehe unten |
| F4 Anthropic | ok – „in der Dokumentation zu seinem Modell Claude, dass diese Erlaubnis … deutlich verringern kann“ |
| F5 „genauso sicher“ | ok – Z. 15 und Box Punkt 1 „kann … genauso sicher klingen“ |
| F6 „Genau dort“ | ok – „Bei solchen Fakten entstehen Halluzinationen.“, Satz geteilt |
| F7 Kalai | ok – Vergangenheit, „einem der Autoren des Forschungsbeitrags“, „gab er drei verschiedene Antworten. Keine davon stimmte.“ |
| F8 „die meisten“ | ok – „Fünf Regeln, die viele Fehler abfangen“ |
| V1 Steckachse | Erklärung ok, **aber neuer Mangel R6-1** (siehe unten) |
| V2 Doppelte Verneinung | ok – „kein Naturgesetz“ |
| V3 Tiger → Halluzination | ok |
| V4 100 vs. 95 | ok – Text, Box Schritt 3, g4 („100 Stück eingeplant“, Fußzeile „95 von 100 Stück verkauft“) |
| V5 „bewertet“ | ok – „Die Tests, mit denen Sprachmodelle trainiert und verglichen werden, zählen meist nur richtige Antworten.“ |
| Q1 quellen.md | ok – Nachtrag 25.10., alte Vermerke als überholt markiert, nicht gelöscht |
| H1–H9, H12, H14 | umgesetzt; H10, H11, H13 bewusst offen (begründet) |

### Neue Aussagen

- **Temporärer Chat (Z. 125):** „Bei ChatGPT geht das am sichersten in einem temporären Chat, denn ein normaler neuer Chat kann je nach Einstellung frühere Gespräche einbeziehen.“ – ok. 8983136: „Chat history allows ChatGPT to reference past conversations“, abschaltbar in den Einstellungen; 8914046: Temporary Chat „won’t access or create memories“, nutzt frühere Gespräche nur „for limited safety and security purposes“ → „am sichersten“ statt „sicher“ ist genau richtig. „Je nach Einstellung“ deckt auch ab, dass der Chatverlauf nur bei bestimmten Konten verfügbar ist. Beide Quellen stehen in der Quellenliste.
- **OLG-Satz (Z. 91):** „So hat das OLG Hamm die Falschangaben eines Website-Chatbots dem Betreiber zugerechnet.“ – ok, deckt sich mit dem OLG-Beitrag („irreführende geschäftliche Handlung nach § 5 UWG, die dem Betreiber zuzurechnen ist“). Keine Verallgemeinerung über den Fall hinaus.
- **Schwund-Absatz (Z. 73):** 10 − 6 − 1 = 3 €; 30 % = 3/10 ✓; 100 × 0,95 = 95 ✓; 3 × 95 = 285 € ✓; 0,3 × 100 × 0,95 = 28,50 ✓; „Anteil statt Euro“ = Faktor 10 = Verkaufspreis ✓. Box Schritt 3/4 und g4 stimmen überein.

### Mangel

**R6-1 – Steckachse: „aus einem einzigen Maß“ geht über Tills Text hinaus** (Z. 53, Satz 2)
Tills Eingang: „ChatGPT hatte **unter anderem** aus der bekannten Hinterrad-Einbaubreite von 148 Millimetern … geschlossen.“ „Aus einem einzigen Maß“ behauptet in Tills Ich-Fall mehr, als er gesagt hat. Der Fehler kommt aus meinem Formulierungsvorschlag V1 in Runde 5.
→ „ChatGPT hatte unter anderem aus der Breite der Hinterradnabe von 148 Millimetern auf die passende Achse geschlossen.“ (Rest des Absatzes bleibt.)

### Hinweise (kein Mangel)

- Z. 33 „nach dem Titel seiner Doktorarbeit“: „seiner“ kann sich auch auf den Chatbot oder das Team beziehen → „nach dem Titel der Doktorarbeit dieses Autors“.
- Z. 87 letzter Satz steht direkt nach dem übermäßigen Vertrauen und liest sich als dessen Folge. OWASP nennt die Folgen für Fehlinformation insgesamt → „Als mögliche Folgen von Fehlinformation nennt OWASP …“.
- Z. 73 „Das ist der Bruttogewinn, den die Formel liefern sollte.“ → genauer „… den die Formel nach ihrer eigenen Logik liefern sollte.“ Der Satz danach grenzt das ohnehin ab.
- Formelkasten Z. 66 nennt C34 weiter „Anzahl der Verkäufe pro Jahr“ (Tills Originalbezeichnung), der Text „100 Stück eingeplant“. Vertretbar, weil es die Originalformel ist.
- INTERN-Absatz (e) erwähnt die neue Steckachsen-Formulierung nicht ausdrücklich; nach R6-1 gibt es keinen Grund mehr dafür.
- Ghost hat weiter die Fassung vom 23.10. → nach der Korrektur neu laden (g4, g6, Vorschaubild), dann Punkt 13.

## Runde 7 – 25.10.2026 (Prüfer, Nachprüfung R6-1 und drei Hinweise)

**Ergebnis: BESTANDEN**

Geprüft: `git diff --word-diff HEAD~1 HEAD` auf beitrag.md (Commit a600f6b). Geändert sind genau die vier Stellen, sonst nichts.
`python3 tools/lexical.py` läuft ohne Fehler (rc 0).

| Stelle | Prüfung |
|---|---|
| R6-1, Z. 53 | ok – „ChatGPT hatte unter anderem aus der Breite der Hinterradnabe von 148 Millimetern auf die passende Achse geschlossen.“ Deckt sich mit Tills „unter anderem aus der … Einbaubreite von 148 Millimetern“, Satz grammatisch sauber |
| Z. 33 | ok – „nach dem Titel der Doktorarbeit dieses Autors“, Bezug eindeutig |
| Z. 73 | ok – „den die Formel nach ihrer eigenen Logik liefern sollte“ |
| Z. 87 | ok – „Als mögliche Folgen von Fehlinformation nennt OWASP …“ = „This vulnerability can lead to … reputational damage, and legal liability“ |

Damit sind alle Mängel aus Runde 5 und 6 behoben. Offen bleiben nur bewusst entschiedene Punkte: Länge (H10), Titel (H11), Eintrag zu Tills Bild-Wunsch in `entscheidungen.md` (H13) sowie die INTERN-Punkte für Till.
Vor der Freigabe: Ghost-Entwurf neu laden (g4, g6, Vorschaubild) und die Vorschau prüfen (Punkt 13, doppelter Titel).

## Runde 8 – 25.10.2026 (Prüfer, neue Stellen aus Commit 879fa0c: Ton, Kurzfassung, Regel 2 mit Studie, Prompt)

**Ergebnis: NICHT BESTANDEN** (vier kleine Mängel, alle mit je einem Satz lösbar; der Ton ist jetzt ausgewogen)

Geprüft: `git diff HEAD~1` auf beitrag.md (nur die neuen Stellen), quellen.md, `python3 tools/lexical.py` (rc 0).
Studie selbst gelesen: PubMed 40753316 (Abstract) und medRxiv-Preprint 10.1101/2025.03.18.25324184 (Volltext-PDF).
doi.org/10.1038/s43856-025-01021-3 (Nature-Seite) war für mich nicht abrufbar (WebFetch-Freigabe nicht beantwortet).
Die Angaben aus PubMed decken sich mit Titel, Band 5, Artikel 330, 02.08.2025 und DOI.

### Abgleich der neuen Aussagen

| Stelle | Quelle | Ergebnis |
|---|---|---|
| Studie: „Communications Medicine, August 2025“ | PubMed: Commun Med 5(1):330, 02.08.2025 | ok |
| „in 300 Fallbeschreibungen je einen erfundenen Begriff, etwa einen Laborwert, den es nicht gibt“ | 300 ärztlich geprüfte Vignetten, je ein erfundenes Detail (Laborwert, körperliches/radiologisches Zeichen, Krankheit) | ok |
| „sechs KI-Modellen“ | 6 LLMs, 5.400 Ausgaben | ok |
| „im Schnitt in 66 Prozent … auf den erfundenen Begriff ein, als gäbe es ihn“ | „elaborated on the fabricated detail“; Mittel über alle Modelle 66 % (Preprint 65,9 %) | ok |
| „nur gesicherte Informationen … Unsicherheit zuzugeben, statt zu spekulieren … 44 Prozent“ | „use only clinically validated information and acknowledge uncertainty instead of speculating further“; 44 % (44,2 %), p < 0,001 | ok („gesicherte“ für „clinically validated“ ist vertretbar) |
| „Die Anweisung verringert Fehler, beseitigt sie aber nicht.“ | „While prompt engineering reduces errors, it does not eliminate them.“ | ok |
| „Der Test war absichtlich schwer“ | adversarial attack, erfundene Angaben bewusst eingebaut | ok, aber Einschränkung fehlt → M3 |
| Regel 2: „Laut OpenAI kann sie auch bei falschen Antworten große Sicherheit ausdrücken.“ | Help: „The model may express high confidence even in incorrect answers.“ | ok |
| „denn die KI bemerkt nicht immer, dass sie falschliegt“ | eigene Folgerung, durch den OpenAI-Satz gedeckt | ok (Hinweis H-c) |
| Kurzfassung Punkt 2: „Anfällig sind vor allem seltene Fakten, Datumsangaben, Zitate und Quellen sowie Fragen, bei denen wichtige Angaben fehlen.“ | OpenAI-Paper: seltene Einzelfakten („arbitrary low-frequency facts“) führen zu Halluzinationen. Hilfeseite: „Incorrect definitions, dates, or facts“, „Fabricated quotes, studies, citations or references“, „Overconfident answers to ambiguous or complex questions“ als Beispiele. Fehlende Angaben: Tills Fall 1 | **die Inhalte sind gedeckt, „vor allem“ und „nicht wahllos“ nicht** → M2 |
| Kurzfassung Punkt 4: „Ein Zusatz im Prompt hilft nachweislich: … „weiß ich nicht“ … und Fakten von Annahmen trennen lassen.“ | Studie testete „nur gesicherte Informationen + Unsicherheit zugeben“; Anthropic: Herstellerangabe zu „I don’t know“; „Fakten und Annahmen trennen“ hat niemand getestet | **„nachweislich“ überdehnt** → M1 |
| Einleitung, Satz nach Regel 5 | keine Faktenaussage | ok |
| Prompt-Kasten, zwei neue Sätze | redaktionell, im INTERN-Absatz (f) als „bitte bestätigen“ markiert | ok |
| Quellenliste | Originalveröffentlichung (DOI) verlinkt, Titel, Band, Nummer, Datum korrekt | ok |

Kurzfassung: genau 5 Punkte – ok. `lexical.py` – ok.

### Ton

Ausgewogen, ohne zu beschönigen. Die Einleitung stellt das Vertrauen klar. Die Kurzfassung ist jetzt lösungsorientiert (Stufen, Prompt, Test), und der Satz nach Regel 5 begrenzt den Aufwand auf Stufe 2 und 3. Die Studie nennt beide Zahlen und sagt ausdrücklich „nicht auf null“. Einziges Risiko für den Ton: Ohne Einordnung liest man 66 Prozent als allgemeine Fehlerquote (M3) – das wäre wieder zu negativ und fachlich falsch.

### Mängel

**M1 – Kurzfassung Punkt 4: „nachweislich“ deckt nicht beide Hälften**
Belegt ist eine Anweisung, bei Unsicherheit nichts zu erfinden (Studie; Anthropic als Herstellerangabe). „Fakten von Annahmen trennen“ hat niemand getestet.
→ „Ein Zusatz im Prompt hilft: der KI erlauben, „weiß ich nicht“ zu sagen. In einer Studie senkte eine solche Anweisung die Fehler deutlich, aber nicht auf null.“

**M2 – Kurzfassung Punkt 2: „nicht wahllos … vor allem“ ist eine Rangfolge ohne Beleg**
Die Hilfeseite nennt Beispiele, keine Häufigkeiten. Die Inhalte sind gedeckt, die Gewichtung nicht.
→ „Typische Fehlerstellen nennt OpenAI selbst: seltene Fakten, Datumsangaben, Zitate und Quellen. Dazu kommen Fragen, bei denen wichtige Angaben fehlen.“

**M3 – Studie: Geltungsbereich der Prozentwerte fehlt** (Regel 2, Absatz 2, nach „… waren es 44 Prozent.“)
Checkliste Punkt 2: Die Zahlen gelten für Fallbeschreibungen mit absichtlich eingebauten falschen Angaben in der Medizin, nicht für normale Fragen. Ohne diesen Satz liest der Bäcker „KI geht in zwei von drei Fällen auf Erfundenes ein“.
→ Einfügen: „Die Prozentwerte gelten für diesen Test mit absichtlich falschen Angaben, nicht für normale Fragen im Alltag.“

**M4 – `quellen.md` ohne die Studie**
Kein Eintrag zu Omar, Klang u. a. → ergänzen: DOI, PubMed 40753316, medRxiv 10.1101/2025.03.18.25324184, 300 Vignetten, 6 Modelle, 5.400 Ausgaben, 65,9 % → 44,2 % (Abstract 66 → 44 %), Wortlaut des Mitigation-Prompts laut Preprint, Temperatur 0 ohne Effekt, Fazit-Zitat. Dazu der Vermerk, dass die Nature-Seite nicht selbst gelesen wurde.

### Hinweise (kein Mangel)

- **H-a Einleitung:** „Das heißt nicht, dass man KI nicht vertrauen kann.“ ist eine doppelte Verneinung, und „wissen sollte … und dort gezielt hinschaut“ ist grammatisch schief → „Das heißt nicht, dass man KI misstrauen muss. Man sollte aber wissen, wo sie danebenliegen kann, und dort gezielt hinschauen.“
- **H-b Prompt:** Der Satz davor spricht von „technischen Produkten“, der Kasten heißt jetzt „für wichtige Fragen“ → Einleitungssatz anpassen oder den Kasten wieder „für technische Fragen“ nennen. Till muss die zwei neuen Sätze im Kasten bestätigen (INTERN f).
- **H-c Regel 2:** „bemerkt nicht immer“ vermenschlicht. Genauer: „denn die KI kann auch bei falschen Antworten sehr sicher klingen“ – dann lässt sich der zweite Halbsatz mit „Laut OpenAI …“ kürzen.
- **H-d Regel 2, Satz Z. 119:** „Regel 1 und 2 stützen sich auf Empfehlungen von OWASP und von Anthropic“ – jetzt kommt auch eine Studie dazu. Optional: „… von OWASP, Anthropic und einer Studie“.
- **H-e Länge:** etwa 2.370 Wörter Fließtext + 330 in Boxen ≈ 2.700 (Runde 5: ≈ 2.350; Format 1.900–2.000). Regel 2 ist jetzt der längste Abschnitt. Wenn kürzen: Kalai-Absatz (Z. 33), Z. 43 und Z. 89 Satz 1.
- **H-f Ghost:** weiter Fassung vom 23.10. → nach Korrektur neu laden, dann Punkt 13.

## Runde 9 – 25.10.2026 (Prüfer, Nachprüfung Runde 8)

**Ergebnis: BESTANDEN**

Geprüft: `git diff --word-diff HEAD~1` (Commit 66e6d28) auf beitrag.md und quellen.md. Geändert sind nur die genannten Stellen.
`python3 tools/lexical.py` läuft ohne Fehler (rc 0). Die Kurzfassung hat weiter genau 5 Punkte.

| Punkt | Prüfung |
|---|---|
| M1 Kurzfassung 4 | ok – „Ein Zusatz im Prompt hilft: der KI erlauben, „weiß ich nicht“ zu sagen. In einer Studie senkte eine solche Anweisung die Fehler deutlich, aber nicht auf null.“ Deckt sich mit 66 → 44 % und „does not eliminate them“ |
| M2 Kurzfassung 2 | ok – „Typische Fehlerstellen nennt OpenAI selbst: seltene Fakten, Datumsangaben, Zitate und Quellen. Dazu kommen Fragen, bei denen wichtige Angaben fehlen.“ Keine Rangfolge mehr; die Aufzählung ist durch das Paper und die Hilfeseite gedeckt |
| M3 Geltungsbereich | ok – „Die Prozentwerte gelten für diesen Test mit absichtlich falschen Angaben, nicht für normale Fragen im Alltag.“ |
| M4 quellen.md | ok – Nachtrag mit DOI, PubMed, medRxiv, Aufbau, 65,9 → 44,2 %, GPT-4o 53 → 23 %, Temperatur 0, Wortlaut laut Preprint, Fazit-Zitat, Einschränkung, Vermerk „Nature-Seite nicht selbst gelesen“. Alle Zahlen stimmen mit meiner Lektüre aus Runde 8 überein |
| H-a Einleitung | ok – „Das heißt nicht, dass man KI misstrauen muss. Man sollte aber wissen, wo sie danebenliegen kann, und dort gezielt hinschauen.“ |
| H-b Prompt-Kasten | ok – wieder „Mein Zusatz für technische Fragen“, passt zum Satz davor |
| H-c Regel 2 | ok – „denn laut OpenAI kann die KI auch bei falschen Antworten sehr sicher klingen“ = „may express high confidence even in incorrect answers“ |
| H-d Z. 119 | ok – „… sowie auf eine Studie“ |

### Hinweise (kein Mangel)

- quellen.md nennt die Koautoren Sorin und Nadkarni, PMC12318031 und die Beispiel-Begriffe („Serum Neurostatin“ usw.). Das habe ich nicht selbst gegengelesen. Es steht nur intern, nicht im Beitrag.
- Bewusst offen: Länge (≈ 2.700 Wörter, H-e), Titel (H11), Eintrag in `entscheidungen.md` (H13), Bestätigung der zwei neuen Prompt-Sätze durch Till (INTERN f).
- Vor der Freigabe: Ghost-Entwurf neu laden (g4, g6, Vorschaubild) und die Vorschau prüfen (Punkt 13).

## Runde 10 – 25.10.2026 (Prüfer, Tills KI-Beispielbild statt g6)

**Ergebnis: BESTANDEN** (nur Hinweise)

Geprüft: `git diff HEAD~1` (Commit 8327dcb) auf beitrag.md und entscheidungen.md, `ki-beispielbild-hund-tiger.jpg` angesehen
(1122 × 1402, 405 KB). `python3 tools/lexical.py` läuft ohne Fehler (rc 0). `lexical.IMG` erkennt alle 5 Bildzeilen,
die Bildkarte hat Alt-Text und Bildunterschrift. `ghost.py` lädt lokale Bilder unabhängig von der Endung hoch (.jpg ok).
Zum Vergleich gelesen: eigener Beitrag `ai-act-ki-bilder-kennzeichnen` (Referenz).

| Punkt | Ergebnis |
|---|---|
| Text passt zum Bild | ok – „Ein Hund **liegt** im Schatten eines Zauns“ (im Bild liegt er, früher hieß es „steht“). „Die Schattenstreifen lassen sein Fell gestreift aussehen“, grüner Rahmen „Tiger“, „den Zaun, der den Schatten wirft“ = Pfeil „Context“ auf das Gitter. Ausschnitt unten im Alt-Text beschrieben |
| KI-Kennzeichnung ehrlich | ok – Bildunterschrift beginnt mit „Mit KI erstelltes Beispielbild“, Alt-Text mit „Mit KI erstelltes Foto“. Im Text „könnte daraus einen Tiger machen“, „Das Beispiel ist ausgedacht und das Bild mit KI erstellt, es ist kein Messergebnis“. Nicht als echter Fall lesbar. Entspricht der eigenen Empfehlung im AI-Act-Beitrag („in der ersten Zeile der Bildunterschrift“) |
| Alt-Text | ok – nennt Art (mit KI erstelltes Foto) und Inhalt, inkl. Rahmen, Pfeil und Ausschnitt |
| Bildunterschrift | ok – Kennzeichnung plus Lesehilfe. Hat zwei Sätze; die Ein-Satz-Regel in `kmk-ci-grafik` gilt für Grafiken, hier geht die Kennzeichnung vor (Hinweis H10-1) |
| Bildanzahl | ok – 5 Bilder: KI-Foto, g1, g4, g3, g5 (4 Schaubilder + 1 Foto, Rahmen Langtext 4–5). g6 bleibt als Datei, nicht eingebunden |
| Bildsprache / CI | ok – Ausnahme zu „echte Fotos“ in `entscheidungen.md` mit Tills Wortlaut festgehalten; kein KI-erzeugter Mensch, kein Logo, keine Marke |
| entscheidungen.md | ok – Eintrag angehängt, nichts gelöscht |

### Hinweise (kein Mangel)

- **H10-1 Bildunterschrift in einem Satz** (optional, CI-näher): „Mit KI erstelltes Beispielbild: Die Streifen sind nur der Schatten des Zauns – wer das übersieht, sieht einen Tiger.“
- **H10-2 Satzmodus:** Vor dem Bild steht der Konjunktiv („könnte … machen“), danach der Indikativ („Die KI erkennt … Und sie meldet keinen Zweifel“), dann wieder Konjunktiv („wäre“). Einheitlicher: „Sie würde das Muster erkennen, aber nicht den Zusammenhang: den Zaun, der den Schatten wirft. Und sie würde keinen Zweifel melden.“
- **H10-3 „Context“:** Das Bild ist auf Englisch beschriftet, der Text sagt „Zusammenhang“. Für Leser ohne Englisch: „… aber nicht den Zusammenhang (im Bild: „Context“) …“.
- **H10-4 Rechtlich, keine Rechtsberatung:**
  - Die sichtbare Kennzeichnung direkt am Bild genügt dem, was der eigene AI-Act-Beitrag für realistisch wirkende KI-Bilder empfiehlt.
  - Wird das Bild ohne Unterschrift gezeigt (Social, Bildersuche), fehlt der Hinweis. Ein kleines „Mit KI erstellt“ in der Bildecke wäre robuster.
  - Die JPG-Datei enthält keine Herkunfts-Metadaten (nur JFIF). Die maschinenlesbare Markierung ist Pflicht des Anbieters, nicht von Till.
  - Der Bildaufbau (grüner Rahmen „Tiger“, Pfeil „Context“) gleicht dem LinkedIn-/Siali-Bild. Bitte bei Till klären: Hat er das Bild nur aus einem Text-Prompt erzeugt oder das Original als Vorlage hochgeladen? Im zweiten Fall wäre es eine Bearbeitung eines fremden Bildes, und die Rechtefrage stellt sich wieder.
- **H10-5 INTERN (b)** enthält noch den alten Satz „Ursprünglich als eigene Grafik nachgestellt … falls du einen Löwen meinst …“ – für Till verwirrend, kürzen.
- **H10-6** Bewusst offen wie in Runde 9: Länge, Titel, Bestätigung der Prompt-Sätze. Vor der Freigabe Ghost neu laden (neues Bild, g4, Vorschaubild), dann Punkt 13.

## Runde 11 – 25.10.2026 (Prüfer, gekürzte Fassung, Commit 3321372)

**Ergebnis: NICHT BESTANDEN** (fünf kleine Mängel, alle durch das Kürzen entstanden, jeder mit einem Satz lösbar)

Geprüft: gesamte neue Fassung von beitrag.md (Text, Kurzfassung, Box, Bildzeilen, Quellen) gegen die in Runde 5–10 gelesenen Originale und gegen
Tills Eingang, dazu `entscheidungen.md`, g4 und g5 gegen den neuen Text. `python3 tools/lexical.py` läuft ohne Fehler (rc 0).
Die Kurzfassung hat 5 Punkte. Format Langtext ok: Einleitung 2 Absätze, Kurzfassung, H2-Abschnitte, Box „Zum Ausprobieren“, Meine Einschätzung · Gedanke · Quellen.
Bilder: KI-Foto + g1, g4, g3, g5.

### Nachgerechnet
10 − 6 − 1 = 3 € · 3 × 100 = **300 €** (Box Schritt 2, ohne Schwund) · 3 × 100 × 0,95 = 285 € · (3/10) × 100 × 0,95 = 28,50 · 100.000 × 1,1² = 121.000 (linear 120.000) – alles richtig.

### Weiter korrekt (Stichproben am Original)
- OpenAI-Definition, Pretraining/Haustier-Geburtstag, 1 zu 365, „kein Naturgesetz“ (= „not inevitable … abstain“), „ersten Entwurf, nicht endgültige Quelle“ (Hilfeseite).
- Regel 2 „laut OpenAI kann die KI auch bei falschen Antworten sehr sicher klingen“ (Hilfeseite).
- OWASP: Fehlinformation in den Top 10, Overreliance verstärkt den Schaden, Folgen Reputation/Haftung.
- Studie: 300 Fälle, je ein erfundener Begriff, sechs Modelle, 66 → 44 %, Einschränkung „nicht für den Alltag“.
- Steckachse „unter anderem aus der Breite der Hinterradnabe“, Protokoll, OLG Hamm, Exposé/Speisekarte als ausgedacht.
- Die entfernten Quellen (Temporary Chat, Memory) werden im Text nicht mehr gebraucht – konsistent.

### Mängel

**K1 – Fall 2: Der Fehler der Formel ist verkürzt falsch beschrieben**
Text: „eine zentrale Formel teilte den Gewinn pro Stück durch den Verkaufspreis, machte daraus also einen Anteil statt eines Eurobetrags.“
Das Teilen allein ist nicht der Fehler. Tills Text sagt ausdrücklich: „grundsätzlich sinnvoll, wenn man diese Marge anschließend mit einem Umsatzbetrag in Euro multipliziert.“ Falsch war das Malnehmen mit der Stückzahl.
→ „Und eine zentrale Formel machte aus dem Gewinn pro Stück einen Anteil am Preis und nahm diesen dann mit der Stückzahl mal statt mit dem Umsatz. Heraus kam kein Eurobetrag.“

**K2 – Fall 3: „unter anderem“ fehlt**
Text: „Es fand die Excel-Kalkulation und die Steckachse.“ Till: „Darunter auch die Excel-Kalkulation und die Steckachse.“
→ „Es fand unter anderem die Excel-Kalkulation und die Steckachse.“

**K3 – Regel 2: Anthropic-Aussage wieder ohne Claude-Bezug** (Rückfall von F4, Runde 5)
Text: „Laut Anthropic kann das falsche Angaben deutlich verringern.“ Die Doku sagt das für Claude („Explicitly give Claude permission …“).
→ „Laut Anthropics Dokumentation zu Claude kann das falsche Angaben deutlich verringern.“

**K4 – Kurzfassung Punkt 2 hat keine Entsprechung mehr im Text**
„Datumsangaben, Zitate und Quellen“ standen im gestrichenen Hilfeseiten-Absatz. Im Text steht jetzt nur noch „seltene Einzelfakten“.
→ Im Absatz „Halluzinationen sind laut OpenAI trotzdem kein Naturgesetz …“ vor dem letzten Satz einfügen: „Als typische Fehler nennt OpenAI falsche Datumsangaben sowie erfundene Zitate und Quellen.“ (Hilfeseite, bereits verlinkt.)

**K5 – Prompt-Kasten „Mein Zusatz“: zwei redaktionelle Sätze ohne Kennzeichnung**
„Wenn du etwas nicht sicher weißt, sag das, statt zu raten. Erfinde keine Zahlen, Quellen oder technischen Daten.“ hat die Redaktion ergänzt (Runde 8, INTERN f: „bitte bestätigen“). Der neue INTERN-Absatz erwähnt das nicht mehr und sagt sogar „Deine Ich-Fälle … nichts hinzugefügt“. Eine Bestätigung steht nicht in `entscheidungen.md`. Verstoß gegen harte Regel 2 (Ich-Form).
→ In den INTERN-Absatz aufnehmen: „Im Kasten ‚Mein Zusatz‘ sind die ersten zwei Sätze von der Redaktion ergänzt (deine Idee ‚Erfinde keine Fakten‘) – bitte bestätigen.“ Oder Tills Bestätigung in `entscheidungen.md` nachtragen, falls sie im Chat schon kam.

### Hinweise (kein Mangel)

- **OWASP-Absatz:** „zu den zehn wichtigsten Risiken für solche Anwendungen“ hat kein Bezugswort → „für Anwendungen mit Sprachmodellen“. Der letzte Satz steht wieder direkt nach dem übermäßigen Vertrauen → „Als mögliche Folgen von Fehlinformation nennt OWASP …“ (war in Runde 7 schon so).
- **„Genau dort setzt du mit deinem Prompt an (Regel 2).“** OpenAI meint Training und Bewertung, nicht den Prompt → „Ähnlich kannst du mit deinem Prompt nachhelfen (Regel 2).“
- **Fall 1:** Ohne „und an der der Anhänger befestigt wird“ versteht ein Laie nicht, warum der Anhänger eine Achse braucht → Halbsatz wieder ergänzen.
- **Fall 2:** „Sie verwechselte Zellen“ – die Tabelle verwechselt nichts, ChatGPT tat es beim Bauen → „ChatGPT verwechselte dabei Zellen für Prozent und Euro.“ Für die 285 € braucht man die 5 % Schwund, die nur im Schaubild stehen → „(Zahlen im Schaubild)“ anhängen.
- **Box Schritt 2 (300 €) und g4 (285 €)** mit fast denselben Zahlen können irritieren → „Hier bleiben 3 € pro Stück, also 300 € (ohne Schwund), bevor weitere Kosten abgehen.“
- **Regel 2 Studie:** „zeigt die Größenordnung“ widerspricht leicht dem Satz „nicht für den Alltag“ → „zeigt, wie viel so eine Anweisung bringen kann“.
- **Regel 3:** „deckt oft den Fehler auf“ – „oft“ ist nicht belegt → „kann den Fehler aufdecken“.
- **g5 und Text:** In g5 heißt Regel 3 „Zahlen nicht der KI glauben“, im Text „Zahlen von Hand nachrechnen“ → eins angleichen (am einfachsten den Text). Sonst passt g5 zu den fünf Regeln. g4 passt zum Text und ist jetzt der einzige Ort mit der Herleitung – richtig so.
- **Bild:** Laut INTERN und `entscheidungen.md` ist das Foto mit dem Originalbild aus dem Netz als Vorlage erzeugt. Till hat es nach dem Hinweis auf das Urheberrechts-Risiko bewusst freigegeben („Nimm das Foto“). Die Kennzeichnung „Mit KI nachgestelltes Beispielbild nach einem Motiv, das im Netz kursiert“ ist ehrlich. Das Rechtsrisiko bleibt Tills Entscheidung; g6 liegt als Ersatz bereit.
