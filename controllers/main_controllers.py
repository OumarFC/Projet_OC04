import sys
from views import views, menu
from controllers import tournament_controller
from controllers import player_reports
from controllers import player_controller
from controllers import tournament_reports


class HomeMenuController:

    def __init__(self):
        self.create_menu = menu.LoadMenus()
        self.view = views.MainDisplay()
        self.choice_controller = None

    def __call__(self):
        self.view.display_title()
        entry = self.create_menu.load_menu(self.create_menu.main_menu())

        if entry == "1":
            self.choice_controller = TournamentMenuController()
            self.go_to_tournament_menu_controller()
        if entry == "2":
            self.choice_controller = PlayerMenuController()
            self.go_to_player_menu_controller()
        if entry == "3":
            self.choice_controller = QuitAppController()
            self.go_to_quit_app_controller()

    def go_to_tournament_menu_controller(self):
        return self.choice_controller()

    def go_to_player_menu_controller(self):
        return self.choice_controller()

    def go_to_quit_app_controller(self):
        return self.choice_controller()


class TournamentMenuController(HomeMenuController):

    def __init__(self):
        super().__init__()
        self.create_menu = menu.LoadMenus()
        self.create_tournament = tournament_controller.TournamentController()
        self.home_menu_controller = HomeMenuController()
        self.tournament_reports = tournament_reports.TournamentReports()

    def __call__(self):

        entry = self.create_menu.load_menu(self.create_menu.tournament_menu())

        if entry == "1":
            self.choice_controller = self.create_tournament.add_tournament()
        if entry == "2":
            self.choice_controller = self.create_tournament.add_players_id_to_tournament()
        if entry == "3":
            self.choice_controller = self.create_tournament.run_tournament()
        if entry == "4":
            self.choice_controller = self.tournament_reports()
        if entry == "5":
            self.home_menu_controller()


class PlayerMenuController(HomeMenuController):

    def __init__(self):
        super().__init__()
        self.create_menu = menu.LoadMenus()
        self.create_player = player_controller.PlayerController()
        self.home_menu_controller = HomeMenuController()
        self.player_reports = player_reports.PlayerReports()

    def __call__(self):

        entry = self.create_menu.load_menu(self.create_menu.player_menu())

        if entry == "1":
            self.choice_controller = self.create_player.add_players()
        if entry == "2":
            self.choice_controller = self.create_player.update_rank()
        if entry == "3":
            self.choice_controller = self.player_reports()
        if entry == "4":
            self.home_menu_controller()


class QuitAppController:
    def __call__(self):
        sys.exit()
