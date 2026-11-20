# Referensdesign – signal till scenario och beslut
**Status:** konceptuell data-/processarkitektur för forskningsstudie, ingen implementerad insamling.

## Dataobjekt
| ID | Objekt | Obligatoriska metadata | Definition |
|---|---|---|---|
| SRC | Ursprungskälla | URL/dokument, upphov, datum, version, arkiv, rättslig grund | Får vara offentlig myndighetsdata, civildata, berättelse, modell eller historisk källa |
| OBS | Observation | när/var/av vem som grupp, metod, kvalitet, osäkerhet, risk för bias | Vad som faktiskt iakttogs |
| NAR | Narrativ | datum, frivillig anonym text, egen signifiering, samtycke | Vad deltagaren upplevde; inte en mätning |
| SIG | Signalkandidat | länkat OBS/NAR/SRC, varför avvikande, nuvarande antagande, motförklaring | Hypotes om förändring, inte en riskdom |
| VAL | Valideringsbeslut | kompetens, jämförelse med mätdata, återbesök, status | Stödd, förkastad, omstridd eller okänd signal |
| FRS | Foresightcase | signaler, scenariodrivare, antaganden, alternativa framtider | Flera plausibla utvecklingar; ej prognos |
| DEC | Beslut | ansvar/rådighet, datum, resurser, förklaring | Beslut om prövning, övning, åtgärd, avstående eller bevakning |
| FDB | Återkoppling | till vem, när, resultat, nytt värde, oenighet | Motverkar extraktiv datainsamling |

## Process
`SRC/OBS/NAR → SIG → VAL + alternativa tolkningar → FRS (scenarier) → DEC → FDB`.
Inför varje övergång: dokumenterad anledning, dataägande/tillstånd, facklig och juridisk behörighet och osäkerhet.

### Tidsfönster
- *Långsam förändring:* halvårsvis/årsvis mönster, underhållsfrågor, föreningars livskraft.
- *Säsongsförändring:* regn/markmättnad/erosion, återbesök och lokala rörelser.
- *Akut förlopp:* SMHI-varning, registrerade nivåer, driftlarm och lägesuppfattningar. Krisledning beslutar; medborgarflöde får inte störa akut respons.

### Data som ska skiljas åt
- **Officiellt mätvärde** (metod, station, period).
- **Civilt observert förhållande** (plats, tid, täckning, observationstyp).
- **Deltagarens meningsskapande** (SenseMaker-liknande berättelser och självsignifiering, kvalitativ analys).
- **Expertbedömning** (fakta, kausal hypotes, ekologisk och juridisk bedömning).
- **Scenariodata** (kontrafaktisk/hypotetisk, aldrig rapporterad som observerad).

## Exempel, helt hypotetiskt
1. Orienteringsförening beskriver ökad stående vattenmängd på samma skogsväg över flera säsonger.
2. En markägare rapporterar samtidigt förändrat flöde längre nedströms.
3. Fackpersoner kontrollerar höjdmodell, nederbörd, markanvändning, naturvärden och om eventuella vattenanläggningar omfattas av skötselansvar.
4. Flera scenarier prövas: normal regnsäsong; återkommande skyfall med markmättnad; kombinerat flöde och funktionsbortfall.
5. Behörig aktör tar ställning till mätning, information, åtgärd eller motiverat avstående.
6. Deltagande föreningar får veta vad som blev av deras kunskap.

Detta är INTE en redogörelse för Heby 2023 och inte uppmaning till rensning av naturliga vattendrag eller obehöriga ingrepp.

## Mätbara nyttor och kostnader
**Kunskapsnytta:** verifierat nya, oberoende signaler; ökad faktisk områdestäckning; förbättrade antaganden.
**Organisatorisk nytta:** klarare mottagningsvägar, kortare svarscykler, återkoppling, gemensam tolkningskompetens.
**Beredskapsnytta:** förbättrat beslut, övning, reservlösning eller proportionerlig åtgärd.
**Kostnader:** föreningsadministration, kvalitetssäkring, återkoppling, risken för felaktiga signaler och integritetsskydd.
**Bevisning:** påstående om faktisk effekt kräver logg över åtgärd och en rimlig kontrafaktisk prövning.
