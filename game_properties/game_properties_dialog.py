import sys, os
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from game_properties.UI.game_properties import Ui_Dialog
import json
import shutil


class PropertiesDialog(qtw.QDialog, Ui_Dialog):
    uninstalled_game = qtc.Signal()

    def __init__(self, game, games_dic):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(qtc.Qt.WindowType.FramelessWindowHint)
        # Set a transparent background for the window
        self.setAttribute(qtc.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.fakepb_icon.setDisabled(True)
        self.games_dic = games_dic
        self.game = game


        # Connect close button
        self.pb_close.clicked.connect(self.close)
        self.pb_cancel.clicked.connect(self.close)
        self.pb_min.clicked.connect(self.showMinimized)
        self.pushButton.clicked.connect(self.uninstall_game)

        # Enable dragging by setting mouse event handlers on title bar
        self.drag_pos = None
        self.f_titlebar.mousePressEvent = self.start_drag
        self.f_titlebar.mouseMoveEvent = self.drag_window

        # TEMP SETUP
        self.le_name.setDisabled(True)
        self.le_exe.setDisabled(True)
        self.le_dir.setDisabled(True)
        self.pb_ok.hide()

        # POPULATE FIELDS
        self.le_name.setText(game.get('name'))
        self.game_dir = os.path.abspath(game.get('directory'))
        self.le_dir.setText(self.game_dir)
        self.le_exe.setText(game.get('exe'))

    def uninstall_game(self):
        if os.path.exists(self.game_dir):
            if os.path.isfile(self.game_dir):
                os.remove(self.game_dir)
            elif os.path.isdir(self.game_dir):
                shutil.rmtree(self.game_dir)

        # Update the in-memory data
        self.game['status'] = 'Not Installed'

        # Save the updated data to the JSON file
        with open("games.json", "w") as file:
            json.dump(self.games_dic, file, indent=4)

        # Emit the signal to notify MainWindow
        self.uninstalled_game.emit()
        self.close()

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

    window = PropertiesDialog()
    window.show()

    sys.exit(app.exec())