import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from UI.main_window import Ui_MainWindow
from menubar import CMenuBar

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

        # Connect close button
        self.pb_close.clicked.connect(self.close)
        self.pb_min.clicked.connect(self.showMinimized)
        self.cmenubar = CMenuBar(self.mpb_file)
        self.mpb_file.clicked.connect(self.cmenubar.show_menu)

        # Enable dragging by setting mouse event handlers on title bar
        self.f_titlebar.mousePressEvent = self.start_drag
        self.f_titlebar.mouseMoveEvent = self.drag_window

        # Disable Editing
        self.tbl_games.setEditTriggers(qtw.QAbstractItemView.EditTrigger.NoEditTriggers)

        row_position = self.tbl_games.rowCount()  # Get the current row count to append at the end
        self.tbl_games.insertRow(row_position)  # Insert a new empty row
        row_data = ["Added Game", "Installed", "1999", "Blizzard"]
        for col, data in enumerate(row_data):
            self.tbl_games.setItem(row_position, col, qtw.QTableWidgetItem(data))

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
