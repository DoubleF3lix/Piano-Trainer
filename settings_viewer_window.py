from __future__ import annotations

import typing

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow

from ui.settings_viewer_ui import Ui_SettingsViewer

if typing.TYPE_CHECKING:
    from debug_window import DebugWindow


class SettingsViewerWindow(QMainWindow):
    def __init__(self, pseudo_parent: DebugWindow = None):
        self.pseudo_parent: DebugWindow = pseudo_parent

        super().__init__()
        self.ui: Ui_SettingsViewer = Ui_SettingsViewer()
        self.ui.setupUi(self)

        self.timer = QTimer()
        self.timer.setInterval(3000)
        self.timer.timeout.connect(self.update_settings_display)
        self.timer.start()

    def update_settings_display(self):
        old_scrollbar_value = self.ui.settings_display.verticalScrollBar().value()
        self.ui.settings_display.setText(
            self.pseudo_parent.pseudo_parent.parent.FileAccessAPI.load_settings(
                as_string=True
            )
        )
        self.ui.settings_display.verticalScrollBar().setValue(old_scrollbar_value)
