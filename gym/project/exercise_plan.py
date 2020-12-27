class ExercisePlan:
    auto_exercise_plan_id_number_creator = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id: int = trainer_id
        self.equipment_id: int = equipment_id
        self.duration: int = duration  # Duration is in minutes
        self.id = ExercisePlan.auto_exercise_plan_id_number_creator
        ExercisePlan.auto_exercise_plan_id_number_creator += 1

    @staticmethod
    def convert_hours_in_minutes(hours: int):
        return hours * 60     # 60 are minutes in one hour.

    @classmethod
    def form_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(
            trainer_id,
            equipment_id,
            ExercisePlan.convert_hours_in_minutes(hours)
        )

    @staticmethod
    def get_next_id():
        return ExercisePlan.auto_exercise_plan_id_number_creator

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"


# plan = ExercisePlan(1, 1, 20)
# print(plan)
# plan2 = ExercisePlan(11, 10, 120)
# print(plan2)
# print(ExercisePlan.get_next_id())
# plan3 = ExercisePlan.form_hours(2, 3, 3)
# print(plan3.__dict__)
