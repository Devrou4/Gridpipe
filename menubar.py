from PySide6.QtWidgets import QMenu


class CMenuBar:
    def __init__(self, button):
        self.button = button

    def show_menu(self):
        # Create a menu
        menu = QMenu()

        # Add actions to the menu
        option1 = menu.addAction("Option 1")
        option2 = menu.addAction("Option 2")
        option3 = menu.addAction("Option 3")

        # Connect actions to methods
        option1.triggered.connect(self.option1)
        option2.triggered.connect(self.option2)
        option3.triggered.connect(self.option3)

        # Show the menu at the position of the button
        menu.exec_(self.button.mapToGlobal(self.button.rect().bottomLeft()))

    def option1(self):
        print("Option 1 selected")

    def option2(self):
        print("Option 2 selected")

    def option3(self):
        print("Option 3 selected")