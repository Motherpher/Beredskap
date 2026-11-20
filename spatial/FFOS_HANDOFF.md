# FFOS – föreslaget integrations- och uppdragsöverlämnande

**Status: DISCOVERY_ONLY / NOT_DISPATCHED.** En ny QGIS-gren innebär inte att det finns FFOS-jobb, tillstånd, tokens eller annan operativ runtime.

## Behåll källans auktoritet
- Beredskaps GitHub-ärende och kartkrav utgör beslutskälla för tematisk fråga.
- FF-Spatial job ID, geodata-asset, QA och produkt versioneras i FF-Spatial.
- FFOS kan **projektera** till portfolio eller dirigera ett manuellt godkänt jobb, men får inte bli primär källa till kartans empiriska innehåll.
- Direktors acceptans krävs separat för cross-repo skrivning, källpromovering, dataåtkomst och publicering.

## Kontroller som ännu inte passerats
1. Driver/Director-godkänt integrationsändamål, inklusive om FFOS:s frivilliga DevOps-modell ska användas – **ingen automatisk aktivering**.
2. Exakt godkänd job/asset- och eventstruktur, med autentisering och minstprivilegium.
3. Test i isolerad miljö med GitHub receipt och FF-Spatial verifierad output.
4. Eventuell operativ registrering i FFOS:s styrning efter godkännande.
5. Oberoende teknisk, HARP- och integritetskontroll i Beredskap.

Läs: [FFOS-mandat](https://github.com/Motherpher/FFOS/blob/main/README.md) · [Projekt-synkronisering – review candidate](https://github.com/Motherpher/FFOS/blob/main/docs/governance/github-estate/PROJECT-SYNCHRONISATION-CONTRACT-v1.md).

**Ingen extern ändring i FFOS görs som ett led i denna initiering.**


## Koordinerad uppföljning via GitHub
- [Beredskap #12 – tematik och leveransacceptans](https://github.com/Motherpher/Beredskap/issues/12).
- [FF-Spatial #51 – source promotion, asset/QGIS compatibility](https://github.com/Motherpher/FF-Spatial/issues/51).
- [FFOS #127 – framtida upptäckt av cross-repo-samordning](https://github.com/Motherpher/FFOS/issues/127), **inte aktiverad dispatch**.
- [Beredskap Draft PR #11 – QGIS-grenen](https://github.com/Motherpher/Beredskap/pull/11).

Samordningsärenden är granskbara beroenden, inte bevis för att API:er, geodata eller runtime är operativa.
