# Ukens oppgaver

## Oppgave 2.9

1. Kopier listen med vinnere av gullballen 👇👇 inn i en python-fil og print ordboken til den første spilleren.
2. Lag en for-løkke som printer navn og nasjonalitet på hver spiller.
3. Utvid koden slik at for-løkken også printer antall gullballer spillerne har vunnet.

<details>
<summary>Klikk for startkode</summary>

```python
gullballen = [
  {
    "navn": "Luís Figo",
    "år": [2000],
    "nasjonalitet": "Portugal",
    "klubber": ["Real Madrid"]
  },
  {
    "navn": "Michael Owen",
    "år": [2001],
    "nasjonalitet": "England",
    "klubber": ["Liverpool"]
  },
  {
    "navn": "Ronaldo",
    "år": [2002],
    "nasjonalitet": "Brasil",
    "klubber": ["Real Madrid"]
  },
  {
    "navn": "Pavel Nedvěd",
    "år": [2003],
    "nasjonalitet": "Tsjekkia",
    "klubber": ["Juventus"]
  },
  {
    "navn": "Andriy Shevchenko",
    "år": [2004],
    "nasjonalitet": "Ukraina",
    "klubber": ["Milan"]
  },
  {
    "navn": "Ronaldinho",
    "år": [2005],
    "nasjonalitet": "Brasil",
    "klubber": ["Barcelona"]
  },
  {
    "navn": "Fabio Cannavaro",
    "år": [2006],
    "nasjonalitet": "Italia",
    "klubber": ["Real Madrid"]
  },
  {
    "navn": "Kaká",
    "år": [2007],
    "nasjonalitet": "Brasil",
    "klubber": ["Milan"]
  },
  {
    "navn": "Cristiano Ronaldo",
    "år": [2008, 2013, 2014, 2016, 2017],
    "nasjonalitet": "Portugal",
    "klubber": ["Manchester United", "Real Madrid"]
  },
  {
    "navn": "Lionel Messi",
    "år": [2009, 2010, 2011, 2012, 2015, 2019, 2021, 2023],
    "nasjonalitet": "Argentina",
    "klubber": ["Barcelona", "Paris Saint-Germain F.C.", "Inter Miami"]
  },
  {
    "navn": "Luka Modric",
    "år": [2018],
    "nasjonalitet": "Kroatia",
    "klubber": ["Real Madrid"]
  },
  {
    "navn": "Karim Benzema",
    "år": [2022],
    "nasjonalitet": "Frankrike",
    "klubber": ["Real Madrid"]
  }
]
```

</details>

## Oppgave 2.10

1. Kopier listen med informasjon over de 30 mest fulgte Instagram-kontoene 👇👇 inn i en python-fil.
2. Hvor mange følgere har kontoene på listen i gjennomsnitt?
3. Hvor mange kontoer på listen kommer ikke fra USA?

<details>
<summary>Klikk for startkode</summary>

```python
top_30 = [
    {"name": "Cristiano Ronaldo", "account": "@cristiano", "followers": 617.16, "nationality": "Portugal"},
    {"name": "Leo Messi", "account": "@leomessi", "followers": 497.05, "nationality": "Argentina"},
    {"name": "Selena Gomez", "account": "@selenagomez", "followers": 429.66, "nationality": "United States"},
    {"name": "Kylie Jenner", "account": "@kyliejenner", "followers": 399.45, "nationality": "United States"},
    {"name": "Dwayne Johnson", "account": "@therock", "followers": 395.59, "nationality": "United States"},
    {"name": "Ariana Grande", "account": "@arianagrande", "followers": 380.78, "nationality": "United States"},
    {"name": "Kim Kardashian", "account": "@kimkardashian", "followers": 364, "nationality": "United States"},
    {"name": "Beyoncé", "account": "@beyonce", "followers": 319.6, "nationality": "United States"},
    {"name": "Khloé Kardashian", "account": "@khloekardashian", "followers": 311.3, "nationality": "United States"},
    {"name": "Nike", "account": "@nike", "followers": 306, "nationality": "United States"},
    {"name": "Justin Bieber", "account": "@justinbieber", "followers": 304.9, "nationality": "Canada"},
    {"name": "Taylor Swift", "account": "@taylorswift", "followers": 282.8, "nationality": "United States"},
    {"name": "Neymar Jr", "account": "@neymarjr", "followers": 282.7, "nationality": "Brazil"},
    {"name": "Kendall Jenner", "account": "@kendalljenner", "followers": 279.9, "nationality": "United States"},
    {"name": "Jennifer Lopez", "account": "@jlo", "followers": 277.2, "nationality": "United States"},
    {"name": "Nicki Minaj", "account": "@nickiminaj", "followers": 262.5, "nationality": "Trinidad and Tobago"},
    {"name": "National Geographic", "account": "@natgeo", "followers": 206.9, "nationality": "United States"},
    {"name": "Lionel Andrés Messi Cuccittini", "account": "@leomessi10", "followers": 201.8, "nationality": "Argentina"},
    {"name": "Miley Cyrus", "account": "@mileycyrus", "followers": 198.7, "nationality": "United States"},
    {"name": "Katy Perry", "account": "@katyperry", "followers": 198.4, "nationality": "United States"},
    {"name": "Kourtney Kardashian", "account": "@kourtneykardash", "followers": 196.8, "nationality": "United States"},
    {"name": "Kevin Hart", "account": "@kevinhart4real", "followers": 195.8, "nationality": "United States"},
    {"name": "Ellen DeGeneres", "account": "@theellenshow", "followers": 194.7, "nationality": "United States"},
    {"name": "Virat Kohli", "account": "@virat.kohli", "followers": 194.5, "nationality": "India"},
    {"name": "Billie Eilish", "account": "@billieeilish", "followers": 193.9, "nationality": "United States"},
    {"name": "Rihanna", "account": "@badgalriri", "followers": 191.5, "nationality": "Barbados"},
    {"name": "Zendaya", "account": "@zendaya", "followers": 190.9, "nationality": "United States"},
    {"name": "Drake", "account": "@champagnepapi", "followers": 190.8, "nationality": "Canada"},
    {"name": "Emma Watson", "account": "@emmawatson", "followers": 189.7, "nationality": "United Kingdom"},
    {"name": "LeBron James", "account": "@kingjames", "followers": 188.8, "nationality": "United States"}
]
```

</details>

### Oppgave 2.11

1. Kopier listen med informasjon over de 30 mest befolkede land 👇👇 inn i en python-fil og print ordboken til Argentina.
2. Lag en for-løkke som printer navn, hovedstad og antall språk for hvert land.
3. Hvilket land har flest språk?
4. Lag en ordbok som holder oversikt over språk og antall land som har språket som offisielt språk.
    - Tips: Språk er en liste - du burde bruke en for-løkke som går gjennom språk inne i for-løkken for land.
5. Sorter ordboken og print ut språket med flest land og antall land.
    - Fasit: `Engelsk: 7`

<details>
<summary>Klikk for startkode</summary>

```python
land_info = [
    {"land": "Kina", "hovedstad": "Beijing", "befolkning": 1410000000, "språk": ["Mandarin"]},
    {"land": "India", "hovedstad": "New Delhi", "befolkning": 1390000000, "språk": ["Hindi", "Engelsk"]},
    {"land": "USA", "hovedstad": "Washington, D.C.", "befolkning": 331000000, "språk": ["Engelsk"]},
    {"land": "Indonesia", "hovedstad": "Jakarta", "befolkning": 273000000, "språk": ["Indonesisk"]},
    {"land": "Pakistan", "hovedstad": "Islamabad", "befolkning": 225000000, "språk": ["Urdu", "Engelsk"]},
    {"land": "Brasil", "hovedstad": "Brasília", "befolkning": 213000000, "språk": ["Portugisisk"]},
    {"land": "Nigeria", "hovedstad": "Abuja", "befolkning": 211000000, "språk": ["Engelsk"]},
    {"land": "Bangladesh", "hovedstad": "Dhaka", "befolkning": 166000000, "språk": ["Bengali"]},
    {"land": "Russland", "hovedstad": "Moskva", "befolkning": 146000000, "språk": ["Russisk"]},
    {"land": "Mexico", "hovedstad": "Mexico City", "befolkning": 128000000, "språk": ["Spansk"]},
    {"land": "Japan", "hovedstad": "Tokyo", "befolkning": 125000000, "språk": ["Japansk"]},
    {"land": "Etiopia", "hovedstad": "Addis Ababa", "befolkning": 118000000, "språk": ["Amharisk"]},
    {"land": "Filippinene", "hovedstad": "Manila", "befolkning": 113000000, "språk": ["Filippinsk"]},
    {"land": "Egypt", "hovedstad": "Kairo", "befolkning": 104000000, "språk": ["Arabisk"]},
    {"land": "Vietnam", "hovedstad": "Hanoi", "befolkning": 97400000, "språk": ["Vietnamesisk"]},
    {"land": "DR Kongo", "hovedstad": "Kinshasa", "befolkning": 90000000, "språk": ["Fransk"]},
    {"land": "Turkey", "hovedstad": "Ankara", "befolkning": 83700000, "språk": ["Tyrkisk"]},
    {"land": "Iran", "hovedstad": "Teheran", "befolkning": 83700000, "språk": ["Persisk"]},
    {"land": "Tyskland", "hovedstad": "Berlin", "befolkning": 83000000, "språk": ["Tysk"]},
    {"land": "Thailand", "hovedstad": "Bangkok", "befolkning": 70000000, "språk": ["Thai"]},
    {"land": "Frankrike", "hovedstad": "Paris", "befolkning": 67000000, "språk": ["Fransk"]},
    {"land": "Storbritannia", "hovedstad": "London", "befolkning": 67000000, "språk": ["Engelsk"]},
    {"land": "Italia", "hovedstad": "Roma", "befolkning": 60300000, "språk": ["Italiensk"]},
    {"land": "Sør-Afrika", "hovedstad": "Pretoria, Cape Town, Bloemfontein", "befolkning": 60000000,
     "språk": ["Afrikaans", "Engelsk", "isiNdebele", "isiXhosa", "isiZulu", "sesotho", "Setswana", "siSwati", "Tshivenda", "Xitsonga"]},
    {"land": "Myanmar", "hovedstad": "Naypyidaw", "befolkning": 54400000, "språk": ["Burmese"]},
    {"land": "Sør-Korea", "hovedstad": "Seoul", "befolkning": 51700000, "språk": ["Koreansk"]},
    {"land": "Colombia", "hovedstad": "Bogotá", "befolkning": 50300000, "språk": ["Spansk"]},
    {"land": "Kenya", "hovedstad": "Nairobi", "befolkning": 49000000, "språk": ["Swahili", "Engelsk"]},
    {"land": "Spania", "hovedstad": "Madrid", "befolkning": 47000000, "språk": ["Spansk"]},
    {"land": "Argentina", "hovedstad": "Buenos Aires", "befolkning": 45000000, "språk": ["Spansk"]},
]
```

</details>

<details>
<summary>Klikk for fasit til deloppgave 3</summary>

```python
{
  'Mandarin': 1,
  'Hindi': 1,
  'Engelsk': 7,
  'Indonesisk': 1,
  'Urdu': 1,
  'Portugisisk': 1,
  'Bengali': 1,
  'Russisk': 1,
  'Spansk': 4,
  'Japansk': 1,
  'Amharisk': 1,
  'Filippinsk': 1,
  'Arabisk': 1,
  'Vietnamesisk': 1,
  'Fransk': 2,
  'Tyrkisk': 1,
  'Persisk': 1,
  'Tysk': 1,
  'Thai': 1,
  'Italiensk': 1,
  'Afrikaans': 1,
  'isiNdebele': 1,
  'isiXhosa': 1,
  'isiZulu': 1,
  'sesotho': 1,
  'Setswana': 1,
  'siSwati': 1,
  'Tshivenda': 1,
  'Xitsonga': 1,
  'Burmese': 1,
  'Koreansk': 1,
  'Swahili': 1
}
```

</details>

## Oppgave 2.18

I denne oppgaven skal du lage et værprogram der brukeren kan skrive inn navnet på et stedsnavn og få ut værmeldingen på det aktuelle stedet.

1. Bruk bibliotektet [Geocoder](https://geocoder.readthedocs.io/providers/ArcGIS.html) og lag et program der brukeren kan skrive inn et stedsnavn, også printer programmet lengdegrad (lon) og breddegrad (lat) til stedet.
2. Bruk Meterologisk intstitutts API og utvid programmet slik at værmeldingen for stedet brukeren skrev inn i printes.
