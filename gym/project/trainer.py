class Trainer:
    auto_trainer_id_number_creator = 1

    def __init__(self, name: str):
        self.name: str = name
        self.id: int = Trainer.auto_trainer_id_number_creator
        Trainer.auto_trainer_id_number_creator += 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def git_next_id():
        return Trainer.auto_trainer_id_number_creator


# trainer = Trainer("Peter")
# print(trainer)
# trainer2 = Trainer("Jordan")
# print(trainer2)
# print(Trainer.git_next_id())
# print(trainer2.__dict__)