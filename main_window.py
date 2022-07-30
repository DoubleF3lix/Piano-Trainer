from PySide6.QtWidgets import QMainWindow

from file_access_api import FileAccessAPI
from settings_window import SettingsWindow
from ui.main_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        self.FileAccessAPI: FileAccessAPI = FileAccessAPI()

        super().__init__()
        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)

        # Buttons
        self.ui.settings_button.clicked.connect(self.settings_button_clicked)
        self.ui.skip_button.clicked.connect(self.skip_button_clicked)

        # Set label text
        # self.ui.tally_label.setText("Hello")
        # self.ui.skips_label.setText("World!")
        # Get label text (should store values in a variable though)
        # self.ui.tally_label.text()
        # self.ui.skips_label.text()

        self.settings_window: SettingsWindow = SettingsWindow(self)

        if self.FileAccessAPI.get_debug_setting("INSTANTLY_OPEN_SETTINGS_WINDOW"):
            self.settings_button_clicked()

        if self.FileAccessAPI.get_debug_setting("INSTANTLY_OPEN_NOTE_DEBUGGER_WINDOW"):
            self.settings_window.debug_window.note_debugger_window.show()

    def settings_button_clicked(self):
        self.settings_window.show()

    def skip_button_clicked(self):
        ...


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
