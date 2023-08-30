from PySide6.QtCore import QThread
from PySide6.QtGui import QCloseEvent
from PySide6.QtSvgWidgets import QGraphicsSvgItem
from PySide6.QtWidgets import QGraphicsScene, QMainWindow

from file_access_api import FileAccessAPI
from note_detection import NoteDetectionThread
from settings_window import SettingsWindow
from sheet_music_generation import SheetMusicGenerator
from ui.main_ui import Ui_MainWindow
from util import Note


class MainWindow(QMainWindow):
    def __init__(self):
        # Handles pretty much all IO stuff
        self.FileAccessAPI: FileAccessAPI = FileAccessAPI()

        super().__init__()
        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)

        # Hook up UI
        self.ui.start_button.clicked.connect(self.start_button_clicked)
        self.ui.stop_button.clicked.connect(self.stop_button_clicked)
        self.ui.reset_button.clicked.connect(self.reset_button_clicked)
        self.ui.settings_button.clicked.connect(self.settings_button_clicked)
        self.ui.skip_button.clicked.connect(self.skip_button_clicked)

        self.settings_window: SettingsWindow = SettingsWindow(self)

        # UI tally variables
        self.correct_tally: int = 0
        self.total_tally: int = 0
        self.skips_tally: int = 0

        # Stored so we don't keep creating threads if the user keeps pressing the start button
        # Also stops issues with the stop button being clicked when a game isn't running
        self.game_running: bool = False # TODO replace with note_detection_thread.isRunning()?
        self.settings_opened_when_game_running: bool = False

        self.expected_note: Note = None

        # Create threads (these will freeze the UI if they are run in the main thread)
        # The note detection thread runs for the lifetime of the program
        # The sheet music thread is created and destroyed as needed
        self.note_detection_thread = NoteDetectionThread(self)
        self.sheet_music_gen_thread: NewSheetMusicThread = None
        self.sheet_music_generator: SheetMusicGenerator = SheetMusicGenerator(self)

        if self.FileAccessAPI.get_debug_setting("INSTANTLY_OPEN_SETTINGS_WINDOW"):
            self.settings_button_clicked()

        if self.FileAccessAPI.get_debug_setting("INSTANTLY_OPEN_NOTE_DEBUGGER_WINDOW"):
            self.settings_window.debug_window.note_debugger_window.show()

    # Start a new game if one isn't already running, otherwise do nothing
    def start_button_clicked(self):
        if not self.game_running:
            self.game_running = True
            self.note_detection_thread.start()
            self.new_sheet_music()

    # Reset the UI if a game is running and clean up threads, otherwise do nothing
    def stop_button_clicked(self):
        self.ui.tally_label.setText("0/0 Correct")
        self.ui.skips_label.setText("0 Skips")
        if q := self.ui.music_display.scene():
            q.clear()
        self.ui.music_display.viewport().update()
        self.note_detection_thread.stop()

        self.correct_tally = 0
        self.total_tally = 0
        self.skips_tally = 0
        self.game_running = False

    # Literally the exact same as pressing start then stop
    def reset_button_clicked(self):
        self.stop_button_clicked()
        self.start_button_clicked()

    def settings_button_clicked(self):
        # Check if it's running so we don't crash when using the instantly open settings debug option
        if self.game_running:
            self.settings_opened_when_game_running = True
            self.note_detection_thread.stop()
        self.settings_window.show()

    def skip_button_clicked(self):
        # Pass 0 as a special argument to the note_detected function to indicate a skip
        if self.game_running:
            self.note_detected(None)

    def note_detected(self, note: Note | None):
        # Update the note debugger window
        if note:
            note_debugger_display = self.settings_window.debug_window.note_debugger_window.ui.note_debugger_display # Average python attribute access
            last_tree_widget_item = note_debugger_display.topLevelItem(note_debugger_display.topLevelItemCount() - 1)
            last_tree_widget_item.setText(3, str(note))
            last_tree_widget_item.setText(4, str(round(note.frequency, 2)))

        # Check if the note was correct
        if str(note) == str(self.expected_note):
            self.correct_tally += 1
        self.total_tally += 1

        # Confirm this is a skip
        if not note:
            self.skips_tally += 1
            self.ui.skips_label.setText(f"{self.skips_tally} Skips")
        else:
            # Update the tally display
            self.ui.tally_label.setText(f"{self.correct_tally}/{self.total_tally} Correct")

        # Queue up another sheet
        self.new_sheet_music()

    def new_sheet_music(self):
        # If we don't stop the thread and it goes out of scope (AKA we start a new one before finishing the old one),
        # the program WILL crash
        if self.sheet_music_gen_thread:
            self.sheet_music_gen_thread.terminate()

        self.sheet_music_gen_thread = NewSheetMusicThread(self)
        self.sheet_music_gen_thread.start()

    def closeEvent(self, event: QCloseEvent):
        self.note_detection_thread.stop() # This may not be necessary
        event.accept()


# Kind of a hack, need to fix
# A year later, IDK why this is a hack, I mean I guess it should go into it's own file but who cares?
class NewSheetMusicThread(QThread):
    def __init__(self, pseudo_parent: MainWindow):
        super().__init__()
        self.pseudo_parent: MainWindow = pseudo_parent

    # Automatically called when thread is initialized, should clean itself up too when it finishes
    def run(self):
        lilypond_score, expected_note = self.pseudo_parent.sheet_music_generator.generate_sheet_music()

        # Write the LP score to a file, compile it, and get the path
        sheet_music_svg_path = self.pseudo_parent.FileAccessAPI.compile_lilypond_file(
            lilypond_score
        )

        # Take the SVG output file and put it on the UI
        svg_item: QGraphicsSvgItem = QGraphicsSvgItem(sheet_music_svg_path)
        music_display_width = self.pseudo_parent.ui.music_display.width()
        music_display_height = self.pseudo_parent.ui.music_display.height()
        svg_bounding_rect = svg_item.boundingRect()
        svg_height = svg_bounding_rect.height()
        svg_width = svg_bounding_rect.width()

        # music_display_width and height are off by like 2 pixels so this accounts for it so there is no scrollbar
        scaling_ratio = (
            min(music_display_width / svg_width, music_display_height / svg_height)
            - 0.02
        ) / 1.5
        svg_item.setScale(scaling_ratio)

        scene: QGraphicsScene = QGraphicsScene()
        scene.addItem(svg_item)
        self.pseudo_parent.ui.music_display.setScene(scene)

        self.pseudo_parent.expected_note = expected_note
        # Update the note debugger window
        self.pseudo_parent.settings_window.debug_window.note_debugger_window.add_note(expected_note)
