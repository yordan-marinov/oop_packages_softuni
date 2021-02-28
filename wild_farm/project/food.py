from abc import ABC


class Food(ABC):
    def __init__(self, quantity: float):
        self.quantity = quantity


class Vegetable(Food):
    pass


class Fruit(Food):
    pass


class Meat(Food):
    pass


class Seed(Food):
    pass
