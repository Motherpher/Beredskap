# Data- och processmodell: lokal observation + självtolkad berättelse
**Status:** schema för metodpilot; inga rader utgör faktiskt insamlade Hebyobservationer.

## A. Observation (OBS)
| Fält | Typ | Betydelse |
|---|---|---|
| obs_id | sträng | pseudonymt ID, inte personidentifierare |
| event_at | tidsstämpel/datum | när observationen avser |
| submitted_at | datum | när den rapporterades; kan skilja sig avsevärt |
| area_id | grovt område/avrinningsdel | undvik exakta koordinater offentligt vid risk |
| location_accuracy | klass | exakt med godkänd åtkomst, approximativ, okänd |
| observation_type | klass | vattenstånd visuellt, trumma, dike, sediment, vegetation, erosion, framkomlighet, naturvärde, annat |
| observation_text | neutral text | vad som sågs, skilt från förklaringar och åtgärdsönskemål |
| evidence_type | klass | foto, jämförande foto, annan dokumentation, enbart minnesuppgift |
| conditions | strukturerat | säsong, väder, tidigare regn, markfuktighet om känd |
| revisit_id | ID/NULL | knyter observationsserie till samma plats eller stråk |
| visit_mode | klass | planerat återbesök / rutinmässig tur / opportunistisk observation |
| role_group | grov kategori | förening, markägare, boende, annan; lämna identifiering frivillig |
| ecological_caution | text/flagga | skyddat område, naturvärde, okänt |
| self_reported_effect | klass | vad deltagaren upplevde (inte verifierad kausalitet) |
| validation | klass | ny/triagerad/validerad/motsagd/under utredning |
| expert_notes | kort text | fackbedömning, käll-ID, tillämpad ansvarskedja |
| feedback_at | datum/NULL | återkoppling till deltagare |
| action_outcome | klass | ej aktuellt/följ upp/utred/åtgärda/avstå med motivering |
| release_status | klass | intern/aggregerad/publik/sekretessprövad |

## B. SenseMaker-kompatibel narrativpost (NAR)
- `narrative_id`, `related_obs_id` frivilligt, `told_at`, `short_story`, `self_signification`, `optional_context_tags`, `consent_for_use`, `publication_scope`.
- Exempel på öppen inbjudan: **'Berätta om en plats i kommunen där du märkt en förändring som du tror kan påverka hur människor eller naturen klarar kraftigt regn.'**
- Exempel på egen triangulär meningsmarkering (koncept, inte färdig licensierad enkät): *I din berättelse var det främst … (A) vattnets väg och framkomlighet, (B) landskapets ekologiska funktion, (C) människors vardagliga möjligheter*. Låt deltagaren vikta utan att tvinga in berättelsen i en 'risk = dåligt'-tolkning. Pilotpröva innan insamling.
- Berättelser är **subjektiva erfarenheter**, inte standardiserade hydrologiska mätningar eller automatiska prognossignaler.

## C. Geografisk täckning (VISIT)
- `visit_id | date | segment_id | season | conditions | covered_or_not | observation_count | coverage_limit`.
- Värdera andelen återbesök och områden som aldrig besöks, inte bara positiva rapporter.
- Ingen kontinuerlig GPS-spårning av individer; använd planerade stråk och grova aggregeringar.

## D. Triage- och åtgärdskedja
`OBS/NAR → kvalitetskontroll → ansvar/rådighet → expertbedömning → beslut/avstående → publik återkoppling → uppdaterad lägesbild`.

**Åtgärdsgate:** Inga instruktioner till frivilliga att rensa diken, flytta nedfallna träd, beträda privata områden eller undersöka känslig infrastruktur. När observation avser naturligt vattendrag eller gammal vattenanläggning krävs ekologisk och juridisk kompetens innan slutsats om underhållsbehov.
