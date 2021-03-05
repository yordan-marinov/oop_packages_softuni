class Topping:
    def __init__(self, topping_type, weight: str):
        self.__topping_type = topping_type
        self.__weight = weight

    def __repr__(self):
        return f"{self.topping_type}: {self.weight}"

    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, new_type):
        self.__topping_type = new_type

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, w):
        self.__weight = w * 2
