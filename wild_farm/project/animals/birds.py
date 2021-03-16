from project.animals.animal import Bird, Animal
from project.food import Meat, Vegetable, Seed, Fruit


class Owl(Bird):
    weight_index = 0.25
    food_to_eat = (Meat, )

    def make_sound(self):
        return "Hoot Hoot"
    
    def feed(self, food):
        return Animal.feeder(self, food)

class Hen(Bird):
    weight_index = 0.35
    food_to_eat = (Meat, Vegetable, Fruit, Seed)
    
    def make_sound(self):
        return "Cluck"
    
    def feed(self, food):
        return Animal.feeder(self, food)
