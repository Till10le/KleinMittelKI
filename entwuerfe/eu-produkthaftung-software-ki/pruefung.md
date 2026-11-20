# Prüfung: eu-produkthaftung-software-ki

Datum: 20.11.2026 · Prüfer (unabhängig) · Format Langtext, Wissen / Leitfäden, geplant Di 24.11.2026 7:00

## Ergebnis: NICHT BESTANDEN

Die Fakten sind sauber: Jede Paragraphen-Angabe stimmt mit dem Wortlaut überein. Gelesen habe ich selbst das
BGBl. 2026 I Nr. 321 (PDF von recht.bund.de), BR-Drs. 584/26 und 584/26(B), die Richtlinie (EU) 2024/2853
(amtlicher Text über publications.europa.eu, weil EUR-Lex leer antwortet) und das alte ProdHaftG §§ 2, 10, 11.
Drei Mängel verhindern trotzdem die Freigabe. Zwei davon sind schnell behoben (Punkte 1 und 3). Der dritte ist die Kürzung
(Punkt 2), um die Till ausdrücklich gebeten hat.

## Direkt korrigiert (in beitrag.md)

1. § 19 („Wenn es vor Gericht geht“): „Auf Antrag kann das Gericht anordnen …“ → „Macht die geschädigte Person ihren
   Anspruch plausibel, ordnet das Gericht auf ihren Antrag an …“. Das Gesetz sagt „ordnet … an“, wenn der Anspruch
   plausibel ist. Es ist keine Kann-Vorschrift.
2. § 16: „… von Fehler, Schaden und Hersteller weiß“ → „… weiß oder hätte wissen müssen“ (Wortlaut: „Kenntnis erlangt
   hat oder hätte erlangen müssen“).
3. § 6 Abs. 3, im Text und in der Karte: „ein Produkt, das nie verkauft wurde“ → „… nie verkauft oder weitergegeben
   wurde“. Inverkehrbringen umfasst auch die unentgeltliche Abgabe (§ 6 Abs. 1, 2).

`python3 tools/lexical.py` läuft danach fehlerfrei (45 Knoten, 9 H2).

## Mängel

1. **Art. 12 Abs. 2: Einschränkung fehlt** (Checkliste „Was du jetzt prüfen kannst“, Punkt 4). Der Text sagt
   „mit einem kleinen Softwarezulieferer“. Die Richtlinie verlangt aber ein Kleinst- oder Kleinunternehmen im Sinne der
   Empfehlung 2003/361/EG, also unter 50 Beschäftigte und höchstens 10 Mio. Euro Jahresumsatz oder Bilanzsumme.
   Zur Schwelle siehe die KMU-Definition der EU-Kommission:
   https://single-market-economy.ec.europa.eu/smes/sme-fundamentals/sme-definition_de.
   Für die Kernzielgruppe (20–150 Beschäftigte) ist das entscheidend: Ein Zulieferer mit 60 Leuten fällt nicht darunter.
   Außerdem ist es eine Regel der Richtlinie. Das deutsche Gesetz hat dazu keine eigene Vorschrift, nur § 15 Satz 2
   („soweit nichts anderes bestimmt ist“).
   Korrektur: „Die Richtlinie sieht ausdrücklich vor, dass ein Hersteller mit einem Softwarezulieferer, der ein
   Kleinst- oder Kleinunternehmen ist (nach EU-Definition unter 50 Beschäftigte und höchstens 10 Millionen Euro
   Jahresumsatz oder Bilanzsumme), vereinbaren kann, auf den Rückgriff zu verzichten (Art. 12 Abs. 2).“
   Die Quelle der Schwelle gehört in quellen.md.

2. **Länge** (Tills Rückmeldung vom 25.10.: „generell viel zu lange“). Der Fließtext hat rund 1.880 Wörter.
   Dazu kommen rund 360 Wörter in Box und Karte. Gelesen werden also rund 2.250 Wörter. Ziel: Fließtext höchstens
   1.300–1.400 Wörter. Konkret:
   - „Wer betroffen ist“ (497 Wörter + Karte 253): Die vier Fall-Bullets und der Absatz „Eher nicht betroffen“ sagen
     dasselbe wie die Karte „Bin ich Hersteller?“ (Zeilen 1, 2, 5 und 7). Bullets streichen. Das Motor-Bild aus dem
     KI-Modell-Beitrag als einen Satz an die Komponenten-Erklärung hängen. „Eher nicht betroffen“ auf zwei Sätze kürzen.
     Ersparnis rund 250 Wörter.
   - „Was sich am 9. Dezember ändert“ (361): Absatz 1 erzählt den Gesetzgebungsweg (Bundestag, Bundesrat, BGBl.). Die
     Zeitstrahl-Grafik zeigt genau das. Ein Satz reicht: „Deutschland setzt sie mit dem Gesetz zur Modernisierung des
     Produkthaftungsrechts um, verkündet am 27.10.2026, in Kraft ab 9.12.2026.“ „Lernende Systeme zählen mit“ in den
     Software-Absatz ziehen. Ersparnis rund 100 Wörter.
   - „Wenn es vor Gericht geht“ (179): auf drei Sätze kürzen. Die Botschaft „Dokumentation ist im Streitfall das
     wichtigste Werkzeug“ in Checklisten-Punkt 6 aufnehmen. Fristen in einem Satz. Ersparnis rund 100 Wörter.
     Alternativ den ganzen Abschnitt in die Checkliste auflösen.
   - Chatbot/AI-Act-Absatz am Ende von „Wer betroffen ist“: auf einen Satz mit den zwei internen Links kürzen. Ersparnis
     rund 40 Wörter.
   - Updates: Die vier § 9-Bullets in einen Satz fassen. Ersparnis rund 30 Wörter.
   - Dreifach-Dopplungen auflösen: Der Stichtag steht in Text, Grafiktitel und Bildunterschrift. Bildunterschrift
     besser auf die Grenze lenken, etwa „Offen bleibt, ob ein großes Update ein Altprodukt ins neue Recht holt.“
     „Keine Rechtsberatung“ steht im Checklisten-Vorspann, in der Kartenunterschrift und im Schlussabsatz. Einmal im
     Schluss reicht, die Karte behält ihre Standardzeile.
   Die INTERN-Angabe „rund 1.980 Wörter, oberer Rand“ danach anpassen.

3. **Format: Grafik-Anzahl ohne Begründung** (#14). Langtext verlangt 3–4 Grafiken bzw. 4–5 PNG-Schaubilder. Der
   Entwurf hat zwei: eine HTML-Prüfliste und ein PNG. Inhaltlich passt das zum Muster „Leitfaden Rechtslage“ (zwei Karten,
   Vorbild AI-Act-Beitrag) und zu Tills Kürzungswunsch. Der INTERN-Absatz nennt aber nur die Zahl, keinen Grund.
   Korrektur: Begründung in INTERN ergänzen („zwei Grafiken wie beim Leitfaden Rechtslage, wegen Kürzung“) und Till
   entscheiden lassen. Keine zusätzlichen Grafiken bauen.

## Kleinere Punkte (keine Freigabe-Hindernisse, aber vor Ghost erledigen)

4. **Titel „Software ist jetzt ein Produkt“**: Am 24.11. gilt das Gesetz noch nicht. Es ist verkündet, aber erst ab
   9.12. in Kraft. Vorschlag: „Software gilt ab 9. Dezember als Produkt: Was die neue Produkthaftung für deinen Betrieb
   heißt“. Danach Vorschaubild neu rendern.
5. **Du/Ihr-Wechsel in der Checkliste**: In Punkt 4 steht „Ihr haftet …“ und zwei Sätze später „Liefert dein Betrieb …“.
   Sonst duzt der Beitrag durchgehend. Einheitlich auf „du/dein Betrieb“ umstellen, wie im übrigen Text.
6. **„Hätte er ein Sicherheitsupdate bereitgestellt …, sähe es anders aus“** (Updates, letzter Absatz): Das ist eine
   Ableitung aus Erwägungsgrund 51. Sie steht nicht in der Liste der Auslegungen im INTERN-Absatz (3). Entweder dort
   ergänzen oder präziser schreiben: „…, läge das nach der Richtlinie außerhalb seiner Kontrolle (Erwägungsgrund 51).“
7. **Ich-Absatz** (INTERN-Vorschlag): „Ich lese das Gesetz weniger als neue Pflicht, sondern als …“ ist dieselbe Formel
   wie im OLG-Hamm-Beitrag („Ich lese das Urteil weniger als …, sondern als …“) und im Stil-Skill. Ein zweites Mal wirkt
   sie wie eine Schablone. Till auf eine andere Formulierung hinweisen.
8. **85 Mio. Euro**: Nach § 10 Abs. 1 des alten Gesetzes ist das ein Gesamt-Höchstbetrag für alle Personenschäden durch
   ein Produkt oder gleiche Produkte mit demselben Fehler. Präziser: „auf insgesamt 85 Millionen Euro je Serienfehler
   begrenzt“.
9. **Link altes ProdHaftG** (Quellen): `gesetze-im-internet.de/prodhaftg/` zeigt nach dem 9.12. womöglich das neue
   Gesetz oder einen Aufhebungsvermerk. Prüfen, oder BGBl. 1989 I S. 2198 als Fundstelle ergänzen.
10. **Fahrplan**: In `redaktion/fahrplan.md` steht für Di 24.11. 7:00 noch `ki-recherche-assistent-selbstversuch`, nicht
    dieser Beitrag. Das muss der Chefredakteur klären.

## Checkliste

| # | Punkt | Ergebnis |
|---|---|---|
| 1 | Zahlen, Daten, Namen gegen Original | ok nach den Korrekturen oben. Geprüft: BGBl. Nr. 321 vom 27.10.2026, Ausfertigung 22.10.2026; BT 8.10.2026 (99. Sitzung); BR 16.10.2026 (1069. Sitzung, kein Antrag nach Art. 77 Abs. 2 GG); Art. 17 Abs. 1 (9.12.2026); Art. 2 (altes Gesetz außer Kraft 9.12.2026); §§ 1–10, 15–21, 23 neu; RL Art. 12 Abs. 2, 22, 23 (in Kraft 8.12.2024), EG 6, 13, 15, 40, 51, 54, 56; alt §§ 2, 10, 11 (85 Mio./500 Euro) |
| 2 | Einschränkungen genannt | Mangel 1 (Größengrenze Art. 12 Abs. 2) |
| 3 | Originalveröffentlichungen verlinkt | ok (recht.bund.de ELI, EUR-Lex ELI, dserver BR-Drs.), Hinweis 9 |
| 4 | Nichts in Tills Namen erfunden | ok: einziger Ich-Absatz in INTERN (5) markiert; Beispiele und Auslegungen markiert, Hinweis 6 |
| 5 | Keine offenen Platzhalter | ok (keine `[TILL:]`/`[GRAFIK:]`) |
| 6 | Überschriften, Länge, Teaser | Teaser 137 Zeichen ok, nicht gleich Titel. Langtext-Gerüst ok (Einstieg 2 Absätze, Box 5 Punkte, Schluss „Was das für den Mittelstand bedeutet“ · „Ein Gedanke“ · „Quellen“ mit Abrufdatum). Mangel 2 (Länge) |
| 7 | Rubrik, Kategorie, Tags | ok: Wissen / Leitfäden, `#wissen` (`#zur-freigabe` setzt ghost.py) |
| 8 | Für-KMU-Zeile | entfällt (kein Aktuell) |
| 9 | Ton, Verbote | ok: kein Hype, keine CTAs, kein Handel (Lebensmittel-Verpackungsmaschinen, Elektrobetrieb, Softwarehaus), nichts Parteipolitisches; Hinweise 5, 7 |
| 10 | KMU-Bezug | ok (Maschinenbauer 60 Leute, Elektrobetrieb 25, Softwarehaus 10–50, Geschäftsführung/Technikleitung) |
| 11 | Grafiken | ok: Prüfliste entspricht `urteil-und-pruefliste.html` (Kicker „Grafik 01 / …“ wie AI-Act-Referenz), PNG im Karten-System mit Kicker, Aussage-Titel, Fußzeile Stand/Quelle, Lime-Kante; Werte stimmen (8.12.2024 = 20. Tag nach 18.11.2024); Alt-Text vorhanden; Social-Kachel angesehen ok. Bildunterschrift siehe Mangel 2 |
| 12 | Vorschaubild | ok: drei Zeilen, Logo, Lime-Kante (bei Titeländerung neu rendern) |
| 12a | Titelbild | ok: Einordnung ohne Beitragstitel, ein Merksatz („Die Verantwortung reicht so weit wie der Update-Kanal.“, steht so im Text, nicht Ich-Form), keine Zahlen, `titelbild:` im Frontmatter |
| 13 | Ghost-Vorschau | entfällt (noch nicht in Ghost) |
| 14 | Vergleich mit Referenz | Mangel 3 (Grafik-Anzahl); Aufbau sonst wie `chatgpt-claude-gemini-ki-modelle-erklaert` (Box, H2-Fragen/Aussagen, Schluss, Quellen) |

Interne Links: alle drei Ziele sind veröffentlicht, die URLs stimmen mit `redaktion/blog-index.json` überein
(chatgpt-claude-gemini-ki-modelle-erklaert, olg-hamm-chatbot-haftung, ai-act-ki-bilder-kennzeichnen). Die Aussage zum
OLG Hamm (Mai 2026, irreführende geschäftliche Handlung) deckt sich mit dem veröffentlichten Beitrag (Urteil 12.05.2026).
