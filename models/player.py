import json
from controllers.database import Database
"""Classe joueur"""
class Player:
    """Represents a player"""

    table_name = "players"

    def __init__(self, name: str, first_name: str, elo: int) -> None:
        self.name = name
        self.first_name = first_name
        self.elo = elo
        self.score = 0

    def __str__(self) -> str:
        return self.name
    
    @classmethod
    def display_ranking_by_name(cls):
        return Database.load_db(cls.table_name, 'name')
    
    @classmethod
    def display_ranking_by_elo(cls):
        return Database.load_db(cls.table_name, 'elo')

    

    @classmethod    
    def deserialize(self, data: dict) -> "Player":
        """Return a Player from a dictionnary"""
        return Player(**data)


    def save(self):
        print("player sauvegardé")

if __name__ == '__main__':
    """Test a player"""
    p1 = Player("Carlsen", 3000)
    p2 = Player("Kasparov", 2800)

    print(p1.table_name)
    print(p2.table_name)
    print(Player.table_name)

    # p1.save()

    print(f"sérialisation p1: {p1.serialize()}")

    data = {'name': "Carlsen", 'elo': 3100}
    player = Player.deserialize(data)
    print(player)
    