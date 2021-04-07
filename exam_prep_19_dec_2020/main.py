from project.supply.supply import Supply
from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply
from project.medicine.medicine import Medicine
from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.survivor import Survivor
from project.bunker import Bunker


fs = FoodSupply()
# print(fs.__dict__)
ws = WaterSupply()
# print(ws.__class__.__name__)
pk = Painkiller()
# print(pk.__dict__)
s = Salve()
# print(s.__dict__)
sur = Survivor("abc", 10)
sur.health -= 2
# print(sur.__dict__)
print(sur.health)
print(sur.needs_healing)
b = Bunker()
b.supplies.append(FoodSupply())
b.supplies.append(FoodSupply())
b.supplies.append(WaterSupply())
# print(b.food)
b.add_survivor(sur)
# b.add_survivor(sur)
# print(b.survivors)
b.add_medicine(pk)
print(b.medicine)
print(b.heal(sur, "painkillers"))
print(b.medicine)
print(sur.health)
