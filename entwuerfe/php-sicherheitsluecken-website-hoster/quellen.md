# Quellen: php-sicherheitsluecken-website-hoster

Stand: 2026-10-23 (Scout, Redaktions-Lauf Freitag). Abgerufen am 23.10.2026.

## Originalquellen (selbst gelesen)

1. **PHP-Projekt, News-Archiv 2026** – Sicherheitsrelease vom **21.10.2026**:
   https://www.php.net/archive/2026.php
   - Veröffentlicht: PHP **8.5.12, 8.4.27, 8.3.36, 8.2.35** (alle 21.10.2026).
   - Behoben: **CVE-2026-109618** (Remote Code Execution durch Speicherknappheit/OOM beim Aufräumen eines Requests,
     GHSA-w8hw-w9fx-j79w) und **CVE-2026-109619** (Remote Code Execution durch veralteten Zustand, den ein späterer
     Request im selben Worker nutzen kann, GHSA-6wmf-4rv5-p3rp).
   - Beide laut Ankündigung vom 20.10.2026 mit **CVSS v4.0 9.2**.
   - Betroffen laut Meldung: alle PHP-Installationen, die Webanfragen bedienen (PHP-FPM, Apache mit mod_php, php-cgi,
     FrankenPHP, LiteSpeed). Höchstes Risiko bei mod_php: Ein Request ohne Anmeldung kann den Angriff auslösen, bevor
     Anwendungscode läuft.
   - PHP 8.1 und älter bekommen keine Updates mehr; das Security-Team hat minimale Backports (Quelltext) für 7.4, 8.0, 8.1
     bereitgestellt. Distributionen/LTS-Anbieter liefern teils eigene Backports.
   - **PHP 8.2 erreicht am 31.12.2026 das Support-Ende.**
   - Empfehlung: sofort aktualisieren. Übergangsmaßnahmen (z. B. `session.upload_progress.enabled=0`) verringern die
     Angriffsfläche, ersetzen das Update aber laut PHP nicht.

2. **BSI, Cybersicherheitswarnung** „Version 1.2: PHP – Kritische Schwachstellen bedrohen Webanwendungen weltweit“,
   Seite vom **22.10.2026** (Vorab-Hinweis 21.10.2026, Update 1 am 21.10., Update 2 am 22.10.):
   https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-297981-1032.html
   - CVE-2026-109618, CVE-2026-109619; CVSS 4.0: 9,2.
   - Ausnutzung: keine bestätigten Fälle, aber unbestätigte Berichte über existierende Exploits; laut Update 2 dem BSI
     keine erfolgreiche Ausnutzung „in der Breite“ bekannt (Stand 22.10.2026).
   - Entdeckt laut BSI zusammen mit OpenAI; Details aus Blogs von Wiz und Calif.
   - Empfehlung BSI: Patch unverzüglich installieren; Hinweise von Herstellern von Netzwerkkomponenten beachten, in denen
     PHP stecken kann.
   - Keine Zahl betroffener Systeme, keine Aussagen zu Hostern oder WordPress.

3. **OpenAI**, „Patch the Planet: global response coordination as agents uncover critical vulnerabilities“, **21.10.2026**:
   https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/
   - Laut OpenAI: rund zwei Monate Koordination mit PHP-Maintainern, Forschern und Sicherheitsanbietern.
     Calif fand eine kritische Lücke mit einem OpenAI-Modell (GPT-5.6 Sol) im Rahmen von „Patch the Planet“;
     Wiz fand und meldete beide Lücken unabhängig. PHP-Maintainer entwickelten die Fixes.
   - Nennt einen Versions-Checker (GitHub openai/php2shell-checker) – nicht geprüft.
   - **Herstellerangabe mit Eigeninteresse** (Werbung für KI-gestützte Sicherheitsforschung). Nur für die Aussage
     „KI war an der Entdeckung beteiligt“ verwenden, zusammen mit dem BSI-Hinweis.

4. **NCSC-NL (niederländisches Cyber-Sicherheitszentrum)**, GitHub „php2shell“, README zuletzt geändert 21.10.2026, 17:25 CEST:
   https://github.com/NCSC-NL/php2shell
   - Bestätigt gepatchte Versionen und betroffene Betriebsarten wie oben; keine Angaben zu aktiver Ausnutzung.

5. SiteGround-Blog (Hoster, Beispiel für Hoster-Reaktion, kein Faktenbeleg):
   https://www.siteground.com/blog/critical-php-vulnerabilities-october-2026 – laut Hoster serverseitige Schutzmaßnahmen
   vor dem Release, Kunden müssen nichts tun. Zeigt: Ob ein Betrieb handeln muss, hängt vom Hoster ab.

## Nicht gelesen / ungeprüft
- CISA-Alert vom 21.10.2026 (https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching) – Abruf fehlgeschlagen.
- Patchstack („attacks ongoing“) – nicht gelesen; widerspricht dem BSI-Stand vom 22.10. → nicht verwenden.
- Phoenix Security („800 Systems affected“) – nicht gelesen, Zahl nicht verwenden.
- Blogs von Wiz und Calif (technische Details) – nicht gelesen.
- **Keine Quelle gelesen** für den Anteil von Websites, die mit PHP oder WordPress laufen. Aussage „viele Firmenwebsites
  laufen auf PHP, z. B. WordPress“ ist allgemein bekannt, aber ohne Zahl formulieren oder Quelle (z. B. W3Techs) nachlesen.

## Einordnung für KMU (Vorschlag Scout, eigene Worte)
- Betroffen ist fast jeder Betrieb mit eigener Website, Kundenportal oder Online-Terminbuchung auf PHP-Basis –
  meist ohne es zu wissen, weil Agentur oder Hoster die Technik betreuen.
- Konkreter Schritt für Inhaber (1–50 Beschäftigte ohne eigene IT): heute beim Hoster oder der Webagentur nachfragen:
  „Ist PHP auf 8.5.12 / 8.4.27 / 8.3.36 / 8.2.35 aktualisiert? Läuft meine Seite noch auf 8.1 oder älter?“
  Antwort mit Datum ablegen. Bei eigenem Server: IT-Dienstleister.
- Zweiter Punkt: PHP 8.2 endet am 31.12.2026 – wer darauf läuft, sollte das Upgrade jetzt mit beauftragen.
- KI-Bezug: KI-Modelle helfen inzwischen, kritische Lücken in weit verbreiteter Software zu finden. Das gilt für
  Verteidiger und Angreifer; der Abstand zwischen Bekanntwerden und Angriff dürfte kleiner werden (Einschätzung, nicht
  aus Quelle belegt → als Tills Meinung nur nach Rückfrage).
- Anknüpfung: ki-sicherheitsstudie-bsi-tuev (KI-gestützte Angriffe), Schatten-KI-Beitrag.

## Mögliche Kennzahl-Grafik
- „9,2 von 10“ – Schweregrad (CVSS 4.0) laut PHP und BSI. Oder vier Versionsnummern als Prüfliste.
