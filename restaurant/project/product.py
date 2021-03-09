class Product:
    def __init__(self, name: str, price: float):
        self.name: str = name
        self.price: float = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @name.setter
    def name(self, name):
        self.__name = name

    @price.setter
    def price(self, name):
        self.__price = name