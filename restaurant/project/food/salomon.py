# from restaurant.project.food.main_dish import MainDish
from project.food.main_dish import MainDish


class Salomon(MainDish):
    SALOMON_GRAMS = 22

    def __init__(self, name, price, grams):
        MainDish.__init__(self, name, price, self.SALOMON_GRAMS)
