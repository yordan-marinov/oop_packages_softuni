class Gym:
    def __init__(self):
        self.customers: list = []  # List of objets
        self.trainers: list = []  # List of objets
        self.equipment: list = []  # List of objets
        self.plans: list = []  # List of objets
        self.subscriptions: list = []  # List of objets

    def add_customer(self, customer):  # customer: Customer(obj)
        return Gym.adding_obj_to_list(self.customers, customer)

    def add_trainer(self, trainer):  # trainer: Trainer(obj)
        return Gym.adding_obj_to_list(self.trainers, trainer)

    def add_equipment(self, equipment):  # equipment: Equipment(obj)
        return Gym.adding_obj_to_list(self.equipment, equipment)

    def add_plan(self, plan):  # plan: Plan(obj)
        return Gym.adding_obj_to_list(self.plans, plan)

    def add_subscription(self, subscription):  # subscription: Subscription(obj)
        return Gym.adding_obj_to_list(self.subscriptions, subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.get_subscription_form_id_number(subscription_id)
        # equipment = [e for e in self.equipment if e.id == subscription.exercise_id][0]

        result = subscription.__repr__ + "\n"
        result += Gym.get_obj_from_id_number(self.customers, subscription.customer_id).__repr__ + "\n"
        result += Gym.get_obj_from_id_number(self.trainers, subscription.trainer_id).__repr__ + "\n"
        result += Gym.get_obj_from_id_number(self.equipment, subscription.exercise_id).__repr__ + "\n"
        result += Gym.get_obj_from_id_number(self.plans, subscription.exercise_id).__repr__ + "\n"

        return result

    @staticmethod
    def adding_obj_to_list(lst: list, obj: object):
        if obj not in lst:
            return lst.append(obj)

    def get_subscription_form_id_number(self, subscription_id: int):
        return [s for s in self.subscriptions if s.id == subscription_id][0]

    @staticmethod
    def get_obj_from_id_number(list_obj: list, number: int):
        return [obj for obj in list_obj if obj.id == number][0]
