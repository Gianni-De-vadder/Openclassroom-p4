from views.view_player import ViewPlayer
from models.player import Player
from controllers.database import Database
import json   


class PlayerController:

    def __repr__(self):
        return json.dumps(self.__dict__, sort_keys=True, indent=4, ensure_ascii=False) 

    def __init__(self) -> None:
        self.view = ViewPlayer()
        self.database = Database()

    def handle_player(self):
        exit_requested = False
        
        while not exit_requested:
            choice = self.view.display_player_menu()

            if choice == "1":
                # creation d'un joueur
                self.create_player()
            elif choice == "2":
                # Update player
                self.update_player()
            elif choice == "3":
                load_players_by_name = Player.display_ranking_by_name()
                print(load_players_by_name)
            elif choice == "4":
                load_players_by_elo = Player.display_ranking_by_name()
                print(load_players_by_elo)
            elif choice == "5":
                # Retour au menu précédent
                exit_requested = True

    def create_player(self):

    # Récupération des infos du joueur
        user_entries = self.view.get_info_player()

    # Création du joueur
        player = Player(user_entries['name'],user_entries['first_name'],user_entries['rank'])


    #Serialization
        serialized_player = Database().serialize(player)
        print(serialized_player)

    # #Sauvegarde du joueur dans la database
        Database().save_db('players', serialized_player)
        return player

    # def auto_increment_player():
    #     if(Database. == ):



    def update_player(self):
        """Manage player update"""
        print("Gestion de la modification d'un joueur")
        input('\nAppuyez sur Entreé pour continuer ')
        

    def display_players_order_by_name(self):
        """Print players order by name"""
        print("Gestion de l'impression de la liste des joueurs triée par nom")
        input('\nAppuyez sur Entreé pour continuer ')

    def display_players_order_by_rank(self):
        """Print players order by rank"""
        print("Gestion de l'impression de la liste des joueurs triée par rang")
        input('\nAppuyez sur Entreé pour continuer ')