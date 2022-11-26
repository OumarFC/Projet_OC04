from controllers import main_controllers
from models.tournaments import Tournament
from models import tours
from models import matchs
from datetime import datetime
from views.menu import LoadMenus
from views.views import DisplayTournamentsReport
import time


class TournamentController:
    """for add informations tournament in data base tournament"""
    def __init__(self):

        self.tournament_values = []

    def create_one_tournament(self):

        self.tournament = Tournament()
        self.tournament_values = [
            self.prompt_tournament_name(),
            self.prompt_tournament_locality(),
            self.prompt_tournament_date(),
            self.prompt_tournament_time_control(),
            self.prompt_tournament_description(),
            self.add_players_id_to_tournament(),
            self.prompt_tournament_id()]

        return self.tournament_values

    def add_tournament(self):
        """Add Tournament to database json """
        self.menu_control = main_controllers.HomeMenuController()
        self.menu = LoadMenus()
        self.nbt = 1
        for nb in range(0, self.nbt):
            self.created_tournament = self.create_one_tournament()
            tournament = Tournament(
                tournament_name=self.created_tournament[0],
                locality=self.created_tournament[1],
                tournament_date=self.created_tournament[2],
                number_of_tours=4,
                time_control=self.created_tournament[3],
                description=self.created_tournament[4],
                players_id=self.created_tournament[5],
                tournament_id=self.created_tournament[6]
            )
            tournament.save_tournament_db()

        self.menu_control()

    def add_players_id_to_tournament(self):

        players_id = []
        for id in [*range(1, 9)]:
            players_id.append(id)
        print(f"ID of Players in Tournament : {players_id}")

        return players_id

    def prompt_tournament_name(self):
        tournament_name = False
        tournament_valid_name = None
        while not tournament_name:
            tournament_valid_name = input("Enter tournament name: ")
            if tournament_valid_name != "":
                tournament_name = True
            else:
                print("You must enter a valid name")
        return tournament_valid_name

    def prompt_tournament_locality(self):

        locality_valid_name = None
        locality_name = False
        while not locality_name:
            locality_valid_name = input("Enter location of the tournament: ")
            if locality_valid_name != "":
                locality_name = True
            else:
                print("You must enter a valid location")
        return locality_valid_name

    def prompt_tournament_date(self):

        tournament_valid_date = None
        tournament_date = False
        while not tournament_date:
            tournament_valid_date = input("Enter the tournament date in the format (JJ/MM/AAAA) : ")
            if tournament_valid_date != "" and str('/') in tournament_valid_date and len(tournament_valid_date) == 10:
                tournament_date = True
            else:
                print("You must enter a valid tournament date")

        return tournament_valid_date

    def prompt_tournament_time_control(self):
        print("Choose time control:")
        control_time = None
        entry = str(LoadMenus.load_menu(LoadMenus.time_control_menu()))
        if entry == "1":
            control_time = "Bullet"
        if entry == "2":
            control_time = "Blitz"
        if entry == "3":
            control_time = "Coup rapide"

        return control_time

    def prompt_tournament_description(self):
        description = input("Enter a tournament description :\n"
                            "-->")
        return description

    @staticmethod
    def prompt_tournament_id():

        tournament_valid_id = None
        tournament_id = False
        while not tournament_id:
            tournament_valid_id = input("Enter Id : ")
            if tournament_valid_id.isdigit():
                tournament_id = True
            else:
                print("You must enter valid Id")

        return int(tournament_valid_id)

    def select_tournament(self):
        home_menu_controller = main_controllers.HomeMenuController()
        tournament = Tournament()
        display_tournament = DisplayTournamentsReport()

        valid_entry = False
        while not valid_entry:
                print("Entrez le chiffre correspondant au tournoi")
                choice = input("--> ")
                if choice.isdigit() and choice != "" and int(choice) == 0:
                    print("Vous devez entrer le chiffre correspondant au tournoi à lancer")
                else:
                    choice_tournament = tournament.data_tournament.get(doc_id=int(choice))
                    tournament_object = tournament.unserialized_tournament(choice_tournament)
                    return tournament_object

        else:
            print("Pas de tournois créé, veuillez créer un tournoi")
            time.sleep(1)
            home_menu_controller()

    @staticmethod
    def run_tournament():
        """Create first round and update player score"""
        tes = TournamentController()
        tourny = tes.select_tournament()
        print(tourny.tournament_name)
        home_menu_controller = main_controllers.HomeMenuController()
        tournament = Tournament()
        first_list_tour = tournament.generate_first_pairs_players()
        first_tour = tours.Tour()
        first_tour.name = "Round1"
        first_tour.begin_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        first_tour.update_score(first_list_tour)

        first_tour.list_match_finished = matchs.Match.list_match_finished
        tours_table = tournament.data_tournament.table("Rounds")
        tours_table.insert(first_tour.serialize_tour())
        first_tour.end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(first_tour.list_match_finished)

        matchs.Match.list_match_finished.clear()

        for i in range(2, tournament.number_of_tours + 1):

            print("Round" + str(i) + ": ---- The next Others Round in Tournament  ---- ")
            others_list_tour = tournament.generate_others_pairs_players()
            other_tour = tours.Tour()
            other_tour.name = "Round" + str(i)

            other_tour.begin_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            other_tour.update_score(others_list_tour)
            other_tour.list_match_finished = matchs.Match.list_match_finished

            other_tour.end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tours_table.insert(other_tour.serialize_tour())

            print(other_tour.list_match_finished)
            matchs.Match.list_match_finished.clear()

        home_menu_controller()
