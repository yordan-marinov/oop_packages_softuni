from project.food.dessert import Dessert


class Cake(Dessert):
    __GRAMS = 250
    __CALORIES = 1000
    __PRICE = 5

    def __init__(self, name: str, price: float, grams: float, calories: float):
        Dessert.__init__(self, name, self.__PRICE, self.__GRAMS, Cake.__CALORIES)
