from PySide6.QtGui import QCloseEvent
from PySide6.QtSvgWidgets import QGraphicsSvgItem
from PySide6.QtWidgets import QGraphicsScene, QMainWindow

from file_access_api import FileAccessAPI
from note_detection import NoteDetectionThread
from settings_window import SettingsWindow
from sheet_music_generation import SheetMusicGenerator
from ui.main_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        self.FileAccessAPI: FileAccessAPI = FileAccessAPI()

        super().__init__()
        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.start_button.clicked.connect(self.start_button_clicked)
        self.ui.stop_button.clicked.connect(self.stop_button_clicked)
        self.ui.reset_button.clicked.connect(self.reset_button_clicked)
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

        self.correct_tally: int = 0
        self.total_tally: int = 0
        self.skips_tally: int = 0

        self.game_running: bool = False

        self.expected_note: list = None

        self.note_detection_thread = NoteDetectionThread(self)
        self.sheet_music_generator: SheetMusicGenerator = SheetMusicGenerator(self)

    def start_button_clicked(self):
        if not self.game_running:
            self.game_running = True
            self.note_detection_thread.start()
            self.new_sheet_music()

    def stop_button_clicked(self):
        if self.game_running:
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

    def reset_button_clicked(self):
        if self.game_running:
            self.stop_button_clicked()
            self.start_button_clicked()
            self.note_detection_thread.start()

    def settings_button_clicked(self):
        self.settings_window.show()

    def skip_button_clicked(self):
        if self.game_running:
            self.note_detected(0, "")

    def note_detected(self, average: int, note: str):
        if note == self.expected_note:
            self.correct_tally += 1
        self.total_tally += 1

        # Confirm this is a skip (magic might be happening if we get a 0hz average though)
        if average == 0 and note == "":
            self.skips_tally += 1
            self.ui.skips_label.setText(f"{self.skips_tally} Skips")

        self.ui.tally_label.setText(f"{self.correct_tally}/{self.total_tally} Correct")

        self.new_sheet_music()

    def new_sheet_music(self):
        sheet_music_info = self.sheet_music_generator.generate_sheet_music()
        sheet_music_lp = sheet_music_info[0]
        sheet_music_svg_path = self.FileAccessAPI.compile_lilypond_file(sheet_music_lp)

        svg_item: QGraphicsSvgItem = QGraphicsSvgItem(sheet_music_svg_path)

        music_display_width = self.ui.music_display.width()
        music_display_height = self.ui.music_display.height()

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
        self.ui.music_display.setScene(scene)

        self.expected_note = sheet_music_info[1].rstrip("012345689")

    def closeEvent(self, event: QCloseEvent):
        self.note_detection_thread.stop()
        event.accept()
