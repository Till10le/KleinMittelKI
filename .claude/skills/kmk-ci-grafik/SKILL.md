---
name: kmk-ci-grafik
description: CI von KLEIN. MITTEL. KI. (Farben, Schriften, Logo, Bildsprache) und der feste Grafik-Baukasten für Beiträge – HTML-Bausteine, PNG-Schaubilder und Vorschaubild. Laden, bevor eine Grafik, ein Schaubild, ein Vorschaubild oder ein Newsletter-Element entsteht oder geprüft wird.
---

# CI und Grafik-Baukasten

Look: Schwarz-Weiß mit Neon-Lime als einzigem Akzent. Lime markiert genau eine Sache (Balken, Kante, Badge auf Schwarz),
nie als Textfarbe auf Weiß, nie flächig.

## Farben

| Rolle | Wert | Einsatz |
|---|---|---|
| Ink | `#111111` | Schrift, dunkle Boxen, Rahmen |
| Weiß | `#FFFFFF` | Seite, Vorschaubilder |
| Lime | `#D7FF00` | Akzent: Balken, Kanten, Badge „Ja“, Zahlen auf Schwarz |
| Grau | `#45453F` | Meta-Zeilen, „kleinmittelki.de“ im Vorschaubild |
| Grau hell | `#5E5E57` | Bildunterschriften |
| Paper | `#F4F3EE` | Kästen, Urteils-Boxen, Text auf Schwarz |
| Kastenfläche | `#F4F4EF` | Karten in Grafiken |
| Linie | `#E2E2DE` | Rahmen von Listen-Karten |

Entschieden 19.10.2026: Für alles, was wir erzeugen, gilt `#D7FF00` – so steht es in allen veröffentlichten Beiträgen.
Das Logo-Paket v4 (`#D4FF00`) bleibt unverändert; der Unterschied ist nicht sichtbar.

## Schriften

- **Schibsted Grotesk 700/800** – Überschriften, Titel im Vorschaubild, große Zahlen
- **Instrument Sans 400–600** – Fließtext, Labels, Kategorie in Versalien mit Laufweite
- Dateien liegen in `assets/fonts/` (SIL Open Font License). Nie andere Schriften verwenden.
- Logo: Block-System v4 (drei Quadrate 5:8:13, Lime-Quadrat als Punkt). Tills Original-Paket liegt in
  `assets/logo-v4/` (SVG und PNG, alle Varianten, `Markenbasics.txt`). Nur diese Dateien verwenden, nie nachbauen.
  Vorschaubild: `assets/logo.png` = `kmk-horizontal-light-transparent.png` (Querformat mit Unterzeile).
  Dunkler Grund: `*-dark-*`; Profilbild/Social: `kmk-avatar-*`; sehr klein: `kmk-k-block-*`.

## Vorbild: die veröffentlichten Beiträge (Stand 19.10.2026)

Alle Beiträge liegen als HTML in `redaktion/referenz/` (`python3 tools/ghost.py referenz`, nur lesen).
Vor jeder Grafik einen Beitrag desselben Formats dort ansehen. Was die Auswertung von 16 Beiträgen ergab:

| Format | Grafiken im Beitrag | Art |
|---|---|---|
| Nachricht | meist 0, höchstens 1 | ein PNG-Schaubild, wenn ein Ablauf oder Stufen es klarer machen; **neu (Till, 19.10.):** hat die Meldung eine starke, belegte Zahl, eine Kennzahl-Grafik (`g-zahlen` oder HTML `kennzahl`) |
| Langtext (Grundlagen) | 4–5 | PNG-Schaubilder im Karten-System, je Hauptabschnitt eins |
| Leitfaden Rechtslage | 2 | HTML-Karten: Rollen/Fälle (`urteil-und-pruefliste`), Prüfliste |
| Lagebericht | 3+ | HTML-Karten: Balken und Kennzahlen mit Quelle `[n]` |
| Praxistest | 1–4 | echte Fotos/Screenshots (anonymisiert) + höchstens ein Schaubild |
| Newsletter | keine Grafik | Bookmark-Karten zu den Beiträgen |

## Regeln für jede Grafik

1. Eine Grafik nur, wenn sie etwas zeigt, das Text schlechter kann: Ebenen, Abläufe, Vergleiche, Checklisten, Zahlen.
2. Aufbau wie veröffentlicht: **Kicker** (kurzes Stichwort, z. B. „So hängt es zusammen“, „Woher die Unterschiede kommen“),
   **Titel als Aussage**, Inhalt, **Fußzeile** links „Vereinfachte Darstellung · Stand: TT.MM.JJJJ · Quelle: …“, rechts **kleinmittelki.de**,
   unten Lime-Kante. Keine Nummerierung „Grafik 01“ im Bild.
3. **Bildunterschrift** in Ghost: ein Satz, der beim Lesen hilft – die Kernaussage oder die Grenze, nicht die Quelle.
   Beispiele: „Der entscheidende Unterschied: Du musst nicht mehr jeden Schritt selbst anstoßen.“ ·
   „Vereinfachte Einordnung. Die genannten Anbieter sind Beispiele, keine Empfehlung.“ ·
   „Zum Abhaken: Je mehr Ja, desto besser eignet sich der Ablauf als Einstieg.“
   Ausnahme Daten-Karten (Balken, Kennzahl): Bildunterschrift nennt Quelle, Grundgesamtheit und Stand.
4. **Alt-Text** beschreibt Art und Inhalt: „Schaubild: …“, „Checkliste mit fünf Fragen: …“, „Stufenmodell mit vier Stufen: …“.
5. „Was die Grafik zeigt: …“ im Text nur bei Daten-Karten (Lagebericht, Studien), nicht bei Erklär-Schaubildern.
6. Nur Werte aus der Quelle (`entwuerfe/<slug>/quellen.md`). Eigene Darstellung kennzeichnen.
7. Nur Bausteine aus `vorlagen/` und `tools/grafik_basis.css`. Keine neuen Farben, Schatten, Verläufe, Icons oder Emojis.

## Baukasten (HTML-Karten im Beitrag, Vorlagen in `vorlagen/`)

| Baustein | Datei | Wofür |
|---|---|---|
| Balkengrafik | `balken.html` | Anteile nach Gruppe, 3–6 Balken |
| Kennzahl(en) | `kennzahl.html` | Eine oder zwei Zahlen mit Lesehinweis |
| Kurzfassung | `kurz.html` | „Das Wichtigste in 30 Sekunden“, genau 5 Punkte |
| Prompt, Hinweis, Serienkopf, Abschnittskopf, Einordnung, Quellenliste | `kaesten.html` | siehe Kommentare in der Datei |
| Ablauf, Karten, Stufenliste, Vergleich, Vorher/Nachher | `ablauf-und-karten.html` | Prozesse, Faktoren, Regeln, Gegenüberstellungen |
| Urteils-Box, Prüfliste | `urteil-und-pruefliste.html` | Ja/Nein/Kommt darauf an, Fallübersicht |

Im `beitrag.md` werden Bausteine als HTML-Block geschrieben:

````
```html
<figure class="kmk-chart">…</figure>
```
````

`tools/lexical.py` macht daraus eine HTML-Karte in Ghost.

## Erklär-Schaubilder als PNG (Karten-System)

So sehen die veröffentlichten Schaubilder aus (`kmk-ki-modelle-g1…g4`, `kmk-ki-agenten-g1…g5`), und so baut sie `tools/grafik.py`:
weiße Karte 800 px (gerendert 1600 px), Rand 44 px, Kicker in Versalien mit Lime-Strich, Titel Schibsted 38 px,
Kästen mit 2 px schwarzem Rahmen, eine Hervorhebung schwarz (`--dunkel`) oder Lime, Fußzeile mit Linie, Lime-Kante 8 px.

| Baustein (`tools/grafik_basis.css`) | Wofür | Vorbild |
|---|---|---|
| `g-spalten` / `g-spalten--pfeile` + `g-box`, `g-pfeil`, `g-kopf`, `g-trenner` | Ebenen nebeneinander, Ablauf links → rechts | Anbieter → Produkt → Modell |
| `g-stufen` + `g-stufe`, `g-nr` | Stufen, Schritte, Reifegrad untereinander | Vier Stufen (Modelle), Einstieg in vier Stufen (Agenten) |
| `g-check` | Fragen zum Abhaken | Fünf Fragen für den ersten Anwendungsfall |
| `g-tabelle` + `g-zeile--dunkel/--lime`, `g-lv`, `g-ja/g-nein` | Vergleich nach Merkmalen | Chatbot · Automatisierung · Agent; Modellstufen |
| `g-zahlen` + `g-zahl(--dunkel)` | zwei Zahlen mit Lesehilfe | „× 100“ / „× 10“ |
| `g-raster(--3)` + `g-karte(--dunkel)`, `g-tag`, `g-legende` | Anbieter, Wege, Beispiele als Karten | Weitere Anbieter; drei Wege zum Agenten |
| `g-vergleich` | zwei Spalten gegenüber (Vorher/Nachher, Chatbot/Agent) | Chatbot vs. Agent an der Mietanfrage |
| `g-notiz` mit `<mark>` | ein Merksatz unter dem Inhalt | „Ein Produkt, Motoren von zwei Herstellern.“ |

Ablauf: HTML-Fragment `entwuerfe/<slug>/g1.html` (Beispiel im Kopf von `tools/grafik.py`) →
`python3 tools/grafik.py entwuerfe/<slug>/g1.html --out entwuerfe/<slug>/kmk-<thema>-g1.png`.
Das Skript verweigert Grafiken ohne Kicker, Titel oder Fußzeile und setzt die Lime-Kante selbst.
Im `beitrag.md`: `![Schaubild: …](kmk-<thema>-g1.png "Ein Satz Lesehilfe")` – `tools/ghost.py draft` lädt lokale Bilder hoch.
**Ansehen ist Pflicht:** Jedes PNG mit dem Read-Werkzeug öffnen (abgeschnittene Wörter, Überlappungen, Trennstriche im Titel).
Texte in der Grafik kurz halten: Titel höchstens zwei Zeilen, Kastentext höchstens zwei Zeilen.
**Immer mit `--social`** rendern: Das erzeugt zusätzlich `kmk-<thema>-gN-social.png` (1080 × 1350) für LinkedIn und Instagram.
Die Kachel nicht in den Beitrag einbinden; auch sie ansehen.

## Vorschaubild (Pflicht für jeden Beitrag, 1200 × 630)

`python3 tools/vorschaubild.py --kategorie "Studien & Zahlen" --titel "…" --out entwuerfe/<slug>/vorschaubild.png`

- Weißer Hintergrund, Rand 84 px
- Oben Kategorie in Versalien (Instrument Sans 600, 24 px, Laufweite 4 px, `#111111`), darunter Lime-Balken 6 px in Textbreite
- Titel Schibsted Grotesk 700, Start 68 px, Zeilenhöhe 1,1, höchstens 3 Zeilen, in 4-px-Schritten bis 48 px verkleinern
- Unten links Logo (340 px breit), unten rechts „kleinmittelki.de“ in `#45453F`, unten Lime-Kante 14 px über die volle Breite
- Wird als `og_image`, `twitter_image` und als Titelbild `titel-<slug>.jpg` (`feature_image`) gesetzt.
  OFFEN: Ob das Titelbild auch `feature_image` sein soll, ist mit Till zu klären; die veröffentlichten Beiträge nutzen es so.

## „Eine Zahl, genau gelesen“ (Startseite)

Band unter dem Hero, Werte im Objekt `KMK_ZAHL` im Footer-Code der Seite (`zahl`, `text`, `genau`, `link`).
Liefert ein neuer Beitrag eine stärkere, belegte Zahl: im Themenboard als Vorschlag für Till eintragen. `genau` erklärt
immer, wie die Zahl richtig zu lesen ist, und nennt die Quelle. Ändern nur nach Freigabe.

## Bildsprache

- Echte Fotos (Till, eigene Aufnahmen aus Tests). Nie Stockbilder, nie KI-generierte Menschen.
- Screenshots anonymisieren: keine Namen, Mailadressen, internen Inhalte.
- Keine Logos oder Motive von Parteien und Marken als Aufmacher.
