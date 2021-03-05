class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: str):
        self.__flour_type = flour_type
        self.__baking_technique = baking_technique
        self.__weight = weight
        
    def __repr__(self):
        return f"{self.flour_type}, {self.baking_technique}, {self.weight}"

    @property
    def flour_type(self):
        return self.__flour_type

    @property
    def baking_technique(self):
        return self.baking_technique

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, amount):
        self.__weight = amount * 2
