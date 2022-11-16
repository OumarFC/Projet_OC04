
from views import menu
from models import tournaments
from models import players
from views import views


class TournamentReports:

    def __call__(self):
        self.clear = views.ClearScreen()
        self.tournament = tournaments.Tournament()
        self.menu = menu.LoadMenus()
        self.player = players.Player()
        self.display_tournament = views.DisplayTournamentsReport()
        self.tournament_db = self.tournament.data_tournament
        self.player_db = self.player.data_players
        player_serialized = []
        tournament_objects = []
        tournament_serialized = []
        round_table = self.tournament_db.table("Rounds")

        for tournament in self.tournament_db:
            tournament_objects.append(tournament)
            tournament_serialized.append(self.tournament.unserialized_tournament(tournament))

            self.clear()
            self.display_tournament()
            entry = str(menu.LoadMenus.load_menu(menu.LoadMenus.tournament_report_menu()))

            if entry == "1":
                for tournament in tournament_serialized:
                    for id in tournament.players_id:
                        player = self.player_db.get(doc_id=id)
                        player_serialized.append(self.player.unserialized_player(player))
                self.display_tournament.display_tournaments(tournament_serialized, player_serialized)
                player_serialized.clear()

            if entry == "2":
                for tour in [1, 2, 3, 4]:
                    round = round_table.get(doc_id=tour)
                    print(f"Nom : {round['name']} - Début: {round['begin_time']} - Fin : {round['end_time']}")
                input("Appuyez sur une touche pour revenir au menu rapport de tournoi")

            if entry == "3":
                for id_round in [1, 2, 3, 4]:
                    round = round_table.get(doc_id=id_round)
                    print(f"{round['name']} :")
                    for match in round['list_match_finished']:
                        print(match)
                        player_1 = match[0][0]
                        player_1 = self.player_db.get(doc_id=player_1)
                        score_player_1 = match[0][1]
                        player_2 = match[1][0]
                        player_2 = self.player_db.get(doc_id=player_2)
                        score_player_2 = match[1][1]
                        print(f"Match : {player_1['first_name']} {player_1['last_name']} -- "
                              f"{player_2['first_name']} {player_2['last_name']}\n"
                              f"Score : {score_player_1} -- {score_player_2}\n")

            if entry == "4":
                TournamentReports.__call__(self)

