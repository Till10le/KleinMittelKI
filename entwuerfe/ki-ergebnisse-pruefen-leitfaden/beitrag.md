---
titel: "KI irrt sich und klingt trotzdem sicher: So prüfst du KI-Ergebnisse im Betrieb"
slug: ki-ergebnisse-pruefen-leitfaden
kategorie: Leitfäden
tags: [#wissen]
teaser: Drei echte Fälle zeigen, wie KI danebenliegt. Drei Stufen und fünf Regeln helfen, Fehler abzufangen, bevor sie Geld kosten.
vorschaubild: vorschaubild.png
titelbild: titel-ki-ergebnisse-pruefen-leitfaden.jpg
---

INTERN – vor Veröffentlichung entfernen: Gekürzt am 25.10.2026 nach deinem Wunsch („Excel viel zu tief erklärt“, „generell viel zu lange“): von rund 2.700 auf rund 1.500 Wörter. Excel-Fall auf einen Absatz plus Grafik, Formel-Kasten und Schwund-Herleitung entfallen. Gestrichen: Beispiel mit dem Doktorarbeit-Titel, Tipp „mehrmals fragen / temporärer Chat“, zweite OpenAI-Folgerung, Exposé-Absatz gekürzt. „Zum Ausprobieren“ von sechs auf drei Schritte, ohne Schwund. Deine Ich-Fälle und „Meine Einschätzung“ sind gekürzt, nichts hinzugefügt. Ausnahme: Im Prompt-Kasten („Mein Zusatz“) stehen zwei Sätze der Redaktion („Wenn du etwas nicht sicher weißt …“, „Erfinde keine Zahlen …“); du hast die Entscheidung am 25.10. der Redaktion überlassen („das musst du mir sagen“). Bild: dein KI-Foto (auf deinen Wunsch, Vorlage war das Originalbild aus dem Netz), gekennzeichnet als „mit KI nachgestellt“. Offen von dir: (1) Steckachse – der Text sagt nur, dass Angaben fehlten, nicht dass die Achse nicht gepasst hat. (2) Der LinkedIn-Beitrag von Alex Lichtenberger ist als Anstoß genannt, nicht verlinkt.

Die Excel-Datei, die ChatGPT mir für ein Geschäftsmodell gebaut hatte, sah professionell aus: saubere Tabellen, Eingabefelder, automatisch berechnete Kennzahlen. Nur: Einige Berechnungen stimmten nicht. Ohne meine eigene Kontrolle hätte ich die Fehler möglicherweise übersehen.

Genau das ist das Tückische: KI kann falschliegen und dabei genauso sicher klingen wie bei richtigen Antworten. Das heißt nicht, dass man KI misstrauen muss. Man sollte aber wissen, wo sie danebenliegen kann, und dort gezielt hinschauen. Den Anstoß zu diesem Beitrag gab ein LinkedIn-Beitrag von Alex Lichtenberger. **Wie setzt ein Betrieb KI sinnvoll ein, wenn er sich nicht auf jede Antwort verlassen kann?**

```html
<div class="kmk-kurz" style="border:2px solid #111;border-left:10px solid #D7FF00;padding:18px 22px;margin:28px 0;background:#fff;color:#111"><p style="margin:0 0 12px;font-weight:700;font-size:13px;letter-spacing:3px;text-transform:uppercase;line-height:1.3">Das Wichtigste in 30 Sekunden</p><ul style="margin:0;padding-left:20px;display:grid;gap:8px;line-height:1.5"><li style="margin:0">KI liegt manchmal falsch und kann dabei genauso sicher klingen wie bei richtigen Antworten.</li><li style="margin:0">Typische Fehlerstellen nennt OpenAI selbst: seltene Fakten, Datumsangaben, Zitate und Quellen. Dazu kommen Fragen, bei denen wichtige Angaben fehlen.</li><li style="margin:0">Nicht jede Antwort braucht dieselbe Kontrolle. Drei Stufen helfen: frei nutzen, gezielt prüfen, nur mit Freigabe.</li><li style="margin:0">Ein Zusatz im Prompt hilft: der KI erlauben, „weiß ich nicht“ zu sagen. In einer Studie senkte eine solche Anweisung die Fehler deutlich, aber nicht auf null.</li><li style="margin:0">Bei Kalkulationen hilft ein einfacher Test: ein Ergebnis mit leicht nachvollziehbaren Zahlen von Hand nachrechnen.</li></ul></div>
```

## Warum KI so überzeugend danebenliegen kann

Ein Bild macht das Prinzip greifbar: Ein Hund liegt im Schatten eines Zauns, die Schattenstreifen lassen sein Fell gestreift aussehen. Eine Bilderkennung, die nur auf das Muster schaut, könnte daraus einen Tiger machen.

![Mit KI nachgestelltes Foto: Ein Hund liegt hinter einem Zaun, dessen Schatten Streifen auf sein Fell wirft. Ein grüner Rahmen mit der Beschriftung „Tiger“ zeigt, was eine Bilderkennung daraus machen könnte; ein Pfeil mit „Context“ zeigt auf den Zaun. Darunter ein Ausschnitt des gestreiften Hundes.](ki-beispielbild-hund-tiger.jpg "Mit KI nachgestelltes Beispielbild nach einem Motiv, das im Netz kursiert: Die Streifen sind nur der Schatten des Zauns – wer das übersieht, sieht einen Tiger.")

Die KI würde das Muster erkennen, aber nicht den Zusammenhang: den Zaun, der den Schatten wirft. Das Motiv kursiert im Netz, unsere Fassung ist mit KI nachgestellt und kein Messergebnis. Streng genommen zeigt es eine falsche Bilderkennung. Das Prinzip ist aber dasselbe wie bei ChatGPT: Die Antwort folgt einem Muster, nicht geprüftem Wissen.

Bei Sprachmodellen wie ChatGPT heißt das **Halluzination**: plausible, aber falsche Aussagen, so die Definition von OpenAI in einem Forschungsbeitrag vom September 2025. Sprachmodelle lernen an riesigen Textmengen, wie ein Text weitergeht. Rechtschreibung folgt festen Mustern, seltene Einzelfakten wie der Geburtstag eines Haustiers nicht. Bei solchen Fakten entstehen Halluzinationen.

Dazu kommt: Die Tests, mit denen Sprachmodelle trainiert und verglichen werden, zählen meist nur richtige Antworten. Wer einen Geburtstag rät, liegt immerhin mit einer Chance von 1 zu 365 richtig. Wer „weiß ich nicht“ schreibt, bekommt sicher null Punkte. Also rät das Modell.

![Schaubild: Warum Sprachmodelle lieber raten – „Ich weiß es nicht“ bringt sicher 0 Punkte, Raten beim Geburtstag immerhin eine Chance von 1 zu 365; Merksatz: Raten wird belohnt, Zugeben nicht](kmk-ki-pruefen-g1.png "Wer raten darf, rät – das gilt auch für Sprachmodelle.")

Als typische Fehler nennt OpenAI falsche Datumsangaben sowie erfundene Zitate und Quellen. Halluzinationen sind laut OpenAI trotzdem kein Naturgesetz: Ein Modell kann bei Unsicherheit auch sagen, dass es etwas nicht weiß. Ähnlich kannst du mit deinem Prompt nachhelfen (Regel 2). OpenAI selbst empfiehlt, ChatGPT als ersten Entwurf zu nutzen, nicht als endgültige Quelle.

## Drei eigene Fälle: sicher im Ton, falsch in der Sache

Nicht jeder dieser Fehler ist eine Halluzination im engen Sinn, manche sind Rechen- oder Logikfehler. Für dich zählt dasselbe: **Eine KI-Antwort ist ein Vorschlag, kein Ergebnis.**

**Fall 1: die Steckachse.** Für einen Fahrradanhänger brauchte ich eine passende Steckachse, also die Achse, die das Hinterrad im Rahmen hält und an der der Anhänger befestigt wird. ChatGPT empfahl ein Modell und war sich irgendwann „100 %“ sicher. Dabei hatte es unter anderem aus der Breite der Hinterradnabe auf die Achse geschlossen. Länge und Gewinde waren nicht geprüft. Erst später räumte ChatGPT ein, dass man dafür die Originalachse prüfen müsste. Für einen Handwerksbetrieb heißt das: Eine plausible Empfehlung für ein Ersatzteil ersetzt keine geprüften technischen Daten.

**Fall 2: die Excel-Kalkulation.** Die Tabelle rechnete mit Preisen, Material, Schwund und Umsatz, also genau das, was auch eine Bäckerei oder ein Gastronom kalkuliert. ChatGPT verwechselte Zellen für Prozent und Euro. Und eine zentrale Formel machte aus dem Gewinn pro Stück einen Anteil am Preis und nahm diesen dann mit der Stückzahl mal statt mit dem Umsatz. Heraus kam kein Eurobetrag: Mit einfachen Beispielzahlen käme statt 285 Euro nur 28,50 heraus (Zahlen im Schaubild). Auch das Wachstum stimmte nicht: Zehn Prozent pro Jahr auf 100.000 Euro ergeben im dritten Jahr 121.000 Euro, nicht 120.000.

![Schaubild: Vergleich mit Beispielzahlen (Verkaufspreis 10 €, Einkaufspreis 6 €, Material 1 €, 100 Stück eingeplant, 5 % Schwund) – die Formel aus der KI-Tabelle =((B8-B9-B11)/B8)*C34*(1-B10/100) ergibt 28,50, in Euro gerechnet sind es 3 € × 100 × 0,95 = 285 €](kmk-ki-pruefen-g4.png "Wer mit einfachen Zahlen nachrechnet, sieht sofort, dass die Formel keine Euro liefert.")

**Fall 3: die Selbstprüfung.** Danach bat ich ChatGPT, unsere bisherigen Chats nach eigenen Fehlern zu durchsuchen. Es fand unter anderem die Excel-Kalkulation und die Steckachse. Ob diese Prüfung vollständig war, konnte es aber nicht garantieren. KI kann Unstimmigkeiten aufdecken. Eine Selbstprüfung ist aber kein unabhängiger Beweis, dass alles stimmt.

## Das eigentliche Risiko: Niemand schaut mehr hin

Das OWASP Gen AI Security Project, eine weltweite, offene Initiative von Fachleuten für IT-Sicherheit, zählt Fehlinformation durch Sprachmodelle zu den zehn wichtigsten Risiken für Anwendungen mit Sprachmodellen (Stand 2025). Verstärkt wird der Schaden durch übermäßiges Vertrauen: Menschen prüfen die Ausgaben nicht und übernehmen sie in Entscheidungen. Als mögliche Folgen von Fehlinformation nennt OWASP Reputationsschäden und rechtliche Haftung.

Je professioneller ein Ergebnis aussieht, desto fertiger wirkt es. Auch im [Protokoll-Selbstversuch](https://www.kleinmittelki.de/protokoll-per-ki-selbstversuch/) hier im Blog waren im fertig wirkenden Entwurf einige Namen falsch geschrieben. Und was ein Chatbot auf der Website deines Betriebs sagt, sagst am Ende du: So hat das [OLG Hamm](https://www.kleinmittelki.de/olg-hamm-chatbot-haftung/) die Falschangaben eines Website-Chatbots dem Betreiber zugerechnet.

Zwei ausgedachte Beispiele zeigen weitere Fehlerarten. Im Exposé wird aus „Dach vermutlich um 2010 erneuert“ plötzlich „Dach 2010 komplett saniert“. Und beim Kürzen einer Speisekarte fällt der Hinweis auf Nüsse weg, oder ein Gericht heißt plötzlich „glutenfrei“. Da geht es nicht mehr um Stil, sondern um die Gesundheit von Gästen.

## Nicht jede Antwort braucht dieselbe Kontrolle

Alles zu prüfen, ist nicht realistisch. Entscheidend ist eine Frage: **Was passiert, wenn dieser Fehler unbemerkt durchrutscht?**

**Stufe 1: Frei nutzen.** Ideen, Überschriften, erste Entwürfe. Ein Fehler fällt sofort auf oder schadet nicht.

**Stufe 2: Gezielt prüfen.** Angebote, Exposés, Kundenantworten, Auswertungen. Geprüft werden Zahlen, Namen, Daten, Zusagen und alles, was nach Tatsache klingt.

**Stufe 3: Nur mit Freigabe.** Buchungen, Preise, Zahlungen, Allergen- und Sicherheitsangaben. Die KI darf vorbereiten, ausgeführt wird erst nach Freigabe durch eine benannte Person.

![Stufenmodell mit drei Stufen: frei nutzen (Ideen, Entwürfe), gezielt prüfen (Angebote, Exposés, Kundenantworten, Auswertungen), nur mit Freigabe (Buchungen, Preise, Zahlungen, Allergenangaben); Leitfrage: Was passiert, wenn dieser Fehler unbemerkt durchrutscht?](kmk-ki-pruefen-g3.png "Nicht das Werkzeug entscheidet über die Kontrolle, sondern die Folgen eines Fehlers.")

Die Speisekarte ist Stufe 1, solange es um den Ton geht, und Stufe 3, sobald Allergene darin stehen. Für den Einstieg reicht eine kurze Teamrunde: Sammelt, wofür bei euch KI genutzt wird, auch im privaten Konto ohne Wissen des Betriebs (siehe [Schatten-KI](https://www.kleinmittelki.de/schatten-ki-deine-mitarbeiter-nutzen-ki-vielleicht-langst-weisst-du-wofur/)), und ordnet jeden Punkt einer Stufe zu.

## Fünf Regeln, die viele Fehler abfangen

Für Stufe 2 und 3 helfen fünf Regeln. Regel 1 und 2 stützen sich auf Empfehlungen von OWASP und von Anthropic, dem Hersteller des KI-Assistenten Claude, sowie auf eine Studie. Regel 3 bis 5 kommen aus den drei Fällen.

![Checkliste mit fünf Regeln: mit eigenen Unterlagen abgleichen, Fakten und Annahmen trennen lassen, Zahlen nicht der KI glauben und von Hand nachrechnen, KI prüft mit und ein Mensch entscheidet, testen, was bei fehlenden Angaben passiert](kmk-ki-pruefen-g5.png "Zum Abhaken: Je mehr davon in deinem Ablauf steckt, desto weniger rutscht durch.")

**1. Mit eigenen Unterlagen abgleichen.** Preise gehören in die Preisliste, Allergene in die Rezeptur, technische Maße ins Datenblatt. Gib der KI diese Unterlagen mit und gleiche das Ergebnis damit ab. Das entspricht der Empfehlung von OWASP.

**2. Fakten und Annahmen trennen lassen.** Ein Satz wie „Erfinde keine Fakten“ ist ein guter Anfang. Allein reicht er nicht, denn laut OpenAI kann die KI auch bei falschen Antworten sehr sicher klingen. Erlaube ihr deshalb ausdrücklich, „weiß ich nicht“ zu sagen. Laut Anthropics Dokumentation zu Claude kann das falsche Angaben deutlich verringern. Wie viel so eine Anweisung bringen kann, zeigt eine Studie (Communications Medicine, 2025): In 300 Fallbeschreibungen mit je einem absichtlich erfundenen Begriff gingen sechs KI-Modelle ohne Zusatz im Schnitt in 66 Prozent der Fälle darauf ein, mit der Anweisung, nur Gesichertes zu verwenden und Unsicherheit zuzugeben, in 44 Prozent. Die Werte gelten für diesen absichtlich schweren Test, nicht für den Alltag. Fehler werden also seltener, aber nicht null. Mein Zusatz, wenn ich nach technischen Produkten frage:

```html
<div class="kmk-prompt"><p class="kmk-prompt__label">Mein Zusatz für technische Fragen</p><p class="kmk-prompt__text">„Wenn du etwas nicht sicher weißt, sag das, statt zu raten. Erfinde keine Zahlen, Quellen oder technischen Daten. Nenne mir ausdrücklich alle Angaben, die für eine zuverlässige Empfehlung noch fehlen. Trenne bestätigte Fakten von Annahmen und behaupte keine Sicherheit, wenn wichtige Informationen nicht geprüft wurden.“</p></div>
```

**3. Zahlen nicht der KI glauben.** Prüf bei Kalkulationen nicht nur das Ergebnis, sondern die Logik: Werden Prozent und Euro unterschieden? Bezieht sich eine Steigerung auf die richtige Basis? Ein einziger Wert, den du selbst von Hand nachrechnest, kann den Fehler schon aufdecken.

**4. Die KI darf mitprüfen, aber nicht allein entscheiden.** Wichtige Ergebnisse brauchen eine unabhängige Kontrolle: eine eigene Rechnung, das Originaldokument oder jemanden mit Fachwissen. In einem Betrieb mit 30 Leuten kann das die Bürokraft für Angebote sein und die Küchenchefin für die Speisekarte.

**5. Testen, was bei fehlenden Angaben passiert.** Lass bewusst eine Information weg. Meldet die KI die Lücke oder füllt sie sie mit etwas Plausiblem, wie bei der Steckachse?

Das betrifft nur Stufe 2 und 3. Für Ideen, Entwürfe und Formulierungen kannst du KI weiter frei nutzen.

```html
<div class="kmk-kurz" style="border:2px solid #111;border-left:10px solid #D7FF00;padding:18px 22px;margin:28px 0;background:#fff;color:#111"><p style="margin:0 0 12px;font-weight:700;font-size:13px;letter-spacing:3px;text-transform:uppercase;line-height:1.3">Zum Ausprobieren: eine KI-Tabelle in fünf Minuten prüfen</p><ol style="margin:0;padding:0;list-style:none;display:grid;gap:10px;line-height:1.5"><li style="margin:0;display:grid;grid-template-columns:30px 1fr;gap:10px;align-items:start"><span style="background:#D7FF00;font-weight:700;text-align:center;line-height:30px;height:30px">1</span><span>Nimm eine Kopie einer Tabelle, die eine KI für dich gebaut hat, und trag einfache Zahlen ein, etwa 10 € Verkaufspreis, 6 € Einkauf, 1 € Material, 100 Stück.</span></li><li style="margin:0;display:grid;grid-template-columns:30px 1fr;gap:10px;align-items:start"><span style="background:#D7FF00;font-weight:700;text-align:center;line-height:30px;height:30px">2</span><span>Rechne ein Ergebnis von Hand nach. Hier bleiben 3 € pro Stück, also 300 € (ohne Schwund), bevor weitere Kosten abgehen. Weicht die Tabelle ab, frag nach: <em>„Warum rechnest du hier so?“</em></span></li><li style="margin:0;display:grid;grid-template-columns:30px 1fr;gap:10px;align-items:start"><span style="background:#D7FF00;font-weight:700;text-align:center;line-height:30px;height:30px">3</span><span>Prüf Steigerungen: 100.000 € Umsatz und 10 % pro Jahr ergeben im dritten Jahr 121.000 €, nicht 120.000 €.</span></li></ol></div>
```

## Meine Einschätzung

Trotz dieser Beispiele würde ich nicht auf die Idee kommen, weniger KI einzusetzen. Gerade kleine Betriebe können damit Angebote vorbereiten, Dokumente strukturieren oder erste Kalkulationen entwickeln, wofür früher deutlich mehr Zeit oder Hilfe von außen nötig war.

KI muss nicht perfekt sein, um sehr nützlich zu sein. Ich nutze ChatGPT weiterhin fast täglich. Aber ich habe gelernt, eine überzeugend formulierte Antwort nicht mit einer richtigen gleichzusetzen. KI kann uns viel Arbeit abnehmen. Die Verantwortung für das Ergebnis nimmt sie uns nicht ab.

## Ein Gedanke zum Mitnehmen

Nimm die letzte Kalkulation oder das letzte Angebot, an dem bei euch eine KI mitgearbeitet hat. Ist klar geregelt, wer das Ergebnis überprüft?

## Quellen

Abgerufen am 23.10.2026, zuletzt geprüft am 25.10.2026

- [OpenAI: Why language models hallucinate (05.09.2025)](https://openai.com/index/why-language-models-hallucinate/)
- [OpenAI Help Center: Does ChatGPT tell the truth? (abgerufen 23.10.2026)](https://help.openai.com/en/articles/8313428-does-chatgpt-tell-the-truth)
- [OWASP Gen AI Security Project: LLM09:2025 Misinformation (OWASP Top 10 for LLM Applications 2025, Stand 17.04.2025)](https://genai.owasp.org/llmrisk/llm092025-misinformation/)
- [Anthropic, Claude-Dokumentation: Reduce hallucinations (abgerufen 23.10.2026)](https://platform.claude.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- [Omar, Klang u. a.: Multi-model assurance analysis showing large language models are highly vulnerable to adversarial hallucination attacks during clinical decision support. Communications Medicine 5, 330 (02.08.2025)](https://doi.org/10.1038/s43856-025-01021-3)
