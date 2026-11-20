# Beredskap
### Kunskapsutveckling och operativ design för civilsamhällets roll i kris och samhällelig resiliens

**Form & Flöde · Fördjupning · Samverkan · Data · System · Strategi · Operativ design**

Beredskap är en öppen, läsbar och spårbar arbetsyta för att förstå **hur samhällens förutsättningar, aktörer, resurser och kunskap utvecklar förmåga före, under och efter kriser**. Fokus ligger på **fredstida samhällsstörningar**, särskilt översvämningar och skogsbränder, med civilsamhället och den idéburna sektorn som ett eget samhällsperspektiv.

> **Viktig avgränsning:** *Heby under ytan* är ett **fördjupningsarbete och kunskapsutveckling**, inte ett formellt forskningsprojekt. Deep Research är en insamlings- och analysmetod för rapportunderlag. Rapporter och artiklar är möjliga kunskapsprodukter, inte syftet i sig.

## Öppna arbetet
| Läsning | Vad du hittar |
|---|---|
| **[DASHBOARD – status och läge](DASHBOARD.md)** | Milstolpar, källor, kartor, nästa beslut och länkar till allt arbete |
| **[STARTA HÄR – läs- och arbetsguide](START_HERE.md)** | Vägledning för att läsa, hitta och arbeta i repot |
| **[Kunskapskarta – alla Markdown-sidor](INDEX.md)** | Samlad navigering till analyser, kataloger, governance och leveranser |
| **[Uppdrag och perspektiv](MISSION.md)** | Varför detta arbete finns, vad som ska utvecklas och begreppen från Form & Flöde |
| **[Fördjupningen Heby under ytan](kunskap/HEBY_UNDER_YTAN.md)** | Del 1, Del 2, historia 1900–2026, krisen 2023 och berättelsen om elcentralen |
| **[Civilsamhället och idéburen beredskap](kunskap/CIVILSAMHALLET.md)** | Förutsättningar, närhet, förmågor, data och nyckelnyttor |
| **[Kartor och den geografiska kontexten](kunskap/KARTOR_OCH_GEOGRAFI.md)** | Multinivåperspektiv på Heby och Uppsala län; FF-Spatial/QGIS-spåret |
| **[Källbiblioteket](kallor/README.md)** | Läsbara Markdown-kataloger, HARP, taggar och källstatus |
| **[Databehov](kunskap/DATA_OCH_BELAGG.md)** | Vad som behövs, vad som hittats och vad som måste verifieras |
| **[Argumentbanken](kunskap/ARGUMENT_OCH_MOTPROVNING.md)** | Vilka resonemang prövas och vad skulle tala emot dem? |
| **[Roadmapen](roadmap/MASTER_ROADMAP.md)** | Arbetsströmmar, WP00–WP23, milstolpar och ansvar |

## Vad är Heby under ytan?
**Heby under ytan – perspektiv på översvämningen 2023** använder ett verkligt krisförlopp för att förstå beredskap som en relation mellan **natur, offentlig styrning, infrastruktur, lokal kunskap och civilsamhällets vardagliga kapacitet**.

| Fördjupning | Kärnfråga | Produkt |
|---|---|---|
| **Del 1 – Vilken kunskap rann förbi?** | Vilken riskkunskap och data fanns, var tog den vägen och hur omsattes den? | Rapportunderlag och artikeln *Ett elverks tragedi* |
| **Del 2 – Hur ser vi det som bara rinner på?** | Hur kan civilsamhällets förutsättningar, relationer och kunskap stärka beredskapen? | Rapportunderlag, behovs-/nyckelnyttemodell och samverkansperspektiv |
| **Multinivåkartor** | Vad blir synligt när samhällsgeografi, civilsamhälle, sårbarheter och förändring möts? | QGIS/FF-Spatial-piloter och kartbaserat kunskapsstöd |

## Status – 20 november 2026
| Register och leverans | Verifierat nuläge |
|---|---:|
| Kanoniskt registrerade källor | **177** |
| Fullständigt HARP RefA-klarerade | **0** |
| Prioriterade databehov | **20** |
| Prövbara argument och motargument | **15** |
| Öppnade ärenden för milstolpar | **9** |
| Färdigverifierade Heby-kartprodukter | **0** |
| API-kopplingar testade för Heby | **0** |

**Status är en nulägesbild, inte en realtidsavläsning.** Fullkvalificerade belägg, QGIS-datainläsning och slutprodukter återstår. Se [dashboarden](DASHBOARD.md).

## Infrastruktur och ansvar
- **Beredskap** äger fördjupningens problemformulering, kontext, aktörer, tematiska kartbehov, argument, HARP-källregister och publikationer.
- **[FF-Spatial](https://github.com/Motherpher/FF-Spatial)** äger auktoritativa geodata, geografisk versionshantering, QGIS-exekvering, lager- och kartkontrakt.
- **[FFOS](https://github.com/Motherpher/FFOS)** är operativ samordning, **inte** automatisk överordnad dataägare eller aktiverad integration.
- **Director** fastställer ambition, godkända API:er, utvecklingsgränser, publicering och aktivering av eventuella arbetsflöden.

**[Öppna QGIS-arbetsgrenen](https://github.com/Motherpher/Beredskap/tree/spatial/qgis-heby-uppsala-v1)** – förberedelser för Heby/Uppsala, utan påstådd liveanslutning.

### Käll- och säkerhetsprincip
En källa som har hittats är inte automatiskt verifierad eller användbar för ett specifikt påstående. *Ex ante* kunskap skiljs från efterhandskunskap. Offentliga kartor över civilsamhället ska inte exponera privata hushåll, känsliga verksamheter eller skyddsvärda detaljer kring kritisk infrastruktur.

---
**Börja med [DASHBOARD](DASHBOARD.md), därefter [STARTA HÄR](START_HERE.md).** All central läsning finns som Markdown, även när maskinregister lagras i JSON/CSV.

## GIS-samordning – status 20 november 2026
QGIS-grenen har nu en [separat Draft PR #11](https://github.com/Motherpher/Beredskap/pull/11) och godkänd statisk kontraktsvalidering. **Detta är ännu inte en fungerande API- eller QGIS-körning.** Följ de tre ansvarsägda ärendena:

- [Beredskap #12 – Heby/Uppsala GIS-uppdrag och acceptans](https://github.com/Motherpher/Beredskap/issues/12).
- [FF-Spatial #51 – geografiska källor, assets och QGIS-kontrakt](https://github.com/Motherpher/FF-Spatial/issues/51).
- [FFOS #127 – möjlig framtida samordning (discovery only)](https://github.com/Motherpher/FFOS/issues/127).

[Öppna QGIS-grenens README](https://github.com/Motherpher/Beredskap/blob/spatial/qgis-heby-uppsala-v1/spatial/README.md) · [Se atlasens åtta kartprodukter](https://github.com/Motherpher/Beredskap/blob/spatial/qgis-heby-uppsala-v1/spatial/ATLAS.md).

## Artiklar – synopsis och storyboard
- **[Artikel 1: Ett elverks tragedi](article/ARTIKEL_01_SYNOPSIS_STORYBOARD.md)** – fyra tidsskalor, elcentralens beroendekedja, historisk kunskap, risk och beslut.
- **[Artikel 2: Vem tar hand om dem som tar hand om krisen?](article/ARTIKEL_02_SYNOPSIS_STORYBOARD.md)** – civilsamhällets vardagliga förutsättningar, logisk/praktisk närhet, egenvärde, data och samverkan.

Båda är **redaktionella synopsis och storyboard v1.0**, inte färdigskrivna eller RefA-sakgranskade artiklar. Artikel 2:s barnomsorgsexempel är hypotetiskt.


### Aktuell redaktionell brief v1.1

[Artikel 1 och 2 – korta, berättande synopsis och storyboard](article/README.md) · [Källor som stödjer, problematiserar och kan kullkasta ett resonemang](article/KALLOR_I_BERATTELSEN.md). Den gemensamma strukturen är **situation → perspektiv 1–3 → källor → syntes → argumentation → relevansgods → brygga**. Artiklarna är essäer inom kunskapsutveckling, inte formaliserade forskningsrapporter.
