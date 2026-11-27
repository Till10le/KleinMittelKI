# Kennzahlen

Baseline 20.11.2026. Nur tatsächlich gemessene Werte mit Quelle. Was nicht messbar war, steht als „nicht verfügbar“ mit Grund.
Fortschreibung wöchentlich (freitags): neue Spalte rechts anhängen, alte Werte nie überschreiben.
Messort: Box von Head of KMI, `curl` und Repo-Auswertung, jeweils eine Messung.

## Gemessen

| Kennzahl | Baseline 20.11.2026 | KW 48 (27.11.) | KW 49 (04.12.) | Quelle |
|---|---|---|---|---|
| Veröffentlichte Beiträge | 22 | 25 (neu: pwc-mittelstand-ki-controlling 23.11., ki-ablage-selbstversuch 23.11., #8 Die Ablage, die für mich mitdenkt 24.11.; alle von Till direkt in Ghost) | | `sitemap-posts.xml` (22 URLs) und `redaktion/blog-index.json` (Stand 19.11.) |
| Versendete Newsletter-Ausgaben | 7 (06.10. bis 17.11.) | | | `redaktion/blog-index.json`, Status `sent` |
| Entwürfe in Ghost | 8 | | | `redaktion/blog-index.json`, Status `draft` |
| Beiträge je Rubrik | Entwicklungen 7 · Studien & Zahlen 5 · Leitfäden 4 · KI in der Praxis 3 · Grundlagen 2 · Lageberichte 1 | | | `redaktion/blog-index.json` |
| Letzte Veröffentlichung | 13.11.2026 (modellwahl-kanonen-auf-spatzen) | 24.11.2026 (8-die-ablage-die-fuer-mich-mitdenkt) | | `sitemap.xml` lastmod Posts, Index |
| Seiten in der Sitemap | 13 Seiten, 22 Beiträge, 6 Tags, 1 Autor | | | `sitemap-*.xml` |
| Seitentitel über 60 Zeichen | 9 von 22 Beiträgen | 0 von 25 (nach SEO-002) | | `<title>` der Beitragsseiten |
| Meta-Beschreibung vorhanden | 22 von 22 Beiträgen (116–168 Zeichen) | | | `<meta name="description">` |
| Beiträge ohne Link auf andere Beiträge im Text | 6 von 22 | | | Artikel-HTML, Mustererkennung |
| Canonical, Open Graph, Twitter Card, Article-Schema | auf allen 22 Beiträgen und der Startseite vorhanden | | | Seitenquelltext |
| Antwortzeit Startseite / Beiträge | 0,3 s / 0,2–0,7 s (gesamt, 1 Messung) | 0,8 s Startseite (1 Messung) | | `curl -w %{time_total}`; Startseite 52 KB |
| Newsletter-Anmeldeformular | auf Startseite und jedem Beitrag; kein Portal-Skript, keine eigene Seite (`/newsletter/` = 404) | /newsletter/ weiterhin 404 | | Seitenquelltext, `curl` |
| `robots.txt`, RSS, `llms.txt` | vorhanden; RSS liefert 15 Einträge | RSS liefert 15 Einträge | | `curl` |

## Google Search Console (sc-domain:kleinmittelki.de)

Abgefragt am 27.11.2026 von Head of KMI über den Search-Console-Connector (`dataState: all`, 26.11. noch unvollständig). Datumsangaben in Pacific Time.

| Kennzahl | KW 48 (20.–26.11.2026) | Quelle |
|---|---|---|
| Klicks | 4 | Search Analytics, gesamt |
| Impressionen | 167 | Search Analytics, gesamt |
| Klickrate | 2,4 % | Search Analytics, gesamt |
| Ø Position | 23,0 | Search Analytics, gesamt |
| Stärkste Seite | ki-plakate-muessen-nicht-nach-ki-aussehen: 59 Impressionen, 2 Klicks, Ø Pos. 6,1 | Dimension page |
| Sitemap | eingereicht 45 URLs (+25 Bilder), „indexed“ 0 laut Sitemap-Bericht, zuletzt geladen 25.11. | listSitemaps |

Hinweis: Die Sitemap-Angabe „indexed 0“ ist bei neuen Properties oft verzögert; Klicks und Impressionen belegen, dass Seiten im Index sind. Vorwoche (13.–19.11.) nicht vergleichbar, Property erst seit 20.11.

## Aus Ghost (Admin API, nur lesen)

Gemessen am 20.11.2026, 17:12 UTC mit `python3 tools/ghost.py kennzahlen` (nur GET, Claude-Sitzung in „KMK-Ghost“, Aufgabe AUD-001).
Fortschreibung: Befehl erneut ausführen, neue Spalte rechts anhängen.

| Kennzahl | 20.11.2026 | Quelle |
|---|---|---|
| Mitglieder gesamt | 22 | `members/` (Seitenangabe `total`) |
| davon frei / bezahlt / geschenkt | 22 / 0 / 0 | `members/?filter=status:…` |
| Newsletter-Abos „KLEIN. MITTEL. KI.“ (aktiv) | 22 (22) | `newsletters/?include=count.members,count.active_members` |
| Beiträge veröffentlicht · nur Newsletter (`sent`) · eingeplant · Entwürfe · gesamt | 22 · 7 · 0 · 10 · 39 | `posts/?filter=status:…` |

Hinweis: Unter den 22 Mitgliedern ist Tills eigene Kontrolladresse (Mitglieder-Notiz „Redaktions-Kontrolle Newsletter“, seit 27.10.).

Fortschreibung KW 48: **nicht gemessen** – der Ghost-Admin-Schlüssel liegt nur in der Claude-Umgebung „KMK-Ghost“; seit dem Wochenbericht KW 47 (22.11.: 22 Mitglieder, 22 Abos) kein neuer `ghost.py kennzahlen`-Lauf im Repo.

### Newsletter je Versand

Öffnungsrate = geöffnet / zugestellt. Klickrate = Mitglieder mit mindestens einem Klick (Ghost `count.clicks`) / zugestellt.
Öffnungen sind ein Näherungswert (Apple Mail Privacy Protection meldet Öffnungen automatisch).

| Versand | Ausgabe | Empfänger | zugestellt | geöffnet | Öffnungsrate | Klicker | Klickrate |
|---|---|---|---|---|---|---|---|
| 17.11.2026 | #7: Welches KI-Modell für welche Aufgabe? | 22 | 22 | 12 | 54,5 % | 4 | 18,2 % |
| 10.11.2026 | #6: Folien ohne KI-Look und KI ohne Anwendungsfall | 22 | 22 | 12 | 54,5 % | 3 | 13,6 % |
| 03.11.2026 | #5: Was Betriebe bei KI bremst und wie viel Technik reicht | 22 | 22 | 12 | 54,5 % | 2 | 9,1 % |
| 27.10.2026 | #4: KI-Ergebnisse prüfen und wer für den Chatbot haftet | 22 | 22 | 13 | 59,1 % | 4 | 18,2 % |
| 20.10.2026 | #3: Was KI-Agenten können und warum gepflegtes Wissen zählt | 18 | 18 | 12 | 66,7 % | 4 | 22,2 % |
| 13.10.2026 | #2: Protokoll per KI – was gut lief und wo die Fehler steckten | 15 | 14 (1 fehlgeschlagen) | 9 | 64,3 % | 2 | 14,3 % |
| 06.10.2026 | #1: KI-Plakate müssen nicht nach KI aussehen | 8 | 8 | 6 | 75,0 % | 3 | 37,5 % |

Beobachtung (keine Bewertung): Die Empfängerzahl steht seit dem 27.10. bei 22; geöffnet haben seitdem je 12–13.
Nicht lesbar mit dem Integrations-Schlüssel: `emails/` (Ghost: „API tokens do not have permission to access this endpoint“), Seitenaufrufe/Besucher.

## Nicht verfügbar

| Kennzahl | Grund |
|---|---|
| Mitglieder / Newsletter-Abonnenten (gesamt, frei, bezahlt) | **Überholt 20.11.2026:** jetzt gemessen, siehe „Aus Ghost“. Ursprünglich: Kein Ghost-Admin- oder Content-Schlüssel auf der Box; er liegt nur in der Claude-Umgebung „KMK-Ghost“. `tools/ghost.py` hat keinen Lesebefehl dafür (Aufgabe AUD-001) |
| Öffnungs- und Klickrate der Newsletter | **Überholt 20.11.2026:** jetzt gemessen, siehe „Aus Ghost“. Ursprünglich: wie oben |
| Seitenaufrufe, Besucher, Herkunft | Ghost Analytics nur mit Admin-Zugang einsehbar; kein Zugang |
| Google-Klicks, Impressionen, Position, Indexabdeckung | Search Console kennt `kleinmittelki.de` nicht (das Konto sieht nur `sc-domain:tributoo.com`); Aufgabe SEO-001 |
| Anzahl indexierter Seiten | `site:`-Suche lieferte keine Ergebnisse (kein Beleg für oder gegen Indexierung); Search Console fehlt |
| Backlinks, LinkedIn-Follower und -Reichweite | kein Zugang, keine Auswertung eingerichtet |
