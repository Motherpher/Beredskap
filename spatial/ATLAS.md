# Multinivåatlas – Heby och Uppsala län

**Syfte:** skilja *exponering* från *förutsättningar* och *kapacitet*. Kartorna kompletterar den berättande fördjupningen med verifierbar rumslig analys.

## Prioriterad kartportfölj

| ID | Kartprodukt | Fråga | Geo-/tidsnivå | Acceptans |
|---|---|---|---|---|
| **MAP-01** | Heby i Uppsala län | Var ligger Heby i regionens naturgeografiska, administrativa och sociala kontext? | Län → kommun → delområde, flera årgångar | Auktoritativt län/kommununderlag, CRS och datum |
| **MAP-02** | Civilsamhällets landskap | Vilka typer av *aktiva* idéburna aktörer kan beläggas och på vilken geografisk nivå? | Heby + län, 2000–2026 | Definition aktiv, registerbias, offentlig källåtkomst |
| **MAP-03** | Föreningarnas verkliga närhet | Hur skiljer sig juridisk hemvist, lokal, verksamhetsområde och mobilitet? | Kommun / aggregerad delnivå | Ej punkt från registreringsadress utan verifiering |
| **MAP-04** | Samhällsförutsättningar och delaktighet | Vilka strukturella möjligheter och hinder finns för deltagande och tillgänglighet? | Län / kommun / aggregerat område | Småtalsskydd, denominatorkontroll, jämförbar tid |
| **MAP-05** | Vatten och riskens geografi | Hur varierar terräng, hydrologi och historiska/modelldefinierade risker? | Örsundaån/Tämnarån separat, 1900–2026 | Modelltyp, scenario och geografi tydligt åtskilda |
| **MAP-06** | Före/under/efter | Hur förändras verksamhet, samhällsfunktion och återhämtning över tid? | 2022–2026 och historiska punkter | Verifierad panel/vintage, inga jämförelser med trasiga tidsserier |
| **MAP-07** | Svaga signaler i landskapet | Var finns säkert dokumenterade observationer som kompletterar offentlig mätdata? | Aggregerat och tidsmärkt, ev. civildatakälla | Samtycke, bias/coverage, myndighetsverifiering skild från observation |
| **MAP-08** | Förutsättnings- och samverkansnätverk | Vilka *möjliga* indirekt möjliggörande resurser och relationer kan analyseras? | Län/kommun och nätverksrepresentation | Ingen fiktiv aktiv insats, kartrelationer explicit belagda |

### Kartfamilj 1 – civilsamhället
**Störst initial nytta:** MAP-02 och MAP-03. Skilj *registrerad organisation*, *verksamma människor*, *faktisk återkommande aktivitet*, *tillgängliga resurser* och *möjlig insatsförmåga*. Den senare får inte infereras från organisationsantal.

### Kartfamilj 2 – exponering och funktion
MAP-05 länkas till Del 1, men inte genom att mappa skyddsvärda elektriska komponenter. Publicera kartscenarier på geografiskt och tekniskt lämplig nivå, utan kritisk detalj.

### Kartfamilj 3 – värden och resurser
MAP-04, MAP-06 och MAP-08 kan användas för att diskutera varför sektorns kapacitet behöver utvecklas kontinuerligt. Geografisk korrelation är **inte** ett belägg för kausal krisförmåga.

## Leveransformat när datakällor väl är accepterade
- Karta med titel, tydliga geografiska nivåer, mätmetod, år/vintage, källor, osäkerhet och datum.
- Verifierat FF-Spatial asset-manifest, metadata och QGIS-vy som refererar till asset snarare än skapar en parallell sanningskälla.
- Tillhörande **tolkning med HARP-ID, motargument och gräns för vad kartan kan visa**.
- Publiceringsklar PNG/SVG/PDF endast efter integritets-, licens- och sakgranskning.

**Inga kartprodukter är skapade i denna arbetsorder.** [Piloten](PILOT_GUIDE.md) anger vad som ska köras när API:erna är redo.
