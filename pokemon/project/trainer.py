# from typing import List
# from pokemon.project.pokemon import Pokemon


class Trainer:
    # name: str
    # pokemon: List[Pokemon]

    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon.name in [p.name for p in self.pokemon]:
            return f"This pokemon is already caught"

        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        trainer_pokemon = [p for p in self.pokemon if pokemon_name == p.name]
        if not trainer_pokemon:
            return "Pokemon is not caught"

        self.pokemon.remove(trainer_pokemon[0])
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n"
        for p in self.pokemon:
            result += f"- {p.pokemon_details()}"

        return result
