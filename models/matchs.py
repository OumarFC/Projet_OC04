
class Match:

    list_match_finished = []

    def __init__(self, players=None):
        """a tuple of players"""
        self.players = players
        self.duel_match = ()

    def __str__(self):
        return f"Match (Joueur : {self.players[0].player_id}) --CONTRE-- Joueur : {self.players[1].player_id}."

    def run_match(self, winner=None):

        if winner == 2:

            self.players[0].tournament_score += 1/2
            self.players[1].tournament_score += 1/2
            self.duel_match = [(self.players[0].player_id, self.players[0].tournament_score),
                               (self.players[1].player_id, self.players[1].tournament_score)]

        elif winner == 0 or winner == 1:

            self.players[winner].tournament_score += 1
            self.duel_match = [(self.players[0].player_id, self.players[0].tournament_score),
                               (self.players[1].player_id, self.players[1].tournament_score)]

        Match.list_match_finished.append(self.duel_match)

