class Subscription:
    _autoincrement_id = 0

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date: str = date
        self.customer_id: int = customer_id
        self.trainer_id: int = trainer_id
        self.exercise_id: int = exercise_id
        Subscription._autoincrement_id += 1
        self.id = Subscription._autoincrement_id

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"

    @staticmethod
    def get_next_id():
        return Subscription._autoincrement_id + 1
