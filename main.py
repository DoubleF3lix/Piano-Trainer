import sys

from PySide6.QtWidgets import QApplication

from main_window import MainWindow

app = QApplication(sys.argv)


def catch_exception(exc_type, exc_value, exc_tb):
    import traceback

    from util import make_message_box

    make_message_box(
        "Fatal Error",
        "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
        + "\nPlease report this error to the developer (just sending a screenshot of this window and some info about what you were doing at the time will suffice).",
    )
    app.quit()


sys.excepthook = catch_exception

window = MainWindow()
window.show()
app.exec()
