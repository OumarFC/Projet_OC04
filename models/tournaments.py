
from models.players import Player
from numpy import array


class DictObj:

    def __init__(self, in_dict: dict):

        assert isinstance(in_dict, dict)

        for key, val in in_dict.items():
            if isinstance(val, (list, tuple)):
                setattr(self, key, [DictObj(x) if isinstance(x, dict) else x for x in val])
            else:
                setattr(self, key, DictObj(val) if isinstance(val, dict) else val)


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
        self.list_of_tours = list_of_tours
        self.tournament_id = tournament_id

    def __repr__(self):
        print(f" la liste des match : {self.list_of_tours}")

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

    def add_tournament_name(self):

        pass

    def add_tournament_locality(self):

        pass

    def add_tournament_date(self):

        pass

    def add_tournament_time_control(self):

        pass

    def add_tournament_description(self):

        pass

    def sort_players_by_rank(self):
        """Sort players by rank (ascending)"""
        player = Player()
        list_all_players = player.load_player_db()
        players_by_rank = sorted(list_all_players, key=lambda x: x.get('rank'))

        return players_by_rank

    def sort_players_by_score(self):
        """Sort players by score (descending)"""
        player = Player()
        list_all_players = player.load_player_db()

        players_by_score = sorted(list_all_players, key=lambda x: x.get('tournament_score'), reverse=True)

        return players_by_score

    def generate_first_pairs_players(self):
        list_all_players = self.sort_players_by_rank()
        print(list_all_players)
        half = int(len(list_all_players) / 2)
        first_list = list_all_players[half:]
        second_list = list_all_players[:half]
        round_1 = list(zip(first_list, second_list))
        self.list_of_tours = round_1

        print("Round 1 :  First Round ")

        return self.list_of_tours

    def generate_others_pairs_players(self):

        players = self.sort_players_by_score()

        players_array = array(players)
        players_index_pairs = [index for index in range(len(players)) if index % 2 == 0]
        players_index_impairs = [index for index in range(len(players)) if index % 2 != 0]
        matches = zip(players_array[players_index_pairs], players_array[players_index_impairs])
        matches = list(matches)
        print(matches)

        return matches


class Tour:

    """
    Chaque tour est une liste de matchs. Chaque match consiste en une paire de joueurs
    avec un champ de résultats pour chaque joueur. Lorsqu'un tour est terminé,
    le gestionnaire du tournoi saisit les résultats de chaque match avant de
    générer les paires suivantes.
    Les instances de tour doivent être stockées dans une liste sur l'instance
    de tournoi à laquelle elles appartiennent.

    doit Renvoyer l'instance de tour """

    def __init__(self, list_of_match, name=None, begin_time=None, end_time=None):
        self.name = name
        self.begin_time = begin_time
        self.end_time = end_time
        self.list_of_round = []
        self.list_of_match = list_of_match

    def serialize_round(self):
        """Return serialized info for round """
        return {
            "name": self.name,
            "begin_time": self.begin_time,
            "end_time": self.end_time,
            "list_of_match": self.list_of_match
        }

    def mettre_jour_score(self):

        for match in self.list_of_match:
            """ faire un match et mettre le score des joueurs qui s'affronte"""
            winner = int(input(" -->"))

            instance_match = Match(match)
            instance_match.run_match(winner)


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
        self.list_players = []
        self.t = ()

    def __str__(self):
        return f"MATCH : {self.players} --CONTRE-- {self.players}."

    def run_match(self, vainqueur=None):

        for player in range(len(self.players)):
            self.list_players.append(DictObj(self.players[player]))

        if vainqueur == 2:

            self.list_players[0].tournament_score += 1/2
            self.list_players[1].tournament_score += 1/2
            self.t = [(self.list_players[1].player_id, self.list_players[1].tournament_score),
                      (self.list_players[0].player_id, self.list_players[0].tournament_score)]

        elif vainqueur == 0 or vainqueur == 1:

            self.list_players[vainqueur].tournament_score += 1
            self.t = [(self.list_players[1].player_id, self.list_players[1].tournament_score),
                      (self.list_players[0].player_id, self.list_players[0].tournament_score)]

        self.list_match_finiched.append(self.t)







