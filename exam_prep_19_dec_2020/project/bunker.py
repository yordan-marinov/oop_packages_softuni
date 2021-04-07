from project.supply.supply import Supply
from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply
from project.medicine.medicine import Medicine
from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors: [Survivor] = []
        self.supplies: [Supply] = []
        self.medicine: [Medicine] = []

    @property
    def food(self):
        all_food = [f for f in self.supplies if isinstance(f, FoodSupply)]
        if not all_food:
            raise IndexError("There are no food supplies left!")
        return all_food
    
    @property
    def water(self):
        all_water = [w for w in self.supplies if isinstance(w, WaterSupply)]
        if not all_water:
            raise IndexError("There are no water supplies left!")
        return all_water
    
    @property
    def painkillers(self):
        all_painkillers = [pk for pk in self.medicine if isinstance(pk, Painkiller)]
        if not all_painkillers:
            raise IndexError("There are no painkillers left!")
        return all_painkillers
    
    @property
    def salves(self):
        all_salves = [s for s in self.medicine if isinstance(s, Salve)]
        if not all_salves:
            raise IndexError("There are no salves left!")
        return all_salves
    
    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)
    
    def add_supply(self, supply: Supply):
        self.supplies.append(supply)
    
    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)
    
    def heal(self, survivor: Survivor, medicine_type: str):
        if not survivor.needs_healing:
            return
        s = self.get_type(medicine_type)
        self.remove_last_obj(s, self.medicine)
        s.apply(survivor)
        return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if not survivor.needs_sustenance:
            return
        s = self.get_type(sustenance_type)
        self.remove_last_obj(s, self.supplies)
        s.apply(survivor)
        return f"{survivor.name} sustained successfully with {sustenance_type}"

    def get_type(self, s_type):
        if s_type == "WaterSupply":
            t = self.water
        elif s_type == "FoodSupply":
            t = self.food
        elif s_type == "Salve":
            t = self.salves()
        else:
            t = self.painkillers
        return t.pop()
    
    def remove_last_obj(self, obj, lst):
        for i in range(len(lst)-1, -1, -1):
            if type(lst[i]).__name__ == type(obj).__name__:
                lst.pop(i)
                return
    
    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age * 2
            self.sustain(s, "FoodSupply")
            self.sustain(s, "WaterSupply")