import aubio
import numpy
import pyaudio as pya

from util.find_note import DataCollector, frequency_to_note

pyaudio = pya.PyAudio()

CHUNK_SIZE = 1024
RATE = 44100
SECONDS = 4000

microphone_input_stream = pyaudio.open(
    format=pya.paFloat32,
    channels=1,
    rate=44100,
    input=True,
    input_device_index=1,
    frames_per_buffer=CHUNK_SIZE,
)
pitch_detection = aubio.pitch("default", CHUNK_SIZE * 2, CHUNK_SIZE, RATE)
pitch_detection.set_unit("Hz")
pitch_detection.set_silence(-40)

collecting_data = False
data_collector = None

for _ in range(int(RATE / CHUNK_SIZE * SECONDS)):
    data = microphone_input_stream.read(CHUNK_SIZE)
    q = numpy.frombuffer(data, dtype=aubio.float_type)
    pitch = pitch_detection(q)[0]

    if not collecting_data and pitch:
        data_collector = DataCollector()
        collecting_data = True

    if collecting_data:
        if pitch == 0:
            collecting_data = False

            point_total = data_collector.data_points
            average = data_collector.get_average()
            note = frequency_to_note(average)
            data_collector = None

            # Make sure we have enough data points so we don't just collect random noise
            if point_total > 5:
                print(f"{average} - {note}")
        else:
            data_collector.add_data(pitch)
