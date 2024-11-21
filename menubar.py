import os, shutil, sys

from PySide6.QtWidgets import QMenu
import json


class CMenuBar:
    def __init__(self, reset_games, game_dic):
        self.reset_games = reset_games
        self.game_dic = game_dic

    # TODO implement show_filemenu, show_editmenu, show_gamesmenu, show_helpmenu with related methods
    def show_debugmenu(self, button):

        # Create a menu
        menu = QMenu()
        menu.setStyleSheet(self.get_menu_stylesheet())



        # Add actions to the menu
        option1 = menu.addAction("Reset Games")
        option2 = menu.addAction("Uninstall all games")
        option3 = menu.addAction("Option 3")

        # Connect actions to methods
        option1.triggered.connect(self.option1)
        option2.triggered.connect(self.option2)
        option3.triggered.connect(self.option3)

        # Show the menu at the position of the button
        menu.exec_(button.mapToGlobal(button.rect().bottomLeft()))

    def show_filemenu(self, button):

        # Create a menu
        menu = QMenu()
        menu.setStyleSheet(self.get_menu_stylesheet())

        # Add actions to the menu
        backup_action = menu.addAction("Backup games...")
        change_user_action = menu.addAction("Change user...")
        settings_action = menu.addAction("Settings")
        exit_action = menu.addAction("Exit")

        # Connect actions to methods
        backup_action.triggered.connect(lambda: print("Backup games"))
        change_user_action.triggered.connect(lambda: print("Change User"))
        settings_action.triggered.connect(lambda: print("Settings"))
        exit_action.triggered.connect(sys.exit)

        # Show the menu at the position of the button
        menu.exec_(button.mapToGlobal(button.rect().bottomLeft()))

    @staticmethod
    def get_menu_stylesheet():
        # Centralize the stylesheet for consistency
        return '''
            QMenu {
                background-color: #2F312D; /* sets background of the menu */
                border: 3px solid #2F312D;
                border-radius: 5px;
            }
            QMenu::item {
                background-color: transparent;
                font: 700 9pt "Segoe UI";
                color: rgb(216, 222, 211);
                padding: 3px;
            }
            QMenu::item:selected {
                background-color: #958831;
                font: 700 9pt "Segoe UI";
                color: rgb(216, 222, 211);
                padding: 3px;
            }
        '''

    def option1(self):
        print("Option 1 selected")
        self.reset_games(self.game_dic)

    def option2(self):
        print("Option 2 selected")
        for game in self.game_dic:
            game['status'] = 'Not Installed'
        with open("games.json", "w") as file:
            json.dump(self.game_dic, file, indent=4)

        folder = os.path.abspath('./games')
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
        sys.exit()

    def option3(self):
        print("Option 3 selected")