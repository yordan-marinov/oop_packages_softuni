from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.__name = name
        self.__dough: Dough = dough
        self.__toppings_capacity: int = toppings_capacity
        self.__toppings = {}
        
    def __repr__(self):
        return f"Name: {self.name}, Dough: {self.dough}, Topping capacity: {self.toppings_capacity}, Toppins: {[str(t) for t in self.toppings.items()]}"

    @property
    def name(self):
        return self.__name

    @property
    def dough(self):
        return self.__dough

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @property
    def toppings(self):
        return self.__toppings
    
    @toppings.setter
    def toppings(self, key, value):
        self.__toppings[key] += value
        
        
    def add_topping(self, topping: Topping):
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight 
            
        if len(self.__toppings) >= self.__toppings_capacity:
            raise ValueError("Not enough space for another topping")
        
        if topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = topping.weight
   
        return self.toppings
    
    def calculate_total_weight(self):
        doung_weight = self.dough.weight
        toppings_weight = sum([t for t in self.toppings.values()])

        return doung_weight + toppings_weight