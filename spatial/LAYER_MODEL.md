# Datamodell: natur, samhälle och civilsamhällets geografier

## Princip
En geografisk kartanalys måste skilja på **plats**, **geografisk räckvidd**, **nätverk**, **tillgänglighet** och **analytisk attribution**. Att sätta en kartnål på en förenings registreringsadress är inte att beskriva var föreningen *faktiskt verkar*.

| Geografisk entitet | Vad den visar | Tillåten upplösning |
|---|---|---|
| `admin_area` | Län, kommun, DeSO/RegSO och deras versioner | Auktoritativt geometriår, oförvanskade koder, administrativ aggregat |
| `hydro_area` | Avrinningsområde, översvämningskartering, våtmark, dike, vattendrag | Hydrologiskt verifierad geometri, håll Tämnarån och Örsundaån isär |
| `civic_org` | Organisationsidentitet, typ, status och verksamhet över tid | Tabell utan automatisk publik punktgeometri |
| `civic_public_venue` | Offentligt verifierad lokal med samtyckt/publicerad verksamhetsplats | Publik lokal nivå om den inte innebär säkerhets-/integritetsrisk |
| `civic_activity_area` | Område där verksamhet faktiskt bedrivs, inte juridisk hemvist | Polygon/kommunnivå efter verifierat underlag och rättighetsbedömning |
| `civic_mobility` | Återkommande rörelsestråk och lokal observationskapacitet | **Endast aggregerad** och frivilligt deltagande; aldrig personspår |
| `community_conditions` | Strukturella behov och tillgängliga resurser | Aggregerade indikatorer, småtalsskydd och antagandekontroll |
| `civil_observation` | Daterad lokal iakttagelse, proveniens och efterföljande verifiering | Säker lagring; generalisera geografiskt före eventuell publicering |
| `risk_scenario` | Modellområde, scenario, regnvaraktighet, hydrologiska antaganden | Modellspecifik geometri, datum och osäkerhet; ej automatiskt empiriskt utfall |
| `decision_trace` | Tidsmässig relation från signal/data till kommunalt beslut | HARP-relaterad tabell; ingen fiktiv kausal geolänk |

## Obligatorisk metadata för varje lager
`dataset_id`, `source_id`, `harp_id`, `asset_id` (om tilldelat), `vintage`, `valid_from`, `valid_to`, `observation_date`, `retrieved_at`, `geography_type`, `code_system`, `crs`, `population/grain`, `coverage`, `license`, `quality`, `privacy_level`, `spatial_join_method`, `uncertainty`, `steward`, `decision_receipt` (när sådant finns).

`source_id` i FF-Spatial är **inte automatiskt samma namespace** som Beredskaps `harp_id`. Kopplingen måste ske explicit med en kontrollerad identifierarmappning.

## Analysens fyra nivålager
- **Nationell/regional ram:** placering och jämförbarhet, inga småtal eller individuella spår.
- **Uppsala län:** kommunövergripande villkor, länsnätverk, indikatorer.
- **Heby kommun:** lokala områdesskillnader, föreningarnas egen kapacitets- och verksamhetsgeografi.
- **Platsnivå:** verifierade offentliga lokaler och miljöobservationer med separat etik/säkerhetsgrind.

## Temporal logik
`2000–2014`, `2015–2022`, `2023 före 1 september`, `kris 1–8 september 2023`, `2024–2026`. Dessa är **analysfönster**, inte garanti för tillgängliga eller jämförbara mätvärden.

**Varning:** Att koppla en modern DeSO-geometri till uppgifter om 2001 utan tids-/crosswalk-prövning kan skapa falska förändringar. Använd hellre auktoritativa vintage-boundaries och uttryck osäkerheter.
