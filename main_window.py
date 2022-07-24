from PySide6.QtWidgets import QMainWindow

from file_access_api import FileAccessAPI
from settings_window import SettingsWindow
from ui.main_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, DEBUG: dict = None):
        self.DEBUG = DEBUG

        self.FileAccessAPI = FileAccessAPI(DEBUG)

        super().__init__()
        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)

        # Menu bar
        self.ui.start_action.triggered.connect(self.start_action_triggered)
        self.ui.stop_action.triggered.connect(self.stop_action_triggered)
        self.ui.reset_action.triggered.connect(self.reset_action_triggered)

        # Buttons
        self.ui.settings_button.clicked.connect(self.settings_button_clicked)
        self.ui.skip_button.clicked.connect(self.skip_button_clicked)

        # Set label text
        # self.ui.tally_label.setText("Hello")
        # self.ui.skips_label.setText("World!")
        # Get label text (should store values in a variable though)
        # self.ui.tally_label.text()
        # self.ui.skips_label.text()

        if self.DEBUG and self.DEBUG["INSTA_OPEN_SETTINGS"]:
            self.settings_button_clicked()

    def start_action_triggered(self):
        print("Start action triggered")

    def stop_action_triggered(self):
        print("Stop action triggered")

    def reset_action_triggered(self):
        print("Reset action triggered")

    def settings_button_clicked(self):
        settings_window: SettingsWindow = SettingsWindow(self)
        settings_window.show()

    def skip_button_clicked(self):
        print("Skip button clicked")


# other lilypond notes:
"""
e
\override NoteHead.color = SeaGreen
\override Stem.color = SeaGreen
g
\revert NoteHead.color
\revert Stem.color
f
"""
# This will make 'g' green, while 'e' and 'f' are black