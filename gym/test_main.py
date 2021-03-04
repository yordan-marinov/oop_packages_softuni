from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


if __name__ == "__main__":
    # customer = Customer("Jordan", "Gabrovo", "jordan@gmail.com")
    # customer2 = Customer("Martin", "Gabrovo", "martin@gmail.com")
    # print(str(customer))
    # print(str(customer2))
    # equipment = Equipment("gladiator")
    # equipment2 = Equipment("kettlebell")
    # print(equipment)
    # print(equipment2)
    # e_plan = ExercisePlan(1, equipment.id, 10)
    # e_plan2 = ExercisePlan.from_hours(2, equipment2.id, 1)
    # print(e_plan)
    # print(e_plan2)
    # subscrip = Subscription("today", customer.id, 1, e_plan.id)
    # subscrip2 = Subscription("tomorow", customer2.id, 2, e_plan2.id)
    # print(subscrip)
    # print(subscrip2)
    # trainer = Trainer("John")
    # trainer2 = Trainer("Kalina")
    # print(trainer)
    # print(trainer2)
    from project.customer import Customer
    from project.equipment import Equipment
    from project.exercise_plan import ExercisePlan
    from project.gym import Gym
    from project.subscription import Subscription
    from project.trainer import Trainer

    customer = Customer("John", "Maple Street", "john.smith@gmail.com")
    equipment = Equipment("Treadmill")
    trainer = Trainer("Peter")
    subscription = Subscription("14.05.2020", 1, 1, 1)
    plan = ExercisePlan(1, 1, 20)

    gym = Gym()

    gym.add_customer(customer)
    gym.add_equipment(equipment)
    gym.add_trainer(trainer)
    gym.add_plan(plan)
    gym.add_subscription(subscription)

    print(Customer.get_next_id())

    print(gym.subscription_info(1))