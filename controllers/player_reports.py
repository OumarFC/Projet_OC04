from operator import attrgetter
from views.menu import LoadMenus
from controllers import main_controllers
from models import players
from views import views


class PlayerReports:

    def __call__(self):
        self.menu = LoadMenus()
        self.display_player = views.DisplayPlayersReport()
        self.player = players.Player()
        self.players_db = self.player.data_players
        player_serialized = []
        self.menu_control = main_controllers.HomeMenuController()

        for player in self.players_db:
            player_serialized.append(self.player.unserialized_player(player))

        self.display_player()
        entry = str(LoadMenus.load_menu(LoadMenus.player_report_menu()))

        if entry == "1":
            player_serialized.sort(key=attrgetter("last_name"))
            self.display_player.display_by_alphabetical(player_serialized)
            PlayerReports.__call__(self)
        if entry == "2":
            player_serialized.sort(key=attrgetter("rank"))
            self.display_player.display_by_rank(player_serialized)
            PlayerReports.__call__(self)

        if entry == "3":
            self.menu_control()
