import json
import os
import subprocess
import sys

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QMessageBox


class FileAccessAPI:
    def __init__(self):
        self.install_path: str = self.get_install_path()
        self.settings_file_path: str = os.path.join(self.install_path, "settings.json")
        self.assets_path: str = os.path.join(self.install_path, "assets")

        self.create_settings_file_if_needed()

    def get_install_path(self) -> str:
        return (
            os.getcwd()
            if sys.argv[-1].endswith(".py") # If it's from VSCode or Python in terminal, it'll end in .py
            else QCoreApplication.applicationDirPath()
        )

    # Make the settings file if it doesn't exist
    def create_settings_file_if_needed(self) -> None:
        if os.path.exists(self.settings_file_path):
            return False

        os.makedirs(os.path.dirname(self.settings_file_path), exist_ok=True)
        with open(self.settings_file_path, "w") as outfile:
            # fmt: off
            json.dump({
                "enabled_notes": {"cS2": True, "d2": True, "dS2": True, "e2": True, "f2": True, "fS2": True, "g2": True, "gS2": True, "a2": True, "aS2": True, "b2": True, "c3": True, "cS3": True, "d3": True, "dS3": True, "e3": True, "f3": True, "fS3": True, "g3": True, "gS3": True, "a3": True, "aS3": True, "b3": True, "c4": True, "cS4": True, "d4": True, "dS4": True, "e4": True, "f4": True, "fS4": True, "g4": True, "gS4": True, "a4": True, "aS4": True, "b4": True, "c5": True, "cS5": True, "d5": True, "dS5": True, "e5": True, "f5": True, "fS5": True, "g5": True, "gS5": True, "a5": True, "aS5": True, "b5": True, "c6": True, "cS6": True, "d6": True, "dS6": True, "e6": True, "f6": True, "fS6": True, "g6": True, "gS6": True, "a6": True, "aS6": True, "b6": True, "c7": True, "cS7": True},
                "key_signatures": {"c": True, "g": False, "d": False, "a": False, "e": False, "b": False, "fs": False, "cs": False, "f": False, "bf": False, "ef": False, "af": False, "df": False, "gf": False, "cf": False},
                "clef": "Treble",
                "DEBUG": {
                    "INSTANTLY_OPEN_SETTINGS_WINDOW": False,
                    "INSTANTLY_OPEN_NOTE_DEBUGGER_WINDOW": False,
                }
            }, outfile, indent=4)
            # fmt: on

    # Load the settings into a file
    def save_settings(self, data: dict, show_success_prompt: bool) -> None:
        with open(self.settings_file_path, "w") as outfile:
            json.dump(data, outfile, indent=4)

        if show_success_prompt:
            msg_box: QMessageBox = QMessageBox()
            msg_box.setWindowTitle("Save Settings")
            msg_box.setText("Settings successfully saved!")
            msg_box.exec()

    # Load the settings from a file
    def load_settings(
        self, discard_debug: bool = False, as_string: bool = False
    ) -> dict:
        with open(self.settings_file_path, "r") as infile:
            contents = json.load(infile)
        if discard_debug:
            del contents["DEBUG"]
        return json.dumps(contents, indent=4) if as_string else contents

    def get_setting(self, setting: str) -> bool | str | dict:
        if "/" in setting:
            setting = setting.split("/")
            return self.load_settings()[setting[0]][setting[1]]
        return self.load_settings()[setting]

    def set_setting(self, setting: str, value: bool | str | dict) -> None:
        current_settings = self.load_settings()
        if "/" in setting:
            setting = setting.split("/")
            current_settings[setting[0]][setting[1]] = value
        else:
            current_settings[setting] = value

        self.save_settings(current_settings, False)

    def get_debug_setting(self, setting: str) -> bool:
        return self.load_settings()["DEBUG"][setting]

    def set_debug_setting(self, setting: str, value: bool) -> None:
        current_settings = self.load_settings()
        current_settings["DEBUG"][setting] = value

        self.save_settings(current_settings, False)

    def get_asset_path(self, local_path: str) -> str:
        return os.path.join(self.assets_path, os.path.normpath(local_path))

    def compile_lilypond_file(self, contents: str) -> None:
        os.makedirs(self.get_asset_path("lp_temp"), exist_ok=True)
        with open(self.get_asset_path("lp_temp/file.ly"), "w") as outfile:
            outfile.write(contents)

        # All valid OS checking is done in main.py
        lilypond_path = self.get_asset_path(f"lilypond/{sys.platform}/bin/lilypond.exe")
        subprocess.call(
            f'"{lilypond_path}" --loglevel=NONE --svg -dcrop file.ly',
            cwd=self.get_asset_path("lp_temp"),
            shell=True,
        )

        return self.get_asset_path("lp_temp/file.cropped.svg")
