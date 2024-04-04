# Oppgaver - apputvikling

I disse oppgavene skal du lage et Pokemon-spill.

## 3.1 - Hovedmeny

Lag en hovedmeny i terminalen med valgene:

```
1. Se pokemonoversikt
2. Se treneroversikt
3. Lag trener
4. Avslutt
```

Du skal bare lage hovedmenyen - ikke implementere menyvalgene.

Svar: Se [main.py](./main.py)

## 3.2 - Lese inn data

1. Last ned filen [pokemon.json](https://raw.githubusercontent.com/thorcc/IT2-nettbok/main/pages/apputvikling/vedlegg/pokemon.json).
2. Les inn filen i et python-program og lagre innholdet i en variabel.

Svar: Se [main.py](./main.py)

## 3.3 - UML-diagram

Lag et UML-diagram som viser hvilke egenskaper en Pokemon skal ha i spillet ditt.

Du velger selv hvilke egenskaper en pokemon skal ha - se hva slags info som finnes i JSON-fila.
Du kan vente med å legge til metoder.

Svar:

![UML-diagram](./uml.png)

## 3.4 - Pokemon-klasse

Lag en Pokemon-klasse som følger UML-diagrammet fra forrige oppgave.

Svar: Se [pokemon.py](./pokemon.py)

## 3.5 - str-metode

Lag en str-metode som returnerer navnet på en pokemon og minst en annen egenskap (eks: `HP`).

Svar: Se [pokemon.py](./pokemon.py)

## 3.6 - Liste med pokemon

Lag en tom liste i programmet ditt, og fyll listen med pokemon-objekter (objekter av klassen Pokemon).

Svar: Se [main.py](./main.py)

## 3.7 - Vis pokemonoversikt

Implementer menyvalget `1. Se pokemonoversikt`.
Hvis brukeren velger dette valget skal en liste over alle pokemon-ene vises i terminalen.

Svar: Se [main.py](./main.py)

## 3.8 - Trener-klasse

En trener skal ha egenskapene navn, som er en streng, og en pokemonliste som er en med pokemon.
Treneren skal også ha en metode for å legge til pokemon i pokemonlisten, og en metode for å fjerne pokemon.

1. Legg til en trener-klasse i UML-diagrammet ditt.
2. Lag Python-kode for trener-klassen.
3. Lag en str-metode som returnerer navnet på treneren og antall pokemon treneren har.

Svar: Se [trainer.py](./trainer.py)

## 3.9 - Legg til trener

Implementer menyvalget `3. Legg til trener`.
Hvis brukeren velger dette valget skal brukeren få spørsmål om navn, også skal programmet opprette en ny trener med dette navnet og en tom liste med pokemon.

Svar: Se [main.py](./main.py)

## 3.10 - Treneroversikt

Implementer menyvalget `2. Se treneroversikt`.
Hvis brukeren velger dette valget skal en liste over alle trenerne vises i terminalen.

Svar: Se [main.py](./main.py)

## 3.11 - Legg-til-pokemon-metode

Lag en metode i trenerklassen som legger til en pokemon i pokemon-lista til en trener.

Svar: Se [trainer.py](./trainer.py)

## 3.12 - Fjern-pokemon-metode

Lag en metode i trenerklassen som tar inn en pokemon og fjerner pokemon-en fra pokemon-lista.

Svar: Se [trainer.py](./trainer.py)
