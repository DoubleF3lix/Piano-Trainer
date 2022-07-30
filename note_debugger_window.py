from __future__ import annotations

import typing

from PySide6.QtWidgets import QMainWindow

if typing.TYPE_CHECKING:
    from debug_window import DebugWindow

from ui.note_debugger_ui import Ui_NoteDebuggerWindow


class NoteDebuggerWindow(QMainWindow):
    def __init__(self, pseudo_parent: DebugWindow = None):
        self.pseudo_parent: DebugWindow = pseudo_parent

        super().__init__()
        self.ui: Ui_NoteDebuggerWindow = Ui_NoteDebuggerWindow()
        self.ui.setupUi(self)
