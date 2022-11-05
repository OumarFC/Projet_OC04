
from tinydb import TinyDB
chmin_data = 'C:/Users/Itec Global Services/PycharmProjects/Projet_OC04/data/'


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

        self.data_players = TinyDB(chmin_data + 'player.json')

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

    def prompt_first_name(self):
        valid_first_name = False
        while not valid_first_name:
            first_name = input("Saisissez un nom: ")
            if first_name != "":
                valid_first_name = True
            else:
                print("Vous devez saisir un nom")

        return first_name

    def prompt_last_name(self):
        valid_last_name = False
        while not valid_last_name:
            last_name = input("Saisissez un prenom : ")
            if last_name != "":
                valid_last_name = True
            else:
                print("Vous devez saisir un prenom")

        return last_name

    def prompt_date_of_birth(self):
        valid_date_of_birth = False
        while not valid_date_of_birth:
            date_of_birth = input("Saisissez une date de naissance (JJ/MM/AAAA) : ")
            if date_of_birth != "" and str('/') in date_of_birth and len(date_of_birth) == 10:
                valid_date_of_birth = True
            else:
                print("Vous devez saisir une date de naissance valide")

        return date_of_birth

    def prompt_gender(self):
        valid_gender = False
        while not valid_gender:
            gender = input("Saisissez un genre ( H ou F ) : ")
            if gender != "" and gender in "H F":
                valid_gender = True
            else:
                print("Vous devez saisir un genre Valide")

        return gender

    def prompt_rank(self):
        valid_rank = False
        while not valid_rank:
            rank = input("Saisissez le Classement  : ")
            if rank.isdigit() and rank != "" and int(rank) >= 0:
               valid_rank = True
            else:
                print("Vous devez saisir un classement valide")

        return rank

    def prompt_tournament_score(self):
        valid_tournament_score = False
        while not valid_tournament_score:
            tournament_score = input("Saisissez le score  : ")
            if tournament_score.isdigit() and tournament_score != "" and int(tournament_score) >= 0:
               valid_tournament_score = True
            else:
                print("Vous devez saisir un score valide")

        return tournament_score

    def prompt_player_id(self):
        valid_player_id = False
        while not valid_player_id:
            player_id = input("Saisissez l'Id : ")
            if player_id.isdigit() and player_id != "" and int(player_id) >= 0:
               valid_player_id = True
            else:
                print("Vous devez saisir un id valide")

        return player_id

    def load_player_db(self):
        """Load player database and return: list of players"""
        players_db = TinyDB(chmin_data + 'player.json')
        players_db.all()
        players = []
        for item in players_db:
            players.append(item)

        return players


