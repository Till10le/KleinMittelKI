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

### iab-betriebe-sehen-keine-ki-anwendung
- Status: wartet-auf-till
- Idee von Till (Chat 23.10.2026, zwei fertige Entwürfe „Gelesen & eingeordnet“ aus einem anderen Werkzeug; Till: „Ja bitte beide Beiträge als Entwürfe anlegen. Perfekt für KMK machen!“)
- Titel: „Fast 90 Prozent der Betriebe ohne KI sehen keinen Einsatz. Vielleicht suchen sie an der falschen Stelle.“ (Till, Chat 24.10.2026; vorher „Ein Bäcker braucht keine KI …“ – gefiel ihm nicht)
- Rubrik/Kategorie: Aktuell / Studien & Zahlen · Format: Nachricht · eine Grafik (Potenzial vs. Nutzung, nur Zahlen aus der IAB-Pressemitteilung)
- Quelle: https://iab-forum.de/weshalb-die-meisten-betriebe-kuenstliche-intelligenz-noch-nicht-nutzen/ (20.10.2026) + IAB-Pressemitteilung (idw)
- Warum für KMU: Kleinbetriebe (Handwerk, Bäckerei) suchen KI im Kerngeschäft statt bei Büroaufgaben
- Braucht von Till: Einschätzung in 2–3 Sätzen oder Freigabe des Vorschlags
- Vorschlag „Eine Zahl, genau gelesen“: zahl „88 %“ · text „der Betriebe ohne KI sehen dafür keine passende Anwendung.“ · genau „Gemeint sind nur Betriebe, die KI weder nutzen noch planen – im zweiten Halbjahr 2025 zwei Drittel aller Betriebe. Selbstauskunft. Quelle: IAB, Oktober 2026.“ · link: Beitrag nach Veröffentlichung. Ändern nur nach Freigabe (Code-Injection, nicht per API).
- Reihenfolge: vor nicht-jedes-problem-braucht-ki veröffentlichen
- Verlauf: 2026-10-23 Chat: Till „Ja“ → freigegeben · Autor/Grafik/Prüfung im Chat-Lauf, Einzelwerte aus Zweitverwertung bewusst weggelassen → geprueft (Sofortstart Ghost-Lauf blockiert, nächster regulärer Lauf So 7:47) · 2026-10-24 Chat: Till will neuen Titel, wählt „Fast 90 Prozent … an der falschen Stelle.“ → Titel, Teaser (wiederholte sonst die Überschrift) und Vorschaubild neu · 2026-10-25 Ghost-Lauf (7:47): Entwurf in Ghost angelegt, Vorschau: https://www.kleinmittelki.de/p/49d77d59-3984-4501-99d4-d71e1b0198c1/

### nicht-jedes-problem-braucht-ki
- Status: wartet-auf-till
- Idee von Till (Chat 23.10.2026, siehe oben)
- Titel: „Nicht jedes Problem braucht KI. Manchmal reicht die einfachere Lösung.“ (Tills Titel, leicht gekürzt)
- Rubrik/Kategorie: Aktuell / Entwicklungen · Format: Nachricht · eine Grafik (Stufenmodell, eigene Darstellung)
- Quelle: https://www.infoworld.com/article/4230874/dont-buy-a-consultants-ai-framework.html (06.10.2026, Original; Computerwoche 16.10. ist Übersetzung) + Fraunhofer HNFIZ (02.10.2026)
- Warum für KMU: Hausverwaltung/Kleinbetrieb – einfachste ausreichende Lösung vor KI-System
- Braucht von Till: Einschätzung in 2–3 Sätzen oder Freigabe des Vorschlags
- Nach Veröffentlichung des IAB-Beitrags: Querverweis darauf ergänzen
- Verlauf: 2026-10-23 Chat: Till „Ja“ → freigegeben · Autor/Grafik/Prüfung im Chat-Lauf → geprueft, Ghost-Lauf angestoßen · 2026-10-25 Ghost-Lauf (7:47): Entwurf in Ghost angelegt, Vorschau: https://www.kleinmittelki.de/p/e41facba-959c-42e3-bf18-7b13fad14cc9/

### ki-ergebnisse-pruefen-leitfaden
- Status: geprueft
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
- Verlauf: 2026-10-23 Till im Chat: „Ja“ → freigegeben, Express-Lauf gestartet · Entwurf 12:47 in Ghost · 2026-10-23 Till schickt eigene Beispiele → zurueck, Express-Lauf · 2026-10-23 Autor (Express-Lauf): Langtext geschrieben, ca. 1.910 Wörter, entwuerfe/ki-ergebnisse-pruefen-leitfaden/beitrag.md + quellen.md. Selbst gelesen: OpenAI „Why language models hallucinate“ (05.09.2025), OpenAI-Hilfeseite „Does ChatGPT tell the truth?“, OWASP LLM09:2025 Misinformation, Anthropic-Doku „Reduce hallucinations“. Ungeprüft/nicht verwendet: BSI-PDF (nicht lesbar), OpenAI-Benchmarkzahlen, OWASP-Beispielfälle, LinkedIn-Beitrag (nur als Anstoß genannt). OLG-Hamm-Urteil selbst nicht abrufbar (robots), nur INTERN-Hinweis zum Verlinken. „Meine Einschätzung“ INTERN-Vorschlag, [TILL: eigene Erfahrung] offen. Fünf [GRAFIK]-Platzhalter (Raten 1 zu 365, Exposé-Vergleich, drei Stufen schwarz/lime, Beispiele-Tabelle optional, Checkliste fünf Regeln); Vorschaubild fehlt noch. · 2026-10-23 Grafik (Express-Lauf): 4 Schaubilder eingebunden (kmk-ki-pruefen-g1 Raten 0 Punkte vs. 1 zu 365, Quelle OpenAI 05.09.2025 · g2 Exposé Vermutung → Tatsache · g3 drei Stufen nur Schwarz/Lime · g5 Checkliste fünf Regeln), je mit -social.png; optionale Beispiele-Tabelle (Nr. 4) weggelassen, weil sie nur die vier Absätze wiederholt und der Beitrag sonst überladen wäre. Vorschaubild 1200 × 630 (vorschaubild.png, Kategorie „Leitfäden“). Alle Bilder angesehen, lexical.py fehlerfrei. Hinweis: INTERN-Absatz nennt noch „fünf Platzhalter [GRAFIK: …]“ – beim Entfernen des INTERN-Absatzes erledigt. · 2026-10-23 Prüfer Runde 1: NICHT BESTANDEN (pruefung.md). Quellen selbst gelesen (OpenAI Blog + Help, OWASP LLM09, Anthropic-Doku): Zahlen/Zitate korrekt. Mängel Autor: A1 INTERN-Absatz nennt veraltete GRAFIK-Platzhalter · A2 „neuer Chat/zweimal“ steht nicht in Anthropic-Doku · A3 „stützen sich auf“ gilt nicht für Regel 4/5 · A4 „ehrlich gesagt“ streichen. Mängel Grafik: G1 g2-Merksatz „nichts erfunden“ widerspricht „komplett saniert“ · G2 g5-Fußzeile Quellen → „eigene Zusammenstellung, u. a. nach …“ · G3 g2 ohne Stand · G4 Bildunterschrift g1 zwei Sätze. lexical.py fehlerfrei. · 2026-10-23 Prüfer Runde 2: BESTANDEN (pruefung.md). A1–A4 und G1–G4 umgesetzt, g2/g5 (+social) angesehen, lexical.py fehlerfrei. Offen für Till: [TILL: …], INTERN-Vorschläge, LinkedIn-Anlass, OLG-Hamm-Link nach Veröffentlichung. · 2026-10-23 Express-Lauf (Chefredakteur): Prüfer Runde 2 bestanden → geprueft; Ghost-Lauf angestoßen. · 2026-10-23 Ghost-Lauf (12:47): Entwurf in Ghost angelegt, Vorschau: https://www.kleinmittelki.de/p/3aa0ec3b-67f5-440d-9514-2a9509cbbfd0/ · 2026-10-23 Autor (Überarbeitung): Tills drei Fälle eingebaut (Steckachse ohne Behauptung „passte nicht“, Excel als Kernbeispiel + „Zum Ausprobieren: eine Kalkulation nachrechnen“, Selbst-Audit → Regel 4), [TILL] ersetzt, „Meine Einschätzung“ nur aus Tills Sätzen, Prompt-Kasten wörtlich, Malerbetrieb/Hausverwaltung gestrichen (Exposé/Speisekarte bleiben), Rechnungen mit python3 nachgerechnet, quellen.md Abschnitt 6. Ca. 2.100 Wörter (ohne Quellen). Schaubilder g1, g2, g3, g5 bleiben; neu ein [GRAFIK]-Platzhalter Excel 28,50 vs. 285 €. lexical.py fehlerfrei. → Grafik, dann Prüfer. · 2026-10-23 Express-Lauf (Chefredakteur, ~12:20): Überarbeitung mit Tills drei Fällen – Autor (Steckachse, Excel-Kernbeispiel + „Zum Ausprobieren“, Selbst-Audit → Regel 4; „Meine Einschätzung“ aus Tills Sätzen, kein INTERN mehr dafür), Grafik (neu g4 Excel 28,50 vs. 285 €, g5 Regeln 3/4 angepasst), Prüfer Runde 3 nicht bestanden (A5 INTERN veraltet, A6 Schwund-Annahme in Schritt 4), Runde 4 bestanden → geprueft. Quellen-Sätze unverändert ggü. Runde 1 (WebFetch im Prüfer-Lauf gesperrt, Abgleich per git diff). Ghost-Entwurf muss aktualisiert werden (neue Fassung, g4 neu, g5 geändert); Vorschau erneut an Till. · 2026-10-23 Ghost-Lauf (12:47, zweiter Lauf): Entwurf in Ghost mit neuer Fassung aktualisiert (g4 neu, g5 geändert), Vorschau: https://www.kleinmittelki.de/p/3aa0ec3b-67f5-440d-9514-2a9509cbbfd0/ · Till bekommt die überarbeitete Fassung über den Mail-Lauf · 2026-10-23 Chat: Titelbild titel-ki-ergebnisse-pruefen-leitfaden.jpg gebaut (Beitragsbild war die Titel-Kachel). Ghost-Lauf: draft neu, sonst blockiert die Veröffentlichung · Status zurück auf geprueft, damit der Ghost-Lauf den Entwurf mit Titelbild neu anlegt (Text unverändert) · 2026-10-23 Ghost-Lauf (18:47): Entwurf mit Titelbild neu in Ghost angelegt, Vorschau-Link unverändert · 2026-10-25 Chat: Till will fachlich 100 % sauber, KMU-verständlich, Bild-Beispiel rein, selbsterklärende Überschrift → überarbeitet (neuer Titel, g6 Hund/„Tiger“ als eigene Grafik, Quellen-Aussagen korrigiert, Schwund präzisiert, OLG-Link, Vorschaubild neu), Prüfer Runde 5 und 6 nicht bestanden, Runde 7 bestanden → geprueft; Ghost-Lauf legt den Entwurf neu an (Vorschau-Link bleibt gleich) · 2026-10-25 Ghost-Lauf (7:47): Entwurf in Ghost angelegt, Vorschau: https://www.kleinmittelki.de/p/3aa0ec3b-67f5-440d-9514-2a9509cbbfd0/ · 2026-10-25 Social (Sonntags-Lauf): Paket vorbereitet, ERST NACH VERÖFFENTLICHUNG (entwuerfe/ki-ergebnisse-pruefen-leitfaden/social.md: WhatsApp-Status am Tag nach Veröffentlichung, LinkedIn Do 5.11. oder statt OLG am 29.10., Karussell 7 Folien). Social: vorbereitet, wartet auf Till. Nichts gepostet. · 2026-10-25 vormittags Chat: Till findet den Ton zu negativ, will Prompt-Tipp „Erfinde keine Fakten“ und das echte Tiger-Bild → Ton ausgewogener, Regel 2 mit Studie (Communications Medicine 2025), Prompt-Kasten ergänzt (Till bestätigt noch); LinkedIn-Bild nicht verwendet (Rechte unklar), KI-Bild von Till folgt ggf. · Prüfer Runde 8 nicht bestanden, Runde 9 bestanden → geprueft · 2026-10-25 Ghost-Lauf (12:47): Entwurf mit Ton-Überarbeitung (Prüfer Runde 9) in Ghost aktualisiert, Vorschau: https://www.kleinmittelki.de/p/3aa0ec3b-67f5-440d-9514-2a9509cbbfd0/ · 2026-10-25 Till liefert eigenes KI-Bild (Hund/„Tiger“/„Context“) → ersetzt g6, gekennzeichnet; Prüfer Runde 10 bestanden → geprueft. Offen bei Till: Original als Vorlage genutzt? Prompt-Sätze bestätigen. · 2026-10-25 Till: KI-Foto mit Originalbild als Vorlage erzeugt → Foto raus, wieder g6 (Text wie Runde 9 geprüft), Datei ki-beispielbild-hund-tiger.jpg nicht verwenden; Status bleibt geprueft · 2026-10-25 Till: „Nimm das Foto“ → KI-Foto wieder drin (Fassung Prüfer Runde 10, Kennzeichnung „nachgestellt nach einem Motiv aus dem Netz“), Status geprueft · 2026-10-25 Ghost-Lauf (15:47): Entwurf mit KI-Foto (Fassung Prüfer Runde 10) in Ghost aktualisiert, Vorschau: https://www.kleinmittelki.de/p/3aa0ec3b-67f5-440d-9514-2a9509cbbfd0/ · 2026-10-25 Till: zu lang, Excel zu tief → auf ca. 1.575 Wörter gekürzt; Prüfer Runde 11 und 12 je ein bis fünf kleine Mängel, alle wörtlich umgesetzt (L1 aus Runde 12 wörtlich) → geprueft · 2026-10-25 Ghost-Lauf (18:47): Entwurf mit gekürzter Fassung (Prüfer Runde 12) in Ghost aktualisiert, Vorschau: https://www.kleinmittelki.de/p/3aa0ec3b-67f5-440d-9514-2a9509cbbfd0/ · 2026-10-25 Mail-Lauf (Abend): gekürzte Fassung als A an Till gemailt (Verlauf 1a173f22500167ff) · 2026-10-25 Till: Excel unverständlich, Rücksicht auf Arbeitgeber (kein Geschäftsmodell erkennbar) → fokussierte Fassung ~1.000 Wörter, g7 Wachstum, drei Regeln; Prüfer Runde 13 zwei kleine Mängel, wörtlich umgesetzt → geprueft · 2026-10-25 Ghost-Lauf (18:47, zweiter Lauf): Entwurf mit fokussierter Fassung (Prüfer Runde 13) in Ghost aktualisiert, Vorschau: https://www.kleinmittelki.de/p/3aa0ec3b-67f5-440d-9514-2a9509cbbfd0/ · Till bekommt die neue Fassung über den Mail-Lauf · 2026-10-25 Mail-Lauf (18:17): fokussierte Fassung als A an Till gemailt (Verlauf 1a174149f9a85de7) · 2026-10-25 Till: Tiger-Bild soll tragen → Umbau mit rotem Faden Kontext; Prüfer Runde 14/15 kleine Mängel, wörtlich umgesetzt (Q1 OWASP wörtlich) → geprueft

### eu-eurobarometer-ki-unternehmen
- Status: wartet-auf-till
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
- Verlauf: 2026-10-19 Till per Mail („KMK Idee: bitte direkt fertig ausarbeiten und Entwurf schicken“) → freigegeben; Scout prüft zuerst das Original und Dubletten (Blog-Index: kein Treffer zu Eurobarometer) · 2026-10-19 Redaktions-Lauf (Abend): Autor prüfte jede Mail-Zahl am Original – alle bestätigt; 42 % = KI ODER automatisierte Systeme für Arbeit/Personal, nur KMU/Mid-Caps 1–749 Beschäftigte, 12.826 Interviews. Grafik: Balken nach Betriebsgröße + Vorschaubild. Prüfer Runde 1 nicht bestanden (Titel), Runde 2 bestanden → geprueft. Details: entwuerfe/eu-eurobarometer-ki-unternehmen/quellen.md, pruefung.md. „Meine Einordnung“ weiter INTERN-Vorschlag. · 2026-10-19 Ghost-Lauf (20:01): Entwurf in Ghost angelegt, Vorschau-Link oben. · 2026-10-23 Chat: Titelbild titel-eu-eurobarometer-ki-unternehmen.jpg gebaut (Beitragsbild war die Titel-Kachel). Ghost-Lauf: draft neu, sonst blockiert die Veröffentlichung · Status zurück auf geprueft, damit der Ghost-Lauf den Entwurf mit Titelbild neu anlegt (Text unverändert) · 2026-10-23 Ghost-Lauf (18:47): Entwurf mit Titelbild neu in Ghost angelegt, Vorschau-Link unverändert

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
- Verlauf: 2026-10-12 Till: als künftigen Praxistest vorgemerkt · 2026-10-19 Scout: Quelle benannt, Originalseite nicht lesbar, Kernbehauptung nicht belegt, Relevanz unter 7 · 2026-10-19 Scout (Redaktions-Lauf): Outlook-Supportseite weiterhin nicht abrufbar (ungeprüft). Gelesen: Microsoft „Fluid dictation“ – Füllwörter/Grammatik-Korrektur beim Diktieren ist eine Windows-Funktion, nur Copilot+ PCs, laut Seite nur Englisch. Titel für deutschen Test nicht haltbar; Relevanz bleibt 6/10. Ersatz-Idee (Diktat + Copilot-Überarbeitung) nur bei Copilot-Lizenz, Frage an Till über Chefredakteur. · 2026-10-19 Scout (Test 2): Outlook-Supportseite (de-de, Stand 17.09.2026) **gelesen**: Diktat in Outlook (365, 2024, .com, neues Outlook, Web) mit Deutsch und automatischer Zeichensetzung; laut Seite keine Speicherung von Audio/Text; **keine Aufräum-Funktion** beschrieben, keine Lizenzangabe. Kernbehauptung bleibt unbelegt, Relevanz bleibt 6/10.

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
- Verlauf: 2026-09-21 im Protokoll-Beitrag angekündigt · 2026-10-19 Scout: keine Quelle lesbar, nichts recherchiert, nur Gerüst angelegt · 2026-10-19 Scout (Redaktions-Lauf): drei Quellen gelesen – GDD-Kurzpapier 4 „Gesprächstranskription“ (Jan. 2026), GDD-Erfa-Konzept „KI-gestützte Transkription von Videokonferenzen“ v1.2 (09.06.2026, mit Vorlagen auch für Betriebe ohne Betriebsrat), Microsoft-Datenschutzseite zu Teams „intelligent recap“ (Herstellerangabe). Keine Aufsichtsbehörden-Quelle gefunden; Google/Zoom/Noota-Doku offen. Relevanz neu: 8/10 (Betroffenheit 2, Handlung 2, Quelle 1, Neuheit 1, Passung 2) – Quelle 1, weil Fachverband statt Aufsicht. · 2026-10-19 Scout (Test 2): Aufsichtsquelle gelesen – LfDI Baden-Württemberg, Leitfaden KI-Transkription (10.06.2026), allerdings für Gemeinderäte; übertragbar: Training mit Daten grundsätzlich unzulässig, Löschung nach Protokoll, menschliche Kontrolle, EU-Verarbeitung. Google-Meet-Hilfe „Take notes for me“ gelesen (Deutsch unterstützt, Zustimmungspflicht standardmäßig aus). Zoom-Seite nicht lesbar (ungeprüft). Aufsichtsquelle speziell für Unternehmen fehlt weiter. Relevanz bleibt 8/10.

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
- Verlauf: 2026-10-12 als stärkster Kandidat vorgeschlagen · 2026-10-19 Scout: Az. und Eckdaten durch mehrere Zweitquellen gestützt, Original nicht abrufbar; vor Schreiben Original beschaffen · 2026-10-19 Scout (Redaktions-Lauf): **Original gelesen** – PM OLG Hamm vom 12.05.2026, https://www.justiz.nrw/presse/2026-05-12. Bestätigt: Az. 4 UKl 3/25, VZ NRW gg. Aesthetify GmbH, § 5 Abs. 1, Abs. 2 Nr. 3 UWG, Zurechnung trotz korrekter Daten, Chatbot kein „Dritter“, Revision zum BGH zugelassen. Nicht in der PM (weiter ungeprüft): Warnhinweis „KI kann irren“ entlastet nicht; ob Revision eingelegt; LG München I 26 O 869/26. Volltext (NRWE) steht aus. Relevanz neu: 10/10 (Quelle 2). Achtung: anderes Verfahren gegen dieselbe Firma (4 UKl 2/24, HWG) nicht verwechseln. · 2026-10-19 Scout (Test 2): **Volltext gelesen** (NRWE, https://nrwe.justiz.nrw.de/olgs/hamm/j2026/4_UKl_3_25_Urteil_20260512.html). Wichtig: NRWE weist das Urteil als **rechtskräftig** aus – Angabe „nicht rechtskräftig“ aus Zweitquellen damit überholt (Prüfer gegenlesen). Kein „KI kann irren“-Hinweis im Urteil; Gericht verneint aber, dass Verbraucher mit KI-Fehlern rechnen. Zurechnung: Chatbot ist technisches Mittel unter Steuerungsgewalt des Betreibers; Halluzinationen waren vorhersehbar. Relevanz bleibt 10/10. · 2026-10-19 Till per Mail (Antwort im Verlauf „KMK-Redaktion · Mo 19.10. (Test)“, 12:08): „Thema 1 bitte ausarbeiten“ → freigegeben. · 2026-10-19 Redaktions-Lauf (Abend): Autor schrieb Nachricht aus PM und NRWE-Volltext (beide selbst gelesen), „Meine Einordnung“ als INTERN-Vorschlag. Vorschaubild, keine Grafik. Prüfer Runde 1 nicht bestanden (zwei Bookmark-Karten), Runde 2 bestanden → geprueft. Vor Veröffentlichung Rechtskraft in NRWE nochmal ansehen. Querverweis: LG München I 26 O 869/26 jetzt am Original bestätigt (siehe ki-suche-falsche-aussagen-ueber-betrieb). · 2026-10-19 Ghost-Lauf (20:01): Entwurf in Ghost angelegt, Vorschau-Link oben. · 2026-10-23 Till per Mail (Verlauf „KMK-Redaktion · Fr 23.10.“, 12:01): „Beitrag A ja / Vorher interne Notizen wegmachen“ → Veröffentlichungsfreigabe sofort über mailfreigabe.py eingetragen (Mail-ID 1a168344dae06238). INTERN-Absatz entfernt ghost.py beim Veröffentlichen. Nächster Ghost-Lauf veröffentlicht. · 2026-10-23 Ghost-Lauf (12:47): veröffentlicht, https://www.kleinmittelki.de/olg-hamm-chatbot-haftung/ (INTERN-Absatz entfernt, 12:38 Uhr MESZ) · 2026-10-23 Chat: Titel-Kachel war Beitragsbild (doppelter Titel, kein Bild in der Übersicht). Neues Titelbild titel-olg-hamm-chatbot-haftung.jpg, Till „Ja und ja“ → Freigabe titelbild, Ghost-Lauf tauscht das Bild · 2026-10-23 Ghost-Lauf (18:47): Titelbild getauscht (Freigabe titelbild ausgeführt) · 2026-10-25 Social (Sonntags-Lauf): Paket vorbereitet (entwuerfe/olg-hamm-chatbot-haftung/social.md: WhatsApp-Status Di 27.10., LinkedIn Do 29.10. mit 2 Kacheln in social/). Social: vorbereitet, wartet auf Till. Nichts gepostet.

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
- Verlauf: 2026-10-12 vorgeschlagen · 2026-10-19 Scout: Frist durch Zweitquellen gestützt, Original und Gesetzesstand ungeklärt, als ungeprüft markiert · 2026-10-19 Scout (Redaktions-Lauf): **Gesetzesstand geklärt aus Original** – BR-Drs. 584/26 gelesen: Bundestag hat Drs. 21/4297 am 08.10.2026 beschlossen (Beschlussempfehlung 21/8429); Bundesrat-Frist 30.10.2026, Verkündung steht aus; Inkrafttreten 9.12.2026; altes Recht für Produkte bis einschl. 8.12.2026 (§ 23). Software ist Produkt (§ 2 Abs. 1 Nr. 3), Begriff „KI“ kommt im Gesetz nicht vor. Richtlinie: EUR-Lex nur Metadaten (23.10.2024, in Kraft 8.12.2024); Art. 2, 4, 8 aus Amtsblatt-Kopie eines Dritten gelesen, gegen EUR-Lex gegenlesen; Art. 12/22 nicht gelesen. Relevanz neu: 9/10 (Betroffenheit 1, Handlung 2, Quelle 2, Neuheit 2, Passung 2). Bundestagsbeschluss ist ein aktueller Anlass; ggf. zusätzlich kurze Nachricht nach Bundesrat. · 2026-10-19 Scout (Test 2): amtliches EUR-Lex-PDF (DE) gelesen – Art. 2 Abs. 1/2, Art. 4 Nr. 1, Art. 8 Abs. 1/2 bestätigt. Art. 12, 21, 22 (Umsetzungsfrist), 23 weiter nicht lesbar (Abruf bricht ab), ungeprüft. Relevanz bleibt 9/10. · 2026-10-23 Scout: **Bundesrat hat entschieden** – BR-Drs. 584/26(B) gelesen, https://dserver.bundestag.de/brd/2026/0584-26B.pdf: 1069. Sitzung am **16.10.2026**, kein Antrag nach Art. 77 Abs. 2 GG (Vermittlungsausschuss nicht angerufen), keine Entschließung. Gesetz damit zustande gekommen; Ausfertigung/Verkündung im BGBl. noch nicht gefunden (ungeprüft). Inkrafttreten 9.12.2026 laut Gesetzesbeschluss (BR-Drs. 584/26). Aktueller Anlass für eine kurze Nachricht oder als Einstieg in den Leitfaden.

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

### newsletter-2026-10-27
- Status: newsletter-vorschlag
- Titel: „#4: KI-Ergebnisse prüfen und wer für den Chatbot haftet“ (Ersatz ohne Leitfaden: „#4: Wenn der Chatbot spricht, haftet der Betrieb“)
- Versand: Dienstag 27.10.2026, 7:00 (nach Tills „N ja“)
- Inhalt: 01 Leitfaden ki-ergebnisse-pruefen-leitfaden (nur wenn Till ihn bis Di 7:00 freigibt) · 02 olg-hamm-chatbot-haftung (live) · 03 Zahl „1 zu 365“ (OpenAI, 05.09.2025) · 04 Gedanke
- Datei: entwuerfe/newsletter-2026-10-27/beitrag.md, Prüfung: pruefung.md
- Braucht von Till: erst über den Leitfaden entscheiden, dann „N ja“; Vorschläge in Ich-Form (INTERN) bestätigen oder ersetzen
- Verlauf: 2026-10-25 Sonntags-Lauf: Autor Entwurf, Prüfer Runde 1 nicht bestanden (T1–T3 Formulierungen, I1–I4 Ersatztexte/Freigabe-Reihenfolge), Runde 2 bestanden → newsletter-vorschlag. Mail-Lauf 10:17 schickt ihn Till. Nicht in Ghost. 2026-10-25 Mail-Lauf 10:17: Fassung 1 gemailt (Mail 1a1725c28e258a9a, Fingerabdruck d2fad333…), wartet auf Tills Antwort.

### ki-recherche-assistent-selbstversuch
- Status: wartet-auf-till
- Idee von Till (Chat 25.10.2026: Praxistest, wie er seinen automatisierten Recherche-Flow nach eigenen Kriterien aufgebaut hat, Ergebnis per Mail)
- Titel: „Mein KI-Rechercheassistent: Die KI sucht. Ich entscheide.“
- Rubrik/Kategorie: Praxistests / KI in der Praxis · Format: Praxistest · g1 Ablauf (vier Stufen) + HTML-Karten, Titelbild, Vorschaubild
- Quelle: eigene Systemunterlagen + Hilfeseiten OpenAI (Tasks), Microsoft (Scheduled prompts), Anthropic (Scheduled tasks), abgerufen 25.10.2026 – siehe quellen.md
- Warum für KMU: Prinzip übertragbar auf Ausschreibungen, Förderprogramme, Normen; fünf Schritte, Beispiel-Anfrage Malerbetrieb, drei Wege nach Ausstattung
- Wichtig (Till, Chat 25.10.2026): Der Beitrag zeigt nur die Recherche. Nichts darüber, dass KI Texte oder Beiträge schreibt – und auch nicht, dass Till selbst schreibt; das bleibt offen.
- Braucht von Till: nur noch „A ja“ (Aufwand/Kosten auf Tills Bitte aus den Chats eingeschätzt, 25.10.)
- Verlauf: 2026-10-25 Chat: Till „Erstelle mir diesen Beitrag …“ → Text, Grafiken, Quellen im Chat erstellt und geprüft (ohne separaten Prüfer-Lauf; Zahlen nur aus quellen.md, alle Bilder angesehen, lexical.py fehlerfrei) · 2026-10-25 Chat: Till will KI-Schreiben nicht erwähnt haben → alle Hinweise darauf entfernt → geprueft · 2026-10-25 Chat: Till bittet, Aufwand und Kosten aus den Chats einzuschätzen → Platzhalter ersetzt, bleibt geprueft · 2026-10-25 Chat: Till will den Technikteil behalten und drei Beispiel-Anfragen → Bäckerei, Handwerk, Hausverwaltung + Grenze „verschlossene Portale“, bleibt geprueft · 2026-10-25 Ghost-Lauf (18:47): Entwurf in Ghost angelegt, Vorschau: https://www.kleinmittelki.de/p/7ef917e2-ee8b-4cc9-b6e7-8e5a18f6a8da/ · 2026-10-25 Mail-Lauf (Abend): als B an Till gemailt (Verlauf 1a173f22500167ff, Vorschlag Do 7:00)

## Archiv

(noch leer)
