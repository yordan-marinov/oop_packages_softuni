from project.player.player import Player
from project.player.beginner import Beginner


class BattleField:
    def fight(self, attacker: Player, enemy: Player):
        self.is_one_of_players_is_dead((attacker, enemy))
        self.is_player_beginner((attacker, enemy))
        self.get_bonus_health_points((attacker, enemy))
        while True:
            if attacker.is_dead or enemy.is_dead:
                break    
            self.battle_players(attacker, enemy)
            self.battle_players(enemy, attacker)
                
            

    @staticmethod
    def is_one_of_players_is_dead(players):
        for player in players:
            if player.is_dead:
                raise ValueError("Player is dead!")

    @staticmethod
    def is_player_beginner(players):
        for player in players:
            if isinstance(player, Beginner):
                player.health += 40
                player.increase_card_damage_points(30)

    @staticmethod
    def health_bonus(player):
        return sum(c.health_bonus for c in player.card_repository.cards)

    def get_bonus_health_points(self, players):
        for player in players:
            player.health += self.health_bonus(player)

    @staticmethod
    def get_current_damage_points(player):
        for card in player.card_repository.cards:
            yield card.damage_points
    
    def battle_players(self, player_1, player_2):
        player_2.take_damage(self.get_current_damage_points(player_1))