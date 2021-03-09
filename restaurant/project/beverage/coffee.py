from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50.0
    PRICE = 3.50

    def __init__(self, name: str, caffeine: float):
        super().__init__(name, price=self.PRICE, milliliters=self.MILLILITERS)
        self.caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
    
    @caffeine.setter
    def caffeine(self, caffeine):
        self.__caffeine = caffeine