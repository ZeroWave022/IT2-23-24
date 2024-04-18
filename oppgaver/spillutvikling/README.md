# Oppgave 4.2: Manic Mansion

> Oppgave 12 fra eksamen H23

I denne oppgaven skal du utvikle et spill som heter Manic Mansion.

I Manic Mansion styrer spilleren et menneske som prøver å hente hjem sauene sine en etter en.
På veien må mennesket ta seg forbi hindringer og unngå å bli tatt av spøkelser.

Spillet starter med et spillebrett, et menneske, et spøkelse, tre hindringer og tre sauer.
Mennesket skal styres av spilleren, og målet med spillet er å komme seg over på den andre siden av brettet og hente en sau flest mulig ganger uten å være i kontakt med noen av spøkelsene.

Du bør sette av om lag to timer til denne oppgaven.

## Krav

- Ved oppstart skal spillet bestå av et spillebrett, et menneskeobjekt, et spøkelsesobjekt, tre hindringsobjekter og tre saueobjekter.
- Det skal være en liten frisone både på venstre og høyre side av spillebrettet hvor kun mennesker og sauer kan oppholde seg, mens det ikke kan være spøkelser eller hindringer der.
- Spøkelses- og hindringsobjektene plasseres på tilfeldige steder på spillebrettet, menneskeobjektet i frisonen på venstre side av spillebrettet og sauene på tilfeldige steder i frisonen på høyre side av spillebrettet. Ingen objekter skal være oppå hverandre.
- Ulike typer objekter skal være visuelt forskjellige.
- Menneskeobjektet starter i ro og kan bevege seg i rolig hastighet opp, ned, til venstre eller til høyre. Retningen styres med piltaster (alternativt tastene W, S, A og D).
- Spøkelsesobjektene starter på et tilfeldig sted på spillebrettet, men altså ikke i noen av frisonene. Spøkelsesobjektene beveger seg med konstart fart i en tilfeldig retning. Spøkelsesobjektene kan bevege seg på skrå i flere forskjellige vinkler. Når et spøkelse treffer kanten av spillebrettet eller kanten på en av frisonene, endrer spøkelset retning. Spøkelset blokkeres ikke av hindringer eller av andre spøkelser, men går tvers gjennom dem.
- Når menneskeobjektet treffer en hinding eller kanten av spillebrettet, blokkeres menneskeobjektet helt til retningen endres.
- Når menneskeobjektet treffer et saueobjekt, skal det følgende skje:
  - Saueobjektet fjernes fra spillebrettet (dette representerer at mennesket bærer sauen). (Alternativt: Saueobjektet «festes» til menneskeobjektet og følger mennesekeobjektets bevegelser.)
  - Farten til menneskeobjektet reduseres.
  - Fram til saueobjektet er levert på den andre siden, vil en kollisjon mellom menneskeobjektet og et annet saueobjekt føre til at spillet stoppes.
- Når menneskeobjektet kommer tilbake til startsonen på venstre side av spillebrettet, skal det følgende skje:
  - Spilleren får et poeng.
  - Farten til menneskeobjektet økes til samme fart som ved spillets start.
  - Et nytt saueobjekt plasseres et tilfeldig sted i frisonen til høyre på spillebrettet.
  - Et nytt spøkelsesobjekt og et nytt hindringsobjekt plasseres på tilfeldige steder på spillebrettet.
- Når menneskeobjektet, med eller uten sau, treffer et spøkelsesobjekt, skal spillet stoppes.
