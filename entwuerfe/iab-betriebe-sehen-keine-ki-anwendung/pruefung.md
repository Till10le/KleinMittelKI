# Prüfung: iab-betriebe-sehen-keine-ki-anwendung

Datum: 23.10.2026 · Prüfung im Chat-Lauf (Claude, auf Tills Auftrag im Chat), kein separater Prüfer-Agent.

## Ergebnis: BESTANDEN (mit offenen Punkten für Till)

| Nr. | Punkt | Ergebnis |
|---|---|---|
| 1 | Zahlen, Daten, Namen | jede Zahl gegen quellen.md abgeglichen; nur Werte aus der Originalquelle |
| 2 | Grundgesamtheit/Einschränkungen | genannt (Basis, Zeitraum, Erfahrungswert statt Studie) |
| 3 | Originalveröffentlichung verlinkt | ja, Zweitverwertungen nicht als Beleg |
| 4 | Ich-Aussagen | „Meine Einordnung“ komplett im INTERN-Absatz als Vorschlag markiert |
| 5 | Platzhalter | keine |
| 6 | Format und Längen | H2 exakt, Abschnitte im Rahmen, Teaser 90–160 Zeichen, Für KMU 50–120 Zeichen, eine Grafik |
| 7 | CI | Schaubild mit tools/grafik.py (+ social), Titelbild ohne Titel, Vorschaubild 1200 × 630 – alle angesehen |
| 8 | Regeln 4/5/7 | kein Arbeitgeber, kein Handel, keine Vertriebs-CTAs; konkrete Betriebsgrößen/Prozesse genannt |
| 9 | lexical.py | fehlerfrei |

Offen für Till: eigene Einordnung in 2–3 Sätzen oder Freigabe des Vorschlags.

# Finale Prüfung (09.11.2026, Chat)

Prüfer-Agent, geprüft vor Tills Freigabe für das Erscheinen am Di 10.11.2026, 7:00 (statt Do 12.11.). Anlass ist die neue Grafik g1 mit zwei Karten.

## Ergebnis: NICHT BESTANDEN

Zwei Punkte sind inhaltlich und gehen an Till bzw. die Grafik. Die übrigen Punkte sind ok.

### Mängel

1. **Fakten nicht selbst gegengelesen (Punkt 1).** idw-online.de und iab-forum.de sind in dieser Sitzung gesperrt
   (Proxy 403 bzw. DNS). Damit beruhen alle Zahlen auf quellen.md vom 23.10. Eine Websuche bestätigt nur: Die 85 Prozent
   stammen vom IAB und beziehen sich auf Nichtnutzer (Sekundärbericht IHK/CIO). Für die 91 Prozent fand die Suche keinen
   Beleg. Offen ist auch, ob sich 85/91 Prozent wie die 88 Prozent auf Betriebe beziehen, die KI „weder nutzen noch planen“,
   oder auf alle Betriebe ohne KI.
   → Vor der Freigabe die Pressemitteilung (Absatz zum Potenzial) aufrufen und Basis sowie 91 Prozent wörtlich bestätigen.
   Gilt die engere Basis, heißt es in der Grafik „der Betriebe ohne KI-Pläne“, in der Bildunterschrift ebenso.
2. **Die Aussage der Grafik geht weiter als die Daten (Punkt 11).** Dazu gehören der Titel „sehen fast alle Betriebe ohne KI keine
   Anwendung“, die Notiz „egal wie viel Potenzial da ist“ und im Text „Unter den übrigen sieht aber fast jeder keine
   Anwendung, egal wie groß das Potenzial ist“. 85 Prozent sind die große Mehrheit, nicht „fast jeder“. Zwischen 85 und
   91 Prozent liegen sechs Punkte, „egal“ ist also zu stark. Die Quelle sagt „selbst wenn … 85 Prozent“. Gedeckt ist „auch bei
   viel Potenzial“, nicht „egal wie viel“. Außerdem ist „die übrigen“ ungenau (siehe Mangel 1).
   → Vorschlag Notiz: „Wer KI nicht nutzt, sieht meist keine Anwendung, <mark>auch wo viel Potenzial da ist.</mark>“
   Titel: „Auch wo KI viel könnte, sieht die große Mehrheit der Betriebe ohne KI keine Anwendung“.
   Text: „Wo KI viel könnte, nutzen sie deutlich mehr Betriebe. Von den Betrieben ohne KI sehen aber auch dort 85 Prozent
   keine Anwendung.“ Danach g1 neu rendern (mit --social) und ansehen.

### Hinweise (kein Mangel)

- Social-Kachel g1: große Leerfläche zwischen Titel und Karten. Bitte beim Neu-Rendern ansehen.
- In g1 sind beide Karten dunkel hervorgehoben, dazu kommt die Lime-Markierung. Wegen des parallelen Aufbaus ist das vertretbar.
- Der Fahrplan (`redaktion/fahrplan.md`) nennt noch Do 12.11. Die Verschiebung auf Di 10.11. trägt der Chefredakteur nach.
  Eine Freigabe liegt noch nicht vor.

### Punkte ok

- Format Nachricht: H2 exakt. Wörter: 108 (davon rund 26 für „Was die Grafik zeigt“), 102, 98 und 19, zusammen 327, mit Grafik im Rahmen.
  Teaser 138 Zeichen, nicht gleich dem Titel. „Für KMU“ 101 Zeichen. Kategorie Studien & Zahlen + #empfehlung. Aufbau wie
  der Referenzbeitrag eu-eurobarometer-ki-unternehmen.
- Ton: keine Floskeln, kein Hype, keine CTAs, kein Handel oder Arbeitgeber. KMU-Bezug: fünf Leute, drei Filialen, Anfrage per Mail.
- INTERN-Absatz: Er nennt die ganze Einordnung, die Beispiele und den Gedanken als Vorschlag. Keine Platzhalter. Beim
  Veröffentlichen entfernt ihn ghost.py. In der Vorschau ist er sichtbar, wie bei Entwürfen üblich.
- Zeitangaben für den 10.11.: „Bitkom im September“ stimmt (14.09.2026). „ein Jahr alt“ heißt jetzt „gut ein Jahr alt“
  (2. Halbjahr 2025).
- Interner Link zum Lagebericht September erreichbar, 30 Prozent und „ab 20 Beschäftigten“ stimmen.
- Originalveröffentlichungen verlinkt (IAB-Forum, Pressemitteilung), keine Zweitverwertung.
- Titelbild (Kerngeschäft → Büro, Merksatz, ohne Titel), Vorschaubild (3 Zeilen, Logo, Lime-Kante) und g1 angesehen.
  Werte 41/13/85/91 stimmen mit quellen.md. Alt-Text vorhanden.
- Ghost-Vorschau: Nummerierung, Box, zwei Quellenkarten, Beitragsbild ohne Titel-Kachel.

### Geändert (formal) und Ghost-Entwurf aktualisiert (`tools/ghost.py draft`)

- Bildunterschrift g1: Grundgesamtheit ergänzt („Die Nutzungsanteile beziehen sich auf alle Betriebe einer Gruppe, die
  Anteile ohne passende Anwendung nur auf die Betriebe ohne KI.“). Daten-Karten verlangen das nach kmk-ci-grafik.
  Falls Mangel 1 die engere Basis ergibt, hier anpassen.
- „Die Befragung ist ein Jahr alt“ → „gut ein Jahr alt“.
