
from models.players import Player


class Tournament:

    def __init__(self, tournament_name=None,
                 locality=None,
                 tournament_date=None,
                 number_tours=4,
                 time_control=None,
                 description=None,
                 players=None,
                 list_of_tours=[],
                 tournament_id=None
                 ):

        self.tournament_name = tournament_name
        self.locality = locality
        self.tournament_date = tournament_date
        self.number_tours = number_tours
        self.time_control = time_control
        self.description = description
        self.players = players
        self.list_of_tours = list_of_tours
        self.tournament_id = tournament_id

    def serialized_tournament(self):
        """Return serialized tournament info"""
        return {
            "tournament_name": self.tournament_name,
            "locality": self.locality,
            "tournament_date": self.tournament_date,
            "number_tours": self.number_tours,
            "time_control": self.time_control,
            "description": self.description,
            "players": self.players,
            "list_of_tours": self.list_of_tours,
            "tournament_id": self.tournament_id,
        }

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
        list_all_players = self.sort_players_by_score()
        print(list_all_players)
        half = int(len(list_all_players) / 2)
        first_list = list_all_players[half:]
        second_list = list_all_players[:half]
        round_1 = list(zip(first_list, second_list))
        self.list_of_tours = round_1

        return self.list_of_tours


class Tour:

    """
    Chaque tour est une liste de matchs. Chaque match consiste en une paire de joueurs
    avec un champ de résultats pour chaque joueur. Lorsqu'un tour est terminé,
    le gestionnaire du tournoi saisit les résultats de chaque match avant de
    générer les paires suivantes.
    Les instances de tour doivent être stockées dans une liste sur l'instance
    de tournoi à laquelle elles appartiennent.

    doit Renvoyer l'instance de tour """

    def __init__(self, list_of_match):

        self.list_of_match = list_of_match

    def mettre_jour_score(self):

        for match in self.list_of_match:
            """ faire un match et mettre le score des joueurs qui s'affronte"""
            winner = int(input(" -->"))

            instance_match = Match(match)
            instance_match.run_match(winner)

    def __repr__(self):
        print(f" la liste des match : {self.list_of_match}")


class Match:

    te = []
    """
     Un match unique doit être stocké sous la forme d'un tuple contenant deux listes,
     chacune contenant deux éléments : une référence à une instance de joueur et un score.
     Les matchs multiples doivent être stockés sous forme de liste sur l'instance du tour.
     """

    def __init__(self, players=None):
        """un tuple de deux joueurs"""
        self.players = players
        self.t = ()

    def run_match(self, vainqueur=None):

        if vainqueur == 0:

            self.players[0]['tournament_score'] += 1/2
            self.players[1]['tournament_score'] += 1/2
            self.t = (self.players[0]['player_id'], self.players[1]['player_id'])
            print((self.players[0]['player_id'], self.players[1]['player_id']))
        else:
            self.players[vainqueur]['tournament_score'] += 1
            print((self.players[0]['player_id'], self.players[1]['player_id']))
            self.t = (self.players[0]['player_id'], self.players[1]['player_id'])

        self.te.append(self.t)
        print(self.te)








