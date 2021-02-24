from project.food.main_dish import MainDish


class Salmon(MainDish):
    __GRAMS = 22

    def __init__(self, name: str, price: float, grams=None):
        MainDish.__init__(self, name, price, Salmon.__GRAMS)

