# QGIS-roadmap – GEO-WP01 till GEO-WP07

GIS-spåret är en tillämpning av Beredskaps kunskapsarbete; geografiska produkter produceras i eller via FF-Spatial. **Inga fiktiva tidsfrister, endpoints eller framgångsmarkeringar.**

| WP | Mål | Beredskapsleverans | FF-Spatial-beroende | Grind |
|---|---|---|---|---|
| **GEO-WP01** | Samordna teknisk och tematisk geodatakatalog | Kartkrav, platsfrågor, underlags-ID | Source registry och existerande spatial assets | Registrerade/ej tillgängliga data klart åtskilda |
| **GEO-WP02** | API-tillgång och källpromovering | Godkända användningsändamål | Provider adapter, rättigheter och QA | Dokumenterad ACCESS_APPROVED/QUALITY_VALIDATED |
| **GEO-WP03** | Geografisk baslinje Heby/Uppsala | MAP-01 och geografiska definitioner | Auktoritativa geometrier, EPSG:3006 och tidsvintage | Valid geodata, inga inkompatibla join |
| **GEO-WP04** | Civilsamhällets landskap | MAP-02/MAP-03 – aktiv verksamhet och olika geografier | Korrekt attribution av organisation till geografi | Aktiv, närvaro och kapacitet särredovisade |
| **GEO-WP05** | Natur och samhällsförutsättningar | MAP-04/MAP-05/MAP-06 | Geodata och indikatorer med historiskt stöd | Ex ante/efter 2023 och modelltyp separerade |
| **GEO-WP06** | Weak signals och samverkanskartor | MAP-07/MAP-08 | Aggregerade observationer, godkända lager, analysmetoder | Etik, privacy, kvalitetskontroll och motprövning |
| **GEO-WP07** | Validering, QGIS-vyer och leverans | Karttolkningar, report-linked figurer och dokumentation | FF-Spatial asset receipt och QGIS/verifierad export | Sakgranskning, HARP och Directoracceptans |

## Milstolpar
**GMS0:** branches/kontrakt skapade, API ej aktiva.
**GMS1:** data- och åtkomstmatris granskad, godkänd källväg.
**GMS2:** geografisk baslinje verifierad.
**GMS3:** civilsamhällets första reproducerbara atlas.
**GMS4:** natural/sociala lager, tidsanalys och svaga signaler prövade.
**GMS5:** validerade och säkert publicerbara kartpaket.

## Beroenden
Beredskaps register `DATA-01–20` och `ARG-01–15` tillhandahåller tematiska frågor. FF-Spatial ansvarar för geodataQA och versionering; FFOS får bara samordna när operativt tillstånd finns. Varje testkörning ska få receipt, dataset- och asset-ID. En färgad kartbild utan kvitto är ingen accepterad leverans.

## Status
GEO-WP01: dokumentation förberedd. GEO-WP02–07: **inte genomförda**. GMS0: struktur levererad. GMS1–GMS5: väntar på åtkomst och validering.


## Koordinerad uppföljning via GitHub
- [Beredskap #12 – tematik och leveransacceptans](https://github.com/Motherpher/Beredskap/issues/12).
- [FF-Spatial #51 – source promotion, asset/QGIS compatibility](https://github.com/Motherpher/FF-Spatial/issues/51).
- [FFOS #127 – framtida upptäckt av cross-repo-samordning](https://github.com/Motherpher/FFOS/issues/127), **inte aktiverad dispatch**.
- [Beredskap Draft PR #11 – QGIS-grenen](https://github.com/Motherpher/Beredskap/pull/11).

Samordningsärenden är granskbara beroenden, inte bevis för att API:er, geodata eller runtime är operativa.
