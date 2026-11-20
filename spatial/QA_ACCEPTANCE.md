# Test- och acceptansmatris för kartor

## Kartfabrikens verkliga acceptans
- [ ] **Asset:** ursprung, källupphov, versions-ID, checksum och lagringsreferens, källlicens och faktiska data finns.
- [ ] **Geografi:** korrekt relation mellan Heby/Uppsala, geografisk nivå, kodsystem, CRS (EPSG:3006 för svensk metrisk analys om inte annat motiveras), geometrivalidering, inga tysta historiska gränsbyten.
- [ ] **Tid:** mätperiod, geografinivå, publikationsdatum och före/efter 1 september 2023 hålls isär.
- [ ] **Semantik:** exempelvis 'förening i kommunen' betyder inte 'förening med verifierad aktivitet i området'; begreppet dokumenteras.
- [ ] **Kvalitet:** bortfall, dubbletter, aktiv-/inaktivkriterium, join-fel, statistikens urval, rimlighetskontroll och motbevis redovisas.
- [ ] **HARP:** väsentlig källa är RefA-klarerad för användandet och angetts med kontrollerad sida, period, geografi och relevans.
- [ ] **Integritet/säkerhet:** småtal, persongeografi, skyddsvärda VA/eltekniska detaljer borttagna; källvillkor tillåter publicering.
- [ ] **Upprepbarhet:** FF-Spatial-jobb/version och källa återproducerar asset och kartvy; QGIS-projekt är en vy, inte primär sanningskälla.
- [ ] **Rapportstöd:** karta har tydlig analytisk fråga, avgränsning, valid tolkning, motargument och rekommenderad kontext.
- [ ] **Godkännande:** faktisk reviewer + Directoracceptans och daterat receipt.

## Få inte falska positiva resultat
En välrenderad karta är **inte** verifierad statistik. En validerad JSON-kravfil är **inte** en lyckad QGIS-körning. Att FF-Spatial kan producera ett globalt ADM1-lager bevisar inte att en civilsamhälleskarta för Heby är klar. En FFOS-work-order är **inte** en körtjänst utan kvitto.

## Testbara kontrakt nu
`spatial/scripts/validate_spatial.py` kontrollerar katalogstruktur, ID:n, frånvaro av skenbar dataklarering och FF-Spatial-jobbets grundfält. Detta är **statisk kontraktsvalidering**, inte live source/QGIS API-test.
