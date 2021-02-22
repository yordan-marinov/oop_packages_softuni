from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(
        self, name: str, budget: int, animal_capacity: int, workers_capacity: int
    ):
        self.name: str = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    @property
    def budget(self):
        return self.__budget
    
    @budget.setter
    def budget(self, amount):
        self.__budget += amount

    
    def add_animal(self, animal, price):
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if price > self.__budget:
            return "Not enough budget"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        worker = [w for w in self.workers if w.name == worker_name]
        if not worker:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(worker[0])
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salaries = sum(w.salary for w in self.workers)
        if self.__budget < salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        tends = sum(a.get_needs() for a in self.animals)
        if self.__budget < tends:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= tends
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"

        lions = [l for l in self.animals if isinstance(l, Lion)]
        result += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result += f"{lion}\n"

        tigers = [t for t in self.animals if isinstance(t, Tiger)]
        result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += f"{tiger}\n"

        cheetahs = [c for c in self.animals if isinstance(c, Cheetah)]
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            result += f"{cheetah}\n"

        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = [k for k in self.workers if isinstance(k, Keeper)]
        result += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            result += f"{keeper}\n"

        caretakers = [c for c in self.workers if isinstance(c, Caretaker)]
        result += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            result += f"{caretaker}\n"

        vets = [v for v in self.workers if isinstance(v, Vet)]
        result += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            result += f"{vet}\n"

        return result.strip()