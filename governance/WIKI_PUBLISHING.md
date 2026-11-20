# GitHub Wiki – publicering och kanonisk information
**Status:** GitHub-repot har `has_wiki=true`, men det anslutna GitHub-verktyget saknar funktion för redigering av det separata `.wiki.git`-förrådet. Sidorna i `wiki/*.md` är därför nu versionsstyrda **wiki-källfiler**, inte verifierat publicerade i Github Wiki-fliken.

## Princip
**Huvudrepo = sanningskälla** för full HARP-data, käll-ID, datakatalog, argument/evidens och WP/milstolpar.
**Wiki = orienterande, redaktionell kunskapstolkning**: navigera i begrepp, metod, forskningsdelar och beslutsgrindar. Ingen kopiering av hela register eller tekniskt känsligt material till wiki.

## Publiceringsanvisning
1. Se till att GitHub Wiki är initierad från repoets Wiki-flik (första sidan måste ibland skapas manuellt).
2. Klona separat `https://github.com/Motherpher/Beredskap.wiki.git` med eget behörigt konto.
3. Kopiera versionsstyrda `wiki/*.md` till wiki-förrådets rot.
4. Kontrollera att relativa länkar till huvudrepoet fungerar. **Vissa `../research/*`-länkar bör då ersättas med permanenta fullständiga GitHub-länkar till vald publicerad gren** (t.ex. efter merge i `main`).
5. `git add . && git commit -m "Publish research navigation wiki" && git push`.
6. Verifiera manuellt `https://github.com/Motherpher/Beredskap/wiki` och alla länkar.
7. Uppdatera wiki endast efter en godkänd repoändring så att sammanfattningar inte driver bort från originaldata.

**Ingen direkt Wiki-publicering är utförd i denna arbetsorder.**
