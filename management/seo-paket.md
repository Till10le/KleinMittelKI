# SEO-Paket zur gesammelten Freigabe (SEO-002, SEO-003, SEO-005)

Stand: 20.11.2026 · erstellt von der Claude-Redaktion für Head of KMI · Status: **vorbereitet**, nichts ist umgesetzt.
An veröffentlichten Beiträgen und am Autorprofil wurde nichts geändert. Umsetzung erst nach Tills Freigabe (Freigabegrenze 1 in
`management/README.md`), danach Ghost-Änderungen über `tools/ghost.py` (heute gibt es dafür keinen Befehl. Dafür braucht es einen
neuen Befehl `meta`/`links`, der die Freigabe prüft, oder Till ändert die Felder selbst im Ghost-Editor).

Datenbasis: Live-`<title>` aller 22 veröffentlichten Beiträge und das Ghost-Feld `meta_title` (Admin API, 20.11.2026, nur gelesen),
Beitragstexte aus `redaktion/referenz/` (Stand 20.11.2026), Autorprofil `users/` (Admin API, nur gelesen).

So antwortet Till (über Head of KMI): „SEO ja“ für alles, oder einzeln, z. B. „T1–T9 ja, L4 nein, S1 ja: <LinkedIn-URL>“.

## 1 · Kürzere Meta-Titel (SEO-002)

Nur das Ghost-Feld **Meta-Titel** (`meta_title`) ändern. Überschrift, Slug und Social-Titel bleiben. 9 von 22 Beiträgen haben einen
Seitentitel über 60 Zeichen. Bei zwei davon (T7, T9) gibt es schon einen Meta-Titel, der aber zu lang ist.
Regel: Hauptbegriff vorn, höchstens 60 Zeichen, keine neue Aussage, die nicht im Beitrag steht.

| Nr | Beitrag (Slug) | heute (`<title>`) | Zeichen | Vorschlag Meta-Titel | Zeichen |
|---|---|---|---|---|---|
| T1 | modellwahl-kanonen-auf-spatzen | Mit Kanonen auf Spatzen: Warum nicht jede KI-Aufgabe das stärkste Modell braucht | 80 | KI-Modelle wählen: Warum das stärkste nicht immer passt | 55 |
| T2 | iab-betriebe-sehen-keine-ki-anwendung | Fast 90 Prozent der Betriebe ohne KI sehen keinen Einsatz. Vielleicht suchen sie an der falschen Stelle. | 104 | IAB-Zahlen: Warum Betriebe ohne KI keinen Einsatz sehen | 55 |
| T3 | ki-ergebnisse-pruefen-leitfaden | KI irrt sich und klingt trotzdem sicher: So prüfst du KI-Ergebnisse im Betrieb | 78 | KI-Ergebnisse prüfen: So erkennst du Fehler im Betrieb | 54 |
| T4 | nicht-jedes-problem-braucht-ki | Nicht jedes Problem braucht KI. Manchmal reicht die einfachere Lösung. | 70 | Nicht jedes Problem braucht KI: Wann es einfacher geht | 54 |
| T5 | eu-eurobarometer-ki-unternehmen | Kosten, Recht, Wissen: Was EU-Betriebe bei KI und Personalsoftware bremst | 73 | Eurobarometer: Was EU-Betriebe bei KI bremst | 44 |
| T6 | olg-hamm-chatbot-haftung | Wenn der Chatbot sich irrt, haftet der Betrieb: Was ein Urteil des OLG Hamm zeigt | 81 | Chatbot-Fehler: Was das OLG Hamm zur Haftung sagt | 49 |
| T7 | wenn-der-meister-in-rente-geht-was-ki-im-wissensmanagement-wirklich-leistet | KI im Wissensmanagement: Firmenwissen sichern ohne eigene Software (Meta-Titel) | 66 | KI im Wissensmanagement: Firmenwissen sichern | 45 |
| T8 | chatgpt-claude-gemini-ki-modelle-erklaert | ChatGPT ist nicht das KI-Modell. Was hinter ChatGPT, Claude und Gemini steckt | 77 | ChatGPT, Claude, Gemini: Welche KI-Modelle dahinterstecken | 58 |
| T9 | wenn-azubis-die-ki-fragen-wird-dein-betrieb-empfohlen | KI-Empfehlungen bei der Azubi-Suche: Wird dein Betrieb gefunden? (Meta-Titel) | 64 | Azubi-Suche per KI: Wird dein Betrieb empfohlen? | 48 |

Hinweis: Das „Eurobarometer“ in T5 steht so im Beitrag („Flash Eurobarometer 578“). Bei T2 stammt „IAB“ aus dem Beitrag
(IAB-Betriebspanel).

## 2 · Interne Links für die 6 Beiträge ohne interne Links (SEO-003)

In jedem Fall wird nur ein **bestehender Wortteil** verlinkt. Der Text bleibt unverändert, es gibt keine Ergänzungssätze.
Alle zitierten Sätze stehen wörtlich im veröffentlichten Text (geprüft gegen `redaktion/referenz/<slug>.html`, 20.11.2026).
Ziele sind nur veröffentlichte Beiträge. Jedes Ziel kommt höchstens zweimal vor.

### L1 · ki-agenten-was-nach-dem-chatbot-kommt-und-was-kmu-davon-haben

| Nr | Stelle (h2) | Satz im Beitrag (wörtlich) | Ankertext | Zielbeitrag | Begründung |
|---|---|---|---|---|---|
| L1.1 | Chatbot, Automatisierung oder Agent? | Wenn ein Ablauf immer gleich ist, brauchst du oft gar keinen Agenten. | brauchst du oft gar keinen Agenten | [Nicht jedes Problem braucht KI. Manchmal reicht die einfachere Lösung.](https://www.kleinmittelki.de/nicht-jedes-problem-braucht-ki/) | Führt genau diesen Gedanken aus: Wann reicht die einfachere Lösung? |
| L1.2 | Warum Zugriff das eigentliche Risiko ist | Ein Chatbot, der eine falsche Antwort schreibt, ist ärgerlich. | Ein Chatbot, der eine falsche Antwort schreibt | [Wenn der Chatbot sich irrt, haftet der Betrieb: Was ein Urteil des OLG Hamm zeigt](https://www.kleinmittelki.de/olg-hamm-chatbot-haftung/) | Echter Fall: Eine falsche Chatbot-Antwort kann mehr als ärgerlich sein. |
| L1.3 | Meine Einschätzung | Ob ein Sprachmodell in einem Benchmark drei Prozent besser abschneidet, verändert den Alltag eines Handwerksbetriebs kaum. | in einem Benchmark drei Prozent besser abschneidet | [Mit Kanonen auf Spatzen: Warum nicht jede KI-Aufgabe das stärkste Modell braucht](https://www.kleinmittelki.de/modellwahl-kanonen-auf-spatzen/) | Dieselbe Haltung: Für Alltagsaufgaben braucht es nicht das stärkste Modell. |

### L2 · wenn-der-meister-in-rente-geht-was-ki-im-wissensmanagement-wirklich-leistet

| Nr | Stelle (h2) | Satz im Beitrag (wörtlich) | Ankertext | Zielbeitrag | Begründung |
|---|---|---|---|---|---|
| L2.1 | Meine Einordnung | Spannender finde ich den Satz, den man leicht überliest: Das Ganze funktioniert nur mit gut gepflegten Daten. | nur mit gut gepflegten Daten | [Mit KI Unternehmenszahlen auswerten – ohne selbst ein Dashboard zu bauen?](https://www.kleinmittelki.de/ki-unternehmenszahlen-data-agent/) | Auch dort hängt der Nutzen an der eigenen Datenqualität. |
| L2.2 | Was bedeutet das für den Mittelstand? | Dafür brauchst du kein großes Softwareprojekt. | kein großes Softwareprojekt | [Nicht jedes Problem braucht KI. Manchmal reicht die einfachere Lösung.](https://www.kleinmittelki.de/nicht-jedes-problem-braucht-ki/) | Der Zielbeitrag verweist schon auf dieses Beispiel; Rücklink stärkt das Paar. |

### L3 · wenn-azubis-die-ki-fragen-wird-dein-betrieb-empfohlen

| Nr | Stelle (h2) | Satz im Beitrag (wörtlich) | Ankertext | Zielbeitrag | Begründung |
|---|---|---|---|---|---|
| L3.1 | Meine Einordnung | Jetzt entscheidet eine KI, welche wenigen Betriebe sie überhaupt nennt. | welche wenigen Betriebe sie überhaupt nennt | [Werbung direkt in ChatGPT: Entsteht hier ein neuer Kanal für Unternehmen?](https://www.kleinmittelki.de/werbung-chatgpt-sponsored-agents/) | Dieselbe Verschiebung: Wie Betriebe in KI-Assistenten auftauchen. |
| L3.2 | Was bedeutet das für den Mittelstand? | Ein schneller Test: Frag selbst eine KI nach guten Ausbildungsbetrieben deiner Branche in deiner Stadt und schau, ob du auftauchst. | Frag selbst eine KI nach guten Ausbildungsbetrieben deiner Branche | [Frag eine KI nach deinem eigenen Unternehmen. Ein Selbsttest in 20 Minuten.](https://www.kleinmittelki.de/frag-eine-ki-nach-deinem-eigenen-unternehmen-ein-selbsttest-in-20-minuten/) | Ausführliche Anleitung zu genau diesem Schnelltest. |

### L4 · chatgpt-claude-gemini-ki-modelle-erklaert

| Nr | Stelle (h2) | Satz im Beitrag (wörtlich) | Ankertext | Zielbeitrag | Begründung |
|---|---|---|---|---|---|
| L4.1 | Was ein KI-Modell eigentlich ist | Daraus folgt eine Eigenschaft, die viele im Alltag irritiert: Weil es für einen Satz oft mehrere plausible Fortsetzungen gibt, kann dieselbe Frage unterschiedliche Antworten liefern. | mehrere plausible Fortsetzungen | [KI irrt sich und klingt trotzdem sicher: So prüfst du KI-Ergebnisse im Betrieb](https://www.kleinmittelki.de/ki-ergebnisse-pruefen-leitfaden/) | Folge dieses Prinzips: plausible, aber falsche Antworten und wie man sie abfängt. |
| L4.2 | Was das für den Mittelstand bedeutet | Häufiger ist nicht geklärt, welche Daten hinein dürfen und welche Aufgaben sich überhaupt lohnen. | welche Aufgaben sich überhaupt lohnen | [Fast 90 Prozent der Betriebe ohne KI sehen keinen Einsatz. …](https://www.kleinmittelki.de/iab-betriebe-sehen-keine-ki-anwendung/) | IAB-Auswertung: Vielen fehlt vor allem der passende Anwendungsfall. |
| L4.3 | Was das für den Mittelstand bedeutet | Im Kleinen heißt das: Nimm drei typische Aufgaben aus deinem Betrieb, probiere sie mit einer kleinen und einer großen Stufe und vergleiche die Ergebnisse. | probiere sie mit einer kleinen und einer großen Stufe | [Mit Kanonen auf Spatzen: …](https://www.kleinmittelki.de/modellwahl-kanonen-auf-spatzen/) | Zielbeitrag führt diesen Test aus („drei Aufgaben, zwei Stufen“) und verlinkt schon zurück. |

### L5 · protokoll-per-ki-selbstversuch

| Nr | Stelle (h2) | Satz im Beitrag (wörtlich) | Ankertext | Zielbeitrag | Begründung |
|---|---|---|---|---|---|
| L5.1 | Wo sind die Grenzen? | So gut das Ergebnis aussah: Fehlerfrei war es nicht. | Fehlerfrei war es nicht | [KI irrt sich und klingt trotzdem sicher: …](https://www.kleinmittelki.de/ki-ergebnisse-pruefen-leitfaden/) | Prüfregeln für genau solche Fehler; der Leitfaden verlinkt schon hierher. Anker liegt in bestehendem Fettdruck. |
| L5.2 | Wo sind die Grenzen? | Eine Vorlage mitgeben: Das bestehende Protokoll-Layout oder das Firmenlogo bringt mehr als lange Anweisungen. | Eine Vorlage mitgeben | [Dreimal dieselbe Präsentation mit KI – und nur eine sieht nach KI aus](https://www.kleinmittelki.de/powerpoint-mit-ki-im-eigenen-design/) | Praxistest zeigt, was eine Vorlage gegenüber Anweisungen bringt. Anker liegt in bestehendem Fettdruck. |
| L5.3 | Mein Fazit | Genau darin sehe ich Potenzial für kleine Unternehmen: bei Besprechungsnotizen, Projektprotokollen oder der Dokumentation wiederkehrender Abläufe. | der Dokumentation wiederkehrender Abläufe | [Wenn der Meister in Rente geht: …](https://www.kleinmittelki.de/wenn-der-meister-in-rente-geht-was-ki-im-wissensmanagement-wirklich-leistet/) | Betriebswissen aufschreiben und pflegen, damit KI es nutzen kann. |

### L6 · schatten-ki-deine-mitarbeiter-nutzen-ki-vielleicht-langst-weisst-du-wofur

| Nr | Stelle (h2) | Satz im Beitrag (wörtlich) | Ankertext | Zielbeitrag | Begründung |
|---|---|---|---|---|---|
| L6.1 | Was bedeutet das für den Mittelstand? | Gerade kleine Betriebe haben selten eine KI-Richtlinie oder jemanden, der Werkzeuge prüft und freigibt. | jemanden, der Werkzeuge prüft und freigibt | [Kosten, Recht, Wissen: Was EU-Betriebe bei KI und Personalsoftware bremst](https://www.kleinmittelki.de/eu-eurobarometer-ki-unternehmen/) | EU-Umfrage nennt fehlendes Fachwissen im Haus als Hürde. |
| L6.2 | Was bedeutet das für den Mittelstand? | Die Absicht ist gut, aber welche Kundendaten dabei eingegeben werden und welche Nutzungsbedingungen gelten, weiß im Betrieb niemand. | welche Nutzungsbedingungen gelten | [ChatGPT ist nicht das KI-Modell. …](https://www.kleinmittelki.de/chatgpt-claude-gemini-ki-modelle-erklaert/) | Abschnitt „Tarif und Datennutzung“ erklärt, wovon die Nutzung der Eingaben abhängt. |
| L6.3 | Ein Gedanke zum Mitnehmen | Die Antwort zeigt dir, wo der eigentliche Bedarf liegt. | wo der eigentliche Bedarf liegt | [Fast 90 Prozent der Betriebe ohne KI sehen keinen Einsatz. …](https://www.kleinmittelki.de/iab-betriebe-sehen-keine-ki-anwendung/) | Zeigt, wie Betriebe ihren Anwendungsfall finden. |

Zielhäufigkeit: ki-ergebnisse-pruefen-leitfaden 2 · modellwahl-kanonen-auf-spatzen 2 · nicht-jedes-problem-braucht-ki 2 ·
iab-betriebe-sehen-keine-ki-anwendung 2 · je 1: olg-hamm, data-agent, werbung-chatgpt, frag-eine-ki, powerpoint, wenn-der-meister,
eu-eurobarometer, chatgpt-claude-gemini.

Hinweis zur Umsetzung: Jede Linkänderung ändert `updated_at` des Beitrags. Für veröffentlichte Beiträge ist das unkritisch (die Sperre
betrifft nur Veröffentlichung), es sollte aber gesammelt in einem Durchgang passieren.

## 3 · LinkedIn im Autorprofil (SEO-005)

| Nr | Was | heute | Vorschlag |
|---|---|---|---|
| S1 | Ghost-Autorprofil `till`, Feld **LinkedIn** | leer (auch Website, Bio und alle anderen Profil-Felder leer, Admin API 20.11.2026) | Tills LinkedIn-Profil-URL eintragen. **Till nennt die URL**; im Repo steht keine. |
| S2 | Gegenprobe nach dem Eintrag | `sameAs` im Article-JSON-LD leer | Seitenquelltext eines Beitrags prüfen, ob `sameAs` die URL enthält. **Ungeprüft**, ob diese Ghost-Version das LinkedIn-Feld in `sameAs` übernimmt; falls nicht: dieselbe URL zusätzlich im Feld **Website** eintragen (das übernimmt Ghost nach bisherigem Stand in `sameAs`, ebenfalls gegenprüfen). |

Optional, nicht beauftragt: Die Autor-Bio ist leer. Ein Vorschlag dafür wäre Tills eigener Text und kommt nur auf Wunsch.
