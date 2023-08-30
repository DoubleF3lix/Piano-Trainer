from __future__ import annotations

import time
import typing

from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem

if typing.TYPE_CHECKING:
    from debug_window import DebugWindow

from ui.note_debugger_ui import Ui_NoteDebuggerWindow
from util import Note


class NoteDebuggerWindow(QMainWindow):
    def __init__(self, pseudo_parent: DebugWindow = None):
        self.pseudo_parent: DebugWindow = pseudo_parent

        super().__init__()
        self.ui: Ui_NoteDebuggerWindow = Ui_NoteDebuggerWindow()
        self.ui.setupUi(self)

        self.ui.note_debugger_display.header().resizeSection(0, 125)

    # Order is time, expected note, expected freq, heard note, heard freq
    def add_note(self, note: Note):
        tree_widget_item = QTreeWidgetItem()
        tree_widget_item.setText(0, time.strftime("%Y-%d-%m %H:%M:%S", time.localtime()))
        tree_widget_item.setText(1, str(note))
        tree_widget_item.setText(2, str(note.frequency))
        tree_widget_item.setText(3, "")
        tree_widget_item.setText(4, "")
        self.ui.note_debugger_display.addTopLevelItem(tree_widget_item)
