import enum
import math

import numpy
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


class DataCollector:
    def __init__(self):
        self._data_points = numpy.array([])

    # https://stackoverflow.com/a/16562028/12465640 - I suck at stats
    def reject_outliers(self):
        d = numpy.abs(self._data_points - numpy.median(self._data_points))
        mdev = numpy.median(d)
        s = d / mdev if mdev else 0.0
        return self._data_points[s < 2.0]

    def add_data(self, data):
        self._data_points = numpy.append(self._data_points, data)

    def get_average(self):
        data_points = list(self.reject_outliers())
        total = sum(data_points)
        return total / len(data_points)

    @property
    def data_points(self):
        data_points = self.reject_outliers()
        return len(data_points)

    @data_points.setter
    def data_points(self, value):
        self._data_points = value


class NoteAccidental(enum.Enum):
    NATURAL = ""  # https://imgur.com/a/GDwgmWI
    SHARP = "s"  # not looking too sharp.
    FLAT = "f"  # I ran over your children with my car


class Note:
    def __init__(
        self,
        note_name: str,
        octave: int,
        accidental: NoteAccidental = NoteAccidental.NATURAL,
        frequency: float = None,
    ):
        self.note_name = note_name.lower()
        self.octave = octave
        self.accidental = accidental

        if frequency:
            self.frequency = frequency
        else:
            # All values at octave 1
            base_frequency = {
                "b": 61.75,
                "c": 32.70,
                "cs": 34.65,
                "d": 36.71,
                "ds": 38.89,
                "e": 41.20,
                "f": 43.65,
                "fs": 46.25,
                "g": 49,
                "gs": 51.91,
                "a": 55,
                "as": 58.27,
            }[self.note_name_with_accidental]
            self.frequency = round(base_frequency * (2 ** (self.octave - 1)), 2)

        self._octave_to_lilypond_markers = {
            2: ",",
            3: "",
            4: "'",
            5: "''",
            6: "'''",
            7: "''''",
        }

    def __str__(self):
        return f"{self.note_name}{self.accidental.value}{self.octave}"

    def __repr__(self):
        return f"Note(note_name='{self.note_name}', octave={self.octave}, accidental={self.accidental}, frequency={self.frequency})"

    @property
    def note_name_with_accidental(self):
        return f"{self.note_name}{self.accidental.value}"

    @property
    def lilypond_octaves(self):
        return self._octave_to_lilypond_markers[self.octave]

    @property
    def lilypond_format(self):
        # Hardcoded length of 4
        return f"{self.note_name_with_accidental}4{self.lilypond_octaves}"

    # Wants something in the form of "A4" or "AS4"
    # Frequency is here to be passed to the main constructor
    @staticmethod
    def parse_from_full(note_string: str, frequency: float = None) -> "Note":
        return Note(
            note_string[0],
            int(note_string[-1]),
            NoteAccidental(note_string[1].lower())
            if len(note_string) > 2
            else NoteAccidental.NATURAL,
            frequency,
        )

    # https://stackoverflow.com/a/70963520/12465640 - I suck at music theory too
    @staticmethod
    def parse_from_frequency(frequency: float) -> "Note":
        notes = ["A", "AS", "B", "C", "CS", "D", "DS", "E", "F", "FS", "G", "GS"]
        note_number = 12 * math.log2(frequency / 440) + 49
        note_number = round(note_number)
        note_name = notes[(note_number - 1) % 12]
        octave = (note_number + 8) // 12
        return Note(
            note_name[0],
            octave,
            NoteAccidental(note_name[1].lower())
            if len(note_name) > 1
            else NoteAccidental.NATURAL,
            frequency,
        )
