import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from UI.main_window import Ui_MainWindow


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(qtc.Qt.WindowType.FramelessWindowHint)
        # Set a transparent background for the window
        self.setAttribute(qtc.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.fakepb_icon.setDisabled(True)
        # Variable to store the offset position for dragging
        self.drag_pos = None

        # Connect close button
        self.pb_close.clicked.connect(self.close)
        self.pb_min.clicked.connect(self.showMinimized)
        # Enable dragging by setting mouse event handlers on title bar
        self.f_titlebar.mousePressEvent = self.start_drag
        self.f_titlebar.mouseMoveEvent = self.drag_window

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