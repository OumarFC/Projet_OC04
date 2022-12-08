from models.matchs import Match


class Tour:

    def __init__(self, name=None, begin_time=None, end_time=None, list_match_finished=None):
        self.name = name
        self.begin_time = begin_time
        self.end_time = end_time
        self.list_match_finished = list_match_finished
        self.list_of_match = []

    def serialize_tour(self):
        """Return serialized info for round """
        return {
            "name": self.name,
            "begin_time": self.begin_time,
            "end_time": self.end_time,
            "list_match_finished": self.list_match_finished
        }

    @staticmethod
    def deserialized_tour(serialized_tour):
        name = serialized_tour["name"],
        begin_time = serialized_tour["begin_time"],
        end_time = serialized_tour["end_time"]
        list_match_finished = serialized_tour["list_match_finished"]

        return Tour(name, begin_time, end_time, list_match_finished)

    def valid_winner(self):

        winner = None
        valid_win = False
        while not valid_win:
            print("Saisissez L'ID du joueur vainqueur:")
            print("[0] - Joueur 1 est gagnant")
            print("[1] - Joueur 2 est gagnant")
            print("[2] - Egalité joueur 1 et joueur 2")
            winner = int(input("--->"))
            if winner in [1, 2, 0]:
                valid_win = True
            else:
                print("Vous devez saisir une valeur entre 0, 1 ou 2")

        return winner

    def update_score(self, list_of_match):

        for match in list_of_match:

            """ make a match and put the score of the players who competed"""
            winner = self.valid_winner()

            instance_match = Match(match)
            print(instance_match.__str__())
            instance_match.run_match(winner)
