from abc import ABC, abstractclassmethod


class Animal(ABC):
    def __init__(self, name: str, age: int, gender: str):
        self.name: str = name
        self.age: int = age
        self.gender: str = gender

    @abstractclassmethod
    def __repr__(self):
        pass

    @abstractclassmethod
    def make_sound(self):
        pass
