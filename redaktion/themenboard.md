# Themenboard

Der gemeinsame Arbeitsstand der Redaktion. Jeder Agent liest das Board vor seiner Arbeit und trägt Änderungen ein.
Nichts wird gelöscht: Erledigtes wandert in den Abschnitt „Archiv“.

**Status:** `vorgeschlagen` → `freigegeben` → `in-arbeit` → `geprueft` → `wartet-auf-till` → `eingeplant` / `veroeffentlicht` → `beworben`
Daneben: `newsletter-vorschlag` (Sonntag per Mail an Till), `verworfen` (mit Grund in `entscheidungen.md`), `zurueck` (Till will Änderungen), `frage-an-till`.

**Format je Eintrag:**

```
### <slug>
- Status: vorgeschlagen
- Titel (Arbeitstitel): …
- Rubrik/Kategorie: Aktuell / Studien & Zahlen
- Format: Nachricht
- Quelle: <URL der Originalveröffentlichung> (Datum)
- Worum es geht: … (ein, zwei Sätze, nur aus der gelesenen Quelle)
- Warum für KMU: … (Betriebsgröße, Rolle oder Prozess; Einschränkung offen nennen)
- Unsere Idee: „<Arbeitstitel>“ – <Ansatz in einem Satz>
- Relevanz: 8/10 (Betroffenheit 2, Handlung 2, Quelle 2, Neuheit 1, Passung 1)
- Braucht von Till: Einschätzung in 2–3 Sätzen / Testergebnis / nichts
- Verlauf: 2026-10-18 Scout: vorgeschlagen
```

## Aktiv

### modellwahl-kanonen-auf-spatzen
- Status: veroeffentlicht
- Idee von Till (Chat 10.11.2026): Bisher geht es im Blog darum, dass Firmen KI nutzen sollen. Jetzt die Firmen ansprechen, die KI schon nutzen: Viele geben ihren Leuten Claude oder ChatGPT, und alles läuft über die größten Modelle, die am meisten Tokens verbrauchen. „Kanonen auf Spatzen.“ Zwei Lösungswege: Mitarbeitern sagen, welches Modell für welche Aufgabe – oder Technik davorschalten, die automatisch einschätzt, ob Opus nötig ist oder ein kleines Modell reicht.
- Titel (Arbeitstitel): „Mit Kanonen auf Spatzen: Warum nicht jede KI-Aufgabe das stärkste Modell braucht“ (Alternative: „Mehr PS, mehr Sprit: So wählt dein Team das passende KI-Modell“)
- Rubrik/Kategorie: Wissen / Leitfäden
- Format: Langtext (ca. 1.900–2.000 Wörter, Box „Das Wichtigste in 30 Sekunden“, 4–5 Schaubilder im Karten-System, Abschnitt „Zum Ausprobieren“). Autor darf auf Anleitung kürzen, wenn es trägt.
- Quelle: Recherche und Einordnung in entwuerfe/modellwahl-kanonen-auf-spatzen/quellen.md (10.11.2026). Kern: Anthropic-Preisliste und Modellwahl-Doku (platform.claude.com, 10.11.2026), RouteLLM (LMSYS/UC Berkeley, 01.07.2024), FrugalGPT (Stanford, 05/2023), Dauner/Socher (Hochschule München, Frontiers in Communication, 06/2025), OpenAI Help Center zu „Auto“.
- Worum es geht: KI-Modelle gibt es in Größen wie Autos mit unterschiedlich viel PS. Das größte Claude-Modell kostet je Token bis zum 80-Fachen des kleinsten (Anthropic-Preisliste). Studien zeigen: Wer einfache Anfragen an kleinere Modelle schickt, spart in Tests 35 bis über 85 % der Kosten bei 95 % der Qualität (RouteLLM).
- Warum für KMU: Betriebe mit 10–150 Leuten, die ChatGPT Business oder Claude Team eingeführt haben (Geschäftsführung, wer die Lizenzen verwaltet). Beim Abo zahlt man pro Platz – die Modellwahl entscheidet dort über Limits, Wartezeit und Strom, nicht über die Rechnung. Echte Euro geht es erst bei eigenen Anwendungen über die Schnittstelle (z. B. Rechnungen oder Anfragen automatisch sortieren). Einschränkung offen: Dass „viele“ Firmen überdimensioniert arbeiten, ist nicht durch Nutzungsdaten belegt → als Beobachtung formulieren.
- Unsere Idee: „Mit Kanonen auf Spatzen“ – mit dem PS-Bild erklären (Kleinwagen, Mittelklasse, Sportwagen = Haiku/Sonnet/Opus bzw. Instant/Thinking/Pro; Sprit = Tokens, Limit, Strom), dann zwei belegte Wege für KMU: (1) Faustregel fürs Team mit konkreter Aufgabenliste je Stufe, Standardmodell festlegen, kurze Antworten bestellen, Dateien hochladen statt reinkopieren; (2) Technik davor: ChatGPT „Auto“ macht das schon, für eigene Anwendungen ein Router (RouteLLM, Kaskade nach FrugalGPT) – aber nur mit eigenem Test an 50–200 echten Fällen.
- Pflicht-Gegenpunkt: Nicht übertreiben. Anthropic vergleicht nach Kosten je erledigter Aufgabe; ein kleines Modell, das scheitert, kostet Nacharbeit, und ein großes Modell auf niedriger Denkstufe kann pro Ergebnis kaum teurer sein. Für schwierige Aufgaben ist das große Modell richtig.
- Interne Verlinkung (Tills Wunsch): „ChatGPT ist nicht das KI-Modell“ (08.10.2026, https://www.kleinmittelki.de/chatgpt-claude-gemini-ki-modelle-erklaert/) früh im Text als Grundlage verlinken; das Auto-Bild von dort (Marke/Fahrzeug/Motor) aufgreifen und um PS und Verbrauch erweitern. Im Social-Paket und Newsletter beide Beiträge zusammen bewerben. Auch „Nicht jedes Problem braucht KI“ verlinken.
- Grafik-Ideen: (1) PS-Vergleich der drei Stufen mit Preis je 1.000 Anfragen (eigene Rechnung aus offizieller Preisliste, Annahmen nennen); (2) Ampel/Faustregel: welche Aufgabe auf welche Stufe; (3) Router-Prinzip: Anfrage → Weiche → kleines oder großes Modell; (4) Abo vs. Schnittstelle: wo die Modellwahl Geld kostet und wo Limits.
- Vorsicht Themenregeln: keine Modell-Rangliste, keine Benchmark-Namen im Text; Testzahlen nur als Größenordnung mit „Herstellermessung“. Zahlen aus 2023/2024 (RouteLLM, FrugalGPT) als Prinzip, nicht als Versprechen. Modellnamen und Preise mit „Stand: November 2026“.
- Relevanz: 9/10 (Betroffenheit 2, Handlung 2, Quelle 2, Neuheit 2, Passung 1)
- Braucht von Till: Einschätzung in 2–3 Sätzen (welche Aufgaben er selbst klein bzw. groß rechnen lässt) – sonst INTERN-Vorschlag im Entwurf
- Verlauf: (ältere Einträge: redaktion/verlauf/modellwahl-kanonen-auf-spatzen.md) 2026-11-12 Chat: Till „bitte morgen 07:00 veröffetlichen“ → Freigabe eingetragen, in Ghost eingeplant Fr 13.11. 7:00 (06:00Z) · 2026-11-13 Lauf 7:47: veröffentlicht 7:00 (Ghost published_at 06:00Z), https://www.kleinmittelki.de/modellwahl-kanonen-auf-spatzen/; Till per Mail gemeldet; Social-Paket im Sonntags-Teil · 2026-11-15 Social (Sonntags-Lauf): Paket vorbereitet (entwuerfe/modellwahl-kanonen-auf-spatzen/social.md, zusammen mit „ChatGPT ist nicht das KI-Modell“: WhatsApp-Status Di 17.11., LinkedIn Do 19.11. vorgeschlagen, Vorrat rückt: Do 26.11. nicht-jedes-problem, Do 03.12. eurobarometer; Karussell 7 Folien). Social: vorbereitet, wartet auf Till. Nichts gepostet.

### iab-betriebe-sehen-keine-ki-anwendung
- Status: veroeffentlicht
- Idee von Till (Chat 23.10.2026, zwei fertige Entwürfe „Gelesen & eingeordnet“ aus einem anderen Werkzeug; Till: „Ja bitte beide Beiträge als Entwürfe anlegen. Perfekt für KMK machen!“)
- Titel: „Fast 90 Prozent der Betriebe ohne KI sehen keinen Einsatz. Vielleicht suchen sie an der falschen Stelle.“ (Till, Chat 24.10.2026; vorher „Ein Bäcker braucht keine KI …“ – gefiel ihm nicht)
- Rubrik/Kategorie: Aktuell / Studien & Zahlen · Format: Nachricht · eine Grafik (Potenzial vs. Nutzung, nur Zahlen aus der IAB-Pressemitteilung)
- Quelle: https://iab-forum.de/weshalb-die-meisten-betriebe-kuenstliche-intelligenz-noch-nicht-nutzen/ (20.10.2026) + IAB-Pressemitteilung (idw)
- Warum für KMU: Kleinbetriebe (Handwerk, Bäckerei) suchen KI im Kerngeschäft statt bei Büroaufgaben
- Braucht von Till: Einschätzung in 2–3 Sätzen oder Freigabe des Vorschlags
- Vorschlag „Eine Zahl, genau gelesen“: zahl „88 %“ · text „der Betriebe ohne KI sehen dafür keine passende Anwendung.“ · genau „Gemeint sind nur Betriebe, die KI weder nutzen noch planen – im zweiten Halbjahr 2025 zwei Drittel aller Betriebe. Selbstauskunft. Quelle: IAB, Oktober 2026.“ · link: Beitrag nach Veröffentlichung. Ändern nur nach Freigabe (Code-Injection, nicht per API).
- Reihenfolge: vor nicht-jedes-problem-braucht-ki veröffentlichen
- Verlauf: (ältere Einträge: redaktion/verlauf/iab-betriebe-sehen-keine-ki-anwendung.md) 2026-11-09 Lauf 18:47: „B ja“ (Mail 1a1c0666e55205d8, 14:01) → Freigabe eingetragen, in Ghost eingeplant für Di 10.11. 7:00 (06:00Z) · 2026-11-10 Lauf 12:47: veröffentlicht Di 10.11. 7:00 (Ghost published_at 06:00Z) → https://www.kleinmittelki.de/iab-betriebe-sehen-keine-ki-anwendung/ · 2026-11-22 Social (Sonntags-Lauf): Paket vorbereitet (entwuerfe/iab-betriebe-sehen-keine-ki-anwendung/social.md: WhatsApp-Status Di 24.11., LinkedIn Do 26.11. vorgeschlagen, Vorrat rückt: Do 03.12. nicht-jedes-problem, Do 10.12. eurobarometer; Karussell 4 Folien). Social: vorbereitet, wartet auf Till. Nichts gepostet.

### nicht-jedes-problem-braucht-ki
- Status: veroeffentlicht
- Idee von Till (Chat 23.10.2026, siehe oben)
- Titel: „Nicht jedes Problem braucht KI. Manchmal reicht die einfachere Lösung.“ (Tills Titel, leicht gekürzt)
- Rubrik/Kategorie: Aktuell / Entwicklungen · Format: Nachricht · eine Grafik (Stufenmodell, eigene Darstellung)
- Quelle: https://www.infoworld.com/article/4230874/dont-buy-a-consultants-ai-framework.html (06.10.2026, Original; Computerwoche 16.10. ist Übersetzung) + Fraunhofer HNFIZ (02.10.2026)
- Warum für KMU: Hausverwaltung/Kleinbetrieb – einfachste ausreichende Lösung vor KI-System
- Braucht von Till: Einschätzung in 2–3 Sätzen oder Freigabe des Vorschlags
- Nach Veröffentlichung des IAB-Beitrags: Querverweis darauf ergänzen
- Verlauf: (ältere Einträge: redaktion/verlauf/nicht-jedes-problem-braucht-ki.md) 2026-10-25 Chat: neuer Takt (Di/Do 7:00), Till „nur einer heute“ → C soll auf Do 29.10. 7:00 (redaktion/fahrplan.md). Freigabe steht noch auf „sofort“; braucht Tills Mail-Antwort „C Donnerstag“, sonst geht C am 25.10. 21:47 online. · 2026-10-25 Ghost-Lauf (21:47): veröffentlicht, https://www.kleinmittelki.de/nicht-jedes-problem-braucht-ki/ (Freigabe „sofort“ aus Mail 18:25; Tills Chat-Wunsch „erst Donnerstag“ kam ohne Mail-Antwort nicht in die Freigabe) · 2026-11-01 Social (Sonntags-Lauf): Paket vorbereitet (entwuerfe/nicht-jedes-problem-braucht-ki/social.md, LinkedIn als Vorrat ab Do 12.11., kein Karussell). Social: vorbereitet, wartet auf Till. Nichts gepostet.

### ki-ergebnisse-pruefen-leitfaden
- Status: veroeffentlicht
- Idee von Till (Chat 23.10.2026, LinkedIn-Anlass + ChatGPT-Entwurf, siehe redaktion/eingang/2026-10-23-chatgpt-ki-fehler-pruefen.md)
- Titel: „KI irrt sich und klingt trotzdem sicher: So prüfst du KI-Ergebnisse im Betrieb“ (25.10.2026, Till: alte Überschrift nicht selbsterklärend; vorher „KI klingt sicher. Aber stimmt es auch? …“)
- Rubrik/Kategorie: Wissen / Leitfäden
- Format: Langtext (ca. 1.900–2.000 Wörter, Box „Das Wichtigste in 30 Sekunden“, 4–5 Schaubilder im Karten-System, Abschnitt „Zum Ausprobieren“)
- Kern: Nicht jede KI-Antwort braucht dieselbe Kontrolle. Drei Stufen nach Folgen eines Fehlers: frei nutzen (Ideen, Entwürfe) · gezielt prüfen (Angebote, Exposés, Auswertungen) · nur mit Freigabe (Buchungen, Preise, Zahlungen). Fünf Regeln als Checkliste.
- Vorgaben aus dem Chat (Till: „Ja“ auf diese Punkte):
  - KEIN Hund-Tiger-Meme und keine fremden Bilder; eigenes Beispiel als Schaubild. **Überholt 25.10.2026:** Till will das Bild-Beispiel jetzt drin haben (Chat) → als eigene Grafik g6, kein fremdes Bild.
  - KEIN Einzelhandels-Beispiel (Regel 4). Beispiele z. B. Handwerksbetrieb (Angebot mit erfundenen Materialpreisen), Hausverwaltung (Nebenkosten), Gastronomie (Allergen-Angaben), Immobilien-Exposé (Vermutung wird Tatsache).
  - Keine Ampelfarben: Stufen-Schaubild nur in Schwarz/Lime (g-stufen oder g-tabelle).
  - Quellen am Original lesen: OpenAI-Hinweise zu Halluzinationen, OWASP Top 10 for LLM Applications (Misinformation), ggf. BSI. LinkedIn-Beitrag von Alex Lichtenberger nur als Anlass nennen, nicht als Beleg (nicht gelesen).
  - Intern verlinken: OLG-Hamm-Beitrag (olg-hamm-chatbot-haftung, sobald online) und KI-Agenten-Beitrag (Zugriffsrechte, Stufen).
  - Ich-Aussagen nur als INTERN-Vorschlag, bis Till eigene Sätze liefert. Kein Praxistest-Ergebnis erfinden; „Zum Ausprobieren“ als Anleitung für den Leser.
- Später: Praxistest als Fortsetzung (Till testet; Redaktion bereitet Beispiel-Preisliste und Prompt vor).
- Tills Einschätzung/Erfahrung (geliefert 23.10.2026 im Chat): `redaktion/eingang/2026-10-23-till-eigene-ki-fehler.md`
  – drei eigene Fälle: (1) Steckachse fürs Mountainbike: ChatGPT „100 %“ sicher, obwohl Einbaubreite 148 mm ≠ Achslänge und
  Gewindesteigung ungeprüft (NICHT behaupten, die Achse habe nachweislich nicht gepasst); (2) Excel-Kalkulation: Schwund/Verbrauchsmaterial
  vertauscht, Formel =((B8-B9-B11)/B8)*C34*(1-B10/100) liefert Marge × Stückzahl statt Euro (Beispiel 285 € vs. 28,50), Wachstum nicht
  kumulativ (100.000 → 110.000 → 121.000); (3) ChatGPT-Selbst-Audit der eigenen Fehler: hilfreich, aber kein unabhängiger Beweis.
- Überarbeitung (Till „Ja“ + Beispiele, 23.10.): Diese drei Fälle ersetzen den `[TILL: …]`-Platzhalter und tragen den Beitrag:
  Steckachse → „fehlende Informationen, trotzdem sicher“; Excel → Kernbeispiel und „Zum Ausprobieren“ (Formel mit einfachen Zahlen
  nachrechnen, Rechnung selbst prüfen); Selbst-Audit → Regel „KI darf mitprüfen, aber nicht allein über ihre eigene Arbeit entscheiden“.
  Ausgedachte Beispiele nur behalten, wo sie etwas zeigen, das Tills Fälle nicht zeigen. „Meine Einschätzung“ aus Tills Text
  (z. B. „KI muss nicht perfekt sein, um nützlich zu sein … Die Verantwortung für das Ergebnis nimmt sie uns nicht ab.“) – damit kein INTERN mehr nötig.
  Aus Tills Text streichen: „Einzelhändler“ (Regel 4). Prompt-Kasten mit Tills Prompt („Nenne mir ausdrücklich alle Angaben, die … fehlen …“).
  Excel-Fall eignet sich für eine Schaubild-Rechnung (falsch 28,50 vs. richtig 285 €) im Karten-System. Rechnungen vor Übernahme nachrechnen.
  Titel bleibt; Alternative für Till in der Vorschau-Mail nennen: „ChatGPT lag falsch. Und war sich trotzdem sicher.“
- Verlauf: (ältere Einträge: redaktion/verlauf/ki-ergebnisse-pruefen-leitfaden.md) 2026-10-25 Ghost-Lauf (21:47): eingeplant für Di 27.10. 7:00 (06:00Z), https://www.kleinmittelki.de/p/3aa0ec3b-67f5-440d-9514-2a9509cbbfd0/ · 2026-10-27 Ghost-Lauf (7:47): veröffentlicht (Index: published), https://www.kleinmittelki.de/ki-ergebnisse-pruefen-leitfaden/ · 2026-11-01 Social (Sonntags-Lauf): Paket Fassung 2 passend zur veröffentlichten Tiger-Fassung (alte Fassung 1 als veraltet markiert): WhatsApp-Status Di 3.11. (falls nicht schon 28.10.), LinkedIn Do 5.11., Karussell 5 Folien. Social: vorbereitet, wartet auf Till. Nichts gepostet.

### eu-eurobarometer-ki-unternehmen
- Status: veroeffentlicht
- Vorschau: https://www.kleinmittelki.de/p/d77e3c23-2a20-4e08-902e-c7eb02041c7e/
- Idee von Till (Mail „KMK Idee: bitte direkt fertig ausarbeiten und Entwurf schicken“, 2026-10-19 13:42, ID 1a153f817ec2e14b)
- Titel: „Kosten, Recht, Wissen: Was EU-Betriebe bei KI und Personalsoftware bremst“ (Redaktion; Mail-Headline „KI ist verfügbar …“ verworfen, weil die Umfrage Verfügbarkeit nicht abfragt – Till entscheidet)
- Rubrik/Kategorie: Aktuell / Studien & Zahlen (vorläufig, Chefredakteur)
- Format: Nachricht (vorläufig)
- Quelle: Pressemitteilung IP/26/2160 (14.10.2026) gelesen, https://ec.europa.eu/commission/presscorner/detail/de/ip_26_2160; Bericht nur als Spiegel-PDF gelesen (Größenklassen 41/49/56/64 % nur dort, ungeprüft am europa.eu-Original); ursprünglicher Hinweis aus der Mail: Europäische Kommission, Flash Eurobarometer 578, https://europa.eu/eurobarometer/surveys/detail/3696 (laut Mail veröffentlicht 14.10.2026, Erhebung 20.03.–13.04.2026)
- Zahlen laut Mail (alle ungeprüft, am Original prüfen): 42 % nutzen KI oder algorithmische Managementsysteme, 21 % planen es, Hürden: 50 % Investitionskosten, 49 % rechtliche Unsicherheit, 48 % fehlendes Fachwissen; rund 12.800 Unternehmen aus 27 EU-Staaten. Laut Mail: 42 % sind keine reine KI-Quote.
- Text der Mail (wörtlich, Auszug ohne Zahlenliste): „Relevanz für KMU: Die drei größten Hürden sind nicht überraschend: Kosten, Rechtssicherheit und fehlendes Wissen. Genau diese Fragen beschäftigen einen Betrieb, der nicht über eine eigene IT-Abteilung verfügt.“ · „Meine Einordnung: Besonders interessant ist, dass technische Verfügbarkeit offenbar nicht der entscheidende Engpass ist. KI-Anwendungen gibt es mittlerweile reichlich. Schwieriger ist es, daraus einen sicheren und wirtschaftlich sinnvollen Unternehmensprozess zu machen.“ · „Redaktionelle Bewertung: 9,5/10“
- Achtung: Der Mailtext trägt Merkmale einer ChatGPT-Ausgabe (Link mit utm_source=chatgpt.com). Ob „Meine Einordnung“ Tills eigene Einschätzung ist, ist offen → im Entwurf bis zur Bestätigung als Vorschlag (INTERN) markieren; Frage an Till gestellt.
- Warum für KMU: Hürden Kosten, Rechtssicherheit, Wissen – betrifft Betriebe ohne eigene IT-Abteilung; Größenklassen-Auswertung im Original suchen.
- Relevanz: vom Scout zu bewerten (Mail nennt 9,5/10)
- Braucht von Till: Bestätigung, ob „Meine Einordnung“ von ihm stammt
- Verlauf: (ältere Einträge: redaktion/verlauf/eu-eurobarometer-ki-unternehmen.md) 2026-10-25 Till per Mail (Verlauf „Vorschau bereit · So 25.10.“, 18:25): „D ja“ → Veröffentlichungsfreigabe sofort über mailfreigabe.py eingetragen (Mail-ID 1a17417b727d7bfb). Nächster Ghost-Lauf (21:47) veröffentlicht. · 2026-10-25 Ghost-Lauf (21:47): veröffentlicht, https://www.kleinmittelki.de/eu-eurobarometer-ki-unternehmen/ · 2026-11-01 Social (Sonntags-Lauf): Paket vorbereitet (entwuerfe/eu-eurobarometer-ki-unternehmen/social.md, LinkedIn als Vorrat ab Do 12.11., kein Karussell). Social: vorbereitet, wartet auf Till. Nichts gepostet.

### outlook-diktat-praxistest
- Status: vorgeschlagen
- Titel (Arbeitstitel): Outlook räumt diktierte Texte auf – ein Praxistest
- Rubrik/Kategorie: Praxistests / KI in der Praxis
- Format: Praxistest
- Quelle: Microsoft-Support "Diktieren Ihrer E-Mails in Outlook" https://support.microsoft.com/de-de/accessibility/outlook/dictate-your-emails-in-outlook (Datum der Seite unbekannt; vom Scout NICHT selbst gelesen, Abruf nicht möglich, ungeprüft)
- Warum für KMU: Diktieren statt Tippen spart Inhabern Zeit bei Kundenmails; läuft im Abo, das viele Betriebe schon haben.
- Relevanz: vorläufig 6/10 (Betroffenheit 1, Handlung 1, Quelle 1, Neuheit 2, Passung 1) – unter Schwelle. Grund: Die Behauptung "Outlook räumt diktierte Texte auf" ist nicht belegt; Treffer nennen nur Diktat mit automatischer Zeichensetzung, Aufräumen wäre Copilot. Titel ungeprüft.
- Braucht von Till: eigenen Test durchführen und Ergebnisse liefern; ob er Microsoft 365/Copilot hat
- Details: entwuerfe/outlook-diktat-praxistest/quellen.md
- Verlauf: (ältere Einträge: redaktion/verlauf/outlook-diktat-praxistest.md) 2026-10-19 Scout: Quelle benannt, Originalseite nicht lesbar, Kernbehauptung nicht belegt, Relevanz unter 7 · 2026-10-19 Scout (Redaktions-Lauf): Outlook-Supportseite weiterhin nicht abrufbar (ungeprüft). Gelesen: Microsoft „Fluid dictation“ – Füllwörter/Grammatik-Korrektur beim Diktieren ist eine Windows-Funktion, nur Copilot+ PCs, laut Seite nur Englisch. Titel für deutschen Test nicht haltbar; Relevanz bleibt 6/10. Ersatz-Idee (Diktat + Copilot-Überarbeitung) nur bei Copilot-Lizenz, Frage an Till über Chefredakteur. · 2026-10-19 Scout (Test 2): Outlook-Supportseite (de-de, Stand 17.09.2026) **gelesen**: Diktat in Outlook (365, 2024, .com, neues Outlook, Web) mit Deutsch und automatischer Zeichensetzung; laut Seite keine Speicherung von Audio/Text; **keine Aufräum-Funktion** beschrieben, keine Lizenzangabe. Kernbehauptung bleibt unbelegt, Relevanz bleibt 6/10.

### werkzeuge-besprechungsnotizen-datenschutz
- Status: vorgeschlagen
- Titel (Arbeitstitel): Besprechungsnotizen per KI: welche Werkzeuge, was beim Datenschutz zählt
- Rubrik/Kategorie: Wissen / Leitfäden
- Format: Langtext
- Quelle: Hersteller-Dokumentationen, Datenschutz-Aufsicht (vom Scout zu recherchieren)
- Warum für KMU: Im Beitrag „Protokoll per KI“ angekündigt; jede Teamrunde betroffen.
- Relevanz: vorläufig 7/10 (Betroffenheit 2, Handlung 2, Quelle 0, Neuheit 1, Passung 2) – Quelle fehlt noch, daher nicht belastbar
- Braucht von Till: Einschätzung, welche Werkzeuge er selbst nutzt
- Details: entwuerfe/werkzeuge-besprechungsnotizen-datenschutz/quellen.md (Quellenliste noch leer; Auftrag für nächsten Lauf mit funktionierendem Abruf)
- Verlauf: (ältere Einträge: redaktion/verlauf/werkzeuge-besprechungsnotizen-datenschutz.md) 2026-10-19 Scout: keine Quelle lesbar, nichts recherchiert, nur Gerüst angelegt · 2026-10-19 Scout (Redaktions-Lauf): drei Quellen gelesen – GDD-Kurzpapier 4 „Gesprächstranskription“ (Jan. 2026), GDD-Erfa-Konzept „KI-gestützte Transkription von Videokonferenzen“ v1.2 (09.06.2026, mit Vorlagen auch für Betriebe ohne Betriebsrat), Microsoft-Datenschutzseite zu Teams „intelligent recap“ (Herstellerangabe). Keine Aufsichtsbehörden-Quelle gefunden; Google/Zoom/Noota-Doku offen. Relevanz neu: 8/10 (Betroffenheit 2, Handlung 2, Quelle 1, Neuheit 1, Passung 2) – Quelle 1, weil Fachverband statt Aufsicht. · 2026-10-19 Scout (Test 2): Aufsichtsquelle gelesen – LfDI Baden-Württemberg, Leitfaden KI-Transkription (10.06.2026), allerdings für Gemeinderäte; übertragbar: Training mit Daten grundsätzlich unzulässig, Löschung nach Protokoll, menschliche Kontrolle, EU-Verarbeitung. Google-Meet-Hilfe „Take notes for me“ gelesen (Deutsch unterstützt, Zustimmungspflicht standardmäßig aus). Zoom-Seite nicht lesbar (ungeprüft). Aufsichtsquelle speziell für Unternehmen fehlt weiter. Relevanz bleibt 8/10.

### olg-hamm-chatbot-haftung
- Status: veroeffentlicht
- Vorschau: https://www.kleinmittelki.de/p/1843fcaf-e8d6-4e41-ad9f-f14ddc24e14a/
- Titel (Arbeitstitel): Wenn der Chatbot sich irrt, haftet der Betrieb
- Rubrik/Kategorie: Aktuell / Entwicklungen
- Format: Nachricht
- Quelle: OLG Hamm, Urteil 12.05.2026, Az. 4 UKl 3/25 – Aktenzeichen und Datum nur aus Zweitquellen (beck-aktuell, Ärzteblatt u. a.), **Original (Pressemitteilung/Volltext) nicht gelesen, URL offen, ungeprüft** → überholt 2026-10-19: PM gelesen, https://www.justiz.nrw/presse/2026-05-12 (Volltext noch nicht veröffentlicht)
- Warum für KMU: Jeder Betrieb mit Chatbot auf der Website ist betroffen (laut Urteil Fall einer Klinik; Übertragung auf andere Branchen ist Auslegung von Kommentatoren). Sachverhalt: Chatbot nannte Ärzte Fachärzte mit nicht existierenden Titeln, § 5 UWG.
- Relevanz: vorläufig 9/10 (Betroffenheit 2, Handlung 2, Quelle 1, Neuheit 2, Passung 2) – hängt an Beschaffung des Originals. Hinweis: Urteil ist vom Mai, kein 72h-Ereignis; Revision zugelassen; laut NRWE rechtskräftig (Stand 19.10.2026) – Angabe „nicht rechtskräftig“ aus Zweitquellen überholt.
- Braucht von Till: nichts mehr – Vorschlag „Meine Einordnung“ mit „A ja“ übernommen (Mail 23.10.)
- Details: entwuerfe/olg-hamm-chatbot-haftung/quellen.md
- Verlauf: (ältere Einträge: redaktion/verlauf/olg-hamm-chatbot-haftung.md) 2026-10-23 Chat: Titel-Kachel war Beitragsbild (doppelter Titel, kein Bild in der Übersicht). Neues Titelbild titel-olg-hamm-chatbot-haftung.jpg, Till „Ja und ja“ → Freigabe titelbild, Ghost-Lauf tauscht das Bild · 2026-10-23 Ghost-Lauf (18:47): Titelbild getauscht (Freigabe titelbild ausgeführt) · 2026-10-25 Social (Sonntags-Lauf): Paket vorbereitet (entwuerfe/olg-hamm-chatbot-haftung/social.md: WhatsApp-Status Di 27.10., LinkedIn Do 29.10. mit 2 Kacheln in social/). Social: vorbereitet, wartet auf Till. Nichts gepostet.

### eu-produkthaftung-software-ki
- Status: wartet-auf-till
- Titel: Software gilt ab 9. Dezember als Produkt: Was die neue Produkthaftung für deinen Betrieb heißt (Arbeitstitel vorher: Neue Produkthaftung für Software und KI ab 9.12.2026)
- Rubrik/Kategorie: Wissen / Leitfäden
- Format: Langtext
- Quelle: Richtlinie (EU) 2024/2853 (EUR-Lex, CELEX 32024L2853) – **Original nicht gelesen** (Abruf nicht möglich); Frist 9.12.2026 nur aus Zweitquellen (IHK Frankfurt, Heuking), **ungeprüft**. Deutsches Umsetzungsgesetz: Stand widersprüchlich (Abstimmung 08.10.2026 vs. Rechtsausschuss), BT-Drs.-Nummer 21/4297 ungeprüft. → überholt 2026-10-19: Gesetzesbeschluss BR-Drs. 584/26 gelesen, https://dserver.bundestag.de/brd/2026/0584-26.pdf (Bundestag 08.10.2026; Bundesrat steht aus) → überholt 2026-11-20: Gesetz verkündet, BGBl. 2026 I Nr. 321 vom 27.10.2026 (ausgefertigt 22.10.2026), https://www.recht.bund.de/eli/bund/bgbl-1/2026/321; Richtlinie (EU) 2024/2853 vollständig im amtlichen Text gelesen (inkl. Art. 12, 21, 22, 23); Empfehlung 2003/361/EG gelesen
- Warum für KMU: Betriebe, die Software oder KI-Funktionen in Produkte einbauen oder anbieten. Reine Anwender von Standard-KI vermutlich nicht betroffen (ungeprüft).
- Relevanz: vorläufig 8/10 (Betroffenheit 1, Handlung 2, Quelle 1, Neuheit 2, Passung 2) – Frist beachten; Aussagen zum deutschen Recht erst nach Klärung des Gesetzesstands
- Braucht von Till: Veröffentlichungsfreigabe; Ich-Absatz („Für mich passt das Gesetz …“) bestätigen oder ersetzen; zwei Grafiken ok? (Vorschläge im INTERN-Absatz)
- Vorschau: https://www.kleinmittelki.de/p/2f923142-bc28-4375-925a-a2465525f725/ · Ghost-ID 6b00856644c3dd0001dc17be · Termin Di 24.11. 7:00 (Fahrplan)
- Details: entwuerfe/eu-produkthaftung-software-ki/quellen.md
- Verlauf: (ältere Einträge: redaktion/verlauf/eu-produkthaftung-software-ki.md) 2026-10-19 Scout (Test 2): amtliches EUR-Lex-PDF (DE) gelesen – Art. 2 Abs. 1/2, Art. 4 Nr. 1, Art. 8 Abs. 1/2 bestätigt. Art. 12, 21, 22 (Umsetzungsfrist), 23 weiter nicht lesbar (Abruf bricht ab), ungeprüft. Relevanz bleibt 9/10. · 2026-10-23 Scout: **Bundesrat hat entschieden** – BR-Drs. 584/26(B) gelesen, https://dserver.bundestag.de/brd/2026/0584-26B.pdf: 1069. Sitzung am **16.10.2026**, kein Antrag nach Art. 77 Abs. 2 GG (Vermittlungsausschuss nicht angerufen), keine Entschließung. Gesetz damit zustande gekommen; Ausfertigung/Verkündung im BGBl. noch nicht gefunden (ungeprüft). Inkrafttreten 9.12.2026 laut Gesetzesbeschluss (BR-Drs. 584/26). Aktueller Anlass für eine kurze Nachricht oder als Einstieg in den Leitfaden. · 2026-11-20 Chefredakteur (Sitzung, Auftrag Head of KMI): Themenwahl durch Head of KMI für Di 24.11. (Status freigegeben für die Umsetzung, keine Veröffentlichungsfreigabe); Autor (Quellen frisch, BGBl. verkündet), Grafik (Prüfliste, Zeitstrahl, Titel-/Vorschaubild), Prüfer Runde 1 nicht bestanden (Größengrenze Art. 12 Abs. 2, Länge, Titel), überarbeitet (ca. 1.410 Wörter), Prüfer Runde 2 **bestanden**; Entwurf in Ghost angelegt (`ghost.py draft`), Status wartet-auf-till. Nicht veröffentlicht. · 2026-11-22 Lauf 7:47: Laut Fahrplan-Eintrag von Head of KMI (Commit ced7b31, 20.11. 19:07) hat Till das Thema im Grok-Bot-Chat abgelehnt (20.11. 19:06: „0,0 Mehrwert für KMUs“). Nicht in einer Claude-Sitzung weitergegeben – Status bleibt bis zur Bestätigung, **nicht veröffentlichen**, Entwurf bleibt in Ghost (nichts gelöscht).

### ki-sicherheitsstudie-bsi-tuev
- Status: vorgeschlagen
- Titel (Arbeitstitel): Jeder sechste Betrieb meldet KI-gestützte Angriffe – aber kaum einer hat einen Plan dafür
- Rubrik/Kategorie: Aktuell / Studien & Zahlen
- Format: Nachricht
- Quelle: TÜV-Verband, PM „Nur jedes zehnte Unternehmen gegen KI-gestützte Angriffe gerüstet – jedes sechste Unternehmen berichtet von Vorfällen“ (07.10.2026), gemeinsame Studie mit dem BSI: https://www.tuev-verband.de/pressemitteilungen/nur-jedes-zehnte-unternehmen-gegen-ki-gestuetzte-angriffe-geruestet-jedes-sechste-unternehmen-berichtet-von-vorfaellen – PM selbst gelesen; Studien-PDF und ACS-Flyer nicht lesbar (ungeprüft)
- Warum für KMU: Befragt wurden Unternehmen ab 20 Beschäftigten (Kernzielgruppe). 17 % berichten von KI-bezogenen Angriffen/Betrugsversuchen (meist Phishing-Mails, 11 % der Betroffenen Deepfakes); nur 11 % der KI-nutzenden Betriebe haben einen Notfallablauf dafür. Konkreter Schritt für Inhaber/IT-Verantwortliche: Notfallplan um Phishing-/Fake-Anruf-Szenario ergänzen; ACS-Flyer „Schutz vor KI-verstärkten Cyberangriffen“ (über DIHK) als Hilfe.
- Relevanz: 8/10 (Betroffenheit 2, Handlung 2, Quelle 1, Neuheit 2, Passung 1) – Quelle 1: nur PM gelesen, Selbstauskunft, Herausgeber mit Eigeninteresse an Zertifizierung, keine Größenklassen; Passung 1: PM vom 07.10., kein Eilthema. Dublettencheck: kein Sicherheitsbeitrag im Index; ergänzt Schatten-KI-Beitrag (21.09.) und Themenspeicher-Idee „Stimmklon-Betrug“ – intern verlinken bzw. als Aufhänger nutzen.
- Braucht von Till: Einschätzung in 2–3 Sätzen; ob als Nachricht oder als Aufhänger für den Stimmklon-Leitfaden
- Details: entwuerfe/ki-sicherheitsstudie-bsi-tuev/quellen.md
- Verlauf: 2026-10-19 Scout (Redaktions-Lauf): vorgeschlagen

### ki-suche-falsche-aussagen-ueber-betrieb
- Status: vorgeschlagen
- Titel (Arbeitstitel): Wenn Googles KI Falsches über deinen Betrieb sagt: Gerichte sehen Google in der Pflicht
- Rubrik/Kategorie: Aktuell / Entwicklungen
- Format: Nachricht
- Quelle: LG München I, Endurteil 28.05.2026, Az. 26 O 869/26. Volltext gelesen: https://cdn.arstechnica.net/wp-content/uploads/2026/06/Google-AI-Overview-Munich-Court-Ruling.pdf (Kopie bei Ars Technica). Pressemitteilung 13/26 vom 12.06.2026 gelesen: https://www.justiz.bayern.de/gerichte-und-behoerden/landgericht/muenchen-1/presse/2026/13.php. Aktueller Anlass: LG Aachen, Beschluss 24.09.2026, Az. 8 O 268/26, bekannt seit 10.10.2026 – Original ist ein Scan, nicht lesbar, ungeprüft.
- Warum für KMU: Jeder Betrieb wird gegoogelt. Die „Übersicht mit KI“ kann ihn mit Betrug oder schlechten Bewertungen in Verbindung bringen. Laut LG München I ist die KI-Übersicht ein eigener Inhalt von Google; nach konkretem Hinweis muss Google prüfen. Für Inhaber: eigenen Firmennamen suchen, Falsches mit Datum und Wortlaut sichern, über den Meldeweg konkret beanstanden, Antwort dokumentieren. Fall dort: zwei Verlage. Einstweiliger Rechtsschutz, laut PM nicht rechtskräftig.
- Relevanz: 9/10 (Betroffenheit 2, Handlung 2, Quelle 2, Neuheit 1, Passung 2) – Neuheit 1, weil München aus Mai/Juni; neu ist die Folgeentscheidung aus Aachen. Ergänzt „Frag eine KI nach deinem eigenen Unternehmen“ und „Wenn Azubis die KI fragen“.
- Braucht von Till: Einschätzung in 2–3 Sätzen; optional: Selbsttest mit Googles KI-Übersicht gemacht?
- Details: entwuerfe/ki-suche-falsche-aussagen-ueber-betrieb/quellen.md
- Verlauf: 2026-10-19 Scout (Redaktions-Lauf Abend): vorgeschlagen. Abgrenzung zu olg-hamm-chatbot-haftung: dort haftet der Betrieb für seinen eigenen Chatbot, hier spricht die KI-Suche eines Dritten über den Betrieb – gegenseitig verlinken, nicht zusammenlegen. LG Hamburg 324 O 404/25 nicht verwenden (Original nicht gelesen, Handel). Googles Meldeweg für KI-Übersichten nicht gelesen.

### php-sicherheitsluecken-website-hoster
- Status: vorgeschlagen
- Titel (Arbeitstitel): Kritische Lücken in PHP, mit KI-Hilfe gefunden: Frag jetzt deinen Hoster
- Rubrik/Kategorie: Aktuell / Entwicklungen
- Format: Nachricht (Kennzahl-Grafik möglich: Schweregrad 9,2 von 10)
- Quelle: PHP-Sicherheitsrelease 21.10.2026, https://www.php.net/archive/2026.php · BSI-Cybersicherheitswarnung Version 1.2 vom 22.10.2026, https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-297981-1032.html · OpenAI 21.10.2026 (KI-Beteiligung, Herstellerangabe), https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/ – alle selbst gelesen
- Warum für KMU: Zwei kritische Lücken (CVE-2026-109618/-109619, CVSS 9,2) in PHP, der Technik hinter vielen Firmenwebsites, Kundenportalen und Buchungsseiten. Angriff ohne Anmeldung möglich. Inhaber kleiner Betriebe (1–50 Beschäftigte ohne eigene IT) wissen oft nicht, worauf ihre Seite läuft. Konkreter Schritt: Hoster oder Webagentur fragen, ob auf 8.5.12 / 8.4.27 / 8.3.36 / 8.2.35 aktualisiert ist; PHP 8.1 und älter ohne offizielle Updates; PHP 8.2 endet am 31.12.2026. KI-Bezug: an der Entdeckung war ein KI-Modell beteiligt (BSI und OpenAI).
- Relevanz: 9/10 (Betroffenheit 2, Handlung 2, Quelle 2, Neuheit 2, Passung 1) – Passung 1: eher IT-Sicherheit als KI-Werkzeug; KI-Bezug nur über die Entdeckung. Eilthema: Wert sinkt nach etwa einer Woche.
- Braucht von Till: Einschätzung in 2–3 Sätzen; ob das Thema für ihn auf den Blog passt (Sicherheit mit KI-Aufhänger)
- Details: entwuerfe/php-sicherheitsluecken-website-hoster/quellen.md
- Verlauf: 2026-10-23 Scout: vorgeschlagen. Ausnutzung laut BSI (22.10.) nicht in der Breite bekannt; Behauptungen „Angriffe laufen“ (Patchstack) und „800 Systeme“ (Phoenix Security) nicht gelesen, nicht verwenden. CISA-Alert nicht abrufbar. Keine Zahl zum PHP-/WordPress-Anteil gelesen. Querverweis: ki-sicherheitsstudie-bsi-tuev (ggf. gemeinsam aufgreifen).

### rechnungen-automatisch-erfassen (Entwurf von Till in Ghost)
- Status: frage-an-till
- Titel: Rechnungen automatisch erfassen statt abtippen: Was KI in der Praxis leistet
- Rubrik/Kategorie: Praxistests / KI in der Praxis
- Format: Praxistest
- Quelle: Tills eigener Ghost-Entwurf (19.09.2026, ca. 270 Wörter)
- Braucht von Till: Soll die Redaktion den Entwurf fertigstellen? Liegen die Testergebnisse vor?
- Verlauf: 2026-10-18 im Blog-Index als Entwurf gefunden

### immobiliensuche-mit-ki (Entwurf von Till in Ghost)
- Status: frage-an-till
- Titel: Immobiliensuche mit KI: So habe ich ChatGPT, Notion und Excel kombiniert
- Rubrik/Kategorie: Praxistests / KI in der Praxis
- Format: Praxistest
- Quelle: Tills eigener Ghost-Entwurf (ca. 2.560 Wörter)
- Braucht von Till: Fertigstellen und veröffentlichen? Inhalt ist privat – passt der KMU-Bezug?
- Verlauf: 2026-10-18 im Blog-Index als Entwurf gefunden

### kundenanfragen-antworten-praxistest (Entwurf von Till in Ghost)
- Status: frage-an-till
- Titel: KI in der Praxis: Kann KI aus Kundenanfragen brauchbare Antworten machen?
- Rubrik/Kategorie: Praxistests / KI in der Praxis
- Format: Praxistest
- Quelle: Tills eigener Ghost-Entwurf
- Braucht von Till: Gibt es schon Testergebnisse? Ohne sie bleibt der Beitrag ein Entwurf.
- Verlauf: 2026-10-18 im Blog-Index als Entwurf gefunden

### angebot-aus-preisliste-praxistest
- Status: vorgeschlagen
- Titel (Arbeitstitel): „Angebot aus der Preisliste: Erfindet die KI Positionen, wenn etwas fehlt?“
- Rubrik/Kategorie: Praxistests / KI in der Praxis
- Format: Praxistest (Serienkopf „Selbst ausprobiert“, 700–1.200 Wörter, Prompt-Kasten, Grenzen-Kasten, Transparenz-Absatz)
- Quelle: Tills eigener Test (steht aus). Keine externe Quelle nötig; intern verlinken auf ki-ergebnisse-pruefen-leitfaden (dort angekündigt: „Später: Praxistest als Fortsetzung … Redaktion bereitet Beispiel-Preisliste und Prompt vor“) und olg-hamm-chatbot-haftung.
- Worum es geht: Till gibt einer KI eine fiktive Preisliste und drei fiktive Kundenanfragen und lässt Angebote erstellen. Gezählt wird, wo die KI Positionen oder Preise ergänzt, die nicht in der Liste stehen, wo sie falsch rechnet und wo sie nachfragt. Ergebnisse gibt es erst, wenn Till den Test gemacht hat.
- Warum für KMU: Angebote schreiben ist für Inhaber und Büro in Handwerks- und Dienstleistungsbetrieben (ca. 5–50 Beschäftigte) eine der naheliegendsten KI-Aufgaben. Ein erfundener Preis im Angebot kostet direkt Geld oder Vertrauen. Einschränkung offen nennen: ein Test mit fiktiven Daten, ein bis zwei Werkzeuge, kein repräsentatives Ergebnis.
- Unsere Idee: „Angebot aus der Preisliste“ – der Leitfaden zum Prüfen von KI-Ergebnissen bekommt einen echten Praxisfall, den jeder Betrieb mit seiner eigenen Preisliste nachmachen kann.
- Testaufbau (unter einer Stunde für Till):
  1. Redaktion liefert vorab (10 Min. Lesen): fiktive Preisliste „Muster-Elektro GmbH“ mit ca. 20 Positionen (Material, Stundensatz Meister/Geselle, Anfahrt, Entsorgung) als Excel/PDF, drei fiktive Kundenanfragen, Prompt und Zählbogen.
     Anfrage A: alles in der Liste enthalten. Anfrage B: eine Leistung fehlt in der Liste (z. B. Wallbox-Montage). Anfrage C: Menge unklar („ein paar Steckdosen im Keller“).
  2. Till gibt jede Anfrage mit Preisliste in ChatGPT (und, wenn er will, in Claude) ein, je ein neuer Chat. Prompt-Vorschlag: „Erstelle aus dieser Preisliste ein Angebot für die folgende Anfrage. Verwende nur Positionen und Preise aus der Liste. Markiere alles, was fehlt oder unklar ist, statt es zu schätzen.“ (ca. 30 Min.)
  3. Zählbogen ausfüllen (ca. 15 Min.): erfundene Positionen · erfundene oder geänderte Preise · Rechenfehler (Summe, Mehrwertsteuer) · Rückfragen/Markierungen. Screenshots sichern.
  4. Optional zweite Runde ohne den Satz „Markiere alles …“, um den Unterschied zu sehen.
- Was der Leser danach tun kann: den Test mit der eigenen Preisliste wiederholen und entscheiden, ob KI-Angebote bei ihm in Stufe „gezielt prüfen“ oder „nur mit Freigabe“ gehören.
- Abgrenzung: Tills Ghost-Entwurf kundenanfragen-antworten-praxistest testet Antwortentwürfe auf Anfragen; hier geht es um Preise und Rechnen. Till entscheidet, ob beides zusammengelegt wird. Kein Einzelhandels-Beispiel.
- Relevanz: 9/10 (Betroffenheit 2, Handlung 2, Quelle 1, Neuheit 2, Passung 2) – Quelle 1, weil das Ergebnis erst mit Tills Test entsteht; Passung 2: Till will eigene Tests statt Funktionslisten (Entscheidung 12.10.2026).
- Monatsrhythmus: Praxistest-Woche 3 im November (Di 17.11.2026), falls Till bis ca. 10.11. testet. Ohne Tills Ergebnisse kein Beitrag (`[TILL: Ergebnis eintragen]`).
- Braucht von Till: ja/nein zum Testaufbau, dann ca. 1 Stunde Test, ausgefüllter Zählbogen, Screenshots, 2–3 Sätze Fazit. Welche Werkzeuge er nutzt (ChatGPT, Claude, Copilot).
- Verlauf: 2026-10-25 Ideen (Sonntags-Lauf): vorgeschlagen

### ki-kompetenz-pflicht-mitarbeiter
- Status: vorgeschlagen
- Titel (Arbeitstitel): „Muss ich meine Leute in KI schulen? Was der AI Act von kleinen Betrieben verlangt“
- Rubrik/Kategorie: Wissen / Leitfäden
- Format: Anleitung, Variante „Rechtslage einfach erklärt“ (Vorbild „Muss ich KI-Bilder jetzt kennzeichnen?“), mit Box „Das Wichtigste in 30 Sekunden“ und Prüfliste
- Quelle: Artikel 4 AI Act (Verordnung (EU) 2024/1689), geändert durch den „Digital Omnibus on AI“ – laut Kanzlei-Zweitquellen Verordnung (EU) 2026/1744 vom 08.07.2026, ABl. 24.07.2026, https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ%3AL_202601744 – **Original nicht gelesen (Abruf gesperrt), Nummer, Datum und neuer Wortlaut ungeprüft**. Gelesen nur als Zweitquelle: Cuatrecasas „Digital Omnibus on AI has been published“ (https://www.cuatrecasas.com/en/spain/intellectual-property/art/digital-omnibus-ai-has-been-published) und Sidley (22.06.2026). Selbst gelesen: Bundesnetzagentur, PM 03.07.2025 zum KI-Service-Desk (https://www.bundesnetzagentur.de/SharedDocs/Pressemitteilungen/EN/2025/20250703_KI_ServiceDesk.html), richtet sich laut PM vor allem an KMU und Start-ups, verweist auf Informationen zu KI-Kompetenz und kostenlosen Schulungen. Offen: Hinweispapier KI-Kompetenz der Bundesnetzagentur am Original suchen (nur Zweitverweise gefunden), deutscher Wortlaut des geänderten Art. 4 auf EUR-Lex.
- Worum es geht: Seit Februar 2025 müssen Betriebe, die KI einsetzen, für ausreichende KI-Kompetenz ihrer Leute sorgen (Art. 4). Laut Zweitquellen hat die EU die Pflicht im Juli 2026 umformuliert: Sie bleibt bei Anbietern und Betreibern, verlangt aber kein bestimmtes Kompetenzniveau; die Kommission soll Praxisbeispiele veröffentlichen. Am EUR-Lex-Original prüfen, bevor etwas davon im Beitrag steht.
- Warum für KMU: Betrifft jeden Betrieb, in dem Beschäftigte ChatGPT, Copilot o. Ä. für die Arbeit nutzen – auch den 10-Personen-Betrieb ohne IT-Abteilung. Inhaber hören von „Schulungspflicht“ und wissen nicht, ob sie ein Zertifikat brauchen. Konkreter Schritt: festhalten, wer welche KI wofür nutzt, eine Seite Regeln fürs Team, kurze Einweisung dokumentieren. Einschränkung: keine Rechtsberatung, Bußgeld-Fragen nur mit Originalquelle.
- Unsere Idee: „Muss ich meine Leute in KI schulen?“ – die Rechtslage nach dem Omnibus in einfachen Worten plus eine Prüfliste, mit der ein Inhaber in einer Stunde einen nachweisbaren ersten Stand hat; verlinkt auf Schatten-KI (Kompetenz und Werkzeuge gehören zusammen) und den neuen Prüf-Leitfaden.
- Relevanz: 9/10 (Betroffenheit 2, Handlung 2, Quelle 1, Neuheit 2, Passung 2) – Quelle 1, bis EUR-Lex-Text und Bundesnetzagentur-Material selbst gelesen sind. Dublettencheck: AI-Act-Beitrag vom 03.10. behandelt nur Art. 50 (Kennzeichnung) und hat die Omnibus-Übergangsfrist 02.12.2026 schon drin; Art. 4 kommt im Blog nicht vor.
- Monatsrhythmus: Wissens-Puffer; passt in Woche 2 oder 4 (Di 10.11. oder 24.11.2026).
- Braucht von Till: Einschätzung in 2–3 Sätzen; ob er selbst schon Einweisungen gemacht hat (nur dann Ich-Form, sonst INTERN-Vorschlag).
- Verlauf: 2026-10-25 Ideen (Sonntags-Lauf): vorgeschlagen

### newsletter-2026-11-17
- Status: versendet
- Titel: „#7: Welches KI-Modell für welche Aufgabe?“ (Fassung 1)
- Versand: Dienstag 17.11.2026, 7:05 (erst nach Tills „N ja“, spätestens Mo 16.11. 18:47)
- Inhalt: 01 modellwahl-kanonen-auf-spatzen (live seit 13.11.) + Grundlage chatgpt-claude-gemini-ki-modelle-erklaert (08.10.) · 02 Zahl „7 von 25“ (Anthropic-Doku „Optimizing for cost and intelligence“, Abruf 15.11.2026) · 03 Gedanke. ki-recherche-assistent-selbstversuch ohne Freigabe nicht im Text (INTERN: bei „A ja“ bis Mo 18:47 Abschnitt „Selbst ausprobiert“ ergänzen)
- Datei: entwuerfe/newsletter-2026-11-17/beitrag.md, Prüfung: pruefung.md
- Verlauf: (ältere Einträge: redaktion/verlauf/newsletter-2026-11-17.md) 2026-11-16 Lauf 12:47: Tills „N ja“ (Mail 1a1e419e76709d63, 11:24Z) – Eintrag vom Auto-Modus abgelehnt, nicht umgangen · 2026-11-16 Lauf 18:47: Freigabe eingetragen (Fassung 1, Hash 9ec5c917…), `abarbeiten` → in Ghost eingeplant Di 17.11. 7:05 (06:05Z) · 2026-11-18 Lauf 7:47: versendet Di 17.11. 7:05 (Ghost published_at 06:05Z, Index 17.11.)

### newsletter-2026-11-10
- Status: versendet
- Titel: „#6: Dreimal dieselbe Präsentation mit KI“ (Fassung 2)
- Versand: Dienstag 10.11.2026, 7:05 (erst nach Tills „N ja“)
- Inhalt: 01 powerpoint-mit-ki-im-eigenen-design (live seit 06.11.) · 02 Zahl „86 %“ (Anthropic Research 27.10.2026 – nimmt Board-Thema ki-agent-beeinflusst-entscheidungen vorweg) · 03 Gedanke. Recherche-Assistent auf Tills Wunsch raus (Chat 09.11.: ein „Selbst ausprobiert“ pro Woche)
- Datei: entwuerfe/newsletter-2026-11-10/beitrag.md, Prüfung: pruefung.md
- Verlauf: (ältere Einträge: redaktion/verlauf/newsletter-2026-11-10.md) 2026-11-09 Lauf 12:47: Fassung 3 gemailt (1a1c024b6f48189f, Fingerabdruck 335a848f…), keine neue Testmail (Fassung unverändert); „N ja“ offen, spätestens 18:47 · 2026-11-09 Lauf 18:47: „N ja“ (Mail 1a1c0666e55205d8) für Fassung 3 (335a848f…) → in Ghost eingeplant Di 10.11. 7:05 (06:05Z) · 2026-11-10 Lauf 12:47: versendet Di 10.11. 7:05 (Ghost status sent, 06:05Z)

### newsletter-2026-11-03
- Status: versendet
- Titel: „#5: Was Betriebe bei KI bremst und wie viel Technik reicht“
- Versand: Dienstag 03.11.2026, 7:05 (erst nach Tills „N ja“)
- Inhalt: 01 eu-eurobarometer-ki-unternehmen (live) · 02 nicht-jedes-problem-braucht-ki (live) · 03 Zahl „90 %“ (EU-Kommission IP/26/2160) · 04 Gedanke. Wird ki-recherche-assistent-selbstversuch vor Di freigegeben, kommt er als 01 dazu (Fassung 2).
- Datei: entwuerfe/newsletter-2026-11-03/beitrag.md, Prüfung: pruefung.md
- Verlauf: (ältere Einträge: redaktion/verlauf/newsletter-2026-11-03.md) 2026-11-02 Till hat die Testmail von Hand in Ghost ausgelöst (11:41) und im Chat „N ja – einplanen“ gegeben → newsletter-text für Di 3.11. 7:05 (06:05Z) eingetragen (Fingerabdruck 3955a5e9…). Nächster Ghost-Lauf plant ein. · 2026-11-02 Lauf 12:47: in Ghost eingeplant für Di 3.11. 7:05 (06:05Z), Vorschau https://www.kleinmittelki.de/p/ba091482-a707-4fda-b51c-69955461cfd6/ · Till gemeldet (Mail 1a19be3873ddb3ea), A/B als Erinnerung. · 2026-11-03 Lauf 7:47/12:47: Newsletter laut Index versendet (sent), https://www.kleinmittelki.de/email/ba091482-a707-4fda-b51c-69955461cfd6/

### newsletter-2026-10-27
- Status: versendet
- Titel: „#4: KI-Ergebnisse prüfen und wer für den Chatbot haftet“ (Ersatz ohne Leitfaden: „#4: Wenn der Chatbot spricht, haftet der Betrieb“)
- Versand: Dienstag 27.10.2026, 7:05 (nach Tills „N ja“; 5 Minuten nach dem Leitfaden)
- Inhalt: 01 Leitfaden ki-ergebnisse-pruefen-leitfaden (nur wenn Till ihn bis Di 7:00 freigibt) · 02 olg-hamm-chatbot-haftung (live) · 03 Zahl „1 zu 365“ (OpenAI, 05.09.2025) · 04 Gedanke
- Datei: entwuerfe/newsletter-2026-10-27/beitrag.md, Prüfung: pruefung.md
- Freigegeben: Till per Mail 27.10. 01:06 („Ja Freigabe bitte einplanen.“, Antwort auf Fassung 2) → newsletter-text für Di 27.10. 7:05 (06:05Z) eingetragen. Früher: „N ja“ auf Fassung 2 (gemailt 25.10. abends, Verlauf 1a1725c28e258a9a). Leitfaden ist freigegeben und für Di 7:00 eingeplant; Fassung 2 passt Einstieg und Abschnitt 01 an die Tiger-Fassung an (Prüfer Runde 3, M1 umgesetzt). · Neu (25.10. abends): Der Ghost-Lauf schickt Fassung 2 als echte Ghost-Testmail an Till (ghost.py testmail). Fassung 2 ist schon gemailt; nach der Testmail nur ein Satz im Newsletter-Verlauf („Testmail ist da, „N ja“ gilt für Fassung 2“), keine Fassung 3.
- Verlauf: (ältere Einträge: redaktion/verlauf/newsletter-2026-10-27.md) 2026-10-27 Mail-Lauf (01:08): Tills Freigabe zu Fassung 2 (Fingerabdruck f436cb09…) über mailfreigabe.py eingetragen (Mail-ID 1a17aad89503bc70), Zeitpunkt Di 7:05; Ghost-Lauf außer der Reihe konnte nicht gestartet werden (Berechtigung); Till gebeten, ihn vor 7:00 von Hand auszuführen – der planmäßige Lauf 7:47 läge nach dem Versandtermin. · 2026-10-25 Sonntags-Lauf: Autor Entwurf, Prüfer Runde 1 nicht bestanden (T1–T3 Formulierungen, I1–I4 Ersatztexte/Freigabe-Reihenfolge), Runde 2 bestanden → newsletter-vorschlag. Mail-Lauf 10:17 schickt ihn Till. Nicht in Ghost. 2026-10-25 Mail-Lauf 10:17: Fassung 1 gemailt (Mail 1a1725c28e258a9a, Fingerabdruck d2fad333…), wartet auf Tills Antwort. · 2026-10-27 Ghost-Lauf (7:47): Newsletter laut Index versendet (sent), https://www.kleinmittelki.de/email/e8343e0e-f003-48de-98a4-721b5c80334a/

### ki-recherche-assistent-selbstversuch
- Status: wartet-auf-till
- Idee von Till (Chat 25.10.2026: Praxistest, wie er seinen automatisierten Recherche-Flow nach eigenen Kriterien aufgebaut hat, Ergebnis per Mail)
- Titel: „Mein KI-Rechercheassistent: Die KI sucht. Ich entscheide.“
- Rubrik/Kategorie: Praxistests / KI in der Praxis · Format: Praxistest · g1 Ablauf (vier Stufen) + HTML-Karten, Titelbild, Vorschaubild
- Quelle: eigene Systemunterlagen + Hilfeseiten OpenAI (Tasks), Microsoft (Scheduled prompts), Anthropic (Scheduled tasks), abgerufen 25.10.2026 – siehe quellen.md
- Warum für KMU: Prinzip übertragbar auf Ausschreibungen, Förderprogramme, Normen; fünf Schritte, Beispiel-Anfrage Malerbetrieb, drei Wege nach Ausstattung
- Wichtig (Till, Chat 25.10.2026): Der Beitrag zeigt nur die Recherche. Nichts darüber, dass KI Texte oder Beiträge schreibt – und auch nicht, dass Till selbst schreibt; das bleibt offen.
- Braucht von Till: Review mit Till am 03.11. (Prozess hat sich geändert), danach „A ja“ oder Änderungen
- Verlauf: (ältere Einträge: redaktion/verlauf/ki-recherche-assistent-selbstversuch.md) 2026-11-02 Chat (abends): Till: nicht Di 3.11.; Selbstversuch wird am 03.11. gemeinsam nochmals reviewt, weil sich der Prozess geändert hat · 2026-11-05 Lauf 7:47: im Briefing als A erinnert (Mail 1a1aa7c89c1cc391, „A ja“ = Di 10.11. 7:00); Review vom 03.11. nicht im Repo dokumentiert · 2026-11-09 Chat: Till will den Beitrag nächste Woche (Di 17.11., Newsletter #7) – keine Freigabe, Review weiter offen

### betriebsrat-ki-einfuehren
- Status: vorgeschlagen
- Titel (Arbeitstitel): „Ich will KI einführen. Muss ich den Betriebsrat fragen?“
- Rubrik/Kategorie: Wissen / Leitfäden
- Format: Anleitung, Variante „Rechtslage einfach erklärt“ (Vorbild „Muss ich KI-Bilder jetzt kennzeichnen?“), Box „Das Wichtigste in 30 Sekunden“, Prüfliste „Bevor das Werkzeug kommt“
- Quelle: Betriebsverfassungsgesetz §§ 80 Abs. 3, 87 Abs. 1 Nr. 6, 90 Abs. 1 Nr. 3, 95 Abs. 2a – **Original nicht gelesen** (https://www.gesetze-im-internet.de/betrvg/__90.html, Abruf im Lauf nicht freigegeben), Wortlaut **ungeprüft**. Selbst gelesen nur als Zweitquelle: CMS Hasche Sigle, „Einführung von KI im Unternehmen – Einbindung des Betriebsrats“ (18.07.2024), https://cms.law/de/deu/legal-updates/einfuehrung-von-ki-im-unternehmen-einbindung-des-betriebsrats. Gerichtsentscheidung zu ChatGPT über private Konten (ArbG Hamburg, Anfang 2024) nur aus Erinnerung, **ungeprüft** – Original suchen oder weglassen.
- Worum es geht: Laut CMS-Beitrag muss der Arbeitgeber den Betriebsrat rechtzeitig über geplante KI unterrichten und mit ihm über die Folgen für die Beschäftigten beraten (§ 90). Mitbestimmung greift, wenn das Werkzeug Verhalten oder Leistung überwachen kann, z. B. weil der Arbeitgeber Nutzungsdaten sieht (§ 87 Abs. 1 Nr. 6). Bei KI gilt ein Sachverständiger für den Betriebsrat als erforderlich (§ 80 Abs. 3), und KI bei Auswahlrichtlinien ist mitbestimmungspflichtig (§ 95 Abs. 2a). Alles am Gesetzestext prüfen, bevor es im Beitrag steht.
- Warum für KMU: Einen Betriebsrat kann es ab fünf Beschäftigten geben; in der Kernzielgruppe (20–150) ist er häufig. Inhaber und Geschäftsführer, die Copilot, ChatGPT-Team oder ein Transkriptionswerkzeug einführen wollen, wissen oft nicht, ob sie fragen müssen oder nur informieren. Ohne Betriebsrat gilt das alles nicht – das gehört offen in den ersten Absatz. Konkrete Prozesse: Lizenz für das ganze Büro kaufen, Besprechungen transkribieren, Bewerbungen vorsortieren. Keine Rechtsberatung.
- Unsere Idee: „Muss ich den Betriebsrat fragen?“ – vier Fälle (informieren, beraten, mitbestimmen, Sachverständiger) als Entscheidungsbaum mit einer Prüfliste, die ein Geschäftsführer vor dem ersten Gespräch durchgeht; verlinkt auf Schatten-KI, ki-kompetenz-pflicht-mitarbeiter und werkzeuge-besprechungsnotizen-datenschutz.
- Relevanz: 8/10 (Betroffenheit 2, Handlung 2, Quelle 1, Neuheit 2, Passung 1) – Quelle 1, bis der Gesetzestext selbst gelesen ist; Passung 1, weil Arbeitsrecht für Till neu ist und er keine Beratung anbieten will. Dublettencheck: Blog-Index und Board ohne Treffer zu Betriebsrat/BetrVG.
- Monatsrhythmus: Wissens-Puffer (Woche 2 oder 4, z. B. Di 24.11. oder 08.12.2026).
- Braucht von Till: Einschätzung in 2–3 Sätzen; ob das Thema für ihn passt (Arbeitsrecht). Eigene Erfahrung mit Betriebsrat nur, wenn er sie selbst liefert – sonst INTERN-Vorschlag.
- Verlauf: 2026-11-01 Ideen (Sonntags-Lauf): vorgeschlagen

### stellenanzeige-mit-ki-praxistest
- Status: vorgeschlagen
- Titel (Arbeitstitel): „Stellenanzeige per KI: Schreibt sie mir eine AGG-Falle?“
- Rubrik/Kategorie: Praxistests / KI in der Praxis
- Format: Praxistest (Serienkopf „Selbst ausprobiert“, 700–1.200 Wörter, Prompt-Kasten, Grenzen-Kasten, Transparenz-Absatz)
- Quelle: Tills eigener Test (steht aus). Rechtlicher Rahmen: § 11 AGG (Stellenausschreibung darf nicht gegen das Benachteiligungsverbot verstoßen) und § 15 AGG (Entschädigung) – **Original nicht gelesen, ungeprüft**. Seite der Antidiskriminierungsstelle des Bundes zu Arbeitgeberpflichten gefunden, Abruf im Lauf nicht freigegeben (https://www.antidiskriminierungsstelle.gov.de/EN/we-offer-advice-to-you/information_material_for_people_seeking_advice/overview_faq/faq_employer_obligations.html) – **ungeprüft**. Vor dem Schreiben: AGG-Wortlaut und eine ADS-Publikation zu Stellenanzeigen selbst lesen.
- Worum es geht: Till lässt eine KI Stellenanzeigen für typische KMU-Stellen schreiben und prüft sie mit einer Liste kritischer Formulierungen (Alter, Geschlecht, Herkunft, Sprache), die die Redaktion vorher aus Originalquellen zusammenstellt. Ergebnisse gibt es erst, wenn Till getestet hat.
- Warum für KMU: Personal suchen ist für Inhaber von Handwerks- und Dienstleistungsbetrieben (ca. 5–100 Beschäftigte, meist ohne Personalabteilung) Dauerthema, und Stellenanzeigen sind eine der ersten Aufgaben, die sie der KI geben. Eine unbedachte Formulierung („junges Team“, „Muttersprache Deutsch“) kann nach AGG Entschädigungsforderungen auslösen (ungeprüft, siehe Quelle). Einschränkung offen nennen: wenige Anzeigen, ein bis zwei Werkzeuge, keine Rechtsberatung.
- Unsere Idee: „Stellenanzeige per KI“ – ein Test, den jeder Betrieb mit der eigenen offenen Stelle nachmachen kann, plus ein Prompt-Satz, der das Risiko senkt (nur, wenn Tills Test das zeigt).
- Testaufbau (unter einer Stunde für Till):
  1. Redaktion liefert vorab (10 Min. Lesen): drei fiktive Stellenprofile (Geselle Elektro, Bürokraft Teilzeit, Azubi Anlagenmechaniker), einen Grund-Prompt, die Prüfliste aus Originalquellen und einen Zählbogen.
  2. Till lässt je Profil eine Anzeige in ChatGPT (optional Claude/Copilot) schreiben, je ein neuer Chat; Prompt bewusst ohne AGG-Hinweis, so wie ein Inhaber fragen würde: „Schreib eine ansprechende Stellenanzeige für … in unserem Familienbetrieb mit 25 Leuten.“ (ca. 20 Min.)
  3. Zweite Runde mit Zusatzsatz: „Achte darauf, dass die Anzeige niemanden wegen Alter, Geschlecht, Herkunft, Religion, Behinderung oder sexueller Identität benachteiligt.“ (ca. 15 Min.)
  4. Zählbogen (ca. 15 Min.): Treffer der Prüfliste je Anzeige und Runde, Screenshots sichern.
- Was der Leser danach tun kann: die eigene Anzeige mit derselben Prüfliste gegenlesen und den Zusatzsatz in den Prompt übernehmen – oder sehen, dass er nichts bringt.
- Relevanz: 8/10 (Betroffenheit 2, Handlung 2, Quelle 1, Neuheit 2, Passung 1) – Quelle 1, Ergebnis entsteht erst mit Tills Test, AGG-Rahmen noch ungeprüft; Passung 1, weil zweiter Praxistest neben angebot-aus-preisliste-praxistest (Till wählt). Dublettencheck: kein Recruiting-Beitrag im Index; „Wenn Azubis die KI fragen“ behandelt Sichtbarkeit, nicht Anzeigen – intern verlinken. Kein Handels-Beispiel.
- Monatsrhythmus: Praxistest-Woche 3 (Di 17.11.) als Alternative zur Preisliste oder Woche 4 (Di 24.11.2026).
- Braucht von Till: ja/nein zum Testaufbau, dann ca. 1 Stunde Test, Zählbogen, Screenshots, 2–3 Sätze Fazit.
- Verlauf: 2026-11-01 Ideen (Sonntags-Lauf): vorgeschlagen

### ki-agent-beeinflusst-entscheidungen
- Status: vorgeschlagen
- Hinweis aus ChatGPT (Eingang 2026-10-31, Punkt 1) – Original selbst gelesen, Zahlen geprüft
- Titel (Arbeitstitel): „Die KI hat eine Tendenz – und plötzlich ist es deine Entscheidung“
- Rubrik/Kategorie: Aktuell / Studien & Zahlen
- Format: Nachricht (ca. 300 Wörter, ca. 2 Min. Lesezeit), Kennzahl-Grafik „86 % der Analyseentscheidungen“ (Bezug: Entscheidungen, nicht Personen)
- Quelle: Anthropic Research, „How AI agents shape experts' judgment calls“, https://www.anthropic.com/research/agents-judgment-calls (27.10.2026)
- Worum es geht: In einem Experiment von Anthropic arbeiteten 50 Datenanalysten mit einem KI-Agenten, der verdeckt je Analyseschritt eine zufällige Tendenz vertrat. Sie folgten ihm in 86 % der Entscheidungen (Zufall: etwa 50 %); nur 15 % nannten den Agenten als Quelle ihrer Argumente.
- Warum für KMU: Wer als Inhaber oder Geschäftsführer (20–150 Leute) Preis-, Investitions- oder Personalfragen mit einem KI-Assistenten vorbereitet, übernimmt womöglich dessen Abwägung, ohne es zu merken. Einschränkung: Herstellerstudie, fiktiver Fall, Tendenz bewusst verstärkt, Teilnehmende waren Analysten, nicht Inhaber – die Übertragung ist unsere Ableitung.
- Unsere Idee: „Die KI hat eine Tendenz – und plötzlich ist es deine Entscheidung“ – Nachricht mit drei einfachen Gegenmitteln aus der Studie (erst eigene Meinung notieren, KI für jede Option das stärkste Argument liefern lassen, festlegen, welche Entscheidungen beim Menschen bleiben); verlinkt auf ki-ergebnisse-pruefen-leitfaden.
- Relevanz: 8/10 (Betroffenheit 1, Handlung 2, Quelle 2, Neuheit 1, Passung 2)
- Braucht von Till: Einschätzung in 2–3 Sätzen (z. B. ob er bei eigenen Entscheidungen erst selbst abwägt oder die KI zuerst fragt)
- Details: entwuerfe/ki-agent-beeinflusst-entscheidungen/quellen.md
- Verlauf: 2026-11-05 Scout: vorgeschlagen (Hinweis aus ChatGPT; Zweitverwertung the-decoder nicht verwenden) · 2026-11-05 Lauf 7:47: als 1 im Briefing gemailt (Mail 1a1aa7c89c1cc391)

### erste-ki-aufgabe-finden-selbsttest
- Status: vorgeschlagen
- Titel (Arbeitstitel): „Wo fange ich mit KI an? Ein Selbsttest: In 30 Minuten zur ersten Aufgabe im Betrieb“
- Rubrik/Kategorie: Wissen / Leitfäden
- Format: Anleitung (ca. 550 Wörter; H2 `Warum das gerade jetzt zählt` · `So machst du den Test` · `Worauf du bei den Antworten achtest` · `Ein Gedanke zum Mitnehmen`), eine Grafik: Auswahl-Raster „Wie oft? × Was kostet ein Fehler?“ (tools/grafik.py, Stufen wie im Prüf-Leitfaden)
- Quelle: keine neue externe Quelle nötig. Aufhänger nur mit bereits gelesenen Originalen: IAB-Pressemitteilung vom 20.10.2026 (88 % der Betriebe, die KI weder nutzen noch planen, sehen keine passende Anwendung; Selbstauskunft, IAB-Betriebspanel 2. Halbjahr 2025 – gelesen für `iab-betriebe-sehen-keine-ki-anwendung`) und Bitkom September 2026 (Einsatzfelder der KI-Anwender, ab 20 Beschäftigten – gelesen für den Lagebericht 21.09.). Methode ist eigene Redaktionsarbeit, keine Studie.
- Worum es geht: Der IAB-Entwurf endet mit dem Satz „eine Woche lang notieren, welche Büroaufgaben immer wiederkommen, und die häufigste ausprobieren“. Dieser Leitfaden macht daraus einen Selbsttest: wiederkehrende Aufgaben auflisten, je Aufgabe Häufigkeit, Minuten, Art der Daten (Kundendaten ja/nein) und Fehlerfolge notieren, mit dem Raster die erste Aufgabe wählen und mit dem Werkzeug testen, das der Betrieb schon hat.
- Warum für KMU: Inhaber und Büro in Betrieben mit 1–50 Beschäftigten ohne IT-Abteilung, die „keine Anwendung sehen“ oder nicht wissen, wo sie anfangen sollen. Konkrete Prozesse: Anfragen beantworten, Angebotstexte, Rückfragen, Protokolle, Stellenanzeigen. Bisher beantwortet kein Beitrag die Frage „Womit fange ich an?“ (Index geprüft). Einschränkung offen nennen: Methode zur Orientierung, kein Nachweis, dass sich die Aufgabe rechnet.
- Unsere Idee: „Wo fange ich mit KI an?“ – Selbsttest im Stil von „Frag eine KI nach deinem eigenen Unternehmen“ (20.09.), der den IAB-Befund in einen Schritt übersetzt; verlinkt auf iab-betriebe-sehen-keine-ki-anwendung, ki-ergebnisse-pruefen-leitfaden (Prüf-Stufen), nicht-jedes-problem-braucht-ki (wenn die einfachere Lösung reicht) und Schatten-KI (Werkzeug, das schon da ist). Kein Handels-Beispiel.
- Was der Leser danach tun kann: eine konkrete erste Aufgabe festlegen, Daten und Prüfaufwand vorher einschätzen, diese Woche einen Versuch machen.
- Relevanz: 9/10 (Betroffenheit 2, Handlung 2, Quelle 1, Neuheit 2, Passung 2) – Quelle 1, weil die Methode redaktionell ist und nur der Aufhänger auf Studien beruht; Passung 2: baut auf dem freigegebenen Prüf-Leitfaden und dem Selbsttest-Format auf, braucht keinen Test von Till. Dublettencheck: Index, Board, Themenspeicher, verlauf/ – kein Beitrag zum Einstieg; `kostenlose-ki-hilfe-fuer-betriebe` (Speicher) nennt Anlaufstellen, nicht die Aufgabe – gegenseitig verlinken.
- Monatsrhythmus: Wissens-Puffer für Di 17.11. (Woche 3; Praxistests ohne Ergebnisse, Fahrplan erlaubt dann den anderen Typ) oder Di 24.11. (Woche 4). Am besten nach der Veröffentlichung von `iab-betriebe-sehen-keine-ki-anwendung`.
- Braucht von Till: Einschätzung in 2–3 Sätzen. Eine eigene erste Aufgabe als Beispiel nur, wenn er sie selbst nennt – sonst bleibt das Beispiel fiktiv und als INTERN-Vorschlag markiert.
- Verlauf: 2026-11-08 Ideen (Sonntags-Lauf): vorgeschlagen

### status-quo-dezember-2026
- Status: vorgeschlagen
- Titel (Arbeitstitel): „KI im deutschen Mittelstand: Wo stehen wir im Dezember 2026?“ (Fortsetzung von „… im September 2026?“, 21.09.)
- Rubrik/Kategorie: Wissen / Lageberichte
- Format: Lagebericht (Serienkopf „Status Quo“, Ausgabe Dezember 2026; ca. 900 Wörter; Abschnitte 01 Verbreitung · 02 Anwendungen · 03 Integration · 04 Hürden · 05 Wirkung; je Abschnitt eine Kennzahl oder Balkengrafik; Box „Meine Einordnung“; „Quellen & Datenbasis“ mit Vergleichbarkeitshinweis)
- Quelle: bereits von der Redaktion am Original gelesen: IAB-Forum/IAB-Pressemitteilung (20.10.2026, Gründe der Nichtnutzung), Flash Eurobarometer 578 (14.10.2026, Hürden nach Größenklasse), TÜV-Verband/BSI-PM (07.10.2026, KI-gestützte Angriffe, ab 20 Beschäftigten), Anthropic Research (27.10.2026, nur als Randnotiz zu „Wirkung“). **Nicht lesbar in diesem Lauf (Netz gesperrt):** Destatis IKT-Erhebung 2026 (Tabelle KI nach Größenklassen; laut Suchtreffer erschien die Vorjahres-Pressemitteilung im November 2024 – ob es 2026-Werte gibt, ungeprüft), ifo-Umfrage „Mehr als die Hälfte der Unternehmen nutzt KI“ (05.06.2026, laut Suchtreffer 54,5 % – **ungeprüft, nicht verwenden, bevor das Original gelesen ist**), Bitkom-PM 02.11.2026 „Unternehmen wollen KI aus Deutschland“ (laut ChatGPT-Eingang 603 Unternehmen ab 20 Beschäftigten – ungeprüft).
- Worum es geht: Was sich seit September verändert hat: Gründe der Nichtnutzung (IAB), Hürden nach Betriebsgröße (Eurobarometer), neue Risiken (TÜV/BSI). Nur Zahlen aus gelesenen Originalen, verschiedene Grundgesamtheiten offen nebeneinander.
- Warum für KMU: Inhaber und Geschäftsführer 10–250 Beschäftigte, die ihren eigenen Stand einordnen wollen. Einschränkung: Selbstauskünfte, verschiedene Größengrenzen (IAB alle Betriebe, Bitkom/TÜV ab 20), Erhebungen teils ein Jahr alt.
- Unsere Idee: Prüfung des Analyst-Vorschlags „Lagebericht November als Hauptbeitrag“: **für Di 10.11. oder 17.11. passt er nicht** – Woche 1 im November ist vorbei, `iab-betriebe-sehen-keine-ki-anwendung` ist noch nicht veröffentlicht (der Lagebericht soll darauf verlinken, nicht ihn doppeln), die Rhythmus-Frage ist offen und die Destatis-Werte 2026 sind ungeprüft. **Stattdessen Ausgabe Dezember am Di 01.12.2026** (Woche 1): passt bei vierteljährlichem Rhythmus genau (September → Dezember), bei monatlichem ist November ohnehin verpasst. Ersetzt die Speicher-Idee `status-quo-november-2026`.
- Was der Leser danach tun kann: eigenen Stand an Verbreitung und Hürden messen und den nächsten Schritt wählen (Verweis auf `erste-ki-aufgabe-finden-selbsttest`).
- Relevanz: 8/10 (Betroffenheit 2, Handlung 1, Quelle 2, Neuheit 1, Passung 2) – Handlung 1, weil Orientierung statt Anleitung; Neuheit 1, weil Fortschreibung. Dublettencheck: einziger Lagebericht ist der vom 21.09.; IAB- und Eurobarometer-Beiträge nur zusammenfassen und verlinken.
- Monatsrhythmus: Hauptbeitrag Di 01.12.2026, 7:00 (Woche 1). Recherche-Schluss ca. 24.11.; vorher Destatis/ifo/Bitkom am Original lesen (Netzfreigabe nötig).
- Braucht von Till: ein Ja/Nein fürs Briefing: „Status Quo vierteljährlich – nächste Ausgabe Di 1.12., danach März 2027; Woche 1 sonst Wissen – ja/nein?“. Dazu 2–3 Sätze Einordnung (sonst Box „Meine Einordnung“ als INTERN-Vorschlag).
- Verlauf: 2026-11-08 Ideen (Sonntags-Lauf): vorgeschlagen (aus Themenspeicher `status-quo-november-2026`, Wochenbericht KW 44 geprüft)

### powerpoint-mit-ki-im-eigenen-design (Beitrag von Till, selbst in Ghost veröffentlicht)
- Status: veroeffentlicht
- Live: https://www.kleinmittelki.de/powerpoint-mit-ki-im-eigenen-design/
- Titel: „Dreimal dieselbe Präsentation mit KI – und nur eine sieht nach KI aus“
- Rubrik/Kategorie: Praxistests / KI in der Praxis · Format: Praxistest („Selbst ausprobiert“)
- Herkunft: Ghost-Entwurf 44ce46b5-… (F1 im Briefing 05.11.), von Till am 06.11.2026 10:06 selbst veröffentlicht; nicht über die Redaktion, keine Freigabe in freigaben.jsonl nötig. Text: redaktion/referenz/powerpoint-mit-ki-im-eigenen-design.html
- Verlauf: 2026-11-08 Lauf 7:47: im Index als veröffentlicht gefunden, im Board nachgetragen, Fahrplan als Ausnahme vermerkt; als 01 in Newsletter #6 (Entwurf) · 2026-11-08 Social (Sonntags-Lauf): Paket vorbereitet (entwuerfe/powerpoint-mit-ki-im-eigenen-design/social.md: WhatsApp-Status Di 10.11., LinkedIn Do 12.11., Karussell 7 Folien; LinkedIn-Vorrat danach Do 19.11. nicht-jedes-problem, Do 26.11. eurobarometer). Social: vorbereitet, wartet auf Till. Nichts gepostet.

### ki-vorlagen-fuers-team
- Status: vorgeschlagen
- Titel (Arbeitstitel): „Einmal gut erklären statt jeden Tag neu prompten: Gemeinsame KI-Vorlagen fürs Team“
- Rubrik/Kategorie: Wissen / Leitfäden
- Format: Anleitung (ca. 550 Wörter; H2 `Warum das gerade jetzt zählt` · `So machst du den Test` · `Worauf du bei den Antworten achtest` · `Ein Gedanke zum Mitnehmen`), eine Grafik: „Was in eine Vorlage gehört“ (Auftrag · Ton · feste Fakten · Prüfregel), tools/grafik.py.
- Quelle: Claude Help Center „What are projects?“ (https://support.claude.com/en/articles/9517075-what-are-projects, abgerufen 15.11.2026, Seite ohne Datum) – **gelesen**: Projekte haben eigene Chat-Verläufe, Wissensbasis (hochgeladene Dateien) und eigene Anweisungen; auf allen Tarifen, Free bis fünf Projekte; Teilen mit der Organisation nur in Team und Enterprise (Rechte „ansehen“/„bearbeiten“). Claude Help Center „Understanding Claude's personalization features“ (https://support.claude.com/en/articles/10185728, „Updated over 3 weeks ago“) – gelesen: Konto-Anweisungen, Projekt-Anweisungen, Skills. **Nicht lesbar (Proxy 403/DNS):** OpenAI Help Center zu eigenen GPTs/Projekten (help.openai.com), Google Workspace Updates „Skills in Workspace“ (workspaceupdates.googleblog.com, 10.11.2026, nur als ChatGPT-Eingang vom 11.11. bekannt, ungeprüft). Ohne diese beiden Originale nur Claude konkret nennen oder Abschnitt neutral halten („die meisten Werkzeuge haben eine solche Funktion“ erst nach Prüfung).
- Worum es geht: In vielen Betrieben schreibt jede Person ihren eigenen Prompt für dieselbe wiederkehrende Aufgabe (Angebotsbegleittext, Antwort auf Terminanfragen, Reklamation). Werkzeuge bieten dafür gemeinsame Vorlagen mit festen Anweisungen und hinterlegten Dateien. Der Leitfaden zeigt, wie ein Betrieb für **eine** Aufgabe eine Vorlage baut, mit zwei Kollegen testet und eine Prüfregel hineinschreibt.
- Warum für KMU: Büro, Innendienst und Geschäftsführung in Betrieben mit 5–50 Beschäftigten, die schon ein Team-Werkzeug haben (Anschluss an „Mit Kanonen auf Spatzen“: dort „Standardmodell festlegen“). Konkreter Prozess: gleiche Kundenanfrage, gleicher Ton, gleiche Pflichtangaben. Einschränkung offen: Teilen nur in Team-/Firmentarifen; eine Vorlage ersetzt nicht das Prüfen (Verweis Prüf-Leitfaden); keine Kundendaten in die Wissensbasis, bevor geklärt ist, was erlaubt ist (Verweis `kundendaten-in-ki-datenschutz`, Speicher). Kein Nachweis, dass Vorlagen Zeit sparen – nicht behaupten.
- Unsere Idee: „Gemeinsame KI-Vorlagen fürs Team“ – keine Funktionsliste (Tills NEIN vom 12.10. zur Copilot-Funktionsgrafik), sondern ein Selbsttest: Aufgabe wählen, Vorlage in vier Bausteinen schreiben, dieselbe Anfrage von zwei Leuten durchlaufen lassen, Unterschiede prüfen. Verlinkt auf modellwahl-kanonen-auf-spatzen, ki-ergebnisse-pruefen-leitfaden, erste-ki-aufgabe-finden-selbsttest (Board) und Schatten-KI.
- Was der Leser danach tun kann: in 30–45 Minuten eine erste gemeinsame Vorlage anlegen und festlegen, wer sie pflegt.
- Relevanz: 8/10 (Betroffenheit 2, Handlung 2, Quelle 1, Neuheit 2, Passung 1) – Quelle 1: nur Hersteller-Hilfeseiten, nur von einem Anbieter gelesen; Passung 1: Nähe zu Herstellerfunktionen, deshalb strikt als Vorgehen, nicht als Produkt. Dublettencheck: Index (36), Board, Speicher, verlauf/ – kein Beitrag zu gemeinsamen Vorlagen; Modellwahl-Beitrag nennt nur das Standardmodell.
- Monatsrhythmus: Wissens-Puffer für Di 24.11. (Woche 4, frei) oder als zweiter Puffer neben `erste-ki-aufgabe-finden-selbsttest`.
- Braucht von Till: Einschätzung in 2–3 Sätzen; ob er selbst Projekte/Vorlagen nutzt (nur wenn er es sagt, sonst bleibt das Beispiel fiktiv und INTERN markiert). Netzfreigabe für help.openai.com und workspaceupdates.googleblog.com, falls ChatGPT und Gemini mit rein sollen.
- Verlauf: 2026-11-15 Ideen (Sonntags-Lauf): vorgeschlagen

### ki-ansprechpartner-im-betrieb
- Status: vorgeschlagen
- Titel (Arbeitstitel): „Wer kümmert sich bei uns eigentlich um KI? Fünf Aufgaben für einen Ansprechpartner im Betrieb“
- Rubrik/Kategorie: Wissen / Leitfäden
- Format: Anleitung (ca. 550 Wörter) mit Prüfliste (HTML-Karte aus dem Baukasten), eine Grafik: fünf Aufgaben als Karten. Wenn es länger wird: Langtext-Variante mit Box „Das Wichtigste in 30 Sekunden“.
- Quelle: keine neue externe Quelle nötig; Aufhänger nur aus Originalen, die die Redaktion schon gelesen hat und die im Index stehen: IW Köln „Schatten-KI“ (https://www.iwkoeln.de/studien/barbara-engels-andrea-hammermann-schatten-ki-beschaeftigte-sind-schneller-als-ihre-betriebe.html; 29,1 % der beruflichen KI-Nutzer verwenden nicht bereitgestellte Anwendungen, in Betrieben unter 50 Beschäftigten 33,5 % – Zahlen aus dem veröffentlichten Beitrag vom 21.09., **in diesem Lauf nicht neu am Original geprüft**) und Flash Eurobarometer 578 (14.10.2026, fehlendes Wissen als Hürde, gelesen für den Beitrag vom 25.10.). Die fünf Aufgaben sind redaktionelle Arbeit, keine Studie – offen sagen.
- Worum es geht: In Betrieben ohne IT-Abteilung ist KI oft niemandes Aufgabe. Der Leitfaden beschreibt eine schlanke Rolle ohne neue Stelle: (1) Liste der erlaubten Werkzeuge und Konten pflegen (Schatten-KI), (2) Standardmodell und gemeinsame Vorlagen festlegen (Modellwahl-Beitrag, `ki-vorlagen-fuers-team`), (3) Prüfstufen je Aufgabe festhalten (Prüf-Leitfaden), (4) Fragen und Fehler im Team sammeln, (5) Pflichten im Blick behalten (KI-Kompetenz/AI Act, Betriebsrat – beides Board, erst verlinken, wenn veröffentlicht).
- Warum für KMU: Geschäftsführer und Inhaber in Betrieben mit 10–150 Beschäftigten, in denen schon einzelne Leute KI nutzen. Rolle: eine Person aus Büro oder Fachabteilung, nicht zwingend IT. Einschränkung offen: kein Zeitbudget und keine Wirkung belegbar – keine Stundenzahl nennen, der Betrieb legt den Umfang selbst fest; bei Betriebsrat Verweis auf `betriebsrat-ki-einfuehren`.
- Unsere Idee: „Wer kümmert sich bei uns um KI?“ – ein Sammelpunkt, der die bisherigen Wissensbeiträge zu einer Aufgabenliste verbindet und intern verlinkt, statt neue Behauptungen aufzustellen. Kein Beratungs-CTA, keine Schulungsangebote.
- Was der Leser danach tun kann: eine Person benennen, ihr die fünf Aufgaben geben und den ersten Punkt (Werkzeugliste) diese Woche erledigen.
- Relevanz: 8/10 (Betroffenheit 2, Handlung 2, Quelle 1, Neuheit 2, Passung 1) – Quelle 1: Aufhänger aus bereits gelesenen Studien, Methode redaktionell; Passung 1: hängt teils an Board-Themen, die noch nicht veröffentlicht sind. Dublettencheck: Index, Board, Speicher – `ki-kompetenz-pflicht-mitarbeiter` behandelt die Schulungspflicht, nicht die Zuständigkeit; gegenseitig verlinken.
- Monatsrhythmus: Wissens-Puffer für Dezember (Di 08.12., Woche 2) – nach `ki-vorlagen-fuers-team`, damit die Verlinkung trägt.
- Braucht von Till: Einschätzung in 2–3 Sätzen (passt die Rolle zu dem, was er in Betrieben sieht?). Eigene Erfahrungen nur, wenn er sie selbst nennt.
- Verlauf: 2026-11-15 Ideen (Sonntags-Lauf): vorgeschlagen

### monatszahlen-mit-ki-pruefen-praxistest
- Status: vorgeschlagen
- Titel (Arbeitstitel): „Monatszahlen mit KI durchsehen: Findet sie die drei Fehler, die wir versteckt haben?“
- Rubrik/Kategorie: Praxistests / KI in der Praxis
- Format: Praxistest (700–1.200 Wörter), Prompt-Kasten, Grenzen-Kasten, anonymisierte Screenshots der Tabelle und der Antworten
- Quelle: keine externe Quelle nötig (eigener Test). Aufhänger optional Tills eigener Entwurf `pwc-mittelstand-ki-controlling` (PwC-Befragung, Zahlen dort am Original belegt; im Controlling haben laut Entwurf 43 % sich noch nicht mit KI befasst, nur 10 % KI eingebunden) – nur verlinken, wenn er veröffentlicht ist.
- Worum es geht: Ein Test, ob ChatGPT oder Claude in einer Monatsübersicht (Kosten nach Kostenstellen, 12 Monate) gezielt eingebaute Auffälligkeiten findet, ohne andere zu erfinden, und ob ein daraus geschriebener Kurzbericht die richtigen Zahlen nennt.
- Warum für KMU: Inhaber, Geschäftsführer und die Person für Buchhaltung/Controlling in Betrieben mit 20–150 Beschäftigten, die monatlich eine BWA oder Kostenliste aus dem Steuerbüro oder der Buchhaltung bekommen und sie mangels Zeit nur überfliegen. Einschränkung offen: fiktive Daten, ein Werkzeug, eine Person – kein Urteil über KI im Controlling insgesamt.
- Unsere Idee: Fortsetzung von Tills eigener These „der Hebel liegt im Controlling“ als Selbstversuch: nicht „Was sagt eine Studie?“, sondern „Was findet die KI in meinen Zahlen – und was erfindet sie?“.
- Testaufbau (unter einer Stunde, für Till): Redaktion liefert eine fiktive Excel-Datei (ca. 8 Kostenarten × 12 Monate, keine echten Firmendaten) mit drei eingebauten Auffälligkeiten und einer Soll-Liste nur für Till: (a) eine doppelt erfasste Rechnung, (b) ein Monatswert mit vertauschten Ziffern, (c) ein Kostensprung in einer Kostenart. Schritt 1 (ca. 15 Min.): Datei hochladen (nicht einfügen – passt zum Hinweis im Modellwahl-Beitrag), Prompt „Was fällt dir in diesen Zahlen auf? Nenne Monat, Kostenart und Betrag.“ Schritt 2 (ca. 10 Min.): „Schreib mir einen Monatsbericht für März in fünf Sätzen.“ Schritt 3 (ca. 20 Min.): Zählbogen: gefunden / übersehen / erfunden; im Bericht jede Zahl gegen die Tabelle prüfen. Zwei Screenshots, 2–3 Sätze Fazit.
- Was der Leser danach tun kann: die eigene Monatsliste mit demselben Prompt durchsehen lassen und wissen, welche Antworten er gegen die Tabelle prüfen muss (Verweis Prüf-Leitfaden, Stufe „gezielt prüfen“).
- Abgrenzung: `ki-unternehmenszahlen-data-agent` (Nachricht über ein Herstellerwerkzeug, kein Test), `preisrunde-mit-ki-praxistest` (Preise neu berechnen, nicht Auffälligkeiten finden), `angebot-aus-preisliste-praxistest` (erfundene Positionen im Angebot), Speicher `gleiche-frage-fuenfmal-praxistest` (Schwankung). Gegenseitig verlinken.
- Relevanz: 9/10 (Betroffenheit 2, Handlung 2, Quelle 1, Neuheit 2, Passung 2) – Quelle 1: eigener Test, keine externe Zahl; Passung 2: knüpft an Tills eigenen Controlling-Entwurf und an seine bisher freigegebenen Selbstversuche (Präsentation, Preisrunde) an, kein Regulierungsthema.
- Monatsrhythmus: Praxistest-Woche Di 15.12. (Woche 3) oder später; höchstens ein „Selbst ausprobiert“ pro Woche (Regel 09.11.).
- Braucht von Till: Ja/Nein, ca. 45 Min. Test mit der vorbereiteten Datei, Zählbogen, Screenshots, 2–3 Sätze Fazit. Ergebnisse nur von Till, Platzhalter `[TILL: Ergebnis eintragen]` bis dahin.
- Verlauf: 2026-11-22 Ideen (Sonntags-Lauf): vorgeschlagen
### ki-zugaenge-im-team-verteilen
- Status: vorgeschlagen
- Titel (Arbeitstitel): „Wer im Team braucht welchen KI-Zugang? Eine Lizenz-Inventur in 30 Minuten“
- Rubrik/Kategorie: Wissen / Leitfäden
- Format: Anleitung (ca. 550 Wörter), Abschnitte nach Anleitungs-Format, eine HTML-Karte (Inventur-Tabelle: Person · Aufgaben pro Woche · Zugang heute · Zugang künftig)
- Quelle: Claude-Preisseite https://claude.com/pricing (gelesen 15.11. und erneut 22.11.2026): Team-Tarif „For teams of 2 to 150“, Standard-Platz 20 $/Monat bei Jahreszahlung bzw. 25 $ monatlich, Premium-Platz 100 $ bzw. 125 $ mit „5x more usage than standard seats“, „Mix and match seat types“; Währung nur „$“, ohne Steuer. ChatGPT-, Copilot- und Gemini-Preisseiten **nicht gelesen** – bis dahin nur als Beispiel eines Anbieters, kein Vergleich. Ob die Admin-Ansicht Nutzung je Person für Chat zeigt, **ungeprüft**: gelesen wurde nur die Hilfeseite zur Claude-Code-Nutzungsanalyse (support.claude.com, „Updated over 3 weeks ago“, Abruf 22.11.2026), die je Person nur Code-Zeilen nennt.
- Worum es geht: Betriebe, die schon zahlen, geben oft allen denselben Zugang oder kaufen Plätze, die kaum genutzt werden. Eine kurze Inventur zeigt, wer täglich mit KI arbeitet, wer gelegentlich, wer gar nicht – und welche Platzart (oder ob überhaupt einer) dazu passt.
- Warum für KMU: Geschäftsführer und Büroleitung in Betrieben mit 20–150 Beschäftigten, die 5–50 KI-Plätze bezahlen. Direkt aus Tills Linie „Firmen ansprechen, die KI schon nutzen“ (Modellwahl-Beitrag, 13.11.). Einschränkung offen: keine Erhebung, wie viele Plätze ungenutzt sind – keine Zahl dazu erfinden; Rechenbeispiel nur mit gelesenen Listenpreisen und Stand-Datum.
- Unsere Idee: drei Fragen je Person (Wofür nutzt du KI pro Woche? Stößt du an Grenzen? Was würdest du ohne vermissen?), daraus vier Gruppen: großer Bedarf (mehr Kapazität), Standard, gelegentlich (Zugang teilen nur wo der Anbieter das erlaubt – Nutzungsbedingungen vorher lesen, sonst weglassen), kein Bedarf. Verlinkt Modellwahl, Schatten-KI (wer ohne Zugang trotzdem nutzt), `ki-vorlagen-fuers-team` und `ki-ansprechpartner-im-betrieb`.
- Was der Leser danach tun kann: die Tabelle diese Woche ausfüllen und bei der nächsten Verlängerung Plätze umschichten statt pauschal verlängern.
- Abgrenzung: Speicher-Idee „Was kostet KI einen 15-Personen-Betrieb im Jahr?“ (Gesamtkosten, Vergleich vier Anbieter, blockiert bis alle Preise gelesen) – hier geht es um die Verteilung im eigenen Betrieb, kein Anbietervergleich. Modellwahl-Beitrag: welches Modell je Aufgabe; hier: welcher Zugang je Person.
- Relevanz: 8/10 (Betroffenheit 2, Handlung 2, Quelle 1, Neuheit 2, Passung 1) – Quelle 1: nur ein Anbieter am Original gelesen; Passung 1: nah an Tills Modellwahl-Idee, aber ungeprüft, ob er Lizenzfragen für Leser relevant hält.
- Monatsrhythmus: Wissens-Puffer für Do 26.11./Di 08.12. – kommt ohne Tills Test aus.
- Braucht von Till: Einschätzung in 2–3 Sätzen (Ist ungleiche Nutzung im Team das, was er in Betrieben sieht?). Eigene Erfahrungen nur, wenn er sie nennt. Netzfreigabe für die Preisseiten von OpenAI, Microsoft, Google, falls ein zweites Beispiel gewünscht ist.
- Verlauf: 2026-11-22 Ideen (Sonntags-Lauf): vorgeschlagen

## Archiv

(noch leer)
