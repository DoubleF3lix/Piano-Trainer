import platform
import sys
import time

from packaging import version
from PySide6.QtWidgets import QApplication

from main_window import MainWindow
from util import make_message_box

app = QApplication(sys.argv)

# Check it's a valid OS
if platform.system() not in {"Windows", "Darwin", "Linux"}:
    make_message_box(
        "Fatal Error",
        f"Unsupported platform: {sys.platform}.\nSupported platforms: Windows (win32), macOS (darwin), Linux (linux)",
    )
    sys.exit()
# If it is, check it's a valid version (Linux has... IDK)
if platform.system() == "Windows" and version.parse(
    q := platform.release()
) < version.parse("10"):
    make_message_box(
        "Unsupported Platform",
        f"Windows {q} is not supported. Please upgrade to Windows 10 or later.",
    )
elif platform.system() == "Darwin" and version.parse(
    q := platform.release()
) < version.parse("10.15"):
    make_message_box(
        "Unsupported Platform",
        f"macOS {q} is not supported. Please upgrade to macOS 10.15 (Catalina) or later.",
    )
# There is no hope for Linux. Good luck.


def catch_exception(exc_type, exc_value, exc_tb):
    import os
    import traceback

    error = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))

    os.makedirs("errors", exist_ok=True)
    with open(f"errors/error-{round(time.time())}.txt", "w") as outfile:
        outfile.write(error)

    make_message_box(
        "Fatal Error",
        error
        + "\nPlease report this error to the developer (just sending a screenshot of this window and some info about what you were doing at the time will suffice).",
    )

    # TODO need to disable all the threads here

    app.quit()


sys.excepthook = catch_exception

window = MainWindow()
window.show()
app.exec()

# TODO attempt to fix "QObject::killTimer: Timers cannot be stopped from another thread"
# TODO make installer
# TODO implement cross-platform executables, add 8va (both clef and lines), and options for it, as well as clef profiles

# TODO precompile all lilypond SVGs?
# TODO for 8va brackets https://lilypond.org/doc/v2.25/Documentation/notation/ottava-brackets
# TODO 8vb clef with `\clef "treble_8"` or `\clef "treble_15"` (use _ for down, ^ for up)
# https://lilypond.org/doc/v2.23/Documentation/snippets/pitches
