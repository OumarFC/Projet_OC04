
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
        self.players_values = [ self.player.prompt_player_id(),
                           self.player.prompt_first_name(),
                           self.player.prompt_last_name(),
                           self.player.prompt_date_of_birth(),
                           self.player.prompt_gender(),
                           self.player.prompt_rank(),
                           self.player.prompt_tournament_score()
        ]
        return self.players_values

    def add_players(self):
        """Add players to database json and return list of players"""
        self.nbj = 2
        for nb in range(0, self.nbj):
            self.created_players = self.create_one_player()
            player = Player(
                player_id=self.created_players[0],
                first_name=self.created_players[1],
                last_name=self.created_players[2],
                date_of_birth=self.created_players[3],
                gender=self.created_players[4],
                rank=self.created_players[5],
                tournament_score=self.created_players[6]
            )
            player.save_player_db()


class TournamentController:

    def __init__(self):

        self.tournament_values = []

    def create_one_tournament(self):

        self.tournament = Tournament()
        self.tournament_values = [
                self.tournament.prompt_tournament_name(),
                self.tournament.prompt_tournament_locality(),
                self.tournament.prompt_tournament_date(),
                self.tournament.prompt_tournament_time_control(),
                self.tournament.prompt_tournament_description(),
                 self.tournament.prompt_tournament_id()
        ]
        return self.tournament_values

    def add_tournament(self):
        """Add Tournament to database json and return list of tournament"""
        self.nbt = 1
        for nb in range(0, self.nbt):
            self.created_tournament= self.create_one_tournament()
            tournament = Tournament(
                tournament_name=self.created_tournament[0],
                locality=self.created_tournament[1],
                tournament_date=self.created_tournament[2],
                number_of_tours=4,
                time_control=self.created_tournament[3],
                description=self.created_tournament[4],
                tournament_id = self.created_tournament[5]
            )
            tournament.save_tournament_db()

    def run_tournament(self):
        """Creer le premier tour et mettre à jour le score des joueurs"""
        tour_ids_in_match =[]
        tournament = Tournament()
        first_list_tour = tournament.generate_first_pairs_players()
        first_tour = Tour(list_of_match=first_list_tour)
        first_tour.mettre_jour_score()
        tournament.list_of_tours.append(Match.list_match_finiched)
        print(tournament.list_of_tours)

        Match.list_match_finiched = []

        for i in range(2, tournament.number_of_tours + 1):
            print( "Roud" + str(i) + ": ---- The Others Round in Tourny  ---- ")
            others_list_tour = tournament.generate_others_pairs_players()
            other_tour = Tour(list_of_match=others_list_tour)
            other_tour.mettre_jour_score()
            tournament.list_of_tours.append(Match.list_match_finiched)
            Match.list_match_finiched = []
            print(tournament.list_of_tours)









control = TournamentController()
control.run_tournament()

#control.save_tournament_statement(obj)

















