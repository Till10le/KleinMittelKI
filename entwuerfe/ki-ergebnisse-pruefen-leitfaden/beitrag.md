---
titel: KI klingt sicher. Aber stimmt es auch? So prüfst du KI-Ergebnisse im Betrieb
slug: ki-ergebnisse-pruefen-leitfaden
kategorie: Leitfäden
tags: [#wissen]
teaser: Nicht jede KI-Antwort braucht dieselbe Kontrolle. Drei Stufen und fünf Regeln helfen, Fehler abzufangen, bevor sie beim Kunden landen.
vorschaubild: vorschaubild.png
---

INTERN – vor Veröffentlichung entfernen: Till hat das Thema im Chat freigegeben, aber noch keine eigenen Sätze geliefert. Vorschläge der Redaktion sind: der ganze Abschnitt „Meine Einschätzung“ (Satzanfänge „Ich halte die drei Stufen …“, „Mich überzeugt …“, „Im Protokoll-Selbstversuch …“ – Letzteres ist aus Tills veröffentlichtem Beitrag abgeleitet, bitte bestätigen) sowie der Gedanke zum Mitnehmen. Der Platzhalter [TILL: …] in „Meine Einschätzung“ wartet auf 2–3 Sätze eigene Erfahrung, wo KI überzeugend falschlag; hast du keine, Absatz streichen. Alle vier Branchenbeispiele sind ausgedacht und im Text als Beispiele gekennzeichnet, keine echten Fälle. Anlass: Der LinkedIn-Beitrag von Alex Lichtenberger ist nur genannt, nicht gelesen (LinkedIn gesperrt) und nicht verlinkt; bitte prüfen, ob die Beschreibung im zweiten Absatz zu seinem Beitrag passt, und ggf. Link ergänzen oder den Satz streichen. OLG-Hamm-Beitrag (olg-hamm-chatbot-haftung) verlinken, sobald er online ist: Stelle im Abschnitt „Das eigentliche Risiko …“, Satz „Was ein Chatbot auf der Website …“ – nicht auf die Vorschau-URL verlinken. Nicht verwendet: OpenAI-Benchmarkzahlen (Modellvergleich), OWASP-Beispielfälle (Originale nicht gelesen), BSI-Papier (PDF nicht lesbar). Grafiken: vier Schaubilder eingebunden (g1, g2, g3, g5); die optionale Beispiele-Tabelle wurde weggelassen.

Montagabend in einem Malerbetrieb mit zwölf Leuten. Der Inhaber hat seine Notizen vom Kundentermin in ChatGPT kopiert: drei Räume, Decken und Wände, eine Wand mit Wasserfleck. Zwei Minuten später steht ein sauber formuliertes Angebot da. Es sieht besser aus als alles, was er abends noch selbst getippt hätte. Erst beim zweiten Lesen fällt ihm auf: Da steht eine Position „Isoliergrund, zwei Eimer“ mit Stückpreis. Den Preis hat er nie genannt. Er stammt auch nicht aus seiner Preisliste. Die KI hat ihn einfach ergänzt, weil er plausibel klingt. (Ein ausgedachtes, aber typisches Beispiel.)

Genau das ist das Tückische: KI liegt nicht nur manchmal falsch. Sie liegt falsch und klingt dabei genauso sicher wie bei richtigen Antworten. Den Anstoß zu diesem Beitrag gab ein LinkedIn-Beitrag von Alex Lichtenberger zur Frage, warum KI überzeugend danebenliegen kann. Hier geht es um die Frage danach: **Wie setzt ein Betrieb KI sinnvoll ein, wenn er sich nicht auf jede Antwort verlassen kann?**

```html
<div class="kmk-kurz" style="border:2px solid #111;border-left:10px solid #D7FF00;padding:18px 22px;margin:28px 0;background:#fff;color:#111"><p style="margin:0 0 12px;font-weight:700;font-size:13px;letter-spacing:3px;text-transform:uppercase;line-height:1.3">Das Wichtigste in 30 Sekunden</p><ul style="margin:0;padding-left:20px;display:grid;gap:8px;line-height:1.5"><li style="margin:0">KI-Modelle erfinden manchmal Fakten, Preise oder Quellen. Der sichere Ton sagt nichts darüber, ob es stimmt.</li><li style="margin:0">Das größere Risiko ist nicht der Fehler selbst, sondern dass niemand mehr nachsieht.</li><li style="margin:0">Nicht jede Antwort braucht dieselbe Kontrolle. Entscheidend ist, was ein unbemerkter Fehler anrichten würde.</li><li style="margin:0">Drei Stufen helfen: frei nutzen, gezielt prüfen, nur mit Freigabe.</li><li style="margin:0">Fünf Regeln fangen die meisten Fehler ab, vom Abgleich mit eigenen Unterlagen bis zum Test mit fehlenden Angaben.</li></ul></div>
```

## Warum KI so überzeugend danebenliegen kann

Für das Problem gibt es einen Fachbegriff: **Halluzination**. OpenAI beschreibt das in einem Forschungsbeitrag vom September 2025 als plausible, aber falsche Aussagen, die ein Sprachmodell erzeugt.

Wie das aussieht, zeigt OpenAI an einem eigenen Mitautor. Fragt man einen verbreiteten Chatbot nach dem Titel seiner Doktorarbeit, nennt er drei verschiedene Titel. Keiner davon stimmt. Beim Geburtstag passiert dasselbe.

Die Erklärung ist unspektakulär. Sprachmodelle werden so trainiert und bewertet, dass Raten sich mehr lohnt als ein ehrliches „Ich weiß es nicht“. OpenAI vergleicht das mit einem Test: Wer den Geburtstag einer Person nicht kennt und rät, liegt immerhin mit einer Chance von 1 zu 365 richtig. Wer „weiß ich nicht“ schreibt, bekommt sicher null Punkte. Also rät das Modell.

Wichtig ist auch, was OpenAI daraus folgert: Fehlerfrei werden Sprachmodelle nie, weil manche Fragen sich schlicht nicht beantworten lassen. Unvermeidbar sind Halluzinationen aber auch nicht, denn ein Modell kann sich bei Unsicherheit zurückhalten. Ob es das tut, hängt davon ab, wie es gebaut und bewertet wird. Darauf hast du als Anwender keinen Einfluss. Auf deinen eigenen Ablauf schon.

![Schaubild: Warum Sprachmodelle lieber raten – „Ich weiß es nicht“ bringt sicher 0 Punkte, Raten beim Geburtstag immerhin eine Chance von 1 zu 365; Merksatz: Raten wird belohnt, Zugeben nicht](kmk-ki-pruefen-g1.png "Wer raten darf, rät – das gilt auch für Sprachmodelle.")

Auch die Hilfeseite von OpenAI zu ChatGPT sagt ausdrücklich, dass ChatGPT sicher klingen kann, auch wenn es falschliegt. Als typische Fehler nennt sie falsche Daten und Fakten sowie erfundene Zitate, Studien und Verweise auf Quellen, die es nicht gibt. Die Empfehlung des Herstellers selbst: ChatGPT als ersten Entwurf nutzen, nicht als endgültige Quelle.

Für den Alltag heißt das: **Eine KI-Antwort ist ein Vorschlag, kein Ergebnis.** Wie bei einem neuen Mitarbeiter, der sehr gut formuliert, aber den Betrieb noch nicht kennt.

## Das eigentliche Risiko: Niemand schaut mehr hin

Dass KI Fehler macht, ist bekannt. Kritisch wird es an einer anderen Stelle. Das OWASP-Projekt, eine gemeinnützige Gemeinschaft für IT-Sicherheit, führt Fehlinformation durch Sprachmodelle in seiner Liste der zehn wichtigsten Risiken für KI-Anwendungen (Stand 2025). Als Ursache nennt es neben den Halluzinationen ausdrücklich das übermäßige Vertrauen: Menschen prüfen die Ausgaben nicht genug und übernehmen falsche Angaben in Entscheidungen und Abläufe. Erst dadurch wird aus einem Fehler ein Schaden. Als mögliche Folgen nennt OWASP Reputationsschäden und rechtliche Haftung.

Das passt zu einer Beobachtung, die viele kennen: Je besser ein Text klingt, desto weniger genau liest man ihn. Ein holpriger Entwurf fordert Korrektur heraus. Ein glatter Text wirkt fertig.

Was ein Chatbot auf der Website deines Betriebs sagt, sagst am Ende du. Und was die KI ins Angebot schreibt, unterschreibst du.

## Wo das im Betriebsalltag passiert

Vier ausgedachte, aber typische Beispiele zeigen, wie unauffällig solche Fehler sind:

**Handwerksbetrieb: das Angebot.** Wie in der Szene oben. Die KI soll aus Stichpunkten ein Angebot machen und ergänzt Material und Preise, die niemand genannt hat. Der Text ist stimmig, die Summe falsch.

**Hausverwaltung: die Nebenkostenfrage.** Ein Mieter fragt, warum seine Nachzahlung so hoch ist. Eine Mitarbeiterin lässt die KI eine Antwort aus der Abrechnung formulieren. Die KI erklärt die Abweichung souverän, nimmt dafür aber den falschen Verteilerschlüssel an. Die Antwort klingt kompetent und schafft genau den Streit, den sie vermeiden sollte.

**Gastronomie: die neue Speisekarte.** Die Inhaberin eines Restaurants lässt die Karte von der KI neu formulieren, schöner und kürzer. Beim Kürzen fällt bei einem Gericht der Hinweis auf Nüsse weg. Bei einem anderen steht plötzlich „glutenfrei“, weil das zum Rezept zu passen schien. Hier geht es nicht mehr um Stil, sondern um die Gesundheit von Gästen.

**Immobilien: das Exposé.** Der Makler notiert nach der Besichtigung: „Dach vermutlich um 2010 erneuert, Eigentümer unsicher“. Im fertigen Exposé steht: „Dach 2010 komplett saniert.“ Aus einer Vermutung ist eine Tatsache geworden. Niemand hat gelogen, aber das Exposé verspricht jetzt etwas, das keiner belegen kann.

![Schaubild: Vergleich am Beispiel eines Exposés – die Notiz „Dach vermutlich um 2010 erneuert, Eigentümer unsicher“ wird im KI-Text zu „Dach 2010 komplett saniert“](kmk-ki-pruefen-g2.png "Der gefährlichste Fehler ist der, der wie eine Verbesserung aussieht.")

Allen vier Fällen ist gemeinsam: Der Fehler ist plausibel. Er sieht aus wie das, was dort stehen könnte. Deshalb fällt er beim Überfliegen nicht auf.

## Nicht jede Antwort braucht dieselbe Kontrolle

Die naheliegende Reaktion wäre: alles prüfen. Das ist nicht realistisch. Wer jeden Ideenzettel der KI Wort für Wort gegenliest, spart keine Zeit mehr. Sinnvoller ist eine einzige Frage vorab:

**Was passiert, wenn dieser Fehler unbemerkt durchrutscht?**

Daraus ergeben sich drei Stufen:

**Stufe 1: Frei nutzen.** Ideen sammeln, Überschriften vorschlagen, einen ersten Entwurf für den Newsletter, Formulierungsvarianten für eine schwierige Mail. Ein Fehler fällt hier sofort auf oder richtet keinen Schaden an, weil ohnehin ein Mensch weiterarbeitet. Hier darf die KI kreativ sein.

**Stufe 2: Gezielt prüfen.** Angebote, Exposés, Kundenantworten, Zusammenfassungen von Verträgen oder Auswertungen. Das Ergebnis geht an Kunden oder fließt in Entscheidungen. Geprüft wird nicht jedes Wort, sondern gezielt: Zahlen, Namen, Daten, Zusagen und alles, was nach Tatsache klingt.

**Stufe 3: Nur mit Freigabe.** Buchungen, Preisänderungen, Zahlungen, Allergen- und Sicherheitsangaben, verbindliche Zusagen. Ein Fehler hier kostet Geld, gefährdet Menschen oder lässt sich nicht einfach zurücknehmen. Die KI darf vorbereiten. Ausgeführt wird erst, wenn eine benannte Person freigegeben hat, am besten gegen feste Regeln wie eine Preisliste oder eine Rezepturdatenbank.

![Stufenmodell mit drei Stufen: frei nutzen (Ideen, Entwürfe), gezielt prüfen (Angebote, Exposés, Kundenantworten, Auswertungen), nur mit Freigabe (Buchungen, Preise, Zahlungen, Allergenangaben); Leitfrage: Was passiert, wenn dieser Fehler unbemerkt durchrutscht?](kmk-ki-pruefen-g3.png "Nicht das Werkzeug entscheidet über die Kontrolle, sondern die Folgen eines Fehlers.")

Derselbe Ablauf kann übrigens die Stufe wechseln. Ein Textentwurf für die Speisekarte ist Stufe 1, solange es um den Ton geht. Sobald Allergene darin stehen, ist es Stufe 3.

Für den Einstieg reicht eine kurze Teamrunde. Sammelt, wofür bei euch heute schon KI genutzt wird, auch das, was einzelne nebenbei im privaten Konto machen (mehr dazu im Beitrag zur [Schatten-KI](https://www.kleinmittelki.de/schatten-ki-deine-mitarbeiter-nutzen-ki-vielleicht-langst-weisst-du-wofur/)). Ordnet jeden Punkt einer Stufe zu. Meist zeigt sich schnell: Das meiste ist Stufe 1. Für die wenigen Fälle in Stufe 2 und 3 braucht es einen klaren Prüfschritt und einen Namen.

Wer KI später nicht nur schreiben, sondern auch handeln lässt, landet bei derselben Logik. Im Beitrag [KI-Agenten: Was nach dem Chatbot kommt](https://www.kleinmittelki.de/ki-agenten-was-nach-dem-chatbot-kommt-und-was-kmu-davon-haben/) geht es darum, warum ein Agent am Anfang nur lesen und vorbereiten sollte, bevor er selbst etwas ausführen darf.

## Fünf Regeln, die die meisten Fehler abfangen

Für alles in Stufe 2 und 3 helfen fünf einfache Regeln. Die ersten drei stützen sich auf die Empfehlungen von OWASP und auf die Hinweise der Anbieter OpenAI und Anthropic selbst; Regel 4 und 5 sind praktische Ergänzungen für den Betriebsalltag.

![Checkliste mit fünf Regeln: mit eigenen Unterlagen abgleichen, Fakten und Annahmen trennen lassen, Zahlen nicht der KI glauben, bei Stufe 3 gibt ein Mensch frei, testen, was bei fehlenden Angaben passiert](kmk-ki-pruefen-g5.png "Zum Abhaken: Je mehr davon in deinem Ablauf steckt, desto weniger rutscht durch.")

**1. Mit eigenen Unterlagen abgleichen.** Die wichtigste Regel. Preise gehören in die Preisliste, Objektdaten in die Objektakte, Allergene in die Rezeptur. Gib der KI diese Unterlagen mit und gleiche das Ergebnis danach mit ihnen ab. OWASP empfiehlt genau das: Antworten auf geprüfte, vertrauenswürdige Quellen stützen und kritische Inhalte von Menschen gegenprüfen lassen.

**2. Fakten und Annahmen trennen lassen.** Bitte die KI ausdrücklich, alles zu markieren, was nicht aus deinen Unterlagen stammt. Und erlaube ihr, „weiß ich nicht“ zu sagen. Anthropic schreibt in seiner Dokumentation, dass allein diese Erlaubnis falsche Angaben deutlich verringern kann. Noch besser: Lass dir zu jeder Aussage die Stelle in deinem Dokument nennen. Findet die KI keine, soll sie die Aussage zurücknehmen. Ein weiterer Trick aus derselben Dokumentation: Stell dieselbe Frage mehrmals, am besten jeweils in einem neuen Chat, und vergleiche die Antworten. Weichen die Antworten bei Zahlen oder Fakten voneinander ab, ist das ein Warnsignal.

**3. Zahlen nicht der KI glauben.** Summen, Flächen, Mengen und Prozentwerte rechnet eine Tabelle zuverlässiger als ein Sprachmodell, das Wörter aneinanderreiht. Lass die KI Texte schreiben, aber Zahlen aus deinem System übernehmen oder mit einem Rechenwerkzeug berechnen, und prüf das Ergebnis stichprobenartig nach.

**4. Bei Stufe 3 gibt ein Mensch frei.** Und zwar eine benannte Person, nicht „irgendwer im Büro“. In einem Betrieb mit 30 Leuten kann das die Bürokraft für Angebote sein und die Küchenchefin für die Speisekarte. Wichtig ist nur: Es ist klar, wer unterschreibt.

**5. Testen, was bei fehlenden Angaben passiert.** Bevor du einen Ablauf regelmäßig nutzt, lass bewusst eine Information weg. Meldet die KI die Lücke oder füllt sie sie mit etwas Plausiblem? Die Antwort zeigt dir, wie sehr du dem Ablauf trauen kannst.

Ein Zusatz, weil er oft fällt: Der Satz „Sag mir, wenn du dir unsicher bist“ im Prompt hilft, ist aber keine Absicherung. Auch Anthropic schreibt, dass solche Techniken Halluzinationen verringern, aber nicht ganz beseitigen, und empfiehlt, kritische Informationen immer zu prüfen. Die Kontrolle gehört deshalb in den Ablauf, nicht nur in den Prompt.

```html
<div class="kmk-kurz" style="border:2px solid #111;border-left:10px solid #D7FF00;padding:18px 22px;margin:28px 0;background:#fff;color:#111"><p style="margin:0 0 12px;font-weight:700;font-size:13px;letter-spacing:3px;text-transform:uppercase;line-height:1.3">Zum Ausprobieren: ein Angebot gegenprüfen</p><ol style="margin:0;padding:0;list-style:none;display:grid;gap:10px;line-height:1.5"><li style="margin:0;display:grid;grid-template-columns:30px 1fr;gap:10px;align-items:start"><span style="background:#D7FF00;font-weight:700;text-align:center;line-height:30px;height:30px">1</span><span>Nimm ein abgeschlossenes Angebot, ein Exposé oder eine Kundenantwort, bei der du das richtige Ergebnis kennst. Entferne Namen, Adressen und Kundendaten.</span></li><li style="margin:0;display:grid;grid-template-columns:30px 1fr;gap:10px;align-items:start"><span style="background:#D7FF00;font-weight:700;text-align:center;line-height:30px;height:30px">2</span><span>Gib der KI nur deine Stichpunkte und deine Preisliste oder Objektdaten.</span></li><li style="margin:0;display:grid;grid-template-columns:30px 1fr;gap:10px;align-items:start"><span style="background:#D7FF00;font-weight:700;text-align:center;line-height:30px;height:30px">3</span><span>Formuliere den Auftrag mit klaren Grenzen, zum Beispiel: <em>„Erstelle aus meinen Stichpunkten ein Angebot. Verwende nur Preise aus der angehängten Preisliste. Fehlt ein Preis, schreib ‚PREIS FEHLT‘ und schätze nichts. Liste am Ende jede Angabe auf, die nicht aus meinen Unterlagen stammt.“</em></span></li><li style="margin:0;display:grid;grid-template-columns:30px 1fr;gap:10px;align-items:start"><span style="background:#D7FF00;font-weight:700;text-align:center;line-height:30px;height:30px">4</span><span>Vergleiche das Ergebnis Zeile für Zeile mit dem Original. Notiere drei Dinge: erfundene Positionen, falsche Zahlen, Vermutungen, die als Tatsache dastehen.</span></li><li style="margin:0;display:grid;grid-template-columns:30px 1fr;gap:10px;align-items:start"><span style="background:#D7FF00;font-weight:700;text-align:center;line-height:30px;height:30px">5</span><span>Wiederhole den Test und lass dabei bewusst einen Preis weg. Meldet die KI die Lücke oder erfindet sie einen Wert?</span></li><li style="margin:0;display:grid;grid-template-columns:30px 1fr;gap:10px;align-items:start"><span style="background:#D7FF00;font-weight:700;text-align:center;line-height:30px;height:30px">6</span><span>Entscheide danach, in welche Stufe der Ablauf gehört und wer ihn künftig freigibt.</span></li></ol><p style="margin:14px 0 0;font-size:15px;color:#45453F">Der Test zeigt dir an deinen eigenen Unterlagen, wie verlässlich der Ablauf ist.</p></div>
```

## Meine Einschätzung

Ich halte die drei Stufen für den eigentlichen Kern dieses Themas. Die Diskussion über KI-Fehler dreht sich oft um die Frage, ob man KI überhaupt trauen kann. Für einen Betrieb ist das die falsche Frage. Die bessere lautet: Wo kann ich ihr trauen, und wo bleibt Kontrolle nötig?

Im [Protokoll-Selbstversuch](https://www.kleinmittelki.de/protokoll-per-ki-selbstversuch/) hier im Blog war es genau so: Der Entwurf sah fertig aus, aber einige Namen waren falsch geschrieben und die Amtszeit der Kassenprüfer stimmte nicht. Aufgefallen sind die Fehler erst bei der Prüfung.

[TILL: 2–3 Sätze eigene Erfahrung, wo KI im Alltag überzeugend falschlag – oder Absatz streichen]

Mich überzeugt an diesem Ansatz, dass er nichts verbietet. KI darf weiter Ideen liefern und Entwürfe schreiben. Sie bekommt nur dort einen Kontrollschritt, wo ein Fehler wirklich wehtut. KI muss man nicht blind vertrauen, um von ihr zu profitieren.

## Ein Gedanke zum Mitnehmen

Nimm die drei Abläufe, in denen bei euch am häufigsten KI im Spiel ist. Frag für jeden: Was passiert, wenn hier ein Fehler unbemerkt durchrutscht? Die Antwort sagt dir, wie genau du hinsehen musst.

## Quellen

Abgerufen und geprüft am 23.10.2026

- [OpenAI: Why language models hallucinate (05.09.2025)](https://openai.com/index/why-language-models-hallucinate/)
- [OpenAI Help Center: Does ChatGPT tell the truth? (abgerufen 23.10.2026)](https://help.openai.com/en/articles/8313428-does-chatgpt-tell-the-truth)
- [OWASP Gen AI Security Project: LLM09:2025 Misinformation (OWASP Top 10 for LLM Applications 2025, Stand 17.04.2025)](https://genai.owasp.org/llmrisk/llm092025-misinformation/)
- [Anthropic, Claude-Dokumentation: Reduce hallucinations (abgerufen 23.10.2026)](https://platform.claude.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
