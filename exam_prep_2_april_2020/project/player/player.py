from abc import ABC, abstractclassmethod
from project.card.card_repository import CardRepository


class Player(ABC):
    def __init__(self, username: str, health: int):
        self.username: str = username
        self.health: int = health
        self.card_repository = CardRepository()
        
    @property
    def username(self):
        return self.__username

    @property
    def health(self):
        return self.__health

    @username.setter
    def username(self, string):
        if not string:
            raise ValueError("Player's username cannot be an empty string.")
        self.__username = string

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Player's username cannot be an empty string.")
        self.__health = value
        
        
    @property
    def is_dead(self):
        if self.health <= 0:
            return True
        return False
        
    # @abstractclassmethod
    def take_damage(self, damage_points: int):
        if damage_points < 0:
            raise ValueError("Damage points cannot be less than zero.")

        self.health -= damage_points