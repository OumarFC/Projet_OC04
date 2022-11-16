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

    @staticmethod
    def update_score(list_of_match):

        for match in list_of_match:
            """ make a match and put the score of the players who compete"""
            winner = int(input(" Enter Winner Id -->"))

            instance_match = Match(match)
            instance_match.run_match(winner)
