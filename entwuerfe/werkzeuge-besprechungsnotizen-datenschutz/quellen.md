# Quellen: werkzeuge-besprechungsnotizen-datenschutz

Stand: 2026-10-19 (Scout). **Status: noch keine Quelle gelesen.** In diesem Lauf war kein Abruf externer Seiten möglich
(DNS-Fehler bei WebFetch), und Suche dazu wurde nicht gemacht, um nichts aus Zweitquellen zu übernehmen.

## Zu beschaffen (alles offen)
- Hersteller-Dokumentation der Werkzeuge, die der Beitrag nennen soll (Auswahl durch Till; Microsoft Teams/Copilot-Recap,
  Google Meet, Zoom, Noota u. a.): jeweils Datenverarbeitung, Speicherort, Aufbewahrung, Training mit Kundendaten.
- Datenschutzaufsicht: Orientierungshilfe/Hinweise zu KI-Transkription und Aufzeichnung von Besprechungen
  (z. B. DSK, Landesbeauftragte). **Nicht gefunden, nicht gelesen.**
- Rechtsgrundlage Einwilligung aller Teilnehmer: Original (DSGVO, ggf. § 201 StGB) nur aus Primärtext.

## Interne Anknüpfung
- Bestehender Beitrag: https://www.kleinmittelki.de/protokoll-per-ki-selbstversuch/ (Quelle dort: https://noota.io/).
  Ankündigung dieses Folgebeitrags laut Board vom 2026-09-21.

## Einschränkungen
- Herstellerangaben sind Selbstauskunft und so zu kennzeichnen.
- Welche Werkzeuge Till nutzt, darf nicht erfunden werden.

---

## Nachtrag 2026-10-19 (Scout, Redaktions-Lauf): erste Quellen gelesen

### 1. GDD-Kurzpapier Nr. 4 „Gesprächstranskription“ (gelesen)
- Herausgeber: Gesellschaft für Datenschutz und Datensicherheit e. V. (GDD), Bonn. Stand: Januar 2026.
  https://www.gdd.de/wp-content/uploads/2026/01/GDD-Kurzpapier-4-Gespraechstranskription.pdf
- Kernaussagen (eigene Worte): Schon die Zwischenspeicherung ist Verarbeitung personenbezogener Daten. Zentrale und
  verlässlichste Rechtsgrundlage ist die Einwilligung (Art. 6 Abs. 1 lit. a DSGVO) – freiwillig, informiert, widerrufbar;
  Schweigen oder automatisch aktivierte Funktionen reichen nicht. Im Arbeitsverhältnis ist Freiwilligkeit fraglich,
  daher Betriebsvereinbarung empfohlen (Art. 88 DSGVO i. V. m. § 26 BDSG), Mitbestimmung beachten. Berechtigtes
  Interesse nur mit Erforderlichkeit und dokumentierter Abwägung. Alle Teilnehmer vorab informieren (Einladung plus
  Hinweis zu Beginn). Löschkonzept; Audio grundsätzlich nach Fertigstellung des Transkripts löschen. AV-Vertrag
  (Art. 28), bei Drittland Garantien (z. B. Standardvertragsklauseln). AI Act beachten (Emotionserkennung u. U. verboten).
- § 201 StGB: Aufnahme des nichtöffentlich gesprochenen Wortes ohne Einwilligung strafbar; strafrechtlich genügt laut
  Papier eine konkludente Zustimmung („Strafrechtlich genügt eine konkludente Zustimmung.“), datenschutzrechtlich wird
  ausdrückliche, dokumentierte Einwilligung empfohlen.
- Einschränkung: Verband/Fachgesellschaft, **keine Aufsichtsbehörde**, keine verbindliche Rechtsauslegung.

### 2. GDD-Erfa-Kreise: „KI-gestützte Transkription von Videokonferenzen – Gesamtkonzept …“ (gelesen)
- Version 1.2, Stand 09.06.2026; erstellt von Mitgliedern der GDD-Erfa-Kreise Dortmund, Essen, Freiburg und Köln;
  kein formaler Herausgeber genannt. https://www.gdd.de/wp-content/uploads/2026/06/KI-Protokoll_Version_1_2_2026-06-09.pdf
- Enthält Vorlagen: Konzept, Betriebsvereinbarung, betriebliche Richtlinie (für Betriebe ohne Betriebsrat), Verhaltenskodex.
- Externe Teilnehmer: aktive Einwilligung (Opt-in, Art. 6 Abs. 1 lit. a DSGVO), Zustimmung nachweisbar dokumentieren;
  bei Ablehnung Meeting ohne KI.
- „Eine dauerhafte Speicherung der Audiospur ist unzulässig.“ Kurze Karenzzeit für Qualitätskontrolle, empfohlen 72 Stunden.
  Transkripte laut BV-Vorlage nach zwei Wochen automatisch löschen, sofern nicht ins Ergebnisprotokoll übernommen.
- AV-Vertrag muss Training der Anbieter-Modelle mit den Daten ausschließen. Fremde Bots (genannt: Otter.ai, Read.ai)
  untersagen; Warteraum (Lobby) als Schutz.
- Tabu-Zonen: Betriebsratssitzungen, Personalgespräche (Kritik-, BEM-Gespräche), Gespräche über besondere Datenkategorien.
  Keine Leistungskontrolle über Transkripte. Transkripte gelten nur als Entwurf, vor Weiterverarbeitung prüfen.
- Einschränkung: Praxisvorlage eines Arbeitskreises, keine Aufsicht. Für Betriebe mit 20–150 Leuten ohne Betriebsrat
  ist die „betriebliche Richtlinie“ der passende Teil.

### 3. Microsoft Learn: „Intelligent recap – data, privacy, and security“ (gelesen, Herstellerangabe)
- https://learn.microsoft.com/en-us/microsoftteams/privacy/intelligent-recap (ms.date 2023-11-08; Metadaten-Update 2026-08-05)
- Nutzt das Besprechungstranskript (Transkription muss an sein), teils auch Aufzeichnung. KI-Notizen/Aufgaben liegen in
  Exchange-Postfächern der Teilnehmer; Transkript im Exchange des Organisators (plus OneDrive bei Aufzeichnung).
  Aufbewahrung folgt der Richtlinie für Besprechungsaufzeichnungen. Daten im geografischen Bereich des Tenants.
- Wörtlich: „Customer data isn't logged or used for any AI model training or testing.“ GPT-Modell über Azure OpenAI,
  keine Weitergabe an OpenAI.
- Lizenz laut Seite: Teil von **Teams Premium** (Add-on). Ob inzwischen auch über Microsoft 365 Copilot – auf dieser
  Seite nicht genannt, **ungeprüft**. Seite ist alt (2023); aktuellen Stand prüfen.
- Einschränkung: Selbstauskunft des Herstellers.

### Weiterhin offen
- **Aufsichtsbehörde** (DSK, Landesbeauftragte) zu KI-Transkription: nicht gefunden. Gefunden, aber nicht gelesen:
  Bayern, Datenschutzhinweise Videokonferenzen https://www.datenschutz-bayern.de/datenschutzhinweise/vk.pdf
  (vermutlich Hinweise der Behörde zu eigenen VKs, nicht Orientierungshilfe).
- Google Meet („Notizen für mich“/Gemini), Zoom AI Companion, Noota: Herstellerdoku noch nicht gelesen.
- Welche Werkzeuge Till nutzt: offen (nicht erfinden).

---

## Nachtrag 2026-10-19 (Scout, Test 2): Aufsichtsbehörde und Herstellerseiten

### 4. LfDI Baden-Württemberg: Leitfaden KI-Transkription (gelesen, Aufsichtsbehörde)
- „Datenschutz-Leitfaden für KI-Transkription von Gemeinderatssitzungen in Baden-Württemberg“, Der Landesbeauftragte für
  den Datenschutz und die Informationsfreiheit Baden-Württemberg, Version 1.0, Stand 10.06.2026:
  https://www.baden-wuerttemberg.datenschutz.de/wp-content/uploads/2026/06/Leitfaden-Ki-Transkription-Gemeinderat-260611.pdf
- **Zielgruppe: öffentliche Stellen (Gemeinden)**, nicht Unternehmen. Rechtsgrundlage über Landesrecht (GemO, LDSG) –
  für Betriebe nicht übertragbar. Der Leitfaden steht unter Vorbehalt künftiger DSK-/EDSA-Aussagen.
- Übertragbare DSGVO-Punkte (eigene Worte): Hinweis an Teilnehmende während der Sitzung, Informationspflichten Art. 13;
  Audio und Transkript löschen, sobald das Protokoll beschlossen ist (oder Höchstspeicherdauer); AV-Vertrag nach Art. 28,
  Verarbeitung möglichst in der EU; **Nutzung der Daten zum Training grundsätzlich unzulässig**; On-Premise/abgeschottete
  Instanz bevorzugt, bei Cloud BSI-Grundschutz/C5; Zusammenfassung dauerhaft menschlich kontrollieren, Transkript
  mindestens stichprobenartig prüfen und Prüfung dokumentieren; Schwellwertanalyse/ggf. DSFA.
- § 201 StGB und AI Act werden nicht behandelt.
- Für den Beitrag: als Orientierung einer Aufsicht zitierbar, aber ausdrücklich „für Kommunen geschrieben“ kennzeichnen.
- Eine Aufsichtsquelle speziell für Unternehmen (DSK, BfDI) wurde weiterhin **nicht gefunden**.
  Hinweis, nicht gelesen (Abruf scheiterte): datenschutz.de „Neue Praxishilfen zu KI in der Verwaltung und KI-Transkription“.

### 5. Google Meet „Take notes for me“ (gelesen, Herstellerangabe)
- https://support.google.com/meet/answer/14754931?hl=en&co=GENIE.Platform%3DDesktop
- Braucht eine berechtigte Workspace-Edition oder einen Google-AI-Plan des Organisators (Editionen nicht genannt).
  Sprachen: Englisch, Französisch, **Deutsch**, Italienisch, Japanisch, Koreanisch, Portugiesisch, Spanisch – eine Sprache
  pro Meeting.
- Notizen als Google-Doc im Drive des Organisators; Organisator wählt Freigabe (alle Eingeladenen inkl. Externer, nur
  interne, nur Hosts). „Eingeladene“ = alle aus der Kalendereinladung, nicht nur Anwesende.
- Teilnehmende werden benachrichtigt (Stift-Symbol). Admins können ausdrückliche Zustimmung vor Notizen/Aufnahme/
  Transkription verlangen – **standardmäßig aus**. Aufbewahrung nach Meet-Richtlinie der Organisation.
- Keine Aussage zum Modelltraining auf dieser Seite.

### 6. Zoom AI Companion – NICHT gelesen
- Datenschutzseite leitet auf https://library.zoom.com/ai/ai-whitepaper.md weiter; Abruf nicht freigegeben. **Ungeprüft.**
