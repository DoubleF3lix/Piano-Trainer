import sys

from PySide6.QtWidgets import QApplication

from main_window import MainWindow

app = QApplication(sys.argv)


DEBUG = {
    "INSTA_OPEN_SETTINGS": True,
    "SHOW_ERRORS_IN_DIALOG": False,
    "IS_RUNNING_PY": True,
}


window = MainWindow(DEBUG)
window.show()
app.exec()
