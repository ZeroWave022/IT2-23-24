from pokemon import Pokemon

class Trainer:
    def __init__(self, name: str, pokemons: list[Pokemon]) -> None:
        self.name = name
        self.pokemons = pokemons

    def __str__(self) -> str:
        return f"{self.name} - Pokemons: {len(self.pokemons)}"

    def add(self, pokemon: Pokemon) -> None:
        self.pokemons.append(pokemon)

    def remove(self, pokemon) -> None:
        self.pokemons.remove(pokemon)
