import sys, os
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from UI.main_window import Ui_MainWindow
from menubar import CMenuBar
import json
from testfetch import GameFetch
import subprocess
import threading


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(qtc.Qt.WindowType.FramelessWindowHint)
        # Set a transparent background for the window
        self.setAttribute(qtc.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.fakepb_icon.setDisabled(True)

        # self.tbl_games.horizontalHeader().hide()
        #
        # # Apply shadow effect to the QTableWidget body only
        # shadow_effect = qtw.QGraphicsDropShadowEffect(self)
        # shadow_effect.setBlurRadius(20)
        # shadow_effect.setOffset(0, 0)
        # shadow_effect.setColor(qtg.QColor(0, 0, 0, 230))  # Semi-transparent black
        # self.tbl_games.setGraphicsEffect(shadow_effect)
        #
        # # Show the headers again after the shadow is applied
        #
        # self.tbl_games.horizontalHeader().show()

        # Variable to store the offset position for dragging
        self.drag_pos = None

        with open("games.json", "r") as file:
            self.games_dic = json.load(file)

        # Connect close button
        self.pb_close.clicked.connect(self.close)
        self.pb_min.clicked.connect(self.showMinimized)
        self.cmenubar = CMenuBar(self.mpb_file, self.populate_games, self.games_dic)
        self.pb_launch.clicked.connect(self.launch_mode)
        self.mpb_file.clicked.connect(self.cmenubar.show_menu)

        # Enable dragging by setting mouse event handlers on title bar
        self.f_titlebar.mousePressEvent = self.start_drag
        self.f_titlebar.mouseMoveEvent = self.drag_window

        self.tbl_games.selectionModel().selectionChanged.connect(self.check_status)

        # Disable Editing
        self.tbl_games.setEditTriggers(qtw.QAbstractItemView.EditTrigger.NoEditTriggers)



        self.populate_games(self.games_dic)
        self.downloader = GameFetch(self.tbl_games)

    def check_status(self):
        if self.tbl_games.item(self.tbl_games.currentRow(), 1).text() == 'Not Installed':
            self.pb_launch.setText('Install')
        elif self.tbl_games.item(self.tbl_games.currentRow(), 1).text() == 'Installed':
            self.pb_launch.setText('Launch')
        else:
            self.pb_launch.setText('Install')

    def launch_mode(self):
        if self.pb_launch.text() == 'Install':
            print('game not installed')
            self.install_game()
            # self.tbl_games.setFocus()
        else:
            print('starting game')
            # self.tbl_games.setFocus()
            for game in self.games_dic:
                if game.get('name') == self.tbl_games.item(self.tbl_games.currentRow(), 0).text():
                    game_path = f'"games/{os.path.join('/', game.get('name'), game.get('exe'))}"'
                    subprocess.Popen(game_path, shell=True)

    def install_game(self):
        if self.tbl_games.item(self.tbl_games.currentRow(), 1).text() != 'Installed':

            for game in self.games_dic:

                def update_games(download_success, game, row):
                    if download_success:
                        os.remove(os.path.abspath('./games/game.zip'))
                        game["status"] = "Installed"
                        print('Installed')
                        with open("games.json", "w") as file:
                            json.dump(self.games_dic, file, indent=4)


                        self.populate_games(self.games_dic)
                    else:
                        if os.path.exists(os.path.abspath('./games/game.zip')):
                            os.remove(os.path.abspath('./games/game.zip'))
                        self.tbl_games.item(row, 1).setText("ERROR")

                if game.get('name') == self.tbl_games.item(self.tbl_games.currentRow(), 0).text():
                    print(game)
                    print('DOWNLOADING')
                    self.tbl_games.item(self.tbl_games.currentRow(), 1).setText("Connecting...")
                    self.tbl_games.item(self.tbl_games.currentRow(), 1).setForeground(qtg.QColor(196, 181, 80))

                    row = self.tbl_games.currentRow()
                    download_thread = threading.Thread(target=lambda: update_games(self.downloader.download_file(game.get('source'), './games/game.zip', row), game, row))
                    download_thread.start()

                    # update_thread = threading.Thread(target=update_games, args=(download_thread, game))
                    # # self.downloader.download_file(game.get('source'), game.get('exe'))
                    # update_thread.start()

    def populate_games(self, games):
        self.tbl_games.setRowCount(0)
        self.tbl_games.setColumnWidth(0, 160)
        self.tbl_games.setColumnWidth(1, 135)
        # TODO check if the executable is in the right place to determine install status
        for game in games:
            row_position = self.tbl_games.rowCount()  # Get the current row count to append at the end
            self.tbl_games.insertRow(row_position)  # Insert a new empty row

            row_data = [game.get('name'), game.get('status'), game.get('year'), game.get('developer')]
            for col, data in enumerate(row_data):
                self.tbl_games.setItem(row_position, col, qtw.QTableWidgetItem(data))

            icon = qtg.QIcon()
            pixmap = qtg.QPixmap(game.get('icon'))
            icon.addPixmap(pixmap, qtg.QIcon.Mode.Normal)
            icon.addPixmap(pixmap, qtg.QIcon.Mode.Selected)
            self.tbl_games.item(row_position, 0).setIcon(icon)

            if row_data[1] == 'Not Installed':
                for col in range(self.tbl_games.columnCount()-1):
                    cell = self.tbl_games.item(row_position, col)
                    cell.setForeground(qtg.QColor(121, 126, 121))

    def start_drag(self, event):
        if event.button() == qtc.Qt.MouseButton.LeftButton:
            # Store the initial position for dragging
            self.drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def drag_window(self, event):
        if self.drag_pos and event.buttons() == qtc.Qt.MouseButton.LeftButton:
            # Calculate the new position
            new_pos = event.globalPosition().toPoint() - self.drag_pos
            self.move(new_pos)
            event.accept()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
