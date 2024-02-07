# Databehandling og algoritmer: Øveprøve

## Del 1 - uten hjelpemidler

### 1.1

```python
hallo = [{"b":[4,3,5], "a":[0]}, ["hei", "hallo"]]
print(hallo[1][1][1])
```

Hva printes?

Svar: `a`

### 1.2

```python
hallo = [{"b":[4,3,5], "a":[0]}, ["hei", "hallo"]]
for i in hallo[1]:
    print(i)
```

Hva printes?

Svar:

```
hei
hallo
```

### 1.3

```python
hallo = [{"b":[4,3,5], "a":[0]}, ["hei", "hallo"]]
for i in hallo[1][1]:
    print(i)
```

Hva printes?

Svar:

```
h
a
l
l
o
```

### 1.4

```python
a = {"a": [1,2,-1], "b": [9, -9, 1]}
print(max(a["b"]))
```

Hva printes?

Svar: `9`

### 1.5

```python
representanter = [
    {
        "etternavn": "Støre",
        "foedselsdato": "25.08.1960"
        "fornavn": "Jonas Gahr",
        "id": "JGS",
        "kjoenn": 2,
        "fylke": {
            "id": "Os",
            "navn": "Oslo"
        },
        "parti": {
            "id": "A",
            "navn": "Arbeiderpartiet",
            "representert_parti": True
        }
    },
    {
        "etternavn": "Solberg",
        "foedselsdato": "24.02.1961",
        "fornavn": "Erna",
        "id": "ES",
        "kjoenn": 1,
        "fylke": {
            "historisk_fylke": False,
            "id": "Ho",
            "navn": "Hordaland"
        },
        "parti": {
            "id": "H",
            "navn": "Høyre",
            "representert_parti": True
        }
    }
]
```

a. Print Jonas Gahr Støres fødselsdag i terminalen  

Svar:

```python
print(representanter[0]["foedselsdato"])
```

b. Print Erna Solbergs fylke i terminalen  

Svar:

```python
print(representanter[1]["fylke"]["navn"])
```

c. Hva er resultatet av følgende kode?

```python
for i in representanter:
    print(i["id"][0])
```

Svar:

```
J
E
```

d. Skriv en kode som bruker en for-løkke for å printe begge representantenes etternavn

Svar:

```py
for representant in representanter:
    print(representant["etternavn"])
```

### 2.1

Skriv koden som Pseudokode.

> Du kan anta at `liste` er definert tidligere i koden, og at den ser slik ut `[2, -4, 5, 1]`

```python
høyest = liste[0]
for tall in liste:
    if tall > høyest:
        høyest = tall
print(høyest)
```

Svar:

```
SET hoyest TO første tall i lista
FOR EACH tall IN liste
  IF tall GREATHER THAN hoyest
    SET hoyest TO tall
  ENDIF
ENDFOR

DISPLAY hoyest
```

### 2.2

Hva printes her?

```pseudo
SET x TO 5
SET y TO 2
WHILE x GREATER THAN y
  DISPLAY x
  DISPLAY y
  DECREMENT x BY 1
  INCREMENT y BY 1
ENDWHILE
```

Svar:

```
5
2
4
3
```

## Del 2 - Med hjelpemidler

### Oppgave 4.1

Fil: [stortinget.json](https://raw.githubusercontent.com/thorcc/IT2-nettbok/main/pages/databehandling-og-algoritmer/vedlegg/stortinget.json)

1. Lag en for-løkke som printer navn og tilhørnde parti på alle politikerne
2. Hvilket parti har flest representanter på Stortinget og hvor mange har de?
3. Lag en ordbok som teller antall representanter hvert parti har
4. Lag et plott som viser en oversikt over partier og antall representanter
5. Hvor mange representanter har hvert parti i gjennomsnitt?

Svar: [Se fil](./oppgave-del2.py)
