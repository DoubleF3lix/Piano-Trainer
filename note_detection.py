from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from main_window import MainWindow

import aubio
import numpy
import pyaudio
from PySide6.QtCore import QThread

from util import DataCollector, Note


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

        # This library is magic. Thank you aubio devs.
        self.pitch_detector = aubio.pitch(
            "default", self.CHUNK_SIZE * 2, self.CHUNK_SIZE, self.RATE
        )
        self.pitch_detector.set_unit("Hz")
        self.pitch_detector.set_silence(-40)

        self.data_collector: DataCollector | None = None
        self.collecting_data: bool = False

    def run(self):
        self.is_running = True
        # Keep the microphone line open for a theoretically infinite time (it's like 3 years or something IDK)
        for _ in range(int(self.RATE / self.CHUNK_SIZE * 2147483647)):
            # Stop once we have a note
            if not self.is_running:
                break

            # I forgot what frombuffer is for, but I assure it's necessary
            data = self.microphone_input_stream.read(self.CHUNK_SIZE)
            q = numpy.frombuffer(data, dtype=aubio.float_type)
            pitch = self.pitch_detector(q)[0]

            # Initialize the DataCollector
            # TODO why is this not initialized at the start of the function?
            if not self.collecting_data and pitch:
                self.data_collector = DataCollector()
                self.collecting_data = True

            # Add the data to the DataCollector
            if self.collecting_data:
                # TODO is pitch 0 when the mic is silent?
                if pitch == 0:
                    self.collecting_data = False

                    # DataCollector has a getter which automatically rejects outliers and returns the length of the internal array
                    data_point_total = self.data_collector.data_points
                    # Get the average note value
                    average = self.data_collector.get_average()
                    # Take the average frequency heard and turn it into a note value
                    note = Note.parse_from_frequency(average)
                    self.data_collector = None

                    # Make sure we have enough data points so we don't just collect random noise
                    if data_point_total > 5:
                        # Inform the main window we have heard a note, and what note that was
                        self.parent.note_detected(note)
                else:
                    self.data_collector.add_data(pitch)

    def stop(self):
        self.is_running = False
