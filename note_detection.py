from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from main_window import MainWindow

import aubio
import numpy
import pyaudio
from PySide6.QtCore import QThread

from util import DataCollector, frequency_to_note


class NoteDetectionThread(QThread):
    def __init__(self, parent: MainWindow = None):
        self.parent: MainWindow = parent

        super().__init__(parent)

        self.is_running: bool = False

        self.pyaudio: pyaudio.PyAudio = pyaudio.PyAudio()

        self.CHUNK_SIZE: int = 1024
        self.RATE: int = 44100

        self.microphone_input_stream: pyaudio.Stream = self.pyaudio.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=self.RATE,
            input=True,
            input_device_index=self.pyaudio.get_default_input_device_info()["index"],
            frames_per_buffer=self.CHUNK_SIZE,
        )

        self.pitch_detector = aubio.pitch(
            "default", self.CHUNK_SIZE * 2, self.CHUNK_SIZE, self.RATE
        )
        self.pitch_detector.set_unit("Hz")
        self.pitch_detector.set_silence(-40)

        self.data_collector: DataCollector | None = None
        self.collecting_data: bool = False

        self.octave_to_markers = {2: ",", 3: "", 4: "'", 5: "''", 6: "'''", 7: "''''"}

    def convert_note_to_lilypond_pitch(self, note: str, octave: int):
        # note, octave with markers
        return f"{note}{self.octave_to_markers[octave]}"

    def run(self):
        self.is_running = True
        for _ in range(int(self.RATE / self.CHUNK_SIZE * 2147483647)):
            if not self.is_running:
                break

            data = self.microphone_input_stream.read(self.CHUNK_SIZE)
            q = numpy.frombuffer(data, dtype=aubio.float_type)
            pitch = self.pitch_detector(q)[0]

            if not self.collecting_data and pitch:
                self.data_collector = DataCollector()
                self.collecting_data = True

            if self.collecting_data:
                if pitch == 0:
                    self.collecting_data = False

                    data_point_total = self.data_collector.data_points
                    average = self.data_collector.get_average()
                    note = frequency_to_note(average)
                    self.data_collector = None

                    # Make sure we have enough data points so we don't just collect random noise
                    if data_point_total > 5:
                        self.parent.note_detected(
                            average,
                            self.convert_note_to_lilypond_pitch(
                                note[:-1].lower(), int(note[-1])
                            ),
                        )
                else:
                    self.data_collector.add_data(pitch)

    def stop(self):
        self.is_running = False
