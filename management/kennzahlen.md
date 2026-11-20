# Kennzahlen

Baseline 20.11.2026. Nur tatsächlich gemessene Werte mit Quelle. Was nicht messbar war, steht als „nicht verfügbar“ mit Grund.
Fortschreibung wöchentlich (freitags): neue Spalte rechts anhängen, alte Werte nie überschreiben.
Messort: Box von Head of KMI, `curl` und Repo-Auswertung, jeweils eine Messung.

## Gemessen

| Kennzahl | Baseline 20.11.2026 | KW 48 (27.11.) | KW 49 (04.12.) | Quelle |
|---|---|---|---|---|
| Veröffentlichte Beiträge | 22 | | | `sitemap-posts.xml` (22 URLs) und `redaktion/blog-index.json` (Stand 19.11.) |
| Versendete Newsletter-Ausgaben | 7 (06.10. bis 17.11.) | | | `redaktion/blog-index.json`, Status `sent` |
| Entwürfe in Ghost | 8 | | | `redaktion/blog-index.json`, Status `draft` |
| Beiträge je Rubrik | Entwicklungen 7 · Studien & Zahlen 5 · Leitfäden 4 · KI in der Praxis 3 · Grundlagen 2 · Lageberichte 1 | | | `redaktion/blog-index.json` |
| Letzte Veröffentlichung | 13.11.2026 (modellwahl-kanonen-auf-spatzen) | | | `sitemap.xml` lastmod Posts, Index |
| Seiten in der Sitemap | 13 Seiten, 22 Beiträge, 6 Tags, 1 Autor | | | `sitemap-*.xml` |
| Seitentitel über 60 Zeichen | 9 von 22 Beiträgen | | | `<title>` der Beitragsseiten |
| Meta-Beschreibung vorhanden | 22 von 22 Beiträgen (116–168 Zeichen) | | | `<meta name="description">` |
| Beiträge ohne Link auf andere Beiträge im Text | 6 von 22 | | | Artikel-HTML, Mustererkennung |
| Canonical, Open Graph, Twitter Card, Article-Schema | auf allen 22 Beiträgen und der Startseite vorhanden | | | Seitenquelltext |
| Antwortzeit Startseite / Beiträge | 0,3 s / 0,2–0,7 s (gesamt, 1 Messung) | | | `curl -w %{time_total}`; Startseite 52 KB |
| Newsletter-Anmeldeformular | auf Startseite und jedem Beitrag; kein Portal-Skript, keine eigene Seite (`/newsletter/` = 404) | | | Seitenquelltext, `curl` |
| `robots.txt`, RSS, `llms.txt` | vorhanden; RSS liefert 15 Einträge | | | `curl` |

## Nicht verfügbar

| Kennzahl | Grund |
|---|---|
| Mitglieder / Newsletter-Abonnenten (gesamt, frei, bezahlt) | Kein Ghost-Admin- oder Content-Schlüssel auf der Box; er liegt nur in der Claude-Umgebung „KMK-Ghost“. `tools/ghost.py` hat keinen Lesebefehl dafür (Aufgabe AUD-001) |
| Öffnungs- und Klickrate der Newsletter | wie oben |
| Seitenaufrufe, Besucher, Herkunft | Ghost Analytics nur mit Admin-Zugang einsehbar; kein Zugang |
| Google-Klicks, Impressionen, Position, Indexabdeckung | Search Console kennt `kleinmittelki.de` nicht (das Konto sieht nur `sc-domain:tributoo.com`); Aufgabe SEO-001 |
| Anzahl indexierter Seiten | `site:`-Suche lieferte keine Ergebnisse (kein Beleg für oder gegen Indexierung); Search Console fehlt |
| Backlinks, LinkedIn-Follower und -Reichweite | kein Zugang, keine Auswertung eingerichtet |
