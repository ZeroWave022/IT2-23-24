# Oppgave 3.16

> Oppgave 6 fra eksamen V23

Vi ønsker å lage et program der brukeren skal skrive inn en poengsum fra og med 0 til og med 100, og programmet skal bestemme og skrive ut tilsvarende karakter etter følgende regler:

- Enhver poengsum under 50 får karakteren "Ikke bestått".
- Enhver poengsum fra og med 50 til og med 69 får karakteren "Bestått".
- Enhver poengsum fra og med 70 til og med 89 får karakteren "Godt bestått".
- Enhver poengsum på 90 eller høyere får karakteren "Meget godt bestått".
- Enhver poengsum som er mindre enn 0 eller større enn 100, får karakteren "Ikke gyldig poengsum!"".

Pseudokoden nedenfor beskriver logikken og programflyten i et forslag til dette programmet:

```pseudo
PRINT "Skriv inn poengsummen din:"
READ poengsum
IF poengsum LESSER THAN 50
  PRINT "Ikke bestått"
ELSE IF poengsum GREATER THAN 50 AND poengsum LESSER THAN 69
  PRINT "Bestått"
ELSE IF poengsum GREATER THAN 70 AND poengsum LESSER THAN 89
  PRINT "Godt bestått"
ELSE IF poengsum GREATER THAN 90 AND poengsum LESSER THAN 100
  PRINT "Meget godt bestått"
ELSE
  PRINT "Ikke gyldig poengsum!"
ENDIF
```

a) Implementer den foreslåtte pseudokoden i det programmeringsspråket du foretrekker, gjennomfør testene som er beskrevet i den følgende testplanen, og fyll inn de faktiske resultatene du får.

| Test nr. | Input-verdier | Forventet resultat    | Faktisk resultat      |
| -------- | ------------- | --------------------- | --------------------- |
| 1        | Poengsum: 30  | Ikke bestått          | Ikke bestått          |
| 2        | Poengsum: 65  | Bestått               | Bestått               |
| 3        | Poengsum: 82  | Godt bestått          | Godt bestått          |
| 4        | Poengsum: 97  | Meget godt bestått    | Meget godt bestått    |
| 5        | Poengsum: 102 | Ikke gyldig poengsum! | Ikke gyldig poengsum! |
| 6        | Poengsum: 0   | Ikke bestått          | Ikke bestått          |
| 7        | Poengsum: 50  | Bestått               | Ikke gyldig poengsum! |
| 8        | Poengsum: 69  | Bestått               | Ikke gyldig poengsum! |
| 9        | Poengsum: 70  | Godt bestått          | Ikke gyldig poengsum! |
| 10       | Poengsum: 89  | Godt bestått          | Ikke gyldig poengsum! |
| 11       | Poengsum: 90  | Meget godt bestått    | Ikke gyldig poengsum! |
| 12       | Poengsum: 100 | Meget godt bestått    | Ikke gyldig poengsum! |
| 13       | Poengsum: -1  | Ikke gyldig poengsum! | Ikke bestått          |

Kode:

```python
poeng_liste = [30, 65, 82, 97, 102, 0, 50, 69, 70, 89, 90, 100, -1]

for i, poeng in enumerate(poeng_liste, 1):
    if poeng < 50:
        print(f"{i} Ikke bestått")
    elif poeng > 50 and poeng < 69:
        print(f"{i} Bestått")
    elif poeng > 70 and poeng < 89:
        print(f"{i} Godt bestått")
    elif poeng > 90 and poeng < 100:
        print(f"{i} Meget godt bestått")
    else:
        print(f"{i} Ikke gyldig poengsum!")
```

b) Er de forventede resultatene like de faktiske resultatene? Hvis ikke: Finn de logiske feilene i pseudokoden som forårsaker det. Skriv inn og forklar svaret ditt.

Resultatene er ikke like, fordi grenseverdiene mellom de ulike nivåene er ikke tatt med. Hvis vi istedenfor bruker operatorene GREATER THAN OR EQUAL og LESSER THAN OR EQUAL vil vi få med grenseverdier (50, 69, 70, 89, osv.) og da blir forventet resultat likt med det faktiske resultatet.

c) Rett opp programmet fra punkt a slik at du får det forventede resultatet. Lever inn kildekoden på slutten av eksamenen.

```python
poeng_liste = [30, 65, 82, 97, 102, 0, 50, 69, 70, 89, 90, 100, -1]

for i, poeng in enumerate(poeng_liste, 1):
    if 0 <= poeng < 50:
        print(f"{i} Ikke bestått")
    elif 50 <= poeng <= 69:
        print(f"{i} Bestått")
    elif 70 <= poeng <= 89:
        print(f"{i} Godt bestått")
    elif 90 <= poeng <= 100:
        print(f"{i} Meget godt bestått")
    else:
        print(f"{i} Ikke gyldig poengsum!")
```
