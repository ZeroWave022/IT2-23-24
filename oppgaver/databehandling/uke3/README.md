# Oppgaver - Databehandling

> Oppgavene besvares i egne filer, én fil per oppgave.

## Oppgave 2.15

Lag et todo-program som leser og skriver gjøremål fra/til en `.txt`-fil.

Svar: Se [todo-app/main.py](./todo-app/main.py)

## Oppgave 2.16

### Spotify Weekly Top Songs Global

1. Hvilken sang har flest uker på Spotifys Weekly Top Songs Global?
2. Hvor mange streams har Taylor Swift til sammen på sangene hennes som er på topplista?
3. Hvilken sang gikk opp flest plasseringer fra forrige uke til denne?

- Fil: [spotify-weekly-top-songs-global-uke2-2023.json](https://raw.githubusercontent.com/thorcc/IT2-VGS-2324/master/databehandling-og-algoritmer/vedlegg/spotify-weekly-top-songs-global-uke2-2023.json)
- Tips: Se [algoritmer.md#eksempel-2-spotify](https://github.com/thorcc/IT2-VGS-2324/blob/master/databehandling-og-algoritmer/algoritmer.md#eksempel-2-spotify)

Svar: Se [spotify/main.py](./spotify/main.py)

## Oppgave 2.17

### IMDB Topp 250

1. Hvilken film ligger øverst på listen og hvem har regissert den?
2. Hva er gjennomsnittskarakteren til alle filmene på listen?
3. Hva er gjennomsnittskarakteren til de ti første filmene?
4. Hvilken regissør har regissert flest filmer på listen?
   - For hver film er regisørrer en liste. Her holder det med første regissør i listen.
   - Bonus: Alle regisørrene i regissørlistene skal telles med.

- Fil: [imdb_top250.json](https://raw.githubusercontent.com/thorcc/IT2-VGS-2324/master/databehandling-og-algoritmer/vedlegg/imdb_top250.json)

Svar: Se [imdb/main.py](./imdb/main.py)

## Oppgave 2.20

### YouTube-statistikk

> Oppgave 11 fra eksamen H23

Du skal lage et program som leser inn informasjon fra et datasett og presenterer den. Last ned datasettet her:

- [CSV/JSON](https://sokeresultat.udir.no/eksamenprovemateriell.html?kategori=rea3049&aar=2023-19&spraak=bokm%C3%A5l&trinn=annet&ferdighet=annet)

Tips: Du står fritt til å velge hvordan programmet skal presentere informasjonen, så lenge presentasjonen er godt egnet til å vise det oppgaven spør etter. Du kan også velge om du besvarer a og b i en samlet oversikt eller lager en oversikt for hvert oppgavepunkt.

Programmet du lager i denne oppgaven, skal inneholde en flerlinjet kommentar øverst som beskriver de vurderingene og valgene du har gjort for å vaske og forberede datasettet til bruk med programmet ditt.

a) Lag et program som finner og presenterer de ti landene i datasettet som har flest YouTube-kanaler.

b) Utvid programmet til å regne ut og presentere gjennomsnittlig antall abonnenter og videovisninger per kanal for hvert av disse landene.

Svar: Se [youtube/main.py](./youtube/main.py)

## Oppgave 2.21

### Oversikt over apper i Google Play Store

> Oppgave 9 fra eksamen V23

Du skal lage et program som leser inn informasjon fra datasettet og presenterer dette i to oversikter.
Last ned datasettet her:

- [CSV](https://sokeresultat.udir.no/eksamenprovemateriell.html?kategori=rea3053&aar=2023-6&spraak=bokm%C3%A5l&trinn=annet&ferdighet=annet)
- [JSON](https://sokeresultat.udir.no/eksamenprovemateriell.html?kategori=rea3053&aar=2023-7&spraak=bokm%C3%A5l&trinn=annet&ferdighet=annet)

Tips: Du står fritt til å velge hvordan programmet skal presentere informasjon, så lenge presentasjonen er godt egnet til å vise det oppgaven spør etter.

a) Lag et program som presenterer en oversikt over de tre største kategoriene målt i antall apper. Oversikten skal vise antallet apper, gjennomsnittsratingen og det gjennomsnittlige antallet installasjoner for hver av disse tre kategoriene.
Tips: For å kunne beregne gjennomsnittet av antallet installasjoner må du tilpasse innholdet i det aktuelle datafeltet. Du vil få noe uttelling om du bare viser antallet apper og gjennomsnittsratingen.

b) Utvid programmet slik at det også presenterer de tre mest populære appene, målt i antall installasjoner, i hver av disse tre kategoriene.

Svar: Se [playstore/main.py](./playstore/main.py)
