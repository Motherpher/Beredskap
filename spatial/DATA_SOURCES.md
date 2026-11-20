# Datakällor och API-anslutningar – kandidatregister

**Inga följande API:er är påstått aktiva eller live-testade för Heby.** Director har uppgett att godkända API:er ska konfigureras senare. Källorna nedan är kandidater för FF-Spatials källpromovering, inte direkt åtkomst från denna gren.

| Källfamilj | Analysbidrag | Förvaltning och särskild kontroll |
|---|---|---|
| **SCB och auktoritativa administrativa gränser** | Län, kommun, tätort, population, DeSO/RegSO och tidsserier | Kodformat, årgång, bortfall och ändrade gränser; FF-Spatial kan ha adapters men status måste testas |
| **Kolada** | Kommunala nyckeltal i jämförbar tid | Exakta indikator-ID, definitioner, år, skilda administrativa nivåer |
| **Lantmäteriet** | Höjddata, topografi och geografi | Rättigheter, upplösning, access, datalicens och publiceringsvillkor |
| **SMHI** | Nederbörd, flöde, temperatur, tidsserier, modellresultat | Station, metodbrytning, kvalitet, tidsskala och modell/observation |
| **SGU** | Jordarter, markens genomsläpplighet, grundvatten | Mätserie vs karta, datakvalitet, geomorfologi och tidsmässig jämförbarhet |
| **MCF/MSB och länsstyrelser** | Översvämningskartering, lågpunkter, risk- och sårbarhetsunderlag | Historisk versions- och täckningskontroll, före/efter 2023 |
| **VISS, vattenråd, vattenvårdsförbund** | Vattenförekomst, ekologisk kontext, lokal delaktighet | Vattenkvalitetsproblem är inte automatiskt översvämningsfara |
| **Region Uppsala, Heby, föreningsarkiv** | Civilsamhällets organisationslandskap, aktiviteter och resurser | Dubletter, klassificering, aktivitet, sekretess, autonoma föreningsperspektiv |
| **Volontärbyrån, nationella civilsamhällesstudier** | Rekrytering, resurser och organisatoriska villkor | Mätpopulation, sample bias, validitet, lokal överförbarhet |
| **Civic sensing (framtida pilot)** | Egna berättelser, observationer och weak signals | Samtycke, dataansvar, informationssäkerhet, observationskvalitet |

## Källpromovering: CANDIDATE → ACTIVE
FF-Spatials egna [Source Promotion Gate](https://github.com/Motherpher/FF-Spatial/blob/main/docs/SOURCE_PROMOTION.md) ska följas. Tekniskt aktiv endpoint är inte samma sak som att användningslicensen eller HARP-sakbelägget är klarerat.

## Viktigaste källgapet för MAP-02
Att få en **tidsbestämd och definitoriskt stabil, aktiv baslinje för idéburen verksamhet i Heby**: sektorsavgränsning, organisationsstatus och aktiviteter, kommunfördelning, informationsinhämtning med rättigheter och metod för geografisk attribution. Utan detta kan en snygg punktkarta bli missvisande.
