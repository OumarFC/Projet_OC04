from models import players


class PlayerController:

    def __init__(self):
        self.players_values = []
        self.created_players = []

    def create_one_player(self):
        self.player = players.Player()
        self.players_values = [
            self.prompt_player_id(),
            self.prompt_first_name(),
            self.prompt_last_name(),
            self.prompt_date_of_birth(),
            self.prompt_gender(),
            self.prompt_rank(),
            self.prompt_tournament_score()
        ]
        return self.players_values

    def add_players(self):
        """Add players to database json"""
        for nb in [*range(0, 8)]:

            self.created_players = self.create_one_player()
            player = players.Player(
                player_id=self.created_players[0],
                first_name=self.created_players[1],
                last_name=self.created_players[2],
                date_of_birth=self.created_players[3],
                gender=self.created_players[4],
                rank=self.created_players[5],
                tournament_score=self.created_players[6]
            )
            player.save_player_db()

    def prompt_first_name(self):
        first_name = None
        valid_first_name = False
        while not valid_first_name:
            first_name = input("Enter first name: ")
            if first_name != "":
                valid_first_name = True
            else:
                print("You must enter a first name")

        return first_name

    def prompt_last_name(self):
        last_name = None
        valid_last_name = False
        while not valid_last_name:
            last_name = input("Enter last : ")
            if last_name != "":
                valid_last_name = True
            else:
                print("You must enter a last name")

        return last_name

    def prompt_date_of_birth(self):
        date_of_birth = None
        valid_date_of_birth = False
        while not valid_date_of_birth:
            date_of_birth = input("Enter a date of birth like (JJ/MM/AAAA) : ")
            if date_of_birth != "" and str('/') in date_of_birth and len(date_of_birth) == 10:
                valid_date_of_birth = True
            else:
                print("You must enter a valid date of birth")

        return date_of_birth

    def prompt_gender(self):
        gender = None
        valid_gender = False
        while not valid_gender:
            gender = input("Enter gender ( H or F ) : ")
            if gender != "" and gender in "H F":
                valid_gender = True
            else:
                print("You must enter a valid gender")

        return gender

    def prompt_rank(self):
        valid_rank = False
        rank = None
        while not valid_rank:
            rank = input("Enter rank  : ")
            if rank.isdigit() and rank != "" and int(rank) >= 0:
                valid_rank = True
            else:
                print("You must enter a valid rank")

        return rank

    def prompt_tournament_score(self):
        tournament_score = None
        valid_tournament_score = False
        while not valid_tournament_score:
            tournament_score = input("Enter score  : ")
            if tournament_score.isdigit():
                valid_tournament_score = True
            else:
                print("You must enter a valid score")

        return int(tournament_score)

    def prompt_player_id(self):
        player_id = None
        valid_player_id = False
        while not valid_player_id:
            player_id = input("Enter Id : ")
            if player_id.isdigit() and player_id != "" and int(player_id) >= 0:
                valid_player_id = True
            else:
                print("You must enter a valid Id")

        return int(player_id)

    def update_rank(self):

        player = players.Player()
        players_db = player.data_players

        valid_id = False
        while not valid_id:
            player_id = input("Enter player number : ")
            if player_id.isdigit() and int(player_id) <= len(players_db):
                valid_id = True
            else:
                print("You must enter number corresponding to the player")

        player_to_modify = players_db.get(doc_id=int(player_id))
        print(f"Player : {player_to_modify['first_name']} {player_to_modify['last_name']} \n"
              f"Actual rank : {player_to_modify['rank']}")

        valid_rank = False
        while not valid_rank:
            new_rank = input("Enter new rank: ")
            if new_rank.isdigit():
                valid_rank = True
            else:
                print("You must enter a positive integer")

        player_to_modify = players_db.get(doc_id=int(player_id))
        player_to_modify["rank"] = new_rank

        print(f"Player : {player_to_modify['first_name']} {player_to_modify['last_name']} \n"
              f"new rank : {player_to_modify['rank']}")
        players_db.update({"rank": int(new_rank)}, doc_ids=[int(player_id)])
