
from tinydb import TinyDB
data_path = "C:\\Users\\Itec Global Services\\PycharmProjects\\Projet_OC04\\data\\"


class Player:

    def __init__(self, player_id=None, first_name=None,
                 last_name=None,
                 date_of_birth=None,
                 gender=None,
                 rank=None,
                 tournament_score=None
                 ):

        self.player_id = player_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.rank = rank
        self.tournament_score = tournament_score

        self.data_players = TinyDB(data_path + 'player.json')

    def serialize_player(self):
        """Return serialized info for player """
        return {
            "player_id": self.player_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "rank": self.rank,
            "tournament_score": self.tournament_score
        }

    def unserialized_player(self, serialized_player):
        player_id = serialized_player["player_id"]
        first_name = serialized_player["first_name"]
        last_name = serialized_player["last_name"]
        date_of_birth = serialized_player["date_of_birth"]
        gender = serialized_player["gender"]
        rank = serialized_player["rank"]
        tournament_score = serialized_player["tournament_score"]
        return Player(player_id,
                      first_name,
                      last_name,
                      date_of_birth,
                      gender,
                      rank,
                      tournament_score,
                      )

    def save_player_db(self):
        """add new player to database and Set player id to doc id """
        players_db = self.data_players
        self.player_id = players_db.insert(self.serialize_player())
        players_db.update({'player_id': self.player_id}, doc_ids=[int(self.player_id)])

    def load_player_db(self):
        """Load player database and return: list of players"""
        players_db = TinyDB(data_path + 'player.json')
        players_db.all()
        players = []
        for item in players_db:
            players.append(item)

        return players
