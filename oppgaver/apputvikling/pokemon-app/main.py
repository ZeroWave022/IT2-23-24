import os
import json
from pokemon import Pokemon

def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

with open("./pokemon.json", encoding="utf-8") as f:
    raw_data = json.load(f)

pokemons = []

for pokemon in raw_data:
    pokemons.append(Pokemon(pokemon))

while True:
    print("--- Pokemon ---")
    print("1. Se pokemonoversikt")
    print("2. Se treneroversikt")
    print("3. Lag trener")
    print("4. Avslutt")

    user_input = input("> ")
    clear_terminal()

    if user_input == "1":
        print("\n".join([pokemon.names["english"] for pokemon in pokemons]))
    elif user_input == "2":
        pass
    elif user_input == "3":
        pass
    elif user_input == "4":
        print("Avslutter...")
        break
    else:
        print("Det er ikke et riktig valg!")

    input("Trykk Enter for å fortsatte...")
    clear_terminal()
