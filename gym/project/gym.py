from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def add_obj_to_list(obj: object, lst: list) -> list:
        if obj not in lst: 
            lst.append(obj)
    
    def add_customer(self, customer: Customer):
        Gym.add_obj_to_list(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        Gym.add_obj_to_list(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        Gym.add_obj_to_list(equipment, self.equipment)
        
    def add_plan(self, plan: ExercisePlan):
        Gym.add_obj_to_list(plan, self.plans)
        
    def add_subscription(self, subscription: Subscription):
        Gym.add_obj_to_list(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int):
        subscription = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer = [c for c in self.customers if c.id == subscription.customer_id][0]
        trainer = [t for t in self.trainers if t.id == subscription.trainer_id][0]
        plan = [p for p in self.plans if p.id == subscription.exercise_id][0]
        equipment = [e for e in self.equipment if e.id == plan.equipment_id][0]
        
        return "\n".join(str(o) for o in [subscription, customer, trainer, equipment, plan])
    