from project.survivor import Survivor

from abc import ABC, abstractclassmethod


class Supply(ABC):
    def __init__(self, needs_increase: int):
        self.needs_increase: int = needs_increase
        
    @property
    def needs_increase(self):
        return self.__needs_increase
    
    @needs_increase.setter
    def needs_increase(self, value):
        if value < 0:
            raise ValueError("Needs increase cannot be less than zero.")
        self.__needs_increase = value

    def apply(self, survivior: Survivor):
        survivior.needs += self.needs_increase