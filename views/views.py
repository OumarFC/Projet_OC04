from models.players import Player


class MainDisplay:
    """Display the main title"""

    def display_title(self):
        print("\n\n//**************************************//")
        print("//       BIENVENUE DANS LE TOURNOI       //")
        print("//         DE JEUX D'ECHEC SUISSE        //")
        print("//**************************************//")


class PlayersDiplay:
    """Display all the players  and these rank in the database"""

    def __call__(self):
        player = Player()
        list_players_to_database = []
        players_database = player.load_player_db()

        for one_player in players_database:
            list_players_to_database.append(player.unserialized_player(one_player))

        for player in list_players_to_database:
            print(f"{player.player_id} -- Prenom/Nom : {player.first_name} "
                  f"{player.last_name} -- Classement : {player.rank}")


class DisplayPlayersReport:
    """Display all the players by alphabetical and by rank """

    def __call__(self):
        print("------------------------------------------------\n"
              "--------Affichages de rapport des joueurs--------\n"
              "------------------------------------------------\n"
              )

    def display_by_alphabetical(self, players_list):
        for player in players_list:
            print(f"{player.last_name} {player.first_name} - {player.date_of_birth}"
                  f" - {player.gender} - Classement : {player.rank}")

    def display_by_rank(self, players_list):
        for player in players_list:
            print(f"Classement :{player.rank} - {player.last_name}"
                  f" {player.first_name} - {player.date_of_birth} - {player.gender}")


class DisplayTournamentsReport:
    """Display all the tournament and players"""
    def __call__(self):
        print("------------------------------------------------\n"
              "---------Affichage de Rapport de tournois ------\n"
              "------------------------------------------------\n"
              )

    def display_tournaments(self, tournaments_list, players_list):
        for tournament in tournaments_list:
            print(f"{tournament.tournament_name} - {tournament.locality} - {tournament.tournament_date}\n"
                  f"Nombre de tours : {tournament.number_of_tours}\n"
                  f"Contrôle du temps : {tournament.time_control}\n"
                  f"Description : {tournament.description}\n"
                  )
            for player in players_list:
                print(f"Joueurs : {player.last_name} - {player.first_name} - Classement : {player.rank}")
            print()
