class Cheetah:
    def __init__(self, name: str, gender: str, age: int):
        self.name: str = name
        self.gender: str = gender
        self.age: int = age

    @staticmethod
    def get_needs():
        return 60

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
