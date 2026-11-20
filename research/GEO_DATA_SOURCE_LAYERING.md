# Källarkitektur – skilda lager för Hebys geografi och samhälle
**Källbatch 5. Forskningsdesign – ännu inte importerade dataserier.**

## 1. Hydrometeorologiska lager
| Lager | Källa | Tidskrav | Begränsning |
|---|---|---|---|
| Intensitet/varaktighet nederbörd | SMHI historiska stationer, radar, kvalitet/status | observation 1900–2023, metadata per station | 130 mm inofficiell uppgift får inte blandas med verifierat officiellt stationsvärde |
| Vattendragsflöde och nivå | SMHI, vattenråd, kommun, relevant hydrostation | särskilt aug–sept 2023 och historiska extremår | Örsundaån ≠ Tämnarån; data enbart från ena systemet räcker inte |
| Terräng och avrinningsvägar | Lantmäteriet/Lst höjdmodeller | exakt version/år 2000–2023 | lågpunktsanalys ≠ dynamisk översvämningsmodell |
| Grundvattennivåer | SGU historiska nivåserier och rapporter | 1984+ anomalikartor, välj 2023 snapshot och lokala stationer | grundvattennivå ≠ ytvattennivå eller direkt mått på markmättnad |
| Geologiska förhållanden | SGU jordarter, berggrund, grundvattenmagasin | dokumentera uppmätningens datum/rumslig upplösning | geologisk typ ≠ bevis om exakt 2023 flödesriktning |
| Vattenstatus och åtgärder | VISS, Vattenmyndigheterna | versionsdatum, förvaltningscykel, status | vattenkvalitet/enskilda avlopp ≠ skyfallsrisk |

SGU:s tidigare grundvattennivåer innehåller avvikelsekartor från **1984**, kartor för grundvattennivå sedan **juni 2020**, och SGU anger metodändring 2020; tidsjämförelser kräver metodkontroll. https://www.sgu.se/grundvatten/grundvattennivaer/tidigare-grundvattennivaer/

## 2. Sociala och organisatoriska lager
| Lager | Källa | Mätbarhet | Begränsning |
|---|---|---|---|
| SCB Medborgarundersökning 2010–2020 | SCB ME0003 | äldre NKI/upplevelser efter kommun och år om deltagande | DESIGNBRYT 2021, inte direkt jämförbar med ny enkät |
| SCB Medborgarundersökning 2021–2025 | SCB nytt frågebatteri | trygghet, miljö, underhåll, information, tillit, VA-nöjdhet | attityd mäter inte objektiv funktionssäkerhet eller övningsförmåga |
| Boverket/SCB områdestyper 2024 | Segregationsbarometern Heby | Heby 14345 personer, 2 RegSO/19.7 % i typ 2, 5/60 % i typ 3, 2/20.3 % i typ 4 | områdestyp ≠ individers utsatthet eller sannolikhet för översvämning |
| SCB avloppsanslutning 2000–2024 | MI0902T01 | olika former av avloppsanslutning historiskt | territoriella/statistiska justeringar 2000/2005 och sekretessbrus fr.o.m. 2024 |
| Civilsamhället och föreningar | Region Uppsala 2022, Heby föreningsdata, AIF | organisatorisk omfattning, verksamhetskontinuitet, samverkan | registrerade ≠ aktiva, socialt kapital ≠ formellt krisuppdrag |

## 3. Tematisk datakorsning
Kartlägg historisk exponering (Örsundaåns översvämningsområden), fysisk/samhällsviktig infrastruktur, boende/ålders- och socioekonomiska områden, föreningsverksamhet, kollektivtrafik och potentiell hjälpstruktur **i aggregerad form**. Använd spatial analys för att testa **ojämn belastning och möjliga hinder**, inte för att inferera enskilda människors ekonomi, hälsa eller krisförmåga.

## 4. Bransch- och mediaavgränsning
Regionala elnätsinvesteringar Vattenfall 2026–2029 >3.9 mdkr är separata från elcentralens **lokala** elsäkerhets-/installationsrisk vid Heby ARV. UNT:s rubrik om nöjdhet kan inte ge några giltiga siffror utan full artikel eller SCB:s specifika urval/år. Båda är sekundära och lågprioriterade för del 1.
