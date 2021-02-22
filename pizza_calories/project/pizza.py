from project.dough import Dough
from project.toppings import Toppings


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.__name = name
        self.__dough: Dough = dough
        self.__topping_capacity: int = toppings_capacity
        self.__toppings = {}

    @property
    def name(self):
        return self.__name

    @property
    def dough(self):
        return self.__dough

    @property
    def toppings_capacity(self):
        return self.__topping_capacity

    @property
    def toppings(self):
        return self.__toppings
    
    @toppings.setter
    def toppings(self, key, value):
        self.__toppings[key] += value
        
        
    def add_topping(self, topping: Toppings):
        pass
    
    def calculate_total_weight(self):
        pass