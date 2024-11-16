import os, shutil, sys

from PySide6.QtWidgets import QMenu
import json

class CMenuBar:
    def __init__(self, button, reset_games, game_dic):
        self.button = button
        self.reset_games = reset_games
        self.game_dic = game_dic

    # TODO implement show_filemenu, show_editmenu, show_gamesmenu, show_helpmenu with related methods
    def show_menu(self):
        # TODO create menu in __init__
        # Create a menu
        menu = QMenu()

        # Add actions to the menu
        option1 = menu.addAction("Reset Games")
        option2 = menu.addAction("Uninstall all games")
        option3 = menu.addAction("Option 3")

        # Connect actions to methods
        option1.triggered.connect(self.option1)
        option2.triggered.connect(self.option2)
        option3.triggered.connect(self.option3)

        # Show the menu at the position of the button
        menu.exec_(self.button.mapToGlobal(self.button.rect().bottomLeft()))

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