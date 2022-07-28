from PySide6.QtWidgets import QMainWindow

from ui.debug_window_ui import Ui_DebugWindow


class DebugWindow(QMainWindow):
    def __init__(self, parent=None):

        super().__init__(parent)
        self.ui: Ui_DebugWindow = Ui_DebugWindow()
        self.ui.setupUi(self)

        self.ui.reset_settings_button.clicked.connect(
            self.reset_settings_button_clicked
        )
        self.ui.delete_settings_button.clicked.connect(
            self.delete_settings_button_clicked
        )
        self.ui.fetch_settings_button.clicked.connect(
            self.fetch_settings_button_clicked
        )
        self.ui.open_log_button.clicked.connect(self.open_log_button_clicked)
        self.ui.open_note_debugging_button.clicked.connect(
            self.open_note_debugging_button_clicked
        )
        self.ui.recompile_uis_button.clicked.connect(self.recompile_uis_button_clicked)
        self.ui.save_and_quit_button.clicked.connect(self.save_and_quit_button_clicked)

    def reset_settings_button_clicked(self):
        ...

    def delete_settings_button_clicked(self):
        ...

    def fetch_settings_button_clicked(self):
        ...

    def open_log_button_clicked(self):
        ...

    def open_note_debugging_button_clicked(self):
        ...

    def recompile_uis_button_clicked(self):
        ...

    def save_and_quit_button_clicked(self):
        # self.ui.instantly_open_settings_checkbox.isChecked()
        # self.ui.is_running_python_checkbox.isChecked()
        # self.ui.open_dialog_on_error_checkbox.isChecked()
        ...
