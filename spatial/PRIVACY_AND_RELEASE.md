# Dataetik, offentlig säkerhet och kartpublicering

## Fyra grundkrav
1. **Integritet för människor och föreningar:** ingen karta över enskilda volontärers rörelser, barns vardag, särskild utsatthet eller känsliga medlemskategorier. Endast aggregerat, proportionerligt och rättsligt grundat publicerbart material.
2. **Föreningsautonomi:** organisering och kapacitet får inte antas tillhöra en kommunal mobiliseringsstyrka. Kartor får inte klassificera en organisation som frivillig krisresurs utan överenskommelse och verkligt underlag.
3. **Samhällsviktiga anläggningar:** offentliggör inte känsliga nivåer, reservkraftsberoenden, aktuella sårbara tekniska rum, driftförfaranden eller larmdetaljer. En historisk berättelse kräver inte en taktiskt användbar sårbarhetskarta.
4. **Databias och stigmatisering:** registrerade organisationsadresser representerar inte civilt engagemang i ett område. Avsaknad av registerdata betyder inte avsaknad av civilsamhälle; socioekonomisk bakgrund får inte förväxlas med faktisk förmåga eller utsatthet.

## Publiceringsnivå
| Klass | Exempel | Publicerbar? |
|---|---|---|
| `PUBLIC_AGGREGATE` | Kommunvis indikativ täthet eller tematiska verksamhetstyper med metod | Efter HARP/licens/QA |
| `PUBLIC_VERIFIED_VENUE` | Offentligt annonserad föreningslokal med kontrollerad adress | Endast efter bedömd rimlighet och säkerhet |
| `INTERNAL_SENSITIVE` | Geolokaliserade individer, oanonymiserade platsberättelser, riskföremål | Nej, aldrig i öppet repo |
| `RESTRICTED_ASSET` | Driftkritisk anläggnings-/VA/elsäkerhetsinformation | Nej, särskild hantering |

## Krav på karttext
Årtal, geografisk räckvidd, metod/definitioner, osäkerhet, käll-/asset-ID, HARP-koppling, vad kartan *inte* visar, användningsbegränsning, licens och kontakt för rättelse.
