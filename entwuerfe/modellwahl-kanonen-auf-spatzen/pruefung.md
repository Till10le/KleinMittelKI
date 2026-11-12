# Prüfung: modellwahl-kanonen-auf-spatzen

- Datum: 10.11.2026 (Redaktions-Lauf Di 12:47, Prüfrunde 1)
- Prüfer: Prüfer-Agent, unabhängig
- Ergebnis: **NICHT BESTANDEN**

Grund: Eine Kernaussage zu den Abo-Limits ist mit der verlinkten Quelle nicht mehr belegbar (Seite 404), und die heute
erreichbare Anthropic-Seite sagt etwas anderes. Betroffen sind Text, Grafik g2 und Quellenliste. Dazu kommt eine
Pauschalaussage zur Abo-Rechnung, die der Hersteller widerlegt, und der Text ist etwas zu lang. Alles andere ist in Ordnung.

## Mängel (müssen behoben werden)

### M1 – Opus „verbraucht das Wochenlimit schneller als Sonnet“: Quelle weg, Aussage nicht belegt (Punkt 1, 3, 11)
- Fundstellen: beitrag.md Abschnitt „Was der Sprit kostet“, Absatz **Limits** (Satz „Für Team- und Enterprise-Plätze schreibt
  Anthropic ausdrücklich, dass Opus das Wochenlimit schneller verbraucht als Sonnet, und empfiehlt Sonnet für den Alltag.“);
  Grafik `kmk-modellwahl-g2.png` (Abo-Kasten, dritter Punkt „Opus verbraucht das Wochenlimit schneller als Sonnet“);
  Quellenliste, Eintrag „About Team and Enterprise plan usage“.
- Befund: https://support.claude.com/en/articles/9267304-about-team-and-enterprise-plan-usage liefert am 10.11.2026 **HTTP 404**,
  auch ohne Slug. quellen.md hatte schon gewarnt, dass die Seite nur alte Modellnamen (Opus 4.5/Sonnet 4.5) nannte.
  Die aktuellen Help-Center-Seiten sagen etwas anderes:
  - „Usage limit best practices“ (https://support.claude.com/en/articles/9797557-usage-limit-best-practices) nennt die
    **Modellwahl** als Faktor, sagt aber nicht, welches Modell das Limit wie schnell verbraucht. Opus und Sonnet kommen dort
    nicht vor, eine Empfehlung für den Alltag auch nicht.
  - „Claude Fable models on your plan“ (https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan):
    Fable-Modelle „draw from your plan's regular weekly usage limits and use them faster than other Claude models“. Das gilt
    für Max, Ultra und **Premium-Plätze** in Team und sitzbasiertem Enterprise, dort höchstens 50 % des Wochenlimits für Fable.
    Auf **Standard-Team-Plätzen** und bei Pro läuft Fable nur über Nutzungsguthaben (usage credits) und zählt nicht gegen das Limit.
- Korrektur, Text, z. B.: „**Limits:** Laut [Anthropic](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)
  hängt die Nutzungsgrenze unter anderem von der Länge der Nachrichten, der Größe der Dateien und von der Modellwahl ab. Beim
  stärksten Modell schreibt Anthropic es [ausdrücklich](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan):
  Fable verbraucht das Wochenlimit schneller als die anderen Claude-Modelle. Auf Standard-Plätzen im Team-Abo läuft Fable
  nur über zusätzlich bezahltes Guthaben. Wer morgens für jede Kleinigkeit das größte Modell nimmt, steht nachmittags bei der
  wichtigen Auswertung womöglich an der Grenze.“
- Korrektur, Grafik g2 (Grafik-Agent, neu rendern mit `--social`): dritten Punkt ersetzen, z. B. „Das stärkste Modell
  verbraucht das Wochenlimit schneller“. Die Fußzeile bleibt: „Quelle: Anthropic Help Center, Anthropic-Preisliste“.
- Korrektur, Quellen: Eintrag 9267304 streichen. Dafür „Claude Fable models on your plan“ aufnehmen und den Link auf
  9797557 auf die volle URL „…/9797557-usage-limit-best-practices“ ändern. quellen.md Abschnitt 4 nachziehen.

### M2 – „Die Rechnung am Monatsende ändert sich nicht, egal welches Modell“ stimmt so nicht mehr (Punkt 1)
- Fundstellen: beitrag.md Absatz 1 in „Was der Sprit kostet“; Box „Das Wichtigste in 30 Sekunden“, Punkt 2 („Im Abo zahlst
  du pro Platz … Echtes Geld kostet sie erst bei eigenen Anwendungen“); g2 Abo-Kasten, Punkt 1 („Rechnung bleibt gleich“);
  Schlussabschnitt Satz 1.
- Befund: Laut derselben Fable-Seite geht Fable auf Standard-Team-Plätzen und bei Pro nur über Nutzungsguthaben, also mit
  echtem Geld. Die Aussage stimmt für die üblichen Modelle, aber nicht pauschal. Das stützt die These des Beitrags sogar.
- Korrektur: einschränken, z. B. „Solange niemand Zusatzguthaben nutzt, ändert sich die Rechnung am Monatsende nicht.
  Ausnahme: Das stärkste Claude-Modell läuft auf Standard-Plätzen nur über solches Guthaben.“ In der Box reicht
  „… meist nicht über die Rechnung“. In g2 z. B. „Preis pro Platz, Rechnung meist gleich“.

### M3 – Länge über dem Rahmen (Punkt 6, 14)
- Befund: Ohne INTERN-Absatz und Platzhalter hat der Text rund 2.050 Wörter bis „Quellen“ und rund 2.190 mit Quellenliste.
  Die Vorgabe für einen Langtext ist 1.900–2.000. Zum Vergleich die Referenzbeiträge, gleich gezählt mit Quellen:
  Agenten 1.977, Modelle 1.919. Damit liegt der Text etwa 10 % darüber.
- Korrektur: um rund 150 Wörter kürzen. Kandidaten: im Abschnitt „Billig ist nicht immer günstig“ den Satz zu den zwei
  Entwickler-Wegen streichen (für Abo-Nutzer ohne Nutzen); FrugalGPT auf einen Satz kürzen; im Absatz **Strom** den Satz mit
  den Denk-Tokens (543,5/37,7) streichen; die Doppelung „Wie viel ein Router spart …“ streichen, weil sie schon in der
  Bildunterschrift von g4 steht.

## Hinweise (kein Mangel, zur Entscheidung)

- H1: „Sonnet für die meisten Anwendungen“ steht so in der Preisliste („Sonnet for most production workloads“). Die Seiten
  „Models overview“ und „Choosing the right model“ sagen dagegen „start with Claude Opus 5.5 for most workloads“. Das ist
  belegt, aber selektiv. Vorschlag: „Sonnet für Alltagsarbeit wie Texte und Datenanalyse“ (Auswahlmatrix), dann ist es eindeutig.
- H2: Unter der H2 „Zum Ausprobieren: drei Aufgaben, zwei Stufen“ steht eine Box mit eigener Überschrift „Zum Ausprobieren:
  die eigene Faustregel …“. Das wirkt doppelt. Im Agenten-Referenzbeitrag steht die Box ohne eigene H2. Vorschlag: Box-Kopf
  auf „Die eigene Faustregel in einer halben Stunde“ kürzen oder die H2 weglassen.
- H3: Bei den Versuchen zu Antwortlänge und Tabelle hat Anthropic ältere Modelle gemessen (laut Seite „earlier model“ bzw.
  Sonnet 5). Der Text nennt kein Modell und ist damit korrekt. Optional „mit einem älteren Modell“ ergänzen.

## Checkliste

| Nr. | Punkt | Ergebnis |
|---|---|---|
| 1 | Zahlen gegen Originalquelle | **Mangel M1, M2.** Selbst geprüft und ok: Preise Haiku/Sonnet/Opus/Fable, Faktoren 20/40/80, eigene Rechnung 0,35/7/14/28 $, Tests (85/91 %, 1/20, 4,3-fach, 7 %), Antwortlänge 0,49/0,57/1,40 $, Tabelle 7/25 bei 5,01 $ und 25/25 bei 0,40 $, Prompt Caching, „directional, not guarantees“, Denkaufwand als Hebel, zwei Startwege, Stapel 50 %, Haiku „classification, extraction, routing“. **Nicht selbst prüfbar** (Host in dieser Umgebung gesperrt): lmsys.org (RouteLLM), arxiv.org (FrugalGPT), frontiersin.org (Dauner/Socher), help.openai.com (Auto, Admin-Umleitung, Modellwahl im Eingabefeld ab April 2026). Diese Angaben stimmen mit quellen.md überein; vor der Freigabe einmal im offenen Netz gegenlesen. |
| 2 | Grundgesamtheit und Einschränkungen | ok (Herstellermessung, offene Modelle, Forschung 2023/2024, API statt Chat, Annahme 2.000/300) |
| 3 | Originalveröffentlichung verlinkt | Mangel M1 (toter Link 9267304). Sonst Originale verlinkt |
| 4 | Keine erfundene Ich-Form, INTERN vollständig | ok, keine Ich-Form im Text, Vorschläge im INTERN-Absatz aufgezählt |
| 5 | Platzhalter | ok, zwei `[TILL: …]` bewusst offen und im INTERN-Absatz genannt |
| 6 | Überschriften, Länge, Teaser | Mangel M3 (Länge). Teaser 152 Zeichen, ungleich Titel, ok. Struktur nach Langtext ok |
| 7 | Rubrik, Kategorie, Tags | ok (Wissen / Leitfäden, `#wissen`) |
| 8 | „Für KMU“-Zeile | entfällt (kein Aktuell-Beitrag) |
| 9 | Ton und Verbote | ok, kein Hype, kein CTA, kein Handel, kein Arbeitgeber-Bezug |
| 10 | KMU-Bezug | ok (10–150 Leute, Ingenieurbüro mit 40 Leuten, Hausverwaltung, Lizenzverwaltung/Büroleitung) |
| 11 | Grafiken | Mangel M1/M2 in g2. g1, g3, g4: Baukasten, Titel als Aussage, Fußzeile mit Stand und Quelle, Alt-Texte und Bildunterschriften ok, Werte stimmen |
| 12 | Vorschaubild | ok, drei Zeilen, Logo, Lime-Kante |
| 12a | Titelbild | ok, ohne Titel, ein Merksatz, keine Zahl, `titelbild:` im Frontmatter |
| 13 | Ghost-Vorschau | ausgelassen (noch kein Entwurf in Ghost) |
| 14 | Vergleich mit Referenz | Mangel M3 (Länge); siehe auch H2. Aufbau, Box, 4 PNG, Schlussfolge („Was das für den Mittelstand bedeutet“ · „Ein Gedanke zum Mitnehmen“ · „Quellen“) wie in den Referenzen |

## Direkt korrigiert in beitrag.md

1. „**Geld:** Echte Euro geht es erst …“ → „**Geld:** Um echte Euro geht es erst …“ (Grammatik).
2. Preisliste: bei Haiku 5.5 „(bei Anfragen bis 100.000 Tokens)“ ergänzt. Laut Preisliste kostet Haiku darüber 0,50/2,50 $.
3. Stapelverarbeitung: „Antwort innerhalb von 24 Stunden“ → „Antwort meist innerhalb einer Stunde, spätestens nach
   24 Stunden, dafür 50 Prozent Rabatt“ (Batch-Doku: „most batches completing within 1 hour … after 24 hours“).

---

## Runde 2

- Datum: 10.11.2026 (Redaktions-Lauf Di 12:47, Prüfrunde 2, letzte Runde)
- Ergebnis: **BESTANDEN**

Frisch gelesen: beitrag.md, kmk-modellwahl-g2.png (und g2-social), quellen.md Abschnitt 4.

| Mangel / Hinweis | Stand |
|---|---|
| M1 Opus/Sonnet-Limit | behoben. Text stützt sich jetzt auf „Usage limit best practices“ (Modellwahl als Faktor) und die Fable-Seite. Die Opus/Sonnet-Aussage ist gestrichen, auch in g2 („Das stärkste Modell verbraucht das Wochenlimit schneller“). Quellenliste angepasst, 9267304 entfernt. In quellen.md ist der alte Eintrag als VERALTET markiert und nicht gelöscht. Im INTERN-Absatz vermerkt. |
| M2 Rechnung bleibt gleich | behoben. Eingeschränkt im Absatz zu Beginn von „Was der Sprit kostet“, in der Box („meist nicht über die Rechnung“), in g2 („Rechnung meist gleich“) und im Schlussabschnitt (Ausnahme Zusatzguthaben). Deckt sich mit der Fable-Seite. |
| M3 Länge | behoben. Rund 1.970 Wörter bis „Quellen“ (vorher rund 2.050), 2.110 mit Quellenliste. Liegt im Rahmen 1.900–2.000. |
| H1 Sonnet | übernommen („Sonnet für Alltagsarbeit wie Texte und Datenanalyse“, entspricht der Auswahlmatrix). |
| H2 doppelter Kopf | übernommen (Box-Kopf „Die eigene Faustregel in einer halben Stunde“). |

Nichts Neues kaputt: Zahlen unverändert und weiter quellengleich (Preise, 0,35/7/14/28 $, 85/91 %, 4,3-fach, 7 %,
0,49/0,57/1,40 $, 7/25 und 25/25, RouteLLM, FrugalGPT 98 %). Links auf die Originale, beide neuen Help-Center-Links
erreichbar. Keine Ich-Form außerhalb der Platzhalter. Die zwei `[TILL: …]` sind bewusst offen und im INTERN-Absatz genannt.
Ton sachlich. g2 im Baukasten: Titel als Aussage, Fußzeile mit Stand und Quelle, Lime-Kante. Alt-Text und Bildunterschrift
passen zur neuen Fassung.

Direkt korrigiert in Runde 2:
1. Schlussabschnitt: „Für die meisten Betriebe mit Abo geht es bei der Modellwahl meist nicht um …“ → doppeltes „meist“
   gestrichen.
2. Absatz **Limits**: Fable-Aussage auf den Geltungsbereich der Quelle eingeschränkt: „Wo Fable im Limit enthalten ist,
   etwa auf Premium-Plätzen im Team-Abo, verbraucht es das Wochenlimit schneller als die anderen Claude-Modelle.“ Auf
   Standard-Team-Plätzen zählt Fable laut Anthropic nicht gegen das Limit; das steht schon im Absatz davor.

Offen, kein Prüfmangel: lmsys.org, arxiv.org, frontiersin.org und help.openai.com waren in dieser Umgebung nicht erreichbar.
Die Angaben daraus stimmen mit quellen.md überein; Till wird das offen gemeldet.

---

## Runde 3 (Till-Wunsch 12.11.)

- Datum: 12.11.2026 (auf Tills Wunsch im Chat: vollständige, unabhängige Prüfung „ob alles perfekt passt und korrekt ist“)
- Prüfer: Prüfer-Agent, unabhängig, Quellen neu abgerufen
- Ergebnis: **NICHT BESTANDEN**

Grund: Alles, was sich heute prüfen ließ, stimmt: Preise, Modellnamen, eigene Rechnung, Faktoren, Anthropic-Messungen,
Help-Center-Aussagen, interne Links, Grafiken, Titel- und Vorschaubild, Ghost-Vorschau. Ein Abschnitt ist aber
wahrscheinlich überholt (ChatGPT „Auto“, M1), und vier Quellen-Hosts sind in dieser Umgebung gesperrt. Deren Angaben
konnten nicht neu geprüft werden und gelten deshalb nicht als bestanden.

### Mängel

**M1 – ChatGPT „Auto“ und Admin-Umleitung wahrscheinlich überholt (Punkt 1, 3)**
- Fundstellen: Abschnitt „Weg 2: Technik, die vorher entscheidet“, Absatz 2 („In ChatGPT gibt es das bereits, die Auswahl
  heißt ‚Auto‘. In den Release Notes für Enterprise beschreibt OpenAI, dass Administratoren die automatische Weiterleitung
  auf ein kleineres Denkmodell lenken können. … Wer ‚Auto‘ stehen lässt, überlässt die Wahl dem Anbieter. Wer fest das
  größte Modell einstellt, schaltet die Weiche ab.“); Box „Das Wichtigste in 30 Sekunden“, Punkt 5 („In ChatGPT gibt es
  das schon“).
- Befund: help.openai.com ist gesperrt (siehe unten), Original nicht lesbar. Laut Suchergebnissen (WebSearch, 12.11.2026)
  steht in den „ChatGPT Enterprise and Edu release notes“ ein Eintrag vom **28.10.2026**: Das automatische Umschalten von
  Instant auf höhere Denkstufen sei für Enterprise und Edu eingestellt. Die zugehörige Einstellung erscheine nicht mehr unter
  Workspace settings > Models. Wer mehr Denkleistung braucht, wählt die Denkstufe jetzt selbst im Modellwähler. Für Plus und Pro meldet eine
  Zweitquelle (mixed-news.com) dasselbe schon ab 14.09.2026. Für Business ist nichts gefunden. quellen.md stützt sich nur auf
  einen Such-Ausschnitt vom 10.11. mit Einträgen vom 18.03. und 26.06.2026. Diese älteren Einträge sind wohl überholt.
- Korrektur (Vorschlag, inhaltlich, nicht direkt geändert): Vor der Freigabe die beiden OpenAI-Release-Notes im offenen Netz
  lesen. Bestätigt sich der Eintrag vom 28.10., Absatz 2 etwa so fassen: „OpenAI hat in ChatGPT eine solche Weiche
  eingeführt, die automatische Auswahl ‚Auto‘. Für Enterprise-Konten hat OpenAI das automatische Umschalten auf höhere
  Denkstufen im Oktober 2026 wieder eingestellt; dort wählt man die Denkstufe jetzt selbst. [TILL: …]“ Dazu den Satz zu
  „Auto stehen lassen / Weiche abschalten“ streichen oder an den Stand im Business-Konto anpassen. In der Box Punkt 5
  „In ChatGPT gibt es das schon“ ersetzen durch z. B. „Für eigene Anwendungen heißt das Router. Vorher an echten Fällen
  testen.“ Der vorhandene `[TILL: …]`-Platzhalter deckt nur den Namen ab, nicht diese inhaltliche Änderung. Bitte auch
  quellen.md Abschnitt 5 nachziehen (alte Einträge als VERALTET markieren, nicht löschen).

**M2 – Einsatzzweck von Haiku steht in keiner verlinkten Quelle (Punkt 3)**
- Fundstelle: „Gleiche Marke, unterschiedliche Motoren“, Absatz nach der Preisliste („Haiku für viele, zeitkritische
  Aufgaben wie Einordnen, Herausziehen und Weiterleiten“); ebenso g1 (Haiku-Zeile).
- Befund: Die Aussage stimmt, steht aber wörtlich nur auf „What’s new in Claude Haiku 5.5“ („built for high-volume,
  latency-sensitive work such as classification, routing, extraction, and subagent tasks“). Die verlinkte Preisliste sagt
  nur „Haiku for simple tasks“, „Choosing the right model“ nur „lowest latency and price“.
- Korrektur: In die Quellenliste aufnehmen:
  „[Anthropic, Claude-Dokumentation: What’s new in Claude Haiku 5.5 (abgerufen 12.11.2026)](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5)“,
  ebenso in quellen.md.

### Hinweise (kein Mangel, zur Entscheidung)

- H1: g1, Sonnet-Zeile: „die meisten Anwendungen, Alltagsarbeit“. Den Text hat Runde 1 (H1) auf „Alltagsarbeit wie Texte
  und Datenanalyse“ umgestellt, die Grafik nicht. „Most production workloads“ steht so in der Preisliste. „Choosing the
  right model“ sagt aber „Most workloads start with Claude Opus 5.5“. Vorschlag: in g1 „Alltagsarbeit: Texte,
  Datenanalyse“ (Grafik-Agent, mit `--social` neu rendern).
- H2: Stapelverarbeitung „spätestens nach 24 Stunden“: Laut Batch-Doku *verfallen* Anfragen, die nach 24 Stunden nicht fertig
  sind. Genauer: „Antwort meist innerhalb einer Stunde, höchstens 24 Stunden Laufzeit, dafür 50 Prozent Rabatt“.
- H3: „Anthropic nennt den Denkaufwand innerhalb eines Modells **deshalb** oft den besseren Hebel“: Das „deshalb“ ist eine
  Verknüpfung von uns, bei Anthropic steht der Satz für sich („Tuning effort is often a better lever than switching
  models“). Vorschlag: „deshalb“ streichen.
- H4: „Um echte Euro geht es erst …“ bei Beträgen in US-Dollar. Vorschlag: „Um echtes Geld geht es erst …“.
- H5: Kopf der Quellenliste „zuletzt geprüft am 10.11.2026“: Nach Behebung von M1 und nach Prüfung der gesperrten Quellen
  auf das neue Datum setzen. Heute wurden nur die Anthropic-Seiten neu geprüft, deshalb ist das Datum nicht geändert.
- H6: Länge: Nach meiner Zählung (ohne INTERN, Platzhalter, Code) rund 1.870 Wörter bis „Quellen“, 2.000 mit Quellenliste.
  Das liegt im Rahmen, wenn man wie in Runde 1/2 mit der Quellenliste zählt. Ghost zeigt „10 Min. Lesezeit“, weil der
  INTERN-Absatz noch mitgezählt wird.
- H7: „Fable als stärkstes Modell“: genau genommen „most capable model open to all customers“. Claude Mythos 5.2 hat
  dieselben Fähigkeiten und denselben Preis, ist aber nur für verifizierte Organisationen zugänglich. Für KMU ohne
  Belang, deshalb kein Mangel.

### Je Quelle: neu geprüft am 12.11.2026?

| Quelle | Neu geprüft | Ergebnis |
|---|---|---|
| Anthropic Pricing (platform.claude.com) | ja (HTTP 200) | Haiku 5.5 0,10/0,50 $ (bis 100.000 Tokens), Sonnet 5.5 2/10 $, Opus 5.5 4/20 $, Fable 5.2 8/40 $ unverändert. Keine neueren Modelle. „Haiku for simple tasks, Sonnet for most production workloads, Opus for the most complex reasoning“ |
| Anthropic Choosing the right model | ja (200) | Matrix, Haiku „lowest latency and price“, Sonnet Alltagsarbeit/Datenanalyse/Texte, Effort „often a better lever“, Test mit eigenen Daten: ok |
| Anthropic Optimizing for cost and intelligence | ja (200, ganze Seite) | 85/91 %, ein Zwanzigstel, 7 %, 4,3-fach, „directional, not guarantees“, 0,49/0,57/1,40 $ und 2,8-fach (gegenüber Einzeiler), Genauigkeit innerhalb der Messschwankung, 1.862 Zeilen, 7/25 bei 5,01 $, 25/25 bei 0,40 $, ein Zwölftel, Caching „usually the largest lever“: alles ok |
| Anthropic Batch processing (nicht verlinkt, Beleg für 1 h/24 h/50 %) | ja (200) | ok, siehe H2 |
| Anthropic What’s new in Haiku 5.5 (nicht verlinkt) | ja (200) | Beleg für Haiku-Einsatz, siehe M2 |
| Help Center 9797557 Usage limit best practices | ja (200) | Faktoren inkl. „Model choice“, „Message length“, „File attachment size“: ok |
| Help Center 15424964 Claude Fable models on your plan | ja (200) | Max/Ultra/Premium-Plätze: im Limit, „use them faster than other Claude models“, bis 50 %. Pro und Standard-Team: nicht im Limit, nur über „usage credits“: ok |
| OpenAI ChatGPT Enterprise and Edu Release Notes | **nein**: curl „CONNECT tunnel failed, response 403“; WebFetch „getaddrinfo ENOTFOUND help.openai.com … outside the session's allowed network domains“ | nur Suchergebnisse, siehe M1 |
| OpenAI ChatGPT Release Notes (April 2026, Modellwahl im Eingabefeld) | **nein**: wie oben (403 / ENOTFOUND help.openai.com) | nur Drittquelle (ClickUp-Changelog) bestätigt „April 2026, Plus, Pro, Business“; Original ungeprüft |
| LMSYS RouteLLM-Blog | **nein**: curl 403; WebFetch „getaddrinfo ENOTFOUND www.lmsys.org“ | Suchergebnisse (Berkeley-Projektseite) bestätigen über 85/45/35 % und 95 %; 26 %/14 % ungeprüft |
| arXiv FrugalGPT | **nein**: curl 403; WebFetch „getaddrinfo ENOTFOUND arxiv.org“ | „bis zu 98 %“ ungeprüft |
| Frontiers Pressemitteilung | **nein**: curl 403; WebFetch „getaddrinfo ENOTFOUND www.frontiersin.org“ | Suchergebnisse bestätigen 14 Modelle, 1.000 Fragen, bis zu 50-mal CO₂; Dauners Rat ungeprüft |
| DOI 10.3389/fcomm.2025.1572947 | **nein**: curl 403 (doi.org) | ungeprüft |
| Intern: chatgpt-claude-gemini-ki-modelle-erklaert | ja (200) | richtiger Beitrag („ChatGPT ist nicht das KI-Modell …“) |
| Intern: nicht-jedes-problem-braucht-ki | ja (200) | richtiger Beitrag, Mailregel-Gedanke steht dort |

Eigene Rechnung nachgerechnet: (2.000 × Preis hinein + 300 × Preis hinaus) / 1 Mio. × 1.000 = 0,35 / 7 / 14 / 28 US-Dollar,
stimmt. Faktoren 20/40/80 stimmen für Eingabe und Ausgabe. 1,40/0,49 = 2,86 (Quelle „2.8 times“). 5,01/0,40 = 12,5 („about a
twelfth“).

### Checkliste

| Nr. | Ergebnis |
|---|---|
| 1 | Mangel M1. Anthropic-Zahlen ok (neu geprüft). OpenAI, RouteLLM, FrugalGPT, Frontiers nicht neu prüfbar (Sperre) |
| 2 | ok (Herstellermessung, offene Modelle, API statt Chat, Annahme 2.000/300, Forschung 2023/2024) |
| 3 | Mangel M2 (Beleg Haiku-Einsatz fehlt in der Liste). Sonst Originale verlinkt |
| 4 | ok. Keine Ich-Form außerhalb von INTERN und `[TILL: …]`. „Welche würde ich so verschicken“ in Schritt 3 ist die Frage des Lesers an sich selbst |
| 5 | ok, zwei `[TILL: …]` bewusst offen, im INTERN genannt, nicht angefasst |
| 6 | ok. H2 nach Langtext, Teaser 152 Zeichen, ungleich Titel. Länge siehe H6 |
| 7 | ok (Wissen / Leitfäden, `#wissen`) |
| 8 | entfällt |
| 9 | ok, keine Verbotswörter, kein CTA, kein Handel, kein Arbeitgeber |
| 10 | ok (10–150 Leute, Ingenieurbüro mit 40, Hausverwaltung, Büroleitung) |
| 11 | ok. g1–g4 und Social-Kacheln angesehen: Werte gleich Text und Quelle, Titel als Aussage, Fußzeile mit Stand und Quelle, Lime-Kante, Alt-Texte und Bildunterschriften. Siehe H1 |
| 12 | ok, Vorschaubild drei Zeilen, Logo, Lime-Kante |
| 12a | ok, Titelbild ohne Titel, Stufen S/M/L, ein Merksatz, keine Zahl, Kategorie „Leitfäden“ |
| 13 | ok. Ghost-Vorschau erreichbar (200): Titel, Teaser, Titelbild als feature_image, 9 H2 in richtiger Reihenfolge, beide Kästen, Prompt-Kasten, 4 Schaubilder mit Bildunterschriften. Bild-Hashes in ghost.json gleich den lokalen Dateien. og/twitter-Bild = vorschaubild.png. INTERN und `[TILL` erwartungsgemäß noch sichtbar (Entwurf). Die Korrektur unten ist noch nicht in Ghost (`draft` nicht ausgeführt, kein Auftrag) |
| 14 | ok, Aufbau wie Langtext-Referenzen (Box, 4 PNG, Schlussfolge) |

### Direkt korrigiert in beitrag.md (Runde 3)

1. „Was das in **Euro** und Cent heißt, zeigt eine einfache Rechnung“ → „Was das in **Dollar** und Cent heißt …“. Die Rechnung
   steht durchgehend in US-Dollar.

Die Korrektur ist nur lokal. Sie geht erst mit dem nächsten `ghost.py draft` nach Ghost.

---

## Runde 4 – 12.11.2026

**Ergebnis: BESTANDEN** (für die Änderungen nach Runde 3; zwei kleine Korrekturen direkt eingearbeitet, siehe unten).
Offen und nicht als Mangel dieser Runde gewertet: OpenAI, LMSYS, arXiv, Frontiers, doi in der Lauf-Umgebung gesperrt,
nicht neu geprüft. Der `[TILL: …]`-Platzhalter im Schluss ist bewusst offen und nicht angefasst.

### Geprüfte Änderungen

| Punkt | Ergebnis |
|---|---|
| M1 Weg 2 (Screenshots Till 12.11.2026) | im Kern ok, Enterprise-Release-Notes aus Text und Liste raus. Drei Formulierungen gingen über die Screenshots hinaus, direkt korrigiert (1) |
| M1 Box Punkt 5 | „Im ChatGPT-Abo entscheidest du derzeit selbst“ widersprach dem Work-Bereich mit Voreinstellung „Standard“, direkt korrigiert (2) |
| M1 INTERN / quellen.md | ok. Primärbeobachtung und Annahme „Business“ vermerkt, alte Einträge als VERALTET markiert, nicht gelöscht |
| M2 Haiku-5.5-Seite in der Liste | ok. Wie „Choosing the right model“ nur in der Liste, nicht im Text verlinkt; das ist bisherige Praxis |
| H1 g1 | ok. g1.png und g1-social.png angesehen: Sonnet „Mittelklasse · Alltagsarbeit: Texte, Datenanalyse“, Stand 12.11.2026, Werte unverändert, Lime-Kante, Fußzeile vollständig |
| H2 Stapelverarbeitung | ok („meist innerhalb einer Stunde, höchstens 24 Stunden Laufzeit, 50 Prozent Rabatt“) |
| H3, H4 | ok |
| Quellenliste gegen Text | ok. Jede im Text verlinkte Quelle steht in der Liste; Listeneinträge ohne Textlink (Choosing a model, Haiku 5.5) sind Belege. Zeile 36 (April 2026, Modellwahl im Eingabefeld, OpenAI Release Notes) passt zum neuen Absatz |
| Ton, Länge | ok. Keine Floskeln, Duzen durchgehend, Länge praktisch unverändert |

### Direkt korrigiert in beitrag.md (Runde 4)

1. Weg 2, Absatz ChatGPT:
   - „übernimmt so eine Weiche die Wahl derzeit nicht sichtbar“ → „Im Chat von ChatGPT Business ist derzeit keine solche
     Weiche einstellbar.“ (holpriger Satz; auf den Chat beschränkt, weil offen ist, was „Standard“ im Work-Bereich intern tut)
   - „Regler für den Denkaufwand von gering bis hoch“ → „mit drei Stufen“ (sichtbar sind drei Stufen und die Einstellung
     „Hoch“; die Bezeichnung der untersten Stufe ist nicht belegt)
   - „Die Weiche seid ihr selbst“ → „Im Chat bist du selbst die Weiche“ (Leser werden geduzt; Work hat mit „Standard“ eine
     Voreinstellung)
   - „fährt jede Aufgabe mit voller Leistung“ → „rechnet jede Aufgabe mit hohem Denkaufwand“ (ob „Hoch“ die höchste Stufe
     ist, zeigt der Screenshot nicht sicher)
2. Box Punkt 5: „Im ChatGPT-Abo entscheidest du derzeit selbst.“ → „Im ChatGPT-Chat wählst du Modell und Denkaufwand
   derzeit selbst.“

Hinweise: Bitte Till weiter bestätigen lassen, dass die Screenshots aus ChatGPT Business stammen (steht im INTERN).
Korrekturen nur lokal; sie gehen erst mit dem nächsten `ghost.py draft` nach Ghost.

---

## Runde 5 – 12.11.2026 (Endfassung)

**Ergebnis: BESTANDEN** (für die Änderungen nach Runde 4; drei kleine Korrekturen direkt eingearbeitet, siehe unten).
Wie in Runde 4: help.openai.com in der Lauf-Umgebung gesperrt, nicht neu geprüft.

### Geprüfte Änderungen

| Punkt | Ergebnis |
|---|---|
| INTERN-Absatz entfernt | ok. Wörtlich in quellen.md archiviert. Im Beitrag kein „INTERN“, kein `[TILL`, kein `[GRAFIK`, kein Redaktionshinweis mehr |
| Weg 2, ChatGPT-Absatz | im Kern ok und neutral. „Modell und Denkaufwand im Eingabefeld“ gedeckt durch OpenAI Release Notes 28.04.2026 (Plus, Pro, Business; im Text Zeile 34 verlinkt). **„hängt vom Abo ab“ war zu weit:** gestützt nur auf Suchausschnitte von help.openai.com, Original nicht gelesen (Regel 3). „Stand 12.11.2026 lohnt deshalb …“ hängte ein Datum an eine Empfehlung statt an einen Fakt. Beides direkt korrigiert (1) |
| Box Punkt 5 | ok („In ChatGPT lohnt ein Blick, was im eigenen Konto eingestellt ist.“), passt zum Absatz, behauptet nichts Abo-Spezifisches |
| Schlussabsatz „Meine Einschätzung“ | ok mit Korrektur. Kern („viele Betriebe schießen mit Kanonen auf Spatzen“, zwei Wege) deckt sich mit Tills Idee vom 10.11.; keine erfundenen Erfahrungen oder Messwerte. Der Grund „weil das größte Modell eingestellt ist“ ging über Tills Satz („Mitarbeiter nutzen für alles das größte Modell“) hinaus und ist als Voreinstellung nicht belegt; „ihr“ statt Duzen. Direkt korrigiert (2), (3). Die Gewichtung „einfachster Anfang: Faustregel; Technik erst bei eigenen Anwendungen“ ist Redaktionsformulierung auf Tills ausdrücklichen Wunsch (quellen.md, Nachtrag 12.11.) und entspricht dem Fazit des Beitrags; Till bestätigt sie mit der Freigabe |
| Format | ok. Ich-Form nur im Fazit (kmk-schreibstil), Abschnittsfolge unverändert, Leitfäden/#wissen, Teaser unverändert |
| Ghost-Tauglichkeit, Länge | ok. Keine Reste, Frontmatter vollständig; rund 2.000 Wörter Fließtext ohne HTML-Blöcke, gegenüber Runde 4 etwa 190 Wörter kürzer (INTERN raus) |

### Direkt korrigiert in beitrag.md (Runde 5)

1. Weg 2: „…, hängt vom Abo ab, und OpenAI ändert das immer wieder. Stand 12.11.2026 lohnt deshalb ein Blick ins eigene
   Konto.“ → „…, ist von außen nicht immer zu erkennen, und OpenAI ändert die Auswahl immer wieder. Deshalb lohnt ein
   Blick ins eigene Konto.“
2. Schluss: „weil das größte Modell eingestellt ist“ → „weil im Team für alles das größte Modell läuft“ (Tills Wortlaut)
3. Schluss: „wenn ihr eigene Anwendungen baut“ → „wenn dein Betrieb eigene Anwendungen baut“ (Duzen)

Hinweis für die Vorschau-Mail: Till ausdrücklich auf den Absatz „Meine Einschätzung“ hinweisen, da er von der Redaktion
formuliert ist. Korrekturen nur lokal; sie gehen erst mit dem nächsten `ghost.py draft` nach Ghost.
