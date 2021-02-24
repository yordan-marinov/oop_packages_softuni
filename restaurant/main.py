from project.product import Product
from project.beverage.beverage import Beverage
from project.beverage.coffee import Coffee
from project.beverage.cold_beverage import ColdBeverage
from project.beverage.hot_beverage import HotBeverage
from project.beverage.tea import Tea
from project.food.cake import Cake
from project.food.dessert import Dessert
from project.food.food import Food
from project.food.main_dish import MainDish
from project.food.salmon import Salmon
from project.food.soup import Soup
from project.food.starter import Starter


if __name__ == "__main__":
    product = Product("coffee", 2.5)
    print(product.__class__.__name__)
    print(product.name)
    print(product.price)
    beverage = Beverage("coffee", 2.5, 50)
    print(beverage.__class__.__name__)
    print(beverage.__class__.__bases__[0].__name__)
    print(beverage.name)
    print(beverage.price)
    print(beverage.milliliters)
    soup = Soup("fish soup", 9.90, 230)
    print(soup.__class__.__name__)
    print(soup.__class__.__bases__[0].__name__)
    print(soup.name)
    print(soup.price)
    print(soup.grams)
    coffee = Coffee("cof", 1, 10, 100)
    print(coffee.__class__.__name__)
    print(coffee.__class__.__bases__[0].__name__)
    print(coffee.name)
    print(coffee.price)
    print(coffee.milliliters)
    print(coffee.caffeine)
    cake = Cake("keks", 1, 9, 99)
    print(cake.__class__.__name__)
    print(cake.__class__.__bases__[0].__name__)
    print(cake.name)
    print(cake.price)
    print(cake.grams)
    print(cake.calories)
    f = Food("food", 1, 10)
    print(f.__class__.__name__)
    print(f.__class__.__bases__[0].__name__)
    print(f.name)
    print(f.price)
    print(f.grams)
    s = Salmon("salmon", 1.1, 10.0)
    print(s.__class__.__name__)
    print(s.__class__.__bases__[0].__name__)
    print(s.name)
    print(s.price)
    print(s.grams)
    
