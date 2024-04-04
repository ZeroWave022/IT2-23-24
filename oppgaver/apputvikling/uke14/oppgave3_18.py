# fmt: off
formula1_drivers = [
    {"navn": "Max Verstappen", "nasjonalitet": "nederlandsk", "team": "Red Bull Racing", "bilnummer": 1},
    {"navn": "Sergio Perez", "nasjonalitet": "meksikansk", "team": "Red Bull Racing", "bilnummer": 11},
    {"navn": "Lewis Hamilton", "nasjonalitet": "britisk", "team": "Mercedes", "bilnummer": 44},
    {"navn": "George Russell", "nasjonalitet": "britisk", "team": "Mercedes", "bilnummer": 63},
    {"navn": "Charles Leclerc", "nasjonalitet": "monegaskisk", "team": "Ferrari", "bilnummer": 16},
    {"navn": "Kevin Magnussen", "nasjonalitet": "dansk", "team": "Haas F1 Team", "bilnummer": 20},
    {"navn": "Nico Hulkenberg", "nasjonalitet": "tysk", "team": "Haas F1 Team", "bilnummer": 27}
]
# fmt: on

nationalities = {}

for driver in formula1_drivers:
    nationality = driver["nasjonalitet"]
    if driver["nasjonalitet"] not in nationalities:
        nationalities[nationality] = 1
    else:
        nationalities[nationality] += 1

print(nationalities["britisk"])
print(nationalities["tysk"])
