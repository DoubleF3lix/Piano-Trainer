from __future__ import annotations

import os
import typing

from PySide6.QtWidgets import QMainWindow

if typing.TYPE_CHECKING:
    from settings_window import SettingsWindow

from PySide6.QtGui import QCloseEvent

from note_debugger_window import NoteDebuggerWindow
from settings_viewer_window import SettingsViewerWindow
from ui.debug_ui import Ui_DebugWindow
from ui.designer.compile_uis import compile_uis
from util import make_message_box


class DebugWindow(QMainWindow):
    def __init__(self, pseudo_parent: SettingsWindow = None):
        self.pseudo_parent: SettingsWindow = pseudo_parent

        super().__init__()
        self.ui: Ui_DebugWindow = Ui_DebugWindow()
        self.ui.setupUi(self)

        self.settings_viewer_window = SettingsViewerWindow(self)
        self.note_debugger_window = NoteDebuggerWindow(self)

        self.ui.instantly_open_settings_checkbox.setChecked(
            self.pseudo_parent.parent.FileAccessAPI.get_debug_setting(
                "INSTANTLY_OPEN_SETTINGS_WINDOW"
            )
        )
        self.ui.instantly_open_note_debugger_checkbox.setChecked(
            self.pseudo_parent.parent.FileAccessAPI.get_debug_setting(
                "INSTANTLY_OPEN_NOTE_DEBUGGER_WINDOW"
            )
        )

        self.ui.reset_settings_button.clicked.connect(
            self.reset_settings_button_clicked
        )
        self.ui.delete_settings_button.clicked.connect(
            self.delete_settings_button_clicked
        )
        self.ui.open_settings_viewer_button.clicked.connect(
            self.open_settings_viewer_button_clicked
        )
        self.ui.open_note_debugger_button.clicked.connect(
            self.open_note_debugger_button_clicked
        )
        self.ui.recompile_uis_button.clicked.connect(self.recompile_uis_button_clicked)
        self.ui.create_error_button.clicked.connect(self.create_error_button_clicked)

    def reset_settings_button_clicked(self):
        if os.path.isfile(self.pseudo_parent.parent.FileAccessAPI.settings_file_path):
            self.settings_viewer_window.timer.stop()
            os.remove(self.pseudo_parent.parent.FileAccessAPI.settings_file_path)
        self.pseudo_parent.parent.FileAccessAPI.create_settings_file_if_needed()
        self.settings_viewer_window.timer.start()
        make_message_box("Settings Reset", "Settings have been reset")

    def delete_settings_button_clicked(self):
        self.settings_viewer_window.timer.stop()
        if os.path.isfile(self.pseudo_parent.parent.FileAccessAPI.settings_file_path):
            os.remove(self.pseudo_parent.parent.FileAccessAPI.settings_file_path)
        make_message_box("Settings Deleted", "Settings have been deleted")

    def open_settings_viewer_button_clicked(self):
        self.settings_viewer_window.show()

    def open_note_debugger_button_clicked(self):
        self.note_debugger_window.show()

    def recompile_uis_button_clicked(self):
        compile_uis()
        make_message_box("Compile UIs", "UIs have been recompiled")

    def create_error_button_clicked(self):
        raise RuntimeError(
            "Error created for debugging purposes. The program will now quit."
        )

    def closeEvent(self, event: QCloseEvent):
        self.pseudo_parent.parent.FileAccessAPI.set_debug_setting(
            "INSTANTLY_OPEN_SETTINGS_WINDOW",
            self.ui.instantly_open_settings_checkbox.isChecked(),
        )
        self.pseudo_parent.parent.FileAccessAPI.set_debug_setting(
            "INSTANTLY_OPEN_NOTE_DEBUGGER_WINDOW",
            self.ui.instantly_open_note_debugger_checkbox.isChecked(),
        )
