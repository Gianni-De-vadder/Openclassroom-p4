from audioop import reverse
from pathlib import Path
from tinydb import TinyDB, Query
from tinydb import where
from models import player
from models.tournament import Tournament
import json
import pprint

DATABASE_NAME = "../data/"
class Connexion: 
    
    @classmethod
    def TinyDB_Connect(cls,db):
        if(db == 'players' or db == 'tournament'):
            db_connection = TinyDB("data/" + db + ".json")

            return db_connection

        else:
            return print('Please enter valid a database')    


class Database():
    

    # def __init__(self) -> None:
    #     self.db = TinyDB(DATABASE_NAME)
        
        def serialize(self,player) -> dict:
                """Return a dictionnary with the object attribute value"""
                data = {
                    'first_name': player.first_name,
                    'name': player.name,
                    'elo': player.elo
                }
                return data

        def save_db(self,db_name,player):

                db = Connexion.TinyDB_Connect(db_name)
                db.insert(player)
                print(f"{player['name']} sauvegardé avec succès.")


        @classmethod
        def update_db(cls, db_name, serialized_data):
            cls.db = Connexion.TinyDB_Connect(db_name)
            cls.db.update(
                serialized_data,
                where('name') == serialized_data['name']
            )
            print(f"{serialized_data['name']} updaté avec succès.")


        @classmethod
        def update_player_rank(cls,db_name, serialized_data):
            cls.db = Connexion.TinyDB_Connect(db_name)
            cls.db.update(
                    {'rank': serialized_data['rank'], 'total_score': serialized_data['total_score']},
                    where('name') == serialized_data['name']
            )
            print(f"{serialized_data['name']} updaté avec succès.")


        @classmethod
        def load_db_order(cls,db,order):
            if(order == 'name' or order == 'elo' ):
                print(f"sort by {order}")
                players = db.all()
                ordering = [(dict_[order], dict_) for dict_ in players]
                # pprint.pprint(ordering)
                print(type(ordering))
                ordering.sort()
                # ordered_players = pprint.pprint([dict_ for (key, dict_) in ordering])
                # return ordered_players

            else:
                return print("Please enter a valid parameter for order, 'name' or 'elo'")   


        @classmethod
        def load_db(cls,db_name, order):
            # try:
            db = Connexion.TinyDB_Connect(db_name)
            db_ordered = Database.load_db_order(db, order)
            return db_ordered

            # except:
            #     print('Problème durant le chargement de la DB...')
            #     return None
