class Team: 
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []
        
    @property
    def name(self):
        return self.__name

    @property
    def rating(self):
        return self.__rating
    
    @property
    def players(self):
        return self.__players


    def add_player(self, player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.name}"
    
    def remove_player(self, player_name: str):
        player_obj = [p for p in self.__players if p.name == player_name]
        if not player_obj:
            return f"Player {player_name} not found"
        self.__players.remove(player_obj[0])
        return player_obj[0]