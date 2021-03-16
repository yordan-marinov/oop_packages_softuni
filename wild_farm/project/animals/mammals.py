from project.animals.animal import Mammal, Animal
from project.food import Meat, Vegetable, Seed, Fruit




class Mouse(Mammal):
    weight_index = 0.10
    food_to_eat = (Vegetable, Fruit)
    
    def make_sound(self):
        return "Squeak"
    
    def feed(self, food):
        return Animal.feeder(self, food)
        
        
class Dog(Mammal):
    weight_index = 0.40
    food_to_eat = (Meat, )
    
    def make_sound(self):
        return "Woof!"
    
    def feed(self, food):
        return Animal.feeder(self, food)


class Cat(Mammal):
    weight_index = 0.30
    food_to_eat = (Meat, Vegetable)
    
    def make_sound(self):
        return "Meow"
    
    def feed(self, food):
        return Animal.feeder(self, food)


class Tiger(Mammal):
    weight_index = 1.00
    food_to_eat = (Meat, )
    
    def make_sound(self):
        return "ROAR!!!"
    
    def feed(self, food):
        return Animal.feeder(self, food)
