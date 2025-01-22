import sys, os
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from UI.main_window import Ui_MainWindow
from game_properties.game_properties_dialog import PropertiesDialog

from menubar import CMenuBar
import json
from gamefetch import GameFetch
import subprocess
import threading


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(qtc.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(qtc.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.fakepb_icon.setDisabled(True)

        # RESIZING
        # self.setMaximumSize(800,490)
        # self.gripSize = 16
        #
        # self.grips = []
        # for i in range(4):
        #     grip = qtw.QSizeGrip(self)
        #     grip.resize(self.gripSize, self.gripSize)
        #     opacity_effect = qtw.QGraphicsOpacityEffect(grip)
        #     opacity_effect.setOpacity(0.0)  # Makes the grip invisible but functional
        #     grip.setGraphicsEffect(opacity_effect)
        #     self.grips.append(grip)
        # RESIZING

        # OLD ATTEMPT FOR HEADER

        # self.tbl_games.horizontalHeader().hide()

        # Apply shadow effect to the QTableWidget body only
        # shadow_effect = qtw.QGraphicsDropShadowEffect(self)
        # shadow_effect.setBlurRadius(20)
        # shadow_effect.setOffset(5, 0)
        # shadow_effect.setColor(qtg.QColor(0, 0, 0, 230))  # Semi-transparent black
        # self.tbl_games.setGraphicsEffect(shadow_effect)

        # Show the headers again after the shadow is applied

        # self.tbl_games.horizontalHeader().show()

        # Variable to store the offset position for dragging
        self.drag_pos = None

        with open("games.json", "r") as file:
            self.games_dic: dict = json.load(file)

        # Connect close button
        self.pb_close.clicked.connect(self.close)
        self.pb_min.clicked.connect(self.showMinimized)
        self.cmenubar = CMenuBar(self.populate_games, self.games_dic)
        self.pb_launch.clicked.connect(self.launch_mode)
        self.mpb_help.clicked.connect(lambda: self.cmenubar.show_debugmenu(self.mpb_help))
        self.mpb_file.clicked.connect(lambda: self.cmenubar.show_filemenu(self.mpb_file))

        self.pb_properties.clicked.connect(self.open_properties)

        # Enable dragging by setting mouse event handlers on title bar
        self.f_titlebar.mousePressEvent = self.start_drag
        self.f_titlebar.mouseMoveEvent = self.drag_window

        self.tbl_games.selectionModel().selectionChanged.connect(self.check_status)

        # Disable Editing
        self.tbl_games.setEditTriggers(qtw.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.populate_games(self.games_dic)
        self.downloader = GameFetch(self.tbl_games)

    def check_status(self):

        status_col = self.tbl_games.item(self.tbl_games.currentRow(), 1).text().strip()
        self.pb_launch.setMinimumHeight(30)
        self.pb_launch.setMaximumHeight(300)
        self.pb_properties.setMinimumHeight(30)
        self.pb_properties.setMaximumHeight(300)

        self.pb_properties.setStyleSheet('''
            QPushButton {
                background-image: url(:/buttons/buttons/properties_button.png);
                background-position: center; /* Center the image */
                background-repeat: no-repeat; /* Prevent tiling */
                border: none; /* Remove button borders to match the image */
                color: rgba(255, 255, 255, 0);
            }
            QPushButton:hover {
                background-image: url(:/buttons/buttons/properties_button_hover.png);
                background-position: center; /* Center the image */
                background-repeat: no-repeat; /* Prevent tiling */
                border: none; /* Remove button borders to match the image */
                color: rgba(255, 255, 255, 0);
            }
            QPushButton:pressed {
                background-image: url(:/buttons/buttons/properties_button_pushed.png);
                background-position: center; /* Center the image */
                background-repeat: no-repeat; /* Prevent tiling */
                border: none; /* Remove button borders to match the image */
                color: rgba(255, 255, 255, 0);
            }
        
        ''')

        if status_col == 'Not Installed':

            self.pb_properties.setDisabled(True)

            self.pb_launch.setDisabled(False)
            self.pb_launch.setText('Install')
            self.pb_launch.setStyleSheet('''
            QPushButton {
                background-image: url(:/buttons/buttons/install_button.png);
                background-position: center; /* Center the image */
                background-repeat: no-repeat; /* Prevent tiling */
                border: none; /* Remove button borders to match the image */
                color: rgba(255, 255, 255, 0);
            }
            QPushButton:hover {
                background-image: url(:/buttons/buttons/install_button_hover.png);
                background-position: center; /* Center the image */
                background-repeat: no-repeat; /* Prevent tiling */
                border: none; /* Remove button borders to match the image */
                color: rgba(255, 255, 255, 0);
            }
            QPushButton:pressed {
                background-image: url(:/buttons/buttons/install_button_pushed.png);
                background-position: center; /* Center the image */
                background-repeat: no-repeat; /* Prevent tiling */
                border: none; /* Remove button borders to match the image */
                color: rgba(255, 255, 255, 0);
            }
            ''')
        elif status_col == 'Installed':

            self.pb_properties.setDisabled(False)

            self.pb_launch.setDisabled(False)
            self.pb_launch.setText('Launch')
            self.pb_launch.setStyleSheet('''
            QPushButton {
                background-image: url(:/buttons/buttons/launch_button.png);
                background-position: center; /* Center the image */
                background-repeat: no-repeat; /* Prevent tiling */
                border: none; /* Remove button borders to match the image */
                color: rgba(255, 255, 255, 0);
            }
            QPushButton:hover {
                background-image: url(:/buttons/buttons/launch_button_hover.png);
                background-position: center; /* Center the image */
                background-repeat: no-repeat; /* Prevent tiling */
                border: none; /* Remove button borders to match the image */
                color: rgba(255, 255, 255, 0);
            }
            QPushButton:pressed{
                background-image: url(:/buttons/buttons/launch_button_pressed.png);
                background-position: center; /* Center the image */
                background-repeat: no-repeat; /* Prevent tiling */
                border: none; /* Remove button borders to match the image */
                color: rgba(255, 255, 255, 0);
            }

            ''')
        elif status_col.startswith('Downloaded') or status_col.startswith('Installing'):
            self.pb_launch.setDisabled(True)
        else:
            self.pb_launch.setDisabled(False)
            self.pb_launch.setText('Install')
            self.pb_launch.setStyleSheet('''
            QPushButton {
                background-image: url(:/buttons/buttons/install_button.png);
                background-position: center; /* Center the image */
                background-repeat: no-repeat; /* Prevent tiling */
                border: none; /* Remove button borders to match the image */
                color: rgba(255, 255, 255, 0);
            }
            ''')

    def launch_mode(self):
        if self.tbl_games.currentRow() != -1:
            print(self.tbl_games.currentRow())
            if self.pb_launch.text() == 'Install':
                print('game not installed')
                if not threading.active_count() >= 2:
                    self.install_game()
                # TODO make the install button unusable as soon as pressing (not on reselection)
                else:
                    # TODO implement multi downloading
                    self.tbl_games.item(self.tbl_games.currentRow(), 1).setText("Install already in progress!")
                self.tbl_games.clearSelection()
            else:
                print('starting game')
                # self.tbl_games.setFocus()
                for game in self.games_dic:
                    if game.get('name') == self.tbl_games.item(self.tbl_games.currentRow(), 0).text():
                        # game_path = f'"games/{os.path.join('/', game.get('name'), game.get('exe'))}"'
                        game_path = os.path.join(game.get('directory'), game.get('exe'))
                        print(game_path)
                        subprocess.Popen(os.path.abspath(game_path), shell=True)

    def install_game(self):
        if self.tbl_games.item(self.tbl_games.currentRow(), 1).text() != 'Installed':

            for game in self.games_dic:

                def update_games(download_success, game, row):

                    if download_success:
                        print(game)
                        game["status"] = "Installed"
                        with open("games.json", "w") as file:
                            json.dump(self.games_dic, file, indent=4)
                        print('Installed')
                        self.populate_games(self.games_dic)

                if game.get('name') == self.tbl_games.item(self.tbl_games.currentRow(), 0).text():
                    print(game)
                    self.tbl_games.item(self.tbl_games.currentRow(), 1).setText("Connecting...")
                    # TODO make the foreground active on focus
                    self.tbl_games.item(self.tbl_games.currentRow(), 1).setForeground(qtg.QColor(196, 181, 80))

                    row = self.tbl_games.currentRow()
                    source = game.get('source')
                    is_mod = game.get('isMod')
                    download_thread = threading.Thread(target=lambda: update_games(self.downloader.download_file(source, is_mod, row), game, row))

                    download_thread.start()
                    break

    def populate_games(self, games):
        self.tbl_games.setRowCount(0)
        self.tbl_games.setColumnWidth(0, 210)
        self.tbl_games.setColumnWidth(1, 160)
        self.tbl_games.setColumnWidth(2, 100)
        self.tbl_games.setColumnWidth(3, 60)

        for game in games:
            row_position = self.tbl_games.rowCount()  # Get the current row count to append at the end
            self.tbl_games.insertRow(row_position)  # Insert a new empty row

            # Check if game executable is installed
            game_path = os.path.join(game.get('directory'), game.get('exe'))

            if not os.path.exists(game_path):
                game['status'] = 'Not Installed'
                print(f'Game {game.get('name')} is not installed');
                with open("games.json", "w") as file:
                    json.dump(self.games_dic, file, indent=4)

            # Fetch game data
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
        # self.tbl_games.sortByColumn(0, qtc.Qt.SortOrder.AscendingOrder)

    def open_properties(self):
        # TODO remake the properties dialog
        # Uninstalling a game
        if self.tbl_games.currentRow() != -1:
            name_col = self.tbl_games.item(self.tbl_games.currentRow(), 0).text().strip()
            for game in self.games_dic:
                if name_col == game.get('name'):
                    dialog = PropertiesDialog(game, self.games_dic)
                    dialog.uninstalled_game.connect(lambda: self.populate_games(self.games_dic))

                    # Restrict clicking uninstall during installation
                    if self.tbl_games.item(self.tbl_games.currentRow(), 1).text().strip().startswith('Downloaded'):
                        dialog.pushButton.hide()

                    dialog.show()
                    break

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

    # TODO add resize nudge
    # RESIZING
    # def resizeEvent(self, event):
    #     qtw.QWidget.resizeEvent(self, event)
    #     rect = self.rect()
    #     # top left grip doesn't need to be moved...
    #     # top right
    #     self.grips[1].move(rect.right() - self.gripSize, 0)
    #     # bottom right
    #     self.grips[2].move(
    #         rect.right() - self.gripSize, rect.bottom() - self.gripSize)
    #     # bottom left
    #     self.grips[3].move(0, rect.bottom() - self.gripSize)
    # RESIZING


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
