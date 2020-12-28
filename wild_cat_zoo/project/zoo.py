class Zoo:
    def __init__(
            self, name: str,
            budget: int,
            animal_capacity: int,
            workers_capacity: int
    ):
        self.name: str = name
        self.__budget: int = budget
        self.__animal_capacity: int = animal_capacity
        self.__workers_capacity: int = workers_capacity
        self.animals: list = []
        self.workers: list = []

    def add_animal(self, animal: object, price: int) -> str:
        if self.__budget < price:
            return "Not enough budget"

        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: object) -> str:
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    @staticmethod
    def get_object_by_name_from_list(lst_obj: list, name: str):
        return [obj for obj in lst_obj if obj.name == name][0]

    def fire_worker(self, worker_name) -> str:
        worker_object_in_list = Zoo.get_object_by_name_from_list(self.workers, worker_name)

        if not worker_object_in_list:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker_object_in_list)
        return f"{worker_name} fired successfully"

    def all_workers_salaries(self) -> int:
        return sum(worker.salary for worker in self.workers)

    def pay_workers(self) -> str:
        if self.__budget < self.all_workers_salaries():
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= self.all_workers_salaries()
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def all_animal_tends(self) -> int:
        return sum(animal.get_needs() for animal in self.animals)

    def tend_animals(self) -> str:
        if self.__budget < self.all_animal_tends():
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= self.all_animal_tends()
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def lions(self) -> list:
        result = [
            animal.__repr__()
            for animal in self.animals
            if animal.__class__.__name__ == "Lion"
        ]
        if not result:
            return []

        return result

    def tigers(self) -> list:
        result = [
            animal.__repr__()
            for animal in self.animals
            if animal.__class__.__name__ == "Tiger"
        ]
        if not result:
            return []

        return result

    def cheetahs(self) -> list:
        result = [
            animal.__repr__()
            for animal in self.animals
            if animal.__class__.__name__ == "Cheetah"
        ]
        if not result:
            return []

        return result

    def animals_status(self) -> str:
        result = f"You have {len(self.animals)} animals" + "\n"
        result += f"----- {len(self.lions())} Lions:\n"
        result += '\n'.join(self.lions()) + "\n"
        result += f"----- {len(self.tigers())} Tigers:\n"
        result += '\n'.join(self.tigers()) + "\n"
        result += f"----- {len(self.cheetahs())} Cheetahs:\n"
        result += '\n'.join(self.cheetahs())

        return result

    def keepers(self) -> list:
        result = [
            worker.__repr__()
            for worker in self.workers
            if worker.__class__.__name__ == "Keeper"
        ]
        if not result:
            return []

        return result

    def caretakers(self) -> list:
        result = [
            worker.__repr__()
            for worker in self.workers
            if worker.__class__.__name__ == "Caretaker"
        ]
        if not result:
            return []

        return result

    def vets(self) -> list:
        result = [
            worker.__repr__()
            for worker in self.workers
            if worker.__class__.__name__ == "Vet"
        ]
        if not result:
            return []

        return result

    def workers_status(self) -> str:
        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(self.keepers())} Keepers:\n"
        result += '\n'.join(self.keepers()) + "\n"
        result += f"----- {len(self.caretakers())} Caretakers:\n"
        result += '\n'.join(self.caretakers()) + "\n"
        result += f"----- {len(self.vets())} Vets:\n"
        result += '\n'.join(self.vets())

        return result
