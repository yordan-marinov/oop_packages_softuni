from project.product import Product


class Food(Product):
    def __init__(self, name: str, price: float, grams: float):
        super().__init__(name, price)
        self.grams: float = grams

    @property
    def grams(self):
        return self.__grams

    @grams.setter
    def grams(self, grams):
        self.__grams = grams