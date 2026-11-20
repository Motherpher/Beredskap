# Pilotguide – Heby först, Uppsala län sedan

**Körs först efter godkända API:er och FF-Spatial source promotion.** Den här guiden är avsiktligt utan API-nycklar och operativa anrop.

## Test 0 – krav- och källläsning
- Läs [krav för Hebys civilsamhällesatlas](requirements/heby-civic-atlas.requirement.json) och [länets jämförelsebild](requirements/uppsala-context.requirement.json).
- Matcha källor med existerande verified FF-Spatial assets. Inga antagna nationella områdeskoder i joins utan källkontroll.
- Kontrollera att rådata och källversioner får användas för avsett ändamål.

## Test 1 – endast verifierad geografisk referens
- Ta fram läns-/kommungränser med auktoritativ geografi och EPSG:3006. 
- Dokumentera producent, vintage, licens, checksum och exakt period.
- QGIS refererar till asset; Beredskap behåller frågeställningar och synliggör metodgränser.
- Godkänt först efter metadata/geometry-check och reproducerbarhet.

## Test 2 – civilsamhälle utan punkthallucination
- Läs en organisations- och aktivitetskälla med originaldefinitioner.
- Registrera **organisation**, **status**, **verksamhetskategori** och **geografisk nivå** som separata fält.
- Lägg inte organisationspunkt baserat på juridisk adress. Förening kan ha flera verksamhetsområden och viss verksamhet är inte offentligt geokodningsbar.
- Visa t.ex. kommunnivåns omfattning, med saknade värden tydligt synliga; inte påhittade täckningsgrader.

## Test 3 – vatten och historisk risk
- [Hebys vattensystem](requirements/heby-hydro-history.requirement.json) kräver skilda modeller för Örsundaån och Tämnarån.
- Kontrollera scenariots dimensionering, återkomsttid, klimatfaktor, geografisk utbredning och publiceringsdatum.
- Publicera inte anläggningens aktuella känsliga drift- eller placeringselement.

## Test 4 – multiskala och tidsjämförelse
- Koppla aggregerad indikator med auktoritativ matchad geografi samt explicit årgång.
- Kontrollera per capita-täljare/nämnare, klassificering och bortfall.
- Jämför Heby, andra kommuner i länet och länets totalsiffra utan att blandas ihop.

## Test 5 – releasekontroll
Verifiering: [QA](QA_ACCEPTANCE.md), [integritet](PRIVACY_AND_RELEASE.md), [HARP-koppling](HARP_MAPPING.md), FF-Spatial QA-receipt, Directorbeslut. Markera produkt `ACCEPTED` först efter verklig QGIS- eller headless-export med testunderlag.
