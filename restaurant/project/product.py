class Product:
    def __init__(self, name: str, price: float):
        self.__name: str = name
        self.__price: float = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price
