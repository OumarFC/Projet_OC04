
from models.players import Player
from numpy import array
from tinydb import TinyDB
import os
import sys

sys.path.append(os.getcwd())
data_path = f'{os.getcwd()}\data\\'


class Tournament:

    def __init__(self, tournament_name=None,
                 locality=None,
                 tournament_date=None,
                 number_of_tours=4,
                 time_control=None,
                 description=None,
                 players=None,
                 list_of_tours=[],
                 tournament_id=None
                 ):

        self.tournament_name = tournament_name
        self.locality = locality
        self.tournament_date = tournament_date
        self.number_of_tours = number_of_tours
        self.time_control = time_control
        self.description = description
        self.players = players
        self.list_of_tours = []
        self.tournament_id = tournament_id
        self.data_tournament = TinyDB(data_path + 'tournament.json')

    def __str__(self):
            return f"Liste des matchs : {self.list_of_tours})."

    def serialized_tournament(self):
        """Return serialized tournament info"""
        return {
            "tournament_name": self.tournament_name,
            "locality": self.locality,
            "tournament_date": self.tournament_date,
            "number_of_tours": self.number_of_tours,
            "time_control": self.time_control,
            "description": self.description,
            "players": self.players,
            "list_of_tours": self.list_of_tours,
            "tournament_id": self.tournament_id,
        }

    def unserialized_tournament(self, serialized_tournament):
        tournament_name = serialized_tournament["tournament_name"]
        locality = serialized_tournament["locality"]
        tournament_date = serialized_tournament["tournament_date"]
        number_of_tours = serialized_tournament["number_of_tours"]
        time_control = serialized_tournament["time_control"]
        description = serialized_tournament["description"]
        players = serialized_tournament["players"]
        list_of_tours = serialized_tournament["list_of_tours"]
        tournament_id = serialized_tournament["tournament_id"]
        return Tournament(tournament_name,
                      locality,
                      tournament_date,
                      number_of_tours,
                      time_control,
                      description,
                      players,
                      list_of_tours,
                      tournament_id
                      )

    def save_tournament_db(self):
        """add new Tournament to database and Set tournament_id to doc id """
        tournament_db = self.data_tournament
        self.tournament_id = tournament_db.insert(self.serialized_tournament())
        tournament_db.update({'tournament_id': self.tournament_id}, doc_ids=[int(self.tournament_id)])

    def prompt_tournament_name(self):
        tournament_name = False
        while not tournament_name:
            tournament_valid_name = input("Entrez le nom du tournoi: ")
            if tournament_valid_name != "":
                tournament_name = True
            else:
                print("Vous devez entrer un nom")
        return tournament_valid_name

    def prompt_tournament_locality(self):
        locality_name = False
        while not locality_name:
            locality_valid_name = input("Entrez le lieu où se déroule le tournoi: ")
            if locality_valid_name != "":
                locality_name = True
            else:
                print("Vous devez entrer un endroit")
        return locality_valid_name

    def prompt_tournament_date(self):
        tournament_date = False
        while not tournament_date:
            tournament_valid_date = input("Saisissez la date du tournoi au format (JJ/MM/AAAA) : ")
            if tournament_valid_date != "" and str('/') in tournament_valid_date and len(tournament_valid_date) == 10:
                tournament_date = True
            else:
                print("Vous devez saisir une date de tournoi valide")

        return tournament_valid_date

    def prompt_tournament_time_control(self):
        print("Choisissez le contrôle du temps:")
        control_time = None
        #prompt = self.create_menu(self.create_menu.time_control_menu)
        entry = input("->")
        if entry == "1":
            time_control = "Bullet"
        if entry == "2":
            time_control = "Blitz"
        if entry == "3":
            time_control = "Coup rapide"
        return control_time

    def prompt_tournament_description(self):
        description = input("Entrer une description du tournoi :\n"
                            "-->")
        return description

    def prompt_tournament_id(self):
        tournament_id = False
        while not tournament_id:
            tournament_valid_id = input("Saisissez l'Id : ")
            if tournament_valid_id.isdigit() and tournament_valid_id != "" and int(tournament_valid_id) >= 0:
               tournament_id = True
            else:
                print("Vous devez saisir un id valide")

        return tournament_valid_id

    def sort_players_by_rank(self):
        """Sort players by rank (ascending) and make player as objet"""
        player = Player()
        list_players = player.load_player_db()
        players_by_rank = sorted(list_players, key=lambda x: x.get('rank'))

        print(players_by_rank)

        list_all_players_objet = []
        for one_player in players_by_rank:
            list_all_players_objet.append(player.unserialized_player(one_player))
        return list_all_players_objet

    def sort_players_by_score(self):
        """Sort players by score (descending) and make player as objet"""
        player = Player()
        list_players = player.load_player_db()
        players_by_score = sorted(list_players, key=lambda x: x.get('tournament_score'), reverse=True)

        list_all_players_objet = []
        for one_player in players_by_score:
            list_all_players_objet.append(player.unserialized_player(one_player))

        return list_all_players_objet

    def generate_first_pairs_players(self):
        list_all_players = self.sort_players_by_rank()
        half = int(len(list_all_players) / 2)
        first_list = list_all_players[half:]
        second_list = list_all_players[:half]
        list_of_first_tours = list(zip(first_list, second_list))
        print("Round 1 :  First Round ")

        return list_of_first_tours

    def generate_others_pairs_players(self):

        players = self.sort_players_by_score()

        players_array = array(players)
        players_index_pairs = [index for index in range(len(players)) if index % 2 == 0]
        players_index_impairs = [index for index in range(len(players)) if index % 2 != 0]
        list_of_others_tours = zip(players_array[players_index_pairs], players_array[players_index_impairs])
        list_of_others_tours = list(list_of_others_tours)

        return list_of_others_tours


class Tour:

    def __init__(self, name=None, begin_time=None, end_time=None, list_match_finiched=None):
        self.name = name
        self.begin_time = begin_time
        self.end_time = end_time
        self.list_match_finiched = list_match_finiched
        self.list_of_match = []

    def serialize_tour(self):
        """Return serialized info for round """
        return {
            "name": self.name,
            "begin_time": self.begin_time,
            "end_time": self.end_time,
            "list_match_finiched" : self.list_match_finiched,
        }

    def unserialized_tour(self, serialized_tour):
        name = serialized_tour["name"],
        begin_time = serialized_tour["begin_time"],
        end_time = serialized_tour["end_time"]
        list_of_match = serialized_tour["list_match_finiched"]
        return Tour(name,
                begin_time,
                end_time,
                list_match_finiched,
                )

    def mettre_jour_score(self, list_of_match):

        for match in list_of_match:
            """ faire un match et mettre le score des joueurs qui s'affronte"""
            winner = int(input(" -->"))

            instance_match = Match(match)
            instance_match.run_match(winner)

            print(instance_match)


class Match:

    list_match_finiched = []

    """
     Un match unique doit être stocké sous la forme d'un tuple contenant deux listes,
     chacune contenant deux éléments : une référence à une instance de joueur et un score.
     Les matchs multiples doivent être stockés sous forme de liste sur l'instance du tour.
     """

    def __init__(self, players=None):
        """un tuple de deux joueurs"""
        self.players = players
        self.duel_match = ()

    def __str__(self):
        return f"MATCH (Joueur : {self.players[0].player_id}) --CONTRE-- Joueur : {self.players[1].player_id}."

    def run_match(self, vainqueur=None):

        if vainqueur == 2:

            self.players[0].tournament_score += 1/2
            self.players[1].tournament_score += 1/2
            self.duel_match = [(self.players[1].player_id, self.players[1].tournament_score),
                      (self.players[0].player_id, self.players[0].tournament_score)]

        elif vainqueur == 0 or vainqueur == 1:

            self.players[vainqueur].tournament_score += 1
            self.duel_match = [(self.players[1].player_id, self.players[1].tournament_score),
                      (self.players[0].player_id, self.players[0].tournament_score)]

        Match.list_match_finiched.append(self.duel_match)




