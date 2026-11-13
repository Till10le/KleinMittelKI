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
- Verlauf: (ältere Einträge: redaktion/verlauf/modellwahl-kanonen-auf-spatzen.md) 2026-11-12 Chat später: Screenshots waren privat, nicht Business; Till wählt neutrale Formulierung, INTERN raus (archiviert in quellen.md), Schluss-Einschätzung auf Tills Wunsch von der Redaktion formuliert; Runde 5 bestanden; Ghost-Entwurf aktualisiert; offen: nur „C ja“ (Termin Do 19.11. 7:00) · 2026-11-12 Chat: Till „bitte morgen 07:00 veröffetlichen“ → Freigabe eingetragen, in Ghost eingeplant Fr 13.11. 7:00 (06:00Z) · 2026-11-13 Lauf 7:47: veröffentlicht 7:00 (Ghost published_at 06:00Z), https://www.kleinmittelki.de/modellwahl-kanonen-auf-spatzen/; Till per Mail gemeldet; Social-Paket im Sonntags-Teil

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
- Verlauf: (ältere Einträge: redaktion/verlauf/iab-betriebe-sehen-keine-ki-anwendung.md) 2026-11-09 Lauf 12:47: Vorschau (Stand 08:33:51) als B gemailt (1a1c024b6f48189f), Termin Di 10.11. 7:00; „B ja“ offen · 2026-11-09 Lauf 18:47: „B ja“ (Mail 1a1c0666e55205d8, 14:01) → Freigabe eingetragen, in Ghost eingeplant für Di 10.11. 7:00 (06:00Z) · 2026-11-10 Lauf 12:47: veröffentlicht Di 10.11. 7:00 (Ghost published_at 06:00Z) → https://www.kleinmittelki.de/iab-betriebe-sehen-keine-ki-anwendung/

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
- Status: vorgeschlagen
- Titel (Arbeitstitel): Neue Produkthaftung für Software und KI ab 9.12.2026
- Rubrik/Kategorie: Wissen / Leitfäden
- Format: Langtext
- Quelle: Richtlinie (EU) 2024/2853 (EUR-Lex, CELEX 32024L2853) – **Original nicht gelesen** (Abruf nicht möglich); Frist 9.12.2026 nur aus Zweitquellen (IHK Frankfurt, Heuking), **ungeprüft**. Deutsches Umsetzungsgesetz: Stand widersprüchlich (Abstimmung 08.10.2026 vs. Rechtsausschuss), BT-Drs.-Nummer 21/4297 ungeprüft. → überholt 2026-10-19: Gesetzesbeschluss BR-Drs. 584/26 gelesen, https://dserver.bundestag.de/brd/2026/0584-26.pdf (Bundestag 08.10.2026; Bundesrat steht aus)
- Warum für KMU: Betriebe, die Software oder KI-Funktionen in Produkte einbauen oder anbieten. Reine Anwender von Standard-KI vermutlich nicht betroffen (ungeprüft).
- Relevanz: vorläufig 8/10 (Betroffenheit 1, Handlung 2, Quelle 1, Neuheit 2, Passung 2) – Frist beachten; Aussagen zum deutschen Recht erst nach Klärung des Gesetzesstands
- Braucht von Till: Einschätzung
- Details: entwuerfe/eu-produkthaftung-software-ki/quellen.md
- Verlauf: (ältere Einträge: redaktion/verlauf/eu-produkthaftung-software-ki.md) 2026-10-19 Scout (Redaktions-Lauf): **Gesetzesstand geklärt aus Original** – BR-Drs. 584/26 gelesen: Bundestag hat Drs. 21/4297 am 08.10.2026 beschlossen (Beschlussempfehlung 21/8429); Bundesrat-Frist 30.10.2026, Verkündung steht aus; Inkrafttreten 9.12.2026; altes Recht für Produkte bis einschl. 8.12.2026 (§ 23). Software ist Produkt (§ 2 Abs. 1 Nr. 3), Begriff „KI“ kommt im Gesetz nicht vor. Richtlinie: EUR-Lex nur Metadaten (23.10.2024, in Kraft 8.12.2024); Art. 2, 4, 8 aus Amtsblatt-Kopie eines Dritten gelesen, gegen EUR-Lex gegenlesen; Art. 12/22 nicht gelesen. Relevanz neu: 9/10 (Betroffenheit 1, Handlung 2, Quelle 2, Neuheit 2, Passung 2). Bundestagsbeschluss ist ein aktueller Anlass; ggf. zusätzlich kurze Nachricht nach Bundesrat. · 2026-10-19 Scout (Test 2): amtliches EUR-Lex-PDF (DE) gelesen – Art. 2 Abs. 1/2, Art. 4 Nr. 1, Art. 8 Abs. 1/2 bestätigt. Art. 12, 21, 22 (Umsetzungsfrist), 23 weiter nicht lesbar (Abruf bricht ab), ungeprüft. Relevanz bleibt 9/10. · 2026-10-23 Scout: **Bundesrat hat entschieden** – BR-Drs. 584/26(B) gelesen, https://dserver.bundestag.de/brd/2026/0584-26B.pdf: 1069. Sitzung am **16.10.2026**, kein Antrag nach Art. 77 Abs. 2 GG (Vermittlungsausschuss nicht angerufen), keine Entschließung. Gesetz damit zustande gekommen; Ausfertigung/Verkündung im BGBl. noch nicht gefunden (ungeprüft). Inkrafttreten 9.12.2026 laut Gesetzesbeschluss (BR-Drs. 584/26). Aktueller Anlass für eine kurze Nachricht oder als Einstieg in den Leitfaden.

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

## Archiv

(noch leer)
