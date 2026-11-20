# Kanoniskt HARP- och källsökregister v1.0

## Status 2026-11-20
Importerat från **11 tidigare JSON-register**: **162 registreringar**, deduplicerade efter normaliserad locator till **159 unika källa-identiteter**. **0 RefA-godkända**. En tidigare originalinspektion ger inte automatiskt publiceringsklar RefA. Statusen är **registreringsfärdigt men inte fullt verifierat**.

## Filer
- [HARP_MASTER_INDEX.json](HARP_MASTER_INDEX.json) – schemaöversikt, källa/registerstatistik och shardlista.
- `HARP_MASTER_01.json`–`HARP_MASTER_06.json` – fullständiga HARP-records med historiska alias och importproveniens.
- [HARP_SOURCE_INDEX.csv](HARP_SOURCE_INDEX.csv) – en rad per källa med titel, locator, automatisk taggning, prioritet, HARP-status och importerade ID.
- [TAG_TO_SOURCE_INDEX.json](TAG_TO_SOURCE_INDEX.json) – inverterat index `tag → HARP-ID`.
- Äldre originalregister ligger orörda i `sources/` och kan användas för rekonstruktion.

## Vad registren ännu inte kan påstå
- **HARP-klarering:** ingen av posterna har ITR1/2/4/5/6 komplett.
- **Harvard:** `author_candidates` och `date_candidates` är kandidatfält, **inte färdigverifierade referenser**.
- **Tillgänglighet före 2023:** texten på en senare webbplats bevisar inte historisk åtkomst.
- **Innehållsläsning:** `reported_reviews` är tidigare arbetsanteckning, inte ny fullständig granskning.
- **Automatisk taggning:** förslagsklassificering, kan vara överinkluderande eller ofullständig.

## Sökning
`python scripts/search_sources.py --query "Heby" --tag subject:stormwater`
`python scripts/search_sources.py --tag part:d2 --tag subject:civil-society`
`python scripts/search_sources.py --priority P1 --limit 50 --json`
`python scripts/validate_research_registry.py`

## Datastyrning
[HARP Appendix O-tillämpning](../../governance/HARP_REGISTER_PROTOCOL.md), [taggstandard](../../governance/TAG_TAXONOMY.md), [roadmap](../../roadmap/MASTER_ROADMAP.md), [wiki](../../wiki/Home.md).

## Avgränsning
Detta är **all existerande strukturerad JSON-import**. URL:er som enbart förekommer i ostrukturerade Markdown-texter kan kräva separat registrering, och kommer inte automatiskt bli RefA-granskade. Ingen privat lokal `file://`-sökväg eller skyddsvärd anläggningsdetalj ska publiceras.
