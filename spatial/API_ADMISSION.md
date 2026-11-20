# API-införande – säker och reproducerbar kontrollprocess

**Status: ej aktiverat, inga token eller nycklar inlagda.** Director tillhandahåller eventuella redan godkända åtkomster vid ett senare separat steg. Källlicens och åtkomstkontroll är lika viktiga som att en endpoint tekniskt svarar.

## Sex grindar före skarpt datainhämtning
1. **Godkännande och ändamål:** vem har beviljat åtkomst, till vilken källa, geografisk/tidsmässig omfattning, användnings- och publiceringsrätt? För dokumentation används en säker, icke-hemlig metadataanteckning.
2. **API-dokumentation:** kontrollera auktoritativ leverantör, autentisering, datatyp, version, aktuell dokumentation, rate limit och datakvalitet.
3. **Källpromovering i FF-Spatial:** använd dess Source Promotion Gate och befintliga adapters; skapa inte ny hämtmotor i Beredskap.
4. **Sandbox + read-only:** test mot offentlig/testdata, utan skrivning, persondata eller nyckelutskrift. Registrera testtid, kodversion, svarshash och begränsningar.
5. **Semantisk validering:** geokoder, åldrar/vintages, CRS, geometri, metadata, licens, enheter, urvalsbias och geografiska join-fel.
6. **Auktoriserad produkt:** FF-Spatial verifierar rå/deriverad asset samt QA. Beredskap prövar HARP, civilsamhällesbegrepp, integritet och karttolkning; Director godkänner offentliggörande.

## Statusvärden
`CANDIDATE` → `DOCUMENTED` → `ACCESS_APPROVED` → `CONNECTED_TEST` → `QUALITY_VALIDATED` → `ACTIVE_FOR_SCOPE`. Negativt: `BLOCKED`/`REVOKED`.

**Inget får markeras ACTIVE enbart för att användaren har en API-nyckel.** Körningar som har gjorts i FF-Spatial för andra kommuner/år visar inte att just Heby-piloten fungerar.

## Ingen hemlighet i Git
API keys, bearer tokens, autentiseringscookies, skyddsvärda tekniska kartlager och persondata får inte finnas i repo eller Markdown. GitHub secrets eller annat godkänt hemlighetslager förvaltas av rätt system, efter Directorbeslut. Inga inloggningsuppgifter ska skickas i chattext för att dokumentera dem.

## Körordning för första piloten
**MAP-01:** verifiera läns- och kommungräns från auktoritativ FF-Spatial-källa → **MAP-02:** föreningsregister och begränsningar utan nya personpunkter → **MAP-05:** vattensystem och modellernas historiska täckning → **MAP-04/MAP-06:** aggregerad förutsättning och förändring över tid → **MAP-07:** endast separat samtyckt observationspilot.

[API-kandidatregister](API_SOURCE_REGISTER.json) · [FF-Spatial kontrakt](CROSS_REPO_CONTRACT.md) · [Pilotguide](PILOT_GUIDE.md)
