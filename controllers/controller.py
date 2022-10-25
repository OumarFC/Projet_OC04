
from models.players import Player
from models.tournaments import Tournament, Tour, Match
from itertools import combinations
from numpy import array_split
import numpy as np

class PlayerController:

    def __init__(self):
        self.players_values = []
        self.created_players = []

    def create_one_player(self):
        self.player = Player()
        self.player.prompt_player_id()
        self.player.prompt_first_name()
        self.player.prompt_last_name()
        self.player.prompt_date_of_birth()
        self.player.prompt_gender()
        self.player.prompt_rank()
        self.player.prompt_tournament_score()

        return self.player

    def add_players(self):
        """Add players to database json and return list of players"""
        self.nbj = 2
        for nb in range(0, self.nbj):
            self.players_values.append(self.create_one_player())

        player = Player(
            player_id=self.players_values[0],
            first_name=self.players_values[1],
            last_name=self.players_values[2],
            date_of_birth=self.players_values[3],
            gender=self.players_values[4],
            rank=self.players_values[5],
            tournament_score=self.players_values[6]
        )
        player.save_player_db()

        return self.players_values

    def control_tournament(self):
        """Creer le premier tour et mettre à jour le score des joueurs"""

        tournament = Tournament()
        first_list_tour = tournament.generate_first_pairs_players()
        #print(first_list_tour)

        first_tour = Tour(first_list_tour)
        first_tour_score = first_tour.mettre_jour_score()
        players_ids_in_match = Match.te

        player = Player()
        all_players = player.load_player_db()
        all_possible_matches = [match for match in combinations(all_players, 2)]

        all_ids_players = []
        for i in range(len(all_players)):
            all_ids_players.append(all_players[i]["player_id"])
        all_ids_combinations = [player_ids for player_ids in combinations(all_ids_players, 2)]
        

        old = all_ids_combinations
        new = players_ids_in_match



"""test """
control = PlayerController()
control.control_tournament()


"""
my_list_ids = [(a, b) for (a, b) in all_ids_combinations for (c, d) in players_ids_in_match if (a == c) and (b == d) or (a == d) and (b == c)]

list_a_rejouer = []
for i in all_ids_combinations:
    if not i in my_list_ids:
        list_a_rejouer.append(i)
print("Match : ", list_a_rejouer)
"""
"""
    else:
      list_a_rejouer.append(i)
    print("Mismatch : ", list_a_rejouer)
    """
"""


#round = list(zip(np.array(even_index), np.array(odd_index)))
#print(round)


#others_possible_matches = set(all_possible_matches) - set(first_list_tour)
#print(all_possible_matches)
#print(first_list_tour)

"""










