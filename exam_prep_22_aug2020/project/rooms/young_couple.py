from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop


class YoungCouple(Room):
    room_cost = 20
    # appliances = [TV(), Fridge(), Laptop()] * 2
    
    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        budget = salary_one + salary_two
        members_count = 2
        super().__init__(family_name, budget, members_count)
        self.appliances = [TV(), Fridge(), Laptop()] * 2
        self.calculate_expenses(self.appliances)