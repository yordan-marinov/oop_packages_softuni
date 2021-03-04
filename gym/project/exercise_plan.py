class ExercisePlan:
    _autoincerment_id = 0

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id: int = trainer_id
        self.equipment_id: int = equipment_id
        self.duration: int = duration
        ExercisePlan._autoincerment_id += 1
        self.id = ExercisePlan._autoincerment_id

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"

    @staticmethod
    def get_next_id():
        return ExercisePlan._autoincerment_id + 1

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        minutes = hours * 60
        return cls(trainer_id, equipment_id, minutes)
