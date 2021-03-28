from unittest import TestCase, main

from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.zoo import Zoo


class WildCatZooTests(TestCase):
    def setUp(self):
        self.l = Lion("Simba", "Female", 5)
        self.t = Tiger("Tigi", "Male", 1)
        self.c = Cheetah("Chichi", "Female", 2)
        self.k = Keeper("Keepy", 40, 1000)
        self.ctr = Caretaker("Cary", 20, 100)
        self.vet = Vet("Vety", 50, 1100)
        self.zoo = Zoo("Zooland", 100, 3, 3)

    def test_lion_correct_init(self):
        self.assertEqual("Simba", self.l.name)
        self.assertEqual("Female", self.l.gender)
        self.assertEqual(5, self.l.age)

    def test_get_needs_lion_should_return_50(self):
        self.assertEqual(50, self.l.get_needs())

    def test_lion_repr_correct_output(self):
        self.assertEqual("Name: Simba, Age: 5, Gender: Female", str(self.l))

    def test_tiger_correct_init(self):
        self.assertEqual("Tigi", self.t.name)
        self.assertEqual("Male", self.t.gender)
        self.assertEqual(1, self.t.age)

    def test_get_needs_tiger_should_return_50(self):
        self.assertEqual(45, self.t.get_needs())

    def test_tiger_repr_correct_output(self):
        self.assertEqual("Name: Tigi, Age: 1, Gender: Male", str(self.t))

    def test_cheetah_correct_init(self):
        self.assertEqual("Chichi", self.c.name)
        self.assertEqual("Female", self.c.gender)
        self.assertEqual(2, self.c.age)

    def test_get_needs_cheetah_should_return_50(self):
        self.assertEqual(60, self.c.get_needs())

    def test_cheetah_repr_correct_output(self):
        self.assertEqual("Name: Chichi, Age: 2, Gender: Female", str(self.c))

    def test_keeper_correct_init(self):
        self.assertEqual("Keepy", self.k.name)
        self.assertEqual(1000, self.k.salary)
        self.assertEqual(40, self.k.age)

    def test_keeper_repr_correct_output(self):
        self.assertEqual(f"Name: Keepy, Age: 40, Salary: 1000", str(self.k))

    def test_ctr_correct_init(self):
        self.assertEqual("Cary", self.ctr.name)
        self.assertEqual(100, self.ctr.salary)
        self.assertEqual(20, self.ctr.age)

    def test_ctr_repr_correct_output(self):
        self.assertEqual(f"Name: Cary, Age: 20, Salary: 100", str(self.ctr))

    def test_vet_correct_init(self):
        self.assertEqual("Vety", self.vet.name)
        self.assertEqual(1100, self.vet.salary)
        self.assertEqual(50, self.vet.age)

    def test_vet_repr_correct_output(self):
        self.assertEqual(f"Name: Vety, Age: 50, Salary: 1100", str(self.vet))

    def test_zoo_correct_init(self):
        self.assertEqual("Zooland", self.zoo.name)
        self.assertEqual(100, self.zoo._Zoo__budget)
        self.assertEqual(3, self.zoo._Zoo__animal_capacity)
        self.assertEqual(3, self.zoo._Zoo__workers_capacity)
        self.assertEqual([], self.zoo.animals)
        self.assertEqual([], self.zoo.workers)

    def test_zoo_add_animal_when_not_enough_space_should_retur_str(self):
        self.zoo._Zoo__animal_capacity = 0
        self.assertEqual("Not enough space for animal", self.zoo.add_animal(self.l, 10))

    def test_zoo_add_animal_when_not_enough_budget_should_retur_str(self):
        self.zoo._Zoo__budget = 9
        self.assertEqual("Not enough budget", self.zoo.add_animal(self.l, 10))

    def test_zoo_add_animal_when_space_and_enough_budget_should_append_animal_and_reduce_budget_retur_str(
        self,
    ):
        self.assertEqual(
            "Simba the Lion added to the zoo", self.zoo.add_animal(self.l, 10)
        )
        self.assertEqual(90, self.zoo._Zoo__budget)

    def test_zoo_hire_worker_when_not_enough_space_should_retur_str(self):
        self.zoo._Zoo__workers_capacity = 0
        self.assertEqual(0, self.zoo._Zoo__workers_capacity)
        self.assertEqual("Not enough space for worker", self.zoo.hire_worker(self.k))

    def test_zoo_hire_worker_when_enough_space_should_append_worker_to_workers_and_retur_str(
        self,
    ):
        self.assertEqual(
            "Keepy the Keeper hired successfully", self.zoo.hire_worker(self.k)
        )

    def test_fire_worker_when_not_in_workers_list_return_str(self):
        self.assertEqual("There is no Vety in the zoo", self.zoo.fire_worker("Vety"))

    def test_fire_worker_when_in_workers_list_should_remove_it_return_str(self):
        self.zoo.hire_worker(self.vet)
        self.assertEqual("Vety fired successfully", self.zoo.fire_worker("Vety"))

    def test_pay_worker_if_not_enough_budget_for_salaries_should_return_str(self):
        self.zoo.hire_worker(self.vet)
        self.assertEqual(
            "You have no budget to pay your workers. They are unhappy",
            self.zoo.pay_worker(),
        )

    def test_pay_worker_if_enough_budget_for_salaries_should_budget_and_return_str(
        self,
    ):
        self.zoo._Zoo__budget = 1200
        self.zoo.hire_worker(self.vet)
        self.zoo.hire_worker(self.ctr)
        self.assertEqual(
            "You payed your workers. They are happy. Budget left: 0",
            self.zoo.pay_worker(),
        )


if __name__ == "__main__":
    main()
