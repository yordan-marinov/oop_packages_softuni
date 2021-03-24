from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.players: list = []
        self.players_names = set()
        
    @property
    def count(self):
        return len(self.players)

    def add(self, player: Player):
        if player.username in self.players_names:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.players_names.add(player.username)

    def remove(self, player: str):
        if not player:
            raise ValueError("Player cannot be an empty string!")
        player_obj = self.find(player)
        if player_obj:
            self.players.remove(player_obj)
            self.players_names.remove(player_obj.username)
    
    def find(self, username: str):
        obj = [p for p in self.players if p.username == username][0]
        if obj:
            return obj