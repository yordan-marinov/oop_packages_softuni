class Appliance:
    def __init__(self, cost: float):
        self.cost: float = cost

    def get_monthly_expense(self):
        return self.cost * 30
