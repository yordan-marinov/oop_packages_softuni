from abc import ABC, abstractclassmethod
from project.food import Vegetable, Fruit, Seed, Meat, Food


class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name: str = name
        self.weight: float = weight
        self.food_eaten: int = 0

    @abstractclassmethod
    def make_sound(self):
        pass

    @abstractclassmethod
    def feed(self, food):
        pass

    @staticmethod
    def feeder(self_animal, food):
        if not isinstance(food, self_animal.food_to_eat):
            return f"{type(self_animal).__name__} does not eat {type(food).__name__}!"
        self_animal.food_eaten += food.quantity
        self_animal.weight += self_animal.weight_index * food.quantity


class Bird(Animal):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
