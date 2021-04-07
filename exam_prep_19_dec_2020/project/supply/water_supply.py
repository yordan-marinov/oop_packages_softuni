from project.supply.supply import Supply


class WaterSupply(Supply):
    need_increase = 40
    
    def __init__(self):
        super().__init__(self.need_increase)