# HARP – kanonisk källstyrning för Beredskap
**Version 1.0 · datum 2026-11-20 · RefA-status: källgranskning återstår.**

## Normativ grund
*Pius System Codex 5.0*, Appendix O (s. 190–191), samt [governance/EVIDENCE_PROTOCOL.md](EVIDENCE_PROTOCOL.md). För **publicerbara arbeten** krävs RefA, medan MinRA kan användas för intern iterativ analys. Harvard-formatet utgår från University of Sheffields Harvard Guide.

### Exakta ITR-steg i Codex
- **ITR1** Source Identification — hitta originalkälla, rätt upphov och version.
- **ITR2** Full Source Reading and Verification — läs fulltext/metadata, pröva innehåll, tillförlitlighet och relevans.
- **ITR4** Harvard-Style Citation — upphov, år, titel, publikationsuppgifter, fullständig URL och faktiskt åtkomstdatum; vid specificerade påståenden även sidnummer.
- **ITR5** Manual Check — manuell kontroll av belägg, läsbarhet, semantisk överensstämmelse och kvalitet.
- **ITR6** Validation Gate — fastställ `CLEARED`, `EXCLUDED` eller `PENDING`, motivera med kontrollspår.

**ITR3 saknas i den kanoniska Appendix O-texten. Inför inte ett påhittat ITR3.**

## Statusmodell
- `RefA_PENDING`: registrerad men ej klar för publiceringscitering; **samtliga automatiskt importerade källor**.
- `MinRA_INTERNAL`: källa har manuellt lästs och verifierats för avgränsad intern användning; ingen automatisk publiceringsrätt.
- `RefA_CLEARED`: ITR1, ITR2, ITR4, ITR5 och ITR6 dokumenterade och godkända.
- `DISPUTED`: motsägande källor, alternativ tolkning och metodproblem behöver redovisas.
- `EXCLUDED`: källan otillförlitlig, otillgänglig eller irrelevant för ett specifikt påstående; får kvarstå i registret som exkluderat spår.

Blanda aldrig `source inspection status` med `claim evidence status`. En originalkälla kan vara autentisk men sakna stöd för ett specifikt påstående.

## Obligatoriska källfält efter färdig RefA
Käll-ID, titel, upphov (person/organisation), publicerings-/versionsdatum, faktisk observations-/händelsetid, geografisk och teknisk räckvidd, original-URL eller filhash, licens/access, faktisk access date, dokumentets sid-/avsnittsstöd, kontrollanteckning, motprövning, källans `claim_ids`, ansvarig granskare, `reviewed_at`, reproducerbar bibliografisk referens samt beslut om publicering.

## Alla befintliga register bevaras
Original: `sources/*.json`. Nytt kanoniskt register: `sources/registry/HARP_MASTER_INDEX.json` och tillhörande sex shardar samt CSV. En `HARP-xxxxxxxx`-identitet skapas deterministiskt från källans locator; `legacy_aliases` och `origins` bevarar källspåren. URL-sammanfall innebär inte i sig dokumentversionsekvivalens; kontrollera om versionsskillnad kräver separata poster.

## Ex ante och ansvar
Skilj `produced`, `published`, `accessible`, `received_by_heby`, `analyzed_by_heby`, `decision_at`, `implemented_at` och `verified_capacity_at`. Äldre källors tillgänglighet gör inte automatiskt en kommun ansvarig. Material från 2024–2026 får inte användas som ex ante-underlag för september 2023.

## Risk och integritet
Publika register får inte innehålla skyddsvärda elritningar, exakta drift- och säkerhetsdetaljer för aktiv kritisk infrastruktur, identitet på enskilda drabbade eller opublicerat intervjumaterial. Lägg i separat skyddad arbetsmiljö och enbart aggregerad publicerbar tolkning här.

## Publiceringsgrind
Ingen artikel eller sammanfattning får gå till slutpublicering om kritiska påståenden saknar RefA-klarerad originalkälla, sidspår, alternativa förklaringar och relevant teknisk/juridisk sakkunniggranskning.
