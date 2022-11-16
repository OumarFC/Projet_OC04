
from models.players import Player
from numpy import array
from tinydb import TinyDB

data_path = "C:\\Users\\Itec Global Services\\PycharmProjects\\Projet_OC04\\data\\"

class Tournament:

    def __init__(self, tournament_name=None,
                 locality=None,
                 tournament_date=None,
                 number_of_tours=4,
                 time_control=None,
                 description=None,
                 players_id=[],
                 list_of_tours=[],
                 tournament_id=None
                 ):

        self.tournament_name = tournament_name
        self.locality = locality
        self.tournament_date = tournament_date
        self.number_of_tours = number_of_tours
        self.time_control = time_control
        self.description = description
        self.players_id = players_id
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
            "players_id": self.players_id,
            "tournament_id": self.tournament_id,
        }

    def unserialized_tournament(self, serialized_tournament):
        tournament_name = serialized_tournament["tournament_name"]
        locality = serialized_tournament["locality"]
        tournament_date = serialized_tournament["tournament_date"]
        number_of_tours = serialized_tournament["number_of_tours"]
        time_control = serialized_tournament["time_control"]
        description = serialized_tournament["description"]
        players_id = serialized_tournament["players_id"]
        tournament_id = serialized_tournament["tournament_id"]
        return Tournament(tournament_name,
                      locality,
                      tournament_date,
                      number_of_tours,
                      time_control,
                      description,
                      players_id,
                      tournament_id
                      )

    def save_tournament_db(self):
        """add new Tournament to database and Set tournament_id to doc id """
        tournament_db = self.data_tournament
        self.tournament_id = tournament_db.insert(self.serialized_tournament())
        tournament_db.update({'tournament_id': self.tournament_id}, doc_ids=[int(self.tournament_id)])

    def sort_players_by_rank(self):
        """Sort players by rank (ascending) and make player as objet"""
        player = Player()
        list_players = player.load_player_db()
        players_by_rank = sorted(list_players, key=lambda x: x.get('rank'))

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

