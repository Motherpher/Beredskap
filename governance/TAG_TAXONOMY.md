# Kontrollerad taggtaxonomi och sökning v1.0

## Regel
Taggarna är **flerdimensionella** och skrivs `namespace:value`, små bokstäver, bindestreck för mellanslag. Källregistrering ≠ verifierat faktum. Automatiskt importerade taggar har `tagging_method: AUTO_CANDIDATES_NOT_MANUALLY_APPROVED`. Expertgranskning behövs före fasta underlagsurval.

## Ämnesdimension
`subject:hydrology`, `subject:stormwater`, `subject:groundwater`, `subject:va`, `subject:power`, `subject:governance`, `subject:civil-society`, `subject:foresight`, `subject:inclusion`, `subject:finance`, `subject:fire`.
Kompletterande önskad vokabulär: `subject:critical-dependencies`, `subject:risk-communication`, `subject:institutional-learning`, `subject:climate-adaptation`, `subject:law`, `subject:social-capital`, `subject:maintenance`, `subject:public-participation`.

## Forskningsdel
`part:d1`, `part:d2`, `part:bridge`, `part:unassigned`. En källa kan tillhöra båda delarna.

## Tidsdimension
Ex ante: `time:pre2023-candidate` tills exakt datum och tillgänglighet har verifierats.
Kris: `time:event2023`. Efter: `time:post2023-candidate`. Äldre historia: `time:1900-1999`, `time:2000-2014`, `time:2015-2023`, framtida/okänd: `time:unknown`.
**Pre-2023-candidate betyder inte verifierat tillgänglig eller delgiven Heby.**

## Plats- och hydrologidimension
`geo:heby`, `geo:orsundaan`, `geo:tamnaran`, `geo:sala`, `geo:uppsala-lan`, `geo:vastmanland`, `geo:gavle`, `geo:sweden`, `geo:other`. OBS: **Tämnarån och Örsundaån är olika system**. Ett ämnesnamn i en titel säkerställer inte hydrologisk tillämplighet.

## Metod och genre
`data:geospatial`, `genre:academic`, `genre:media`, samt utvidgade `method:interview`, `method:administrative-record`, `method:historical-series`, `method:scenario-model`, `method:citizen-sensing`.

## Evidens och status
Källspecifik status styrs av `harp.overall` och inte av enbart fria taggar. Påståendespecifik status: `claim:documented`, `claim:corroborated`, `claim:interpretation`, `claim:disputed`, `claim:hypothesis`, `claim:unknown`.
Separata åtkomstmarkörer: `access:fulltext`, `access:summary`, `access:paywall`, `access:blocked`, `access:unknown`.

## Arbetspaket
Projektets befintliga identiteter `WP00`–`WP23` och frågor `D1-F1`–`D1-F7`, `D2-F1`–`D2-F9` ska användas i egna relationsfält, inte ersättas av söktagg.

## Sökexempel
- `subject:hydrology` + `geo:heby` + `part:d1`
- `subject:civil-society` + `subject:foresight` + `part:d2`
- `geo:tamnaran` + `time:pre2023-candidate`
- `subject:governance` + `subject:finance` för budget- och mottagningskedjor.

## Hur taggstrukturen upprätthålls
Nya taggar måste motiveras och föras in i denna vokabulär. Befintliga alias och dubbla URL:er dokumenteras i HARP. Versionera taxonomin, validera datakatalogen och dokumentera manuell omtaggning, särskilt när tagg automatiskt kommer från en enda rubrik.
