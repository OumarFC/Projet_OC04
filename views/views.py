from models.players import Player
from controllers.controller import PlayerController, TournamentController

control = TournamentController()
control.run_tournament()


class PlayersDiplay:
    """Display all the players in the database"""

    def __call__(self):
        player = Player()
        list_players_to_database = []
        players_database = player.load_player_db()

        for one_player in players_database:
            list_players_to_database.append(player.unserialized_player(one_player))

        for player in list_players_to_database:
            print(f"{player.player_id} -- Prenom/Nom : {player.first_name} {player.last_name} -- Classement : {player.rank}")


test = PlayersDiplay()
test.__call__()