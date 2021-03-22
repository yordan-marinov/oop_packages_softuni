from project.rooms.room import Room
from project.appliances.tv import TV


class AloneYoung(Room):
    # room_cost = 10
    # appliances = [TV()]
    
    def __init__(self, family_name: str, pension: float):
        super().__init__(name=family_name, budget=pension, members_count=1)
        self.appliances = [TV()]
        self.room_cost = 10
        self.calculate_expenses(self.appliances)
