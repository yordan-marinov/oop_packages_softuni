from project.player.player import Player
from project.card.card import Card


class Beginner(Player):
    initial_health_points = 50

    def __init__(self, username):
        super().__init__(username, self.initial_health_points)

    def increase_card_damage_points(self, value):
        for card in self.card_repository.cards:
            card.damage_points += value
