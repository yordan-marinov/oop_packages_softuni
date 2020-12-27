class Subscription:
    auto_subscription_id_number_creator = 1

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date: str = date
        self.customer_id: int = customer_id
        self.trainer_id: int = trainer_id
        self.exercise_id: int = exercise_id
        self.id = Subscription.auto_subscription_id_number_creator
        Subscription.auto_subscription_id_number_creator += 1

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"

    @staticmethod
    def get_next_id():
        return Subscription.auto_subscription_id_number_creator


# subscription = Subscription("14.05.2020", 1, 1, 1)
# print(subscription)
# subscription2 = Subscription("14.06.2020", 15, 441, 41)
# print(subscription2)
# print(Subscription.get_next_id())
# print(subscription.__dict__)