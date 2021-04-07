from project.supply.supply import Supply


class FoodSupply(Supply):
    need_increase = 20
    
    def __init__(self):
        super().__init__(self.need_increase)
