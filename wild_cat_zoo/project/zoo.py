from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.__budget: int = budget
        self.__animal_capacity: int = animal_capacity
        self.__workers_capacity: int = workers_capacity
        self.name: str = name
        self.animals: list = []
        self.workers: list = []
    
    @staticmethod   
    def is_enough_space(lst, capacity):
        return len(lst) < capacity
    
    @staticmethod
    def is_enough_budget(budget, amount):
        return amount <= budget
    
    @staticmethod
    def find_obj_by_name(lst_objs, name):
        searched_obj = [obj for obj in lst_objs if obj.name == name]
        if searched_obj: 
            return searched_obj[0]
            
    def sum_all_salaries_of_workers(self):
        return sum(w.salary for w in self.workers)

    def add_animal(self, animal: (Lion, Cheetah, Tiger), price):
        if not self.is_enough_space(self.animals, self.__animal_capacity):
            return "Not enough space for animal"
        
        if not self.is_enough_budget(self.__budget, price):
            return "Not enough budget"
        
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {type(animal).__name__} added to the zoo"
    
    def hire_worker(self, worker: (Keeper, Caretaker, Vet)):
        if not self.is_enough_space(self.workers, self.__workers_capacity):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {type(worker).__name__} hired successfully"
    
    def fire_worker(self, worker_name):
        worker_obj = self.find_obj_by_name(self.workers, worker_name)
        if not worker_obj:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(worker_obj)
        return f"{worker_name} fired successfully"
    
    def pay_workers(self):
        all_workers_salaries = self.sum_all_salaries_of_workers()
        if not self.is_enough_budget(self.__budget, all_workers_salaries):
            return "You have no budget to pay your workers. They are unhappy"
            
        self.__budget -= all_workers_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        all_animals_expence = sum(a.get_needs() for a in self.animals)
        if not self.is_enough_budget(self.__budget, all_animals_expence):
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= all_animals_expence
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