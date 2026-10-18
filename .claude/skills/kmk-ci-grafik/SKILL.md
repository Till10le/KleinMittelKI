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

OFFEN: Das Logo-Paket v4 nutzt `#D4FF00`. Bis Till entscheidet, gilt `#D7FF00` für alles, was wir erzeugen.

## Schriften

- **Schibsted Grotesk 700/800** – Überschriften, Titel im Vorschaubild, große Zahlen
- **Instrument Sans 400–600** – Fließtext, Labels, Kategorie in Versalien mit Laufweite
- Dateien liegen in `assets/fonts/` (SIL Open Font License). Nie andere Schriften verwenden.
- Logo: Block-System v4 (drei Quadrate 5:8:13, Lime-Quadrat als Punkt). Datei: `assets/logo.png`.
  Fehlt sie, lädt `tools/vorschaubild.py` sie beim ersten Lauf von storage.ghost.io (geht in der Umgebung „KMK-Recherche“).
  Danach `assets/logo.png` committen, damit alle Umgebungen sie haben.

## Typografische Muster

- Nummerierung „01 · Abschnitt“
- Kategorie-Label in Versalien mit Laufweite, darunter ein Lime-Balken
- Grafik-Kopf: „Grafik 01 / Thema“, dann die **Aussage als Titel** (nicht das Thema)

## Regeln für jede Grafik

1. Eine Grafik nur, wenn sie etwas zeigt, das Text schlechter kann: Zahlen, Abläufe, Vergleiche, Entscheidungen.
   Ziel pro Beitrag: Nachricht 0–1, Anleitung 1–2, Langtext und Lagebericht 3–4.
2. Kopfzeile „Grafik NR / Thema“, Titel als Aussage, Unterzeile: was, wo, wann.
3. Bildunterschrift mit Quelle, Grundgesamtheit und Stand; bei Bedarf „Vereinfachte Darstellung“ oder „keine Rechtsberatung“.
4. Direkt danach im Text ein Satz „Was die Grafik zeigt: …“ mit der Grenze der Aussage.
5. Nur Werte aus der Quelle (`entwuerfe/<slug>/quellen.md`). Eigene Darstellung kennzeichnen.
6. Nur Bausteine aus `vorlagen/`. Keine neuen Farben, Schatten, Verläufe, Icons oder Emojis.

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

## Erklär-Schaubilder als PNG

Für Zusammenhänge mit Ebenen, Stufen oder Gruppen (z. B. „Anbieter, Produkt, Modell“): `tools/grafik.py`.
Du schreibst ein kleines HTML-Fragment mit den CSS-Klassen aus `tools/grafik_basis.css`, das Skript rendert es mit den
CI-Schriften in 1600 px Breite (doppelte Auflösung) als PNG und reduziert auf 48 Farben.
Dateiname `kmk-<thema>-g1.png` im Entwurfsordner, Bildunterschrift mit „Stand: TT.MM.JJJJ“. Im `beitrag.md` als
`![Alt](kmk-<thema>-g1.png "Bildunterschrift")` einbinden – `tools/ghost.py draft` lädt lokale Bilder selbst hoch.
**Ansehen ist Pflicht:** Jedes PNG nach dem Rendern mit dem Read-Werkzeug öffnen und prüfen (abgeschnittene Wörter, Überlappungen).

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
