from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Seed, Fruit


class Mouse(Mammal):
    _WEIGHT_INCREACE_INDEX = 0.10
    _TYPE_OF_FOOD = (Vegetable, Fruit)

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    _WEIGHT_INCREACE_INDEX = 0.40
    _TYPE_OF_FOOD = (Meat,)

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    _WEIGHT_INCREACE_INDEX = 0.30
    _TYPE_OF_FOOD = (Vegetable, Meat)

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    _WEIGHT_INCREACE_INDEX = 1.00
    _TYPE_OF_FOOD = (Meat,)

    def make_sound(self):
        return "ROAR!!!"