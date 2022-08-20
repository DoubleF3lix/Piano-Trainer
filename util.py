import math

import numpy as np
from PySide6.QtWidgets import QMessageBox


def make_message_box(
    title: str,
    text: str,
    icon: QMessageBox.Icon = None,
    buttons: QMessageBox.StandardButton = None,
) -> QMessageBox:
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(text)

    if icon:
        msg_box.setIcon(icon)

    if buttons:
        msg_box.setStandardButtons(buttons)

    msg_box.exec()

    return msg_box


# https://stackoverflow.com/a/16562028/12465640 - I suck at stats
def reject_outliers(data):
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d / mdev if mdev else 0.0
    return data[s < 2.0]


# https://stackoverflow.com/a/70963520/12465640 - I suck at music theory too
def frequency_to_note(frequency):
    notes = ["A", "AS", "B", "C", "CS", "D", "DS", "E", "F", "FS", "G", "GS"]
    note_number = 12 * math.log2(frequency / 440) + 49
    note_number = round(note_number)
    note_name = notes[(note_number - 1) % 12]
    octave = (note_number + 8) // 12
    return f"{note_name}{octave}"


class DataCollector:
    def __init__(self):
        self._data_points = np.array([])

    def add_data(self, data):
        self._data_points = np.append(self._data_points, data)

    def get_average(self):
        data_points = list(reject_outliers(self._data_points))
        total = sum(data_points)
        return total / len(data_points)

    @property
    def data_points(self):
        data_points = reject_outliers(self._data_points)
        return len(data_points)

    @data_points.setter
    def data_points(self, value):
        self._data_points = value
