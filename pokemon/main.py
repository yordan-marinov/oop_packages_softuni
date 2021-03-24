from project.pokemon import Pokemon
from project.trainer import Trainer


def test_pokemon_init():
    p = Pokemon("Jordan", 10)
    print(p.name)
    print(p.health)
    print(p.pokemon_details())

def test_trainer_init():
    t = Trainer("Martin")
    print(t.name)
    print(t.pokemon)

def test_trainer_add_pokemon():
    t = Trainer("Martin")
    p = Pokemon("Jordan", 10)
    print(t.add_pokemon(p))
    print(t.pokemon)

def test_trainer_add_pokemon_already_in():
    t = Trainer("Martin")
    p = Pokemon("Jordan", 10)
    t.add_pokemon(p)
    print(t.add_pokemon(p))
    print(t.pokemon)
    
def test_trainer_release_pokemon_already_in():
    t = Trainer("Martin")
    p = Pokemon("Jordan", 10)
    t.add_pokemon(p)
    print(t.release_pokemon("Jordan"))

def test_trainer_release_pokemon_not_in():
    t = Trainer("Martin")
    print(t.release_pokemon("Jordan"))


if __name__ == "__main__":
    # test_pokemon_init()
    # test_trainer_init()
    # test_trainer_add_pokemon()
    # test_trainer_add_pokemon_already_in()
    # test_trainer_release_pokemon_already_in()
    # test_trainer_release_pokemon_not_in()
    pokemon = Pokemon("Pikachu", 90)
    print(pokemon.pokemon_details())
    trainer = Trainer("Ash")
    print(trainer.add_pokemon(pokemon))
    second_pokemon = Pokemon("Charizard", 110)
    print(trainer.add_pokemon(second_pokemon))
    print(trainer.release_pokemon("Pikachu"))
    print(trainer.trainer_data())