from project.animals.animal import Bird
from project.food import Meat, Vegetable, Seed, Fruit


class Owl(Bird):
    _WEIGHT_INCREACE_INDEX = 0.25
    _TYPE_OF_FOOD = (Meat,)
    
    def make_sound(self):
        return "Hoot Hoot"
    


class Hen(Bird):
    _WEIGHT_INCREACE_INDEX = 0.35
    _TYPE_OF_FOOD = (Meat, Fruit, Seed, Vegetable)
    
    def make_sound(self):
        return "Cluck"



    
    