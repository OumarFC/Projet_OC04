from controllers import main_controllers
from models.tournaments import Tournament
from models import tours
from models import matchs
from datetime import datetime
from views.menu import LoadMenus
from views.views import DisplayTournamentsReport
import time


class TournamentController:

    PLAYER_IN_TOURNAMENT = []

    """for add informations tournament in data base tournament"""
    def __init__(self):

        self.tournament = Tournament()
        self.tour = tours.Tour()
        self.tournament_values = []
        self.display_report = DisplayTournamentsReport()
        self.tournament_db = self.tournament.data_tournament

    def create_one_tournament(self):

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

    def tournament_select(self):
        valid_entry = False
        tournament_objects = []
        tournament_serialized = []
        while not valid_entry:
            for tournament in self.tournament_db:
                tournament_objects.append(tournament)
                tournament_serialized.append(self.tournament.unserialized_tournament(tournament))
            print("-----Liste des Tournoi -----")
            for tournament in tournament_serialized:
                print(f"{tournament.tournament_name} - {tournament.locality} - {tournament.tournament_date}\n"
                      f"ID du Tournoi : {tournament.tournament_id}\n"
                      f"Nombre de tours : {tournament.number_of_tours}\n"
                      f"Contrôle du temps : {tournament.time_control}\n"
                      f"Description : {tournament.description}\n"
                      )
            print("Saisissez l'ID du tournoi correspondant : ")
            choice = input("--> ")
            time.sleep(1)
            try:
                choice.isdigit() is False
                int(choice) < len(self.tournament.data_tournament)
                int(choice) <= 0
            except Exception:
                print("Saisissez un chiffre correspondant au tournoi")
            else:
                choice_tournament = self.tournament.data_tournament.get(doc_id=int(choice))
                objet_tournament = self.tournament.unserialized_tournament(choice_tournament)
                return objet_tournament
        else:
            print("Aucun tournoi créé - Veillez créer un tournoi")

    def run_tournament(self):
        """Create first round and update player score"""
        home_menu_controller = main_controllers.HomeMenuController()
        first_list_tour = self.tournament.generate_first_pairs_players(self.tournament_select())
        self.tour.name = "Tour1"
        self.tour.begin_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tour.update_score(first_list_tour)

        self.tour.list_match_finished = matchs.Match.list_match_finished
        tours_table = self.tournament.data_tournament.table("Rounds")
        tours_table.insert(self.tour.serialize_tour())
        self.tour.end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"{self.tour.name} : {self.tour.list_match_finished}")

        for i in range(2, self.tournament.number_of_tours + 1):
            print("Tour" + str(i) + ": ---- Ajout des Joueurs au Tour suivant---- ")
            others_list_tour = self.tournament.generate_others_pairs_players(self.tour.list_match_finished)
            matchs.Match.list_match_finished.clear()
            self.tour.name = "Tour" + str(i)

            self.tour.begin_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(" ------ Mise à jour du score des joueurs --- ")
            self.tour.update_score(others_list_tour)
            self.tour.list_match_finished = matchs.Match.list_match_finished
            #print(Tournament.MATCH_IN_TOURNAMENT)
            self.tour.end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tours_table.insert(self.tour.serialize_tour())

            print(f"{self.tour.name} : {self.tour.list_match_finished}")
            others_list_tour.clear()

        home_menu_controller()
