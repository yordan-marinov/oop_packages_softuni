from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name: str = name
        self.pokemon: [Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemon:
            return f"This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"
    
    def get_pokemon_by_name(self, name):
        obj = [p for p in self.pokemon if name == p.name]
        if obj:
            return obj[0]
    
    def release_pokemon(self, pokemon_name: str):
        if not self.get_pokemon_by_name(pokemon_name):
            return f"Pokemon is not caught"
        self.pokemon.remove(self.get_pokemon_by_name(pokemon_name))
        return f"You have released {pokemon_name}"
    
    def trainer_data(self):
        s = ""
        s += f"Pokemon Trainer {self.name}\n"
        s += f"Pokemon count {len(self.pokemon)}\n"
        for pokemon in self.pokemon:
            s += f"- {pokemon.pokemon_details()}\n"
        return s.strip()