class Toppings:
    def __init__(self, topping_type, weight: str):
        self.__topping_type = topping_type
        self.__weight = weight

    @property
    def topping_type(self):
        return self.__topping_type

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self):
        self.__weight *= 2

    