# Kartor, civilsamhällets geografier och multinivåanalys
**Status:** Tematiskt GIS-uppdrag definierat; inga nya kartprodukter eller API-test genomförda för Heby.

## Syftet med kartorna
Kartorna ska användas för att **pröva systemiska samband**, förstå luckor i tillgänglig kunskap och visa hur förutsättningar för beredskap skiljer sig mellan geografiska och organisatoriska nivåer.

### Skalor
1. **Plats och mikrosystem:** verifierade historiska riskområden, relevanta vattendrag och offentligt publicerbar funktionell kontext – utan känsliga aktuella tekniska detaljer.
2. **Heby kommun:** administrativa nivåer, samhällsstruktur, föreningslandskap, verksamhet och tillgänglighet.
3. **Uppsala län:** geografiska och organisatoriska relationer, jämförbara mått, regionala nätverk och beroenden.
4. **Jämförelseområden:** jämför metod, kommunstorlek och geografi utan falsk analogi.

### Kartlager som ska prövas
| Lagerfamilj | Varför | Primär metodgrind |
|---|---|---|
| Natur och vatten | Hur nederbörd, mark, höjder, vattenvägar och historiska översvämningar samspelar | Källår, hydrologiskt delsystem, dynamik vs lågpunktsmodell |
| Samhällsstruktur | Kommun, tätorter, DeSO/RegSO och befolkning | Exakt geografisk årgång, kodsystem och aggregeringsnivå |
| Civilsamhällets liv | Organisationer, aktiviteter, lokaler, rörelse-/verksamhetsområden | Frivilligt verifierad geografi, integritet och bias; inte bara registreringsadress |
| Resurser och tillgänglighet | Offentliga mötesplatser, kontaktytor och stödjande förutsättningar | Öppet publika resurser och faktiskt verifierat tillträde |
| Sociala och ekonomiska villkor | Sektorns och invånarnas strukturella förutsättningar | Aggregat, småtalsskydd och kontroll mot ekologiska felslut |
| Tidsförändring | Före/under/efter 2023 och longitudinella skillnader | Tidsgiltighet, metodbrytningar och gränsändringar |

### Tekniskt ägarskap
[FF-Spatial](https://github.com/Motherpher/FF-Spatial) äger källpromovering, geografiska referenstillgångar, geodatabehandling, versionerade produkter, QGIS-projektkontrakt och QA. [FFOS](https://github.com/Motherpher/FFOS) kan senare samordna explicit godkända jobb. Beredskap äger frågor, tematisk relevans, HARP- och kunskapskopplingar.

**[Arbetsgren: spatial/qgis-heby-uppsala-v1](https://github.com/Motherpher/Beredskap/tree/spatial/qgis-heby-uppsala-v1)** – provkörning kan börja när godkända API:er, datalicenser och anslutningar faktiskt är operativa.

### Kvalitetsregel
**Kartan är ett analyserbart påstående, inte illustration utan proveniens.** Rumslig samlokalisering visar inte en kausal effekt; medborgardata visar inte hydrologisk orsak utan verifieringskedja; nuvarande organisationsadress är inte bevis för verksamhetens geografi år 2023.

[Läs FF-Spatials arkitektur](https://github.com/Motherpher/FF-Spatial/blob/main/docs/ARCHITECTURE.md) · [HARP-källbibliotek](../kallor/README.md) · [Dashboard](../DASHBOARD.md)

## GIS-samordning – status 20 november 2026
QGIS-grenen har nu en [separat Draft PR #11](https://github.com/Motherpher/Beredskap/pull/11) och godkänd statisk kontraktsvalidering. **Detta är ännu inte en fungerande API- eller QGIS-körning.** Följ de tre ansvarsägda ärendena:

- [Beredskap #12 – Heby/Uppsala GIS-uppdrag och acceptans](https://github.com/Motherpher/Beredskap/issues/12).
- [FF-Spatial #51 – geografiska källor, assets och QGIS-kontrakt](https://github.com/Motherpher/FF-Spatial/issues/51).
- [FFOS #127 – möjlig framtida samordning (discovery only)](https://github.com/Motherpher/FFOS/issues/127).

[Öppna QGIS-grenens README](https://github.com/Motherpher/Beredskap/blob/spatial/qgis-heby-uppsala-v1/spatial/README.md) · [Se atlasens åtta kartprodukter](https://github.com/Motherpher/Beredskap/blob/spatial/qgis-heby-uppsala-v1/spatial/ATLAS.md).
