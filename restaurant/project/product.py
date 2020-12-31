class Product:
    def __init__(self, name: str, price: float):
        self._name: str = name
        self._price: float = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price
