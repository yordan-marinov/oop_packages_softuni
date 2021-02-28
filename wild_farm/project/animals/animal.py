from abc import ABC, abstractclassmethod


class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name: str = name
        self.weight: float = weight
        self.food_eaten = 0

    @property
    @abstractclassmethod
    def _TYPE_OF_FOOD(self):
        pass

    @property
    @abstractclassmethod
    def _WEIGHT_INCREACE_INDEX(self):
        pass

    @abstractclassmethod
    def make_sound(self):
        pass

    def feed(self, food):
        if not isinstance(food, self._TYPE_OF_FOOD):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.weight += food.quantity * self._WEIGHT_INCREACE_INDEX
        self.food_eaten += food.quantity


class Bird(Animal):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size: float = wing_size

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region: float = living_region

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.living_region}, {self.weight}, {self.food_eaten}]"
