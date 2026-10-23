# Eingang 2026-10-23 · Tills eigene Erfahrungen (im Chat geschickt, Text mit ChatGPT formuliert)

Till: „Hier noch die eigenen Beispiele von mir.“ Die drei Fälle (Steckachse, Excel-Kalkulation, Selbst-Audit) sind Tills eigene Erfahrungen
und dürfen in Ich-Form verwendet werden – nur so, wie sie hier stehen. Nichts ergänzen.
verarbeitet: 2026-10-23 (Board: ki-ergebnisse-pruefen-leitfaden)

---

Ich habe die drei Fälle mit den wiederauffindbaren Stellen aus unseren früheren Gesprächen abgeglichen. Besonders spannend ist der Excel-Fall vom 25. April 2025: Dort lässt sich anhand der ursprünglichen Formel nachvollziehen, warum eine scheinbar plausible Kalkulation ein falsches Ergebnis lieferte.

Zwei Details habe ich bewusst sauber abgegrenzt: Bei der Steckachse ist die unbegründete „100 %“-Zusage dokumentiert, nicht aber die genaue nachgemessene Abweichung. Und beim Halluzinationsaudit war nicht sichergestellt, dass sämtliche alten Chats vollständig zugänglich waren. Diese Grenzen machen den Beitrag glaubwürdiger, nicht schwächer.

Für KMK würde ich ihn unter Eigene Notizen / Selbst ausprobiert veröffentlichen.

ChatGPT lag falsch. Und war sich trotzdem sicher.

Drei persönliche Erfahrungen mit KI-Fehlern – und was kleine und mittelständische Unternehmen daraus lernen können.

Ich nutze ChatGPT mittlerweile für ziemlich viele Dinge. Beruflich, für eigene Projekte und ganz alltägliche Fragen. Und meistens bin ich begeistert, wie viel Arbeit mir KI abnehmen kann.

Aber manchmal liegt sie daneben.

Das Problem dabei ist nicht unbedingt der Fehler selbst. Sondern wie überzeugend er präsentiert wird.

Ich habe in den vergangenen Monaten mehrfach erlebt, dass ChatGPT etwas mit großer Sicherheit behauptet hat, obwohl wichtige Informationen fehlten oder eine Berechnung schlicht nicht stimmte.

Drei Beispiele sind mir besonders in Erinnerung geblieben. Sie zeigen ziemlich gut, warum Unternehmen KI nutzen sollten – aber nicht jedes Ergebnis ungeprüft übernehmen dürfen.

1. Eine Steckachse. Und angeblich 100 % Sicherheit.

Alles begann mit einer eigentlich simplen Frage.

Ich wollte einen Fahrradanhänger an meinem Mountainbike befestigen und brauchte dafür eine passende Steckachse.

Also fragte ich ChatGPT, welches Modell ich kaufen sollte.

Die KI lieferte eine konkrete Empfehlung. Mit Gewindesteigung, Achslänge und passendem Zubehör. Irgendwann war sie sich sogar „100 %“ sicher, dass die empfohlene Achse passen würde.

Klingt praktisch, oder?

Das Problem: Für diese Sicherheit fehlten entscheidende Informationen.

ChatGPT hatte unter anderem aus der bekannten Hinterrad-Einbaubreite von 148 Millimetern auf eine passende Achskonfiguration geschlossen. Aber die Einbaubreite einer Fahrradnabe ist nicht dasselbe wie die benötigte Steckachsenlänge.

Auch die tatsächliche Gewindesteigung war nicht überprüft.

Auf meine Nachfragen wurde die Empfehlung zunächst trotzdem mit großer Sicherheit vertreten. Erst später räumte ChatGPT ein, dass für eine verlässliche Aussage die Originalachse genauer geprüft werden müsste.

Meine Erkenntnis: ChatGPT hatte nicht zwingend alle notwendigen Informationen. Aber es hatte trotzdem eine eindeutige Antwort.

Das ist ein wichtiger Unterschied.

Für einen Handwerksbetrieb kann genau das relevant werden. Zum Beispiel, wenn KI ein Ersatzteil, ein bestimmtes Material oder eine technische Komponente empfiehlt.

Eine plausibel klingende Produktempfehlung ersetzt keine geprüften technischen Spezifikationen.

Und erst recht keine notwendige Herstellerfreigabe.

2. Eine professionelle Excel-Kalkulation. Mit falscher Berechnung.

Dieses Beispiel finde ich für kleine und mittelständische Unternehmen besonders interessant.

Ich hatte ChatGPT gebeten, eine betriebswirtschaftliche Excel-Kalkulation für ein Geschäftsmodell zu erstellen.

Es ging um Verkaufspreise, Einkaufspreise, Verbrauchsmaterial, Schwund, Umsatzentwicklung und Rentabilität.

Also genau die Dinge, die beispielsweise auch ein Bäcker, Einzelhändler oder Gastronom regelmäßig kalkulieren muss.

Das Ergebnis sah zunächst überzeugend aus.

Sauber aufgebaute Tabellen, verschiedene Eingabefelder und automatisch berechnete Kennzahlen.

Nur: Einige Berechnungen stimmten nicht.

Der erste Fehler: Zwei Zellen, zwei völlig unterschiedliche Bedeutungen

In der Kalkulation gab es sowohl einen prozentualen Schwund als auch Kosten für Verbrauchsmaterial.

ChatGPT verwechselte wiederholt die entsprechenden Zellzuordnungen.

Das klingt banal. Ist es aber nicht.

Denn Schwund von beispielsweise fünf Prozent muss anders behandelt werden als Verbrauchsmaterial von zehn Cent pro verkaufter Einheit.

Wer solche Werte in einer Formel vertauscht, verändert die gesamte Kalkulationslogik.

Der zweite Fehler: Eine Formel, die auf den ersten Blick richtig aussah

Besonders deutlich wurde das Problem bei einer Berechnung des jährlichen Bruttogewinns.

In einer Version der Excel-Datei stand folgende Formel:

=((B8-B9-B11)/B8)*C34*(1-B10/100)

Dahinter steckten:

* B8: Verkaufspreis pro Einheit
* B9: Einkaufspreis pro Einheit
* B10: Schwund in Prozent
* B11: Verbrauchsmaterial pro Einheit
* C34: Anzahl der Verkäufe pro Jahr

Fällt dir der Fehler auf?

Durch die Division durch den Verkaufspreis wird aus dem Gewinn pro Einheit zunächst eine relative Marge.

Das ist grundsätzlich sinnvoll, wenn man diese Marge anschließend mit einem Umsatzbetrag in Euro multipliziert.

Hier wurde sie aber mit der Anzahl verkaufter Einheiten multipliziert.

Eine Prozentmarge mal Stückzahl ergibt eben keinen Bruttogewinn in Euro.

Ich bemerkte das und fragte ChatGPT ausdrücklich, warum in der Formel noch einmal durch den Verkaufspreis geteilt wurde.

So sieht der Unterschied aus

Nehmen wir zur Veranschaulichung bewusst einfache Beispielzahlen, nicht die vertraulichen Originaldaten:

Kennzahl	Beispielwert
Verkaufspreis	10,00 €
Einkaufspreis	6,00 €
Verbrauchsmaterial	1,00 €
Verkäufe pro Jahr	100
Schwund	5 %

Der Deckungsbeitrag pro Einheit beträgt zunächst 3 Euro.

Unter der vereinfachten Annahme, dass sich der Schwund als fünfprozentige Reduktion der relevanten Absatzmenge auswirkt, ergibt sich:

3 € × 100 × 0,95 = 285 €

Mit der fehlerhaften Formellogik käme dagegen lediglich der Zahlenwert 28,50 heraus – weil der Deckungsbeitrag vorher durch den Verkaufspreis geteilt wurde.

Diese vereinfachte Rechnung ersetzt keine vollständige Schwund- und Bestandskalkulation. Sie zeigt aber sehr anschaulich den Unterschied zwischen einer Marge in Prozent und einem Gewinnbetrag in Euro.

Und dann war da noch die Umsatzsteigerung

Auch die geplante Umsatzsteigerung wurde zunächst nicht so modelliert, wie ich es vorgegeben hatte.

Mein Wunsch war, dass sich die jährliche Steigerung jeweils auf das Vorjahr bezieht.

Ein einfaches Beispiel:

Bei 100.000 Euro Umsatz und zehn Prozent jährlichem Wachstum ergeben sich:

* Jahr 1: 100.000 €
* Jahr 2: 110.000 €
* Jahr 3: 121.000 €

Nicht 120.000 Euro im dritten Jahr. Denn die Steigerung ist kumulativ.

Das musste ich in der Kalkulation ausdrücklich korrigieren lassen.

Was mich daran besonders beschäftigt hat:

Die Excel-Datei sah professionell aus. Die Formeln waren vorhanden. Alles wirkte durchdacht.

Ohne meine eigene Kontrolle hätte ich die Fehler möglicherweise übersehen.

Und genau darin liegt das Risiko für Unternehmen.

Eine KI kann eine sehr überzeugende Kalkulation erstellen. Ob die betriebswirtschaftliche Logik dahinter stimmt, ist eine andere Frage.

3. Kann ChatGPT wenigstens seine eigenen Fehler zuverlässig erkennen?

Nach solchen Erfahrungen kam mir eine Idee.

Warum nicht einfach ChatGPT selbst fragen, wo es in unseren bisherigen Gesprächen falschgelegen hat?

Also stellte ich sinngemäß diese Frage:

Kannst du unsere bisherigen Chats analysieren und herausfinden, wo du falsche Informationen geliefert hast oder ich dich korrigieren musste?

Die Antwort war interessant.

ChatGPT identifizierte verschiedene Situationen, in denen ich frühere Aussagen korrigiert oder infrage gestellt hatte. Darunter auch die Excel-Kalkulation und die Steckachse.

Das war durchaus hilfreich.

Aber dann kam die eigentlich spannende Frage:

Woher weiß ich, ob dieses Audit selbst vollständig und korrekt ist?

Schließlich konnte ChatGPT nicht garantieren, dass ihm sämtliche ursprünglichen Gespräche und Anhänge vollständig zur Verfügung standen.

Außerdem musste ich auch bei diesem Rückblick unterscheiden, welche Aussagen sich tatsächlich anhand früherer Gesprächsstellen belegen ließen und welche lediglich eine Zusammenfassung oder Interpretation waren.

Mit anderen Worten:

Ich hatte eine KI darum gebeten, ihre eigenen Fehler zu kontrollieren.

Aber auch diese Kontrolle musste ich wieder hinterfragen.

Das bedeutet nicht, dass KI zur Selbstprüfung ungeeignet ist. Im Gegenteil: Sie kann Unstimmigkeiten aufdecken, Formeln hinterfragen und auf mögliche Probleme hinweisen.

Nur ist eine solche Selbstprüfung noch kein unabhängiger Beweis, dass alles richtig ist.

Warum macht KI solche Fehler überhaupt?

Solche Fehler werden häufig als Halluzinationen bezeichnet.

Damit sind Antworten gemeint, bei denen ein KI-Modell falsche Informationen erzeugt, die trotzdem glaubwürdig klingen.

Wichtig ist allerdings: Nicht jeder KI-Fehler ist automatisch eine Halluzination im engeren Sinne. Eine falsch zugeordnete Excel-Zelle kann beispielsweise auch ein Verarbeitungs- oder Logikfehler sein.

Für den Anwender macht das zunächst wenig Unterschied: Das Ergebnis ist falsch.

Sprachmodelle wie ChatGPT erzeugen Antworten auf Grundlage gelernter Muster und Zusammenhänge. Sie sind nicht automatisch mit einem unabhängigen Wahrheitsprüfer ausgestattet.

Dass sie eine Antwort sprachlich hervorragend formulieren können, bedeutet deshalb nicht, dass ihre Aussage auch sachlich korrekt ist.

OpenAI hat dieses Problem selbst untersucht. Eine Forschungsveröffentlichung vom September 2025⁠￼ beschreibt unter anderem, warum Sprachmodelle dazu neigen können, lieber eine plausible Antwort zu liefern, statt Unsicherheit einzugestehen.

Die gute Nachricht: Die Modelle werden besser, und zusätzliche Werkzeuge können helfen, Fehler zu reduzieren.

Vollständig verschwunden ist das Problem aber nicht.

Was bedeutet das konkret für kleine und mittelständische Unternehmen?

Aus meinen Erfahrungen würde ich fünf einfache Regeln ableiten.

1. Je größer die Auswirkung, desto wichtiger die Kontrolle

Einen Entwurf für einen Instagram-Beitrag kann man meistens problemlos von KI erstellen lassen und anschließend kurz durchlesen.

Bei einer Finanzkalkulation, einem verbindlichen Kundenangebot oder einer automatisierten Preisänderung sieht das anders aus.

Hier können kleine Fehler direkte wirtschaftliche Folgen haben.

2. KI sollte fehlende Informationen offen benennen

Wenn ich heute nach technischen Produkten frage, möchte ich nicht nur eine Empfehlung.

Ich möchte auch wissen, welche Angaben für eine sichere Aussage noch fehlen.

Ein hilfreicher Zusatz im Prompt:

„Nenne mir ausdrücklich alle Angaben, die für eine zuverlässige Empfehlung noch fehlen. Trenne bestätigte Fakten von Annahmen und behaupte keine Sicherheit, wenn wichtige Informationen nicht geprüft wurden.“

Das verbessert die Ausgangslage. Es garantiert aber noch keine richtige Antwort.

3. Bei Excel nicht nur Ergebnisse, sondern die Logik prüfen

Besonders bei Kalkulationen würde ich kontrollieren:

* Stimmen die Zellbezüge?
* Werden Prozentwerte und Eurobeträge richtig unterschieden?
* Sind Umsatz und Absatzmenge sauber getrennt?
* Werden Steigerungen auf die richtige Ausgangsbasis angewendet?
* Stimmen die Ergebnisse mit einer unabhängig gerechneten Stichprobe überein?

Mein einfachster Tipp: Eine zentrale Berechnung einmal mit wenigen, leicht nachvollziehbaren Zahlen durchrechnen.

Wenn das Ergebnis dabei nicht stimmt, gehört die gesamte Kalkulation noch einmal auf den Prüfstand.

4. Die KI darf mitprüfen – aber nicht allein über ihre eigene Arbeit entscheiden

Ich nutze ChatGPT durchaus, um Formeln, Texte und Auswertungen noch einmal kritisch prüfen zu lassen.

Aber bei wichtigen Ergebnissen sollte eine zusätzliche, möglichst unabhängige Kontrolle stattfinden.

Das kann eine separate Berechnung in Excel sein, eine Prüfung gegen Originaldokumente oder die Freigabe durch jemanden mit entsprechendem Fachwissen.

Eine zweite KI kann ebenfalls helfen, ersetzt aber keine unabhängige Faktenbasis.

5. KI dort einsetzen, wo sie stark ist

Trotz dieser Beispiele würde ich nicht auf die Idee kommen, weniger KI einzusetzen.

Denn der Nutzen ist enorm.

Gerade kleine und mittelständische Unternehmen können mit KI Tätigkeiten erledigen, für die früher deutlich mehr Zeit oder externe Unterstützung notwendig war.

Angebote vorbereiten, Dokumente strukturieren, Informationen zusammenfassen, Daten auswerten oder erste Kalkulationsmodelle entwickeln.

Entscheidend ist, wie man diese Ergebnisse in die eigenen Prozesse integriert.

Nicht jede Antwort braucht eine aufwendige Kontrolle. Aber bei Entscheidungen mit finanziellen, rechtlichen oder sicherheitsrelevanten Auswirkungen sollte klar geregelt sein, wer oder was das Ergebnis überprüft.

Meine wichtigste Erkenntnis

Was ich aus diesen drei Erfahrungen mitnehme:

KI muss nicht perfekt sein, um unglaublich nützlich zu sein.

Ich nutze ChatGPT auch weiterhin fast täglich. Und bei vielen Aufgaben spart es mir enorm viel Zeit.

Aber ich habe gelernt, eine überzeugend formulierte Antwort nicht automatisch mit einer richtigen Antwort gleichzusetzen.

Eine professionell aussehende Excel-Datei ist noch keine richtige Kalkulation. Eine konkrete Produktempfehlung noch keine geprüfte Kompatibilität. Und eine Selbstkontrolle durch KI noch keine unabhängige Qualitätsprüfung.

Vielleicht ist genau das eine der wichtigsten Fähigkeiten im Umgang mit KI:

Nicht nur zu wissen, wie man gute Antworten bekommt.

Sondern auch, wann man sie besser noch einmal überprüft.

Denn KI kann uns unglaublich viel Arbeit abnehmen.

Die Verantwortung für das Ergebnis nimmt sie uns nicht ab.

⸻

Zum Weiterlesen:

* OpenAI: Why language models hallucinate⁠￼ – Warum selbst leistungsfähige KI-Modelle falsche Aussagen erzeugen können.
* OWASP: LLM09 – Misinformation⁠￼ – Warum fehlerhafte KI-Ausgaben auch für Unternehmen ein Risiko darstellen.
* Alex Lichtenberger auf LinkedIn⁠￼ – Ein Denkanstoß, der mich dazu gebracht hat, meine eigenen KI-Erfahrungen genauer anzusehen.

Veröffentlichung in Ghost

KLEIN. MITTEL. KI.

Eigene Notizen

ARTIKELTITEL

ChatGPT lag falsch. Und war sich trotzdem sicher.

VORSCHAUTEXT / EXCERPT

Eine Steckachse, eine falsche Excel-Kalkulation und ein KI-Selbsttest. Drei persönliche Erfahrungen, die zeigen, warum Unternehmen KI-Ergebnisse prüfen sollten.

SEO-URL

/chatgpt-fehler-halluzinationen-praxisbeispiele/

SEO-TITEL

ChatGPT macht Fehler: 3 Praxisbeispiele für KMU

META-BESCHREIBUNG

ChatGPT lag falsch – und klang überzeugend. Drei echte Praxisbeispiele zeigen, wie Unternehmen KI-Fehler erkennen und teure Folgen vermeiden.

LESEZEIT

ca. 7 Minuten

Die fachliche Einordnung zu Halluzinationen und zum Risiko ungeprüfter KI-Ausgaben deckt sich mit den Veröffentlichungen von OpenAI und OWASP.

Meine Empfehlung: Diesen Text würde ich als redaktionelle Endfassung verwenden. Vor dem Livegang sollten wir lediglich noch einmal den ursprünglichen Steckachsen-Chat beziehungsweise eine tatsächliche Messung heranziehen, falls du ausdrücklich behaupten möchtest, dass die empfohlene Achse nachweislich nicht passte. Die hier formulierte Version bleibt bei den belegbaren Aussagen.

Besonders gelungen finde ich den Excel-Teil: Er zeigt nicht nur, dass KI Fehler macht, sondern erklärt mit einer nachvollziehbaren Rechnung, wie ein KMU solche Fehler selbst erkennen kann. Genau das ist für mich der Unterschied zwischen einem austauschbaren KI-Artikel und einem echten KMK-Praxisbeitrag.