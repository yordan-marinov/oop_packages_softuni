class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: str):
        self.__flour_type = flour_type
        self.__baking_techique = baking_technique
        self.__weight = weight

    @property
    def flour_type(self):
        return self.__flour_type

    @property
    def baking_technique(self):
        return self.__baking_techique

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self):
        self.__weight *= 2
