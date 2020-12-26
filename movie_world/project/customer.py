class Customer:
    def __init__(self, name: str, age: int, id: int):
        self.name: str = name
        self.age: int = age
        self.id: int = id
        self.rented_dvds = []

    def __repr__(self):
        return f"{self.id}: {self.name} of age " \
               f"{self.age} has {len(self.rented_dvds)} rented DVD's " \
               f"({', '.join(dvd.name for dvd in self.rented_dvds)})"
