# QGIS – Heby och Uppsala län
**Gren:** `spatial/qgis-heby-uppsala-v1` · **Status:** kartprogram och integrationskontrakt etablerade, **inga godkända API-anslutningar eller testkartor ännu**.

## Varför finns denna gren?
För att skapa en **multinivåbild av Heby och dess kontext**, med särskilt fokus på civilsamhällets faktiska geografier, lokala resurser, samhälleliga beroenden och historiska risker. Kartor används som ett analytiskt sätt att identifiera vad som är synligt, osynligt och ännu inte känt – inte bara för att illustrera rapporter.

**Heby under ytan** är ett fördjupnings- och kunskapsutvecklingsarbete. Geografi är en viktig metodkomponent, inte ett nytt separat institutionellt forskningsprojekt.

## Börja här
| Läs | Innehåll |
|---|---|
| [Kartatlas och prioriterade frågor](ATLAS.md) | Kartor att producera, nytta, nivåer, utfall och kvalitetsgrindar |
| [Geografisk datamodell](LAYER_MODEL.md) | Skillnad mellan organisationers hemvist, mötesplats, verksamhet och rörelsemönster |
| [Kart- och datakällor](DATA_SOURCES.md) | Identifierade leverantörer, rättigheter, historisk nivå och datakvalitet |
| [API-införande](API_ADMISSION.md) | Vad som krävs för att använda de godkända API:erna |
| [FF-Spatial och FFOS](CROSS_REPO_CONTRACT.md) | Domänägarskap, gränssnitt, jobb och godkännanden |
| [GIS-roadmap](ROADMAP.md) | GEO-WP01–GEO-WP07, beroenden och verifierbara milstolpar |
| [Etik och kartpublicering](PRIVACY_AND_RELEASE.md) | Aggregation, integritet, sårbarheter, bias och medborgardata |
| [Test och mottagning](QA_ACCEPTANCE.md) | Hur vi kan säga att kartan är reproducerbar och användbar |
| [Pilotinstruktion](PILOT_GUIDE.md) | Första testordning när API:erna är aktiva |

## Tre nivåer av ansvar
**Beredskap:** tematiska frågeställningar, civilsamhällets begrepp/kapacitetsram, HARP-ID, relevansbedömning och acceptans av analysen.

**[FF-Spatial](https://github.com/Motherpher/FF-Spatial):** auktoritativa geodata, källresolver, data acquisition, CRS, temporala gränser, QGIS-exekvering, produkter, geospatial QA. Ingen ny parallell data-gateway byggs i detta repo.

**[FFOS](https://github.com/Motherpher/FFOS):** möjlig framtida samordning av explicit godkända jobb; **inget automatiskt dispatch eller erkännande av liveintegration genom att filerna finns**.

## Säker status
| Komponent | Nu |
|---|---|
| GIS-gren, uppdragsram, atlasplan | **Strukturerad** |
| FF-Spatial-referenser, schemakompatibla krav och read-only-jobb | **Förberedda** |
| Källa/API-autentisering för Heby | **Inte utförd** |
| Versionerade faktiska Heby/regiongeometrier i denna gren | **Inga** |
| Verifierade kartor / driftsatt QGIS-projekt | **Inga** |
| FFOS-synk/dispatch | **Inte auktoriserat eller genomfört** |

[Kanonisk Beredskap-portal](https://github.com/Motherpher/Beredskap) · [FF-Spatials QGIS-guide](https://github.com/Motherpher/FF-Spatial/blob/main/qgis/README.md) · [FFOS:s orkestreringsprincip](https://github.com/Motherpher/FFOS/blob/main/README.md)
