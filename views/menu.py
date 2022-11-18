
class LoadMenus:

    @staticmethod
    def main_menu():
        print()
        print(" ---------MENU PRINCIPAL---------------- ")
        print()

        list_menu = [

            "[1] - MENU TOURNOI",
            "[2] - MENU JOUEUR",
            "[3] - QUITTER LE TOURNOI"
        ]
        return list_menu

    @staticmethod
    def player_menu():
        list_player_menu = [
            "[1] - Créer un joueur",
            "[2] - Mettre à jour le classement d'un joueur",
            "[3] - Afficher les rapports des joueurs",
            "[4] - Retour au menu principal"
        ]
        return list_player_menu

    @staticmethod
    def player_report_menu():

        list_player_report_menu = [
            "[1] - Afficher les joeurs par ordre alphabétique",
            "[2] - Afficher les joeurs par ordre de classement",
            "[3] - Retour au menu principal"
        ]
        return list_player_report_menu

    @staticmethod
    def tournament_menu():

        list_tournament_menu = [
            "[1] - Créer un nouveau tournoi",
            "[2] - Ajouter des joueurs au tournoi",
            "[3] - Lancer un tournoi existant",
            "[4] - Afficher les rapports de tournoi",
            "[5] - Retour au menu principal"
        ]
        return list_tournament_menu

    @staticmethod
    def tournament_report_menu():

        list_tournament_report_menu = [
            "[1] - Afficher les tournois",
            "[2] - Afficher les tours d'un tournoi",
            "[3] - Afficher les match des tours",
            "[4] - Retour au menu principal"
        ]
        return list_tournament_report_menu

    @staticmethod
    def time_control_menu():

        list_time_control_menu = [
            "[1] - Bullet",
            "[2] - Blitz",
            "[3] - Coup rapide"
        ]
        return list_time_control_menu

    @staticmethod
    def load_menu(selected_menu):
        """Display a menu and ask the user to choose"""
        for line in selected_menu:
            print(line)
        while True:
            entry = input("-->")
            for line in selected_menu:
                line = line.split("-")[0][1]
                if entry == line:
                    return str(line)
            print("Vous devez entrer le chiffre correspondant")
