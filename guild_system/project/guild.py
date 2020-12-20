# from guild_system.project.player import Player
# from typing import List


class Guild:
    # name: str
    # list_of_players: List[Player]

    def __init__(self, name: str, ):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild != "Unaffiliated" and player.guild != self.name:
            return f"{player.name} is in another guild."

        if player.name in [p.name for p in self.players]:
            return f"Player {player.name} is already in the guild"

        self.players.append(player)
        player.guild = self.name

        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if player_name not in [p.name for p in self.players]:
            return f"Player {player_name} in not in the guild."

        current_player = [
            p for p in self.players
            if player_name == p.name
        ].pop()

        self.players.remove(current_player)
        current_player.guild = "Unaffiliated"

        return f"Player {current_player.name} has been removed from the guild."

    def guild_info(self):
        info = f"Guild: {self.name}\n"
        for players in self.players:
            info += players.player_info()

        return info
