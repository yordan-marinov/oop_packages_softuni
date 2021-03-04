class Trainer:
    _autoincrement_id = 0

    def __init__(self, name: str):
        self.name: str = name
        Trainer._autoincrement_id += 1
        self.id = Trainer._autoincrement_id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer._autoincrement_id + 1
