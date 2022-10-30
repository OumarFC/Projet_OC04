
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
        tour_ids_in_match =[]
        tournament = Tournament()
        first_list_tour = tournament.generate_first_pairs_players()
        print(first_list_tour)
        first_tour = Tour(first_list_tour)
        first_tour_score = first_tour.mettre_jour_score()
        tour_ids_in_match.append(Match.list_match_finiched)
        print(tour_ids_in_match)
        Match.list_match_finiched = []

        for i in range(2, tournament.number_of_tours + 1):
            print( "Roud" + str(i) + ": ---- The Others Round in Tourny  ---- ")
            others_list_tour = tournament.generate_others_pairs_players()
            other_tour = Tour(others_list_tour)
            others_tour_score = other_tour.mettre_jour_score()
            others_players_ids_in_match = Match.list_match_finiched
            tour_ids_in_match.append(others_players_ids_in_match)
            print(tour_ids_in_match)
            Match.list_match_finiched = []
        tournament.list_of_tours = tour_ids_in_match
        print(tournament.list_of_tours)


"""test """




control = PlayerController()
control.control_tournament()
















