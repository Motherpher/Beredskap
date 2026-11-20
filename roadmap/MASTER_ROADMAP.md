# Roadmap – Heby under ytan och Beredskap
**Datum 2026-11-20 · status: arbets- och milstolpeplan, ej bevisad forskningsleverans.**
**Beslut:** Director. Källor och process dokumenteras i öppet repo utan sekretesskänslig information.

## Önskat slutläge
1. **Del 1** *Vilken kunskap rann förbi? – Policy, kunskap och data* (1900–2026, ex ante 2000–2023, händelsen fyra dygn/fyra timmar där underlag finns), med artikelspåret *Ett elverks tragedi*.
2. **Del 2** *Hur ser vi det som bara rinner på?* (civilsamhällets förutsättningar, kunskap, logisk/praktisk närhet och before/during/after).
3. Gemensam datakatalog, HARP RefA och argumentbank. Detta är **två parallella forskningsleveranser**, inte en sammanblandad artikel.

## Programstruktur – sju portföljströmmar (inte nya WP-nummer)
| Ström | Ordinarie WP | Leverans | Milstolpar |
|---|---|---|---|
| P0 Källstyrning och registrering | WP00, WP13 | HARP, original, DOI/filhash, dataetik, RefA | MS0, MS7 |
| P1 Naturhistorisk och geografisk rekonstruktion | WP01, WP02, WP03 | 1900–2023 serier, geografi, kartor och regn/flödesmodeller | MS1, MS2 |
| P2 Teknisk funktionsbiografi och fyra dygn | WP04, WP06, WP07 | anläggningshistoria, elsäkerhetskedja, tidslinje, effekter | MS3 |
| P3 Styrning, rätt och jämförelser | WP05, WP08, WP10, WP11, WP23 | RSA, kunskapsmottagning, beslut, alternativa åtgärder, jämförelsefall | MS4 |
| P4 Civilsamhällets förutsättningsstruktur | WP09, WP14, WP15, WP16, WP17, WP22 | föreningsbaslinje, indirekta stödresurser, behov/nyckelbehov | MS5 |
| P5 Observationssystem och framsyn | WP18, WP20, WP21 | medborgardata, SenseMaker, weak signals, scenarier och återkoppling | MS6 |
| P6 Publicistisk syntes och revision | WP12, WP13, WP19 | två delstudier, artikel, argument/motargument, Harvard och sakgranskning | MS7, MS8 |

## Verifierbara milstolpar
| ID | Leverans | Konkret exit-kriterium | Status |
|---|---|---|---|
| MS0 | Källarkitektur och taggning | All known source batches registered; no false RefA clearance | in_progress |
| MS1 | Datagap och originalåtkomst | Each P1 gap has request, responsible source authority and documented answer | not_started |
| MS2 | Historisk risk- och scenario-baslinje | Pre/post split and geographically verified hypotheses, no basin conflation | not_started |
| MS3 | Teknisk elcentral och krisens förlopp | Critical events time-stamped or explicitly unknown; electrical safety external-reviewed | not_started |
| MS4 | Institutionell kunskap och handlingsalternativ | No negligence asserted without applicable obligation, available action and causation | not_started |
| MS5 | Civilsamhällets baslinje och empiriska kedja | Registered/active/available/activated distinguished; 2023 claims corroborated | not_started |
| MS6 | Civic sensing och strategisk framsyn | At least one counterexample, bias and privacy check; signal not treated as forecast | not_started |
| MS7 | Argumentbank och integrerad syntes | Every central claim has traceable source, strongest counterargument and RefA gate | not_started |
| MS8 | Granskad rapport och två artikelförutsättningar | Independent technical/legal/factual review, HARP RefA, right of reply, public safety audit | not_started |

## Exekveringsordning och beroenden
- **P0 / MS0:** samla källor, ID-korsreferenser, taggar, wiki och evidensstandard. Klar registerstruktur betyder inte färdig fulltextgranskning.
- **P1 + P2 / MS1–MS3:** få originaldata; rekonstruera plats, flöden och elcentralens händelseförlopp. Åtskilj Örsundaån och Tämnarån, planering och faktisk anläggningssäkerhet.
- **P3 / MS4:** analysera institutionell mottagning/åtgärder/juridisk tillämplighet. Arbeta parallellt med Del 2:s baslinje.
- **P4 / MS5:** analysera civilsamhället före/under/efter med egen kapacitetsbaslinje och fall där samverkanskapaciteten faktiskt går att belägga.
- **P5 / MS6:** civic sensing → weak signals → horizon scanning → scenarier, inklusive objektiv kvalitetssäkring, täckningsbias och aktörernas autonomi.
- **P6 / MS7–MS8:** argumentation och motargument säkras, två rapportdelar produceras, efterföljande artiklar skrivs efter RefA, externa experter och bemötanderätt.

## Leveransgrindar
A. Original och versionsdatum för P1-källor. B. Rådata och modeller reproducerbart med metod. C. Händelsetidlinje om möjligt i minuter men aldrig uppfunna klockslag. D. Intern överföring/ansvarsfrågor baserat på handlingar. E. Civilsamhällets egen nytta, kostnad och inflytande prövat. F. Motbevis/hypotesalternativ. G. RefA-citering per kritiskt påstående. H. Publicering utan känsliga uppgifter.

## Data- och argumentstyrning
- [Data requirements](../data/DATA_REQUIREMENTS.json) för önskad/återfunnen/saknad data.
- [Argument ledger](../research/ARGUMENT_LEDGER.json) för önskade och preliminärt funna argument, källspår och nödvändig motprövning.
- [Milstolpar som JSON](MILESTONES.json) och [arbetsströmmar](WORKSTREAMS.json).
- [HARP-master](../sources/registry/HARP_MASTER_INDEX.json), [taxonomi](../governance/TAG_TAXONOMY.md), [wikistart](../wiki/Home.md).

**Resurs-/tidsplan:** inga fiktiva deadline-datum eller personalbudgetar. Efter MS1 ska arbetsbelastning och prioritering tidsättas mot faktisk källtillgång, intervjupersoner och granskning.
