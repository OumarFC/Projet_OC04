import os
from models.players import Player
from models.tours import Tour
from tinydb import TinyDB
import copy
from operator import attrgetter
import time


data_path = f'{os.getcwd()}\\data\\'


class Tournament:

    MATCH_IN_TOURNAMENT = []

    def __init__(self, tournament_name=None,
                 locality=None,
                 tournament_date=None,
                 number_of_tours=4,
                 time_control=None,
                 description=None,
                 players_id=[],
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
            "tournament_id": self.tournament_id
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
        return Tournament(tournament_name, locality, tournament_date,
                          number_of_tours, time_control, description, players_id, tournament_id)

    def save_tournament_db(self):
        """add new Tournament to database and Set tournament_id to doc id """
        tournament_db = self.data_tournament
        self.tournament_id = tournament_db.insert(self.serialized_tournament())
        tournament_db.update({'tournament_id': self.tournament_id}, doc_ids=[int(self.tournament_id)])

    def sort_players_by_rank(self):
        """Sort players by rank """
        player = Player()
        list_players = player.load_player_db()
        players_by_rank = sorted(list_players, key=lambda x: x.get('rank'))

        list_all_players_objet = []
        for one_player in players_by_rank:
            list_all_players_objet.append(player.unserialized_player(one_player))
        return list_all_players_objet

    def sort_players_by_score(self):
        """Sort players by score"""
        player = Player()
        list_players = player.load_player_db()
        players_by_score = sorted(list_players, key=lambda x: x.get('tournament_score'), reverse=True)

        list_all_players_objet = []
        for one_player in players_by_score:
            list_all_players_objet.append(player.unserialized_player(one_player))

        return list_all_players_objet

    def generate_first_pairs_players(self, objet_tournament):
        """ return a list of players sorted by ranking"""
        self.player = Player()
        sorted_players = []
        players_instances = []
        list_of_first_tours = []
        for id in objet_tournament.players_id:
            player = self.player.data_players.get(doc_id=id)
            player = self.player.unserialized_player(player)
            players_instances.append(player)
        for player in players_instances:
            player_1 = player
            index_player_1 = players_instances.index(player)
            if index_player_1 + len(objet_tournament.players_id) / 2 < len(objet_tournament.players_id):
                index_player_2 = index_player_1 + int(len(objet_tournament.players_id) / 2)
                player_2 = players_instances[index_player_2]
                sorted_players.append(player_1)
                sorted_players.append(player_2)
                list_of_first_tours.append((player_1, player_2))
                self.MATCH_IN_TOURNAMENT.append({player_1.player_id, player_2.player_id})
            else:
                pass
        return list_of_first_tours

    def generate_others_pairs_players(self, list_of_finished_matchs):
        """ return a list of players sorted by score"""
        self.player = Player()
        self.tour = Tour()
        players = []
        plaers_sorted_add = []
        players_instance = []
        get_valid_match = set()
        list_of_others_tours = []
        for match in list_of_finished_matchs:
            for player in match:
                players.append(player)
        sorted_score_players = copy.copy(players)
        for player in sorted_score_players:
            plaers_sorted_add.append(player[0])
        sorted_score_players.clear()
        for player_id in plaers_sorted_add:
            player = self.player.data_players.get(doc_id=player_id)
            players_instance.append(self.player.unserialized_player(player))

        # Sort players by score, if score are equals, sort by rank.
        players_instance.sort(key=attrgetter("tournament_score", 'rank'), reverse=True)
        for player_1 in players_instance:
            if player_1 in sorted_score_players:
                continue
            else:
                try:
                    player_2 = players_instance[players_instance.index(player_1) + 1]
                except Exception:
                    break
            get_valid_match.add(player_1.player_id)
            get_valid_match.add(player_2.player_id)

            while get_valid_match in self.MATCH_IN_TOURNAMENT:  # compare match_to_try with matchs already played
                print(f"Attention (!)  Match dejà joué : {player_1.player_id} CONTRE {player_2.player_id}")
                time.sleep(1)
                get_valid_match.remove(player_2.player_id)
                try:
                    player_2 = players_instance[players_instance.index(player_2) + 1]
                except Exception:
                    break
                get_valid_match.add(player_2)
                continue
            else:
                print(f"Ajout du match {player_1.player_id} CONTRE {player_2.player_id}")
                list_of_others_tours.append((player_1, player_2))
                sorted_score_players.append(player_1.player_id)
                sorted_score_players.append(player_2.player_id)
                players_instance.pop(players_instance.index(player_2))
                self.MATCH_IN_TOURNAMENT.append({player_1.player_id, player_2.player_id})
                get_valid_match.clear()
                time.sleep(1)

        return list_of_others_tours
