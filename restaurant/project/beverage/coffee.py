from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    __MILLILITERS = 50.0
    __PRICE = 3.50

    def __init__(self, name: str, price: float, milliliters: float, caffeine: float):
        HotBeverage.__init__(self, name, Coffee.__PRICE, self.__MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
 