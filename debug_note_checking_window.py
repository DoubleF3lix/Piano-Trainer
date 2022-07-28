from PySide6.QtWidgets import QMainWindow

from ui.debug_note_checking_ui import Ui_NoteDebugWindow


class NoteDebugWindow(QMainWindow):
    def __init__(self, parent=None):
        self.parent = parent

        super().__init__(parent)
        self.ui: Ui_NoteDebugWindow = Ui_NoteDebugWindow()
        self.ui.setupUi(self)

        self.ui.clear_button.clicked.connect(self.clear_button_clicked)
        self.ui.close_button.clicked.connect(self.close)

    def clear_button_clicked(self):
        self.ui.note_debug_display.clear()
