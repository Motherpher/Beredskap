# Källbiblioteket
> **Status 2026-11-20:** Dessa är versionsstyrda wiki-sidor i forskningsgrenen. GitHubs separata Wiki är aktiverad men kan inte publiceras direkt med det tillgängliga GitHub-filverktyget. Se [WIKI_PUBLISHING.md](../governance/WIKI_PUBLISHING.md).

## Sanningskälla
- [HARP-master index](../sources/registry/HARP_MASTER_INDEX.json) – antal och shardar.
- [HARP-källindex CSV](../sources/registry/HARP_SOURCE_INDEX.csv) – en rad per unik källa, sökbar i GitHub eller lokalt.
- [Tagg → käll-ID](../sources/registry/TAG_TO_SOURCE_INDEX.json).
- [Originalregister](../sources/) – importerade källor i originalformat, inga poster skrivs över.

## Att söka
`python scripts/search_sources.py --query "Heby" --tag subject:stormwater`

`python scripts/search_sources.py --tag part:d2 --tag subject:civil-society`

`python scripts/search_sources.py --priority P1 --limit 30`

## Att citera
En källas `HARP-xxxxxxxx` är en **intern identitet**, inte en färdig Harvardreferens. Granska originalupphov, datum, sidnummer och åtkomstdatum innan källan används i publicerad text.

## Särskilda skillnader
Tämnarån/Örsundaån, dricksvatten/avloppsreningsverk, 2017-policy/teknisk elcentral samt samverkan/organiserad förmåga hålls metodiskt separata.
