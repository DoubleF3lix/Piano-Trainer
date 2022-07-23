import contextlib
import json
import os
import sys
import typing

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtSvgWidgets import QGraphicsSvgItem
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QMainWindow

if typing.TYPE_CHECKING:
    from main_window import MainWindow

from ui.settings_ui import Ui_SettingsWindow


class SettingsWindow(QMainWindow):
    def __init__(self, parent: MainWindow = None):
        self.parent: MainWindow = parent

        self.SETTINGS_FILE_PATH = self.parent.FileAccessAPI.SETTINGS_FILE_PATH

        # Check if a settings file exists, and if so load the config from it
        existing_settings: dict = self.parent.FileAccessAPI.load_settings()
        self.enabled_notes: dict = existing_settings["enabled_notes"]

        # Functionality for note configuration
        self.is_holding_click: bool = False
        self.note_widget_geometries: dict[str, QtCore.QRect] = {}
        self.toggled_notes: list[str] = []

        # Initialize the UI itself
        super().__init__(parent)
        self.ui: Ui_SettingsWindow = Ui_SettingsWindow()
        self.ui.setupUi(self)

        # Load misc widget values
        self.ui.enable_chord_picking_checkbox.setChecked(
            existing_settings["chord_picking_enabled"]
        )
        self.ui.clef_selection.setCurrentText(existing_settings["clef"])

        # Loop through all the note buttons
        for note, value in self.enabled_notes.items():
            note_widget: QtWidgets.QPushButton = getattr(self.ui, f"piano_{note}")

            # Set note state to saved value
            note_widget.setProperty("note_enabled", value)

            # We need these here otherwise the mouse click won't be detected if we're hovered over a button
            note_widget.mousePressEvent = self.mousePressEvent
            note_widget.mouseReleaseEvent = self.mouseReleaseEvent

            # Set the display of the white notes
            if "S" not in note:
                note_widget.setText(f"\n\n\n\n\n{note[0]}".upper())

            # Initialize a dictionary of the geometries of all the note button widgets so we can compare them when the user clicks
            self.note_widget_geometries[note] = note_widget.geometry()

        self.installEventFilter(self)

        # TODO load state into checkboxes

        # Miscellaneous components
        self.ui.shecret_button.clicked.connect(self.funny_easter_egg)
        self.ui.help_button.clicked.connect(self.display_help)
        self.ui.save_button.clicked.connect(
            lambda: self.save_settings(show_success_prompt=True)
        )
        self.ui.quit_button.clicked.connect(lambda: self.close())

        svg_root: str = os.path.join("assets", "key_signatures")
        for file in os.listdir(svg_root):
            if file.endswith(".svg"):
                file_no_ext = file[:-4]
                svg_item: QGraphicsSvgItem = QGraphicsSvgItem(
                    f"assets\\key_signatures\\{file}"
                )

                svg_display: QGraphicsView = getattr(
                    self.ui, f"{file_no_ext}_major_display"
                )
                svg_item.setScale(1.25)

                scene: QGraphicsScene = QGraphicsScene()
                scene.addItem(svg_item)
                svg_display.setScene(scene)

    # I regret nothing
    def funny_easter_egg(self) -> None:
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle(
            "I put this here on June 19th, 2022 at 10:09 PM and will now promptly forget it exists"
        )
        msg_box.setText(
            "The Game is a game, of which the sole object is to not remember that you are playing it. As soon as you remember that it exists, you have lost and must start again.\n\nWith that, you lose! :)"
        )
        msg_box.exec()

    def display_help(self) -> None:
        msg_box: QtWidgets.QMessageBox = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.setWindowTitle("Settings Help")
        msg_box.setText(
            '"Note Configuration" allows you to choose what notes you want to practice.\nA note highlighted in red means it will not be selected for practice.\nYou can click on each note individually, or you can click and drag over multiple notes to toggle several at a time.\nFor technical reasons, only C#2 to C#7 are supported.\n\n"Enable Chord Picking" will allow multiple notes to appear, where you have to play one of the notes highlighted in green.\n\n"Clef" lets you configure which clef you want to practice. Selecting "Random" will randomly pick between the two every round.'
        )
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec()

    # Toggle the note enabled state
    def invert_note_state(self, note):
        note_widget: QtWidgets.QPushButton = getattr(self.ui, f"piano_{note}")
        note_widget.setProperty(
            "note_enabled", not note_widget.property("note_enabled")
        )
        # Need to refresh the stylesheet so our changes are visible
        note_widget.style().unpolish(note_widget)
        note_widget.style().polish(note_widget)
        self.enabled_notes[note] = not self.enabled_notes[note]

    # Checks what note the user is hovering over
    def get_selected_notes(self, event_pos: QtCore.QPoint) -> None:
        # Loop through the geometries of all the note widgets and check which ones we might be hovering over based on mouse position
        potential_notes_selected: list[list[str, QtCore.QRect]] = [
            [note, note_widget_geometry]
            for note, note_widget_geometry in self.note_widget_geometries.items()
            if note_widget_geometry.contains(event_pos)
        ]

        # If we're hovering over a black note, we'll also be hovering over the white note since they overlap. This will make sure we don't select the white note.
        if len(potential_notes_selected) == 2:
            potential_notes_selected = [
                x for x in potential_notes_selected if "S" in x[0]
            ]

        with contextlib.suppress(IndexError):
            # We can now be confident this the note the user has hovered over
            selected_note = potential_notes_selected[0]

            # Make sure we haven't already toggled this note to avoid constantly toggling it
            if selected_note[0] not in self.toggled_notes:
                self.invert_note_state(selected_note[0])
                self.toggled_notes.append(selected_note[0])

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.LeftButton:
            self.is_holding_click = True
            # Allows you to toggle notes by a single click
            self.get_selected_notes(self.mapFromGlobal(QtGui.QCursor.pos()))

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.LeftButton:
            self.is_holding_click = False
            self.toggled_notes = []

    # Allows you to toggle notes by click dragging
    def eventFilter(self, obj: QtCore.QObject, event: QtGui.QHoverEvent) -> bool:
        if event.type() == QtCore.QEvent.HoverMove and self.is_holding_click:
            self.get_selected_notes(event.pos())

        return False

    # Grab the needed variables from the UI and wrap them in a dictionary
    def convert_state_to_output(self) -> dict:
        return {
            "enabled_notes": self.enabled_notes,
            "key_signatures": {
                "c": self.ui.c_major_checkbox.isChecked(),
                "g": self.ui.g_major_checkbox.isChecked(),
                "d": self.ui.d_major_checkbox.isChecked(),
                "a": self.ui.a_major_checkbox.isChecked(),
                "e": self.ui.e_major_checkbox.isChecked(),
                "b": self.ui.b_major_checkbox.isChecked(),
                "fs": self.ui.fs_major_checkbox.isChecked(),
                "cs": self.ui.cs_major_checkbox.isChecked(),
                "f": self.ui.f_major_checkbox.isChecked(),
                "bf": self.ui.bf_major_checkbox.isChecked(),
                "ef": self.ui.ef_major_checkbox.isChecked(),
                "af": self.ui.af_major_checkbox.isChecked(),
                "df": self.ui.df_major_checkbox.isChecked(),
                "gf": self.ui.gf_major_checkbox.isChecked(),
                "cf": self.ui.cf_major_checkbox.isChecked(),
            },
            "chord_picking_enabled": self.ui.enable_chord_picking_checkbox.isChecked(),
            "fake_pieces_enabled": self.ui.enable_fake_pieces_checkbox.isChecked(),
            "clef": self.ui.clef_selection.currentText(),
        }

    # Load the settings into a file
    def save_settings(self, show_success_prompt: bool) -> None:
        with open(self.SETTINGS_FILE_PATH, "w") as outfile:
            json.dump(self.convert_state_to_output(), outfile, indent=4)

        if show_success_prompt:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Save Settings")
            msg_box.setText("Settings successfully saved!")
            msg_box.exec()

    # Handle unsaved changes
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        # Make sure the user actually made changes before asking them if they want to save
        if self.parent.FileAccessAPI.load_settings() != self.convert_state_to_output():
            msg_box: QtWidgets.QMessageBox = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Warning)
            msg_box.setWindowTitle("Save Settings?")
            msg_box.setText(
                "You have unsaved settings. Do you want to save them?\nIf you don't save, your settings will be lost."
            )
            msg_box.setStandardButtons(
                QtWidgets.QMessageBox.Save
                | QtWidgets.QMessageBox.Discard
                | QtWidgets.QMessageBox.Cancel
            )
            msg_box.exec()

            if msg_box.clickedButton().text() == "Cancel":
                event.ignore()

            elif msg_box.clickedButton().text() == "Save":
                self.save_settings(show_success_prompt=False)
                event.accept()

            elif msg_box.clickedButton().text() == "Discard":
                event.accept()
