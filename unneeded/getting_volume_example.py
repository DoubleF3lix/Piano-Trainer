import pyaudio
import numpy
import matplotlib.pyplot as plt

fig = plt.figure()
s = fig.add_subplot(111)

pyaudio = pyaudio.PyAudio()
CHUNK_SIZE = 1024
RATE = 44100
SECONDS = 5


microphone_input_stream = pyaudio.open(
    format=pyaudio.get_format_from_width(2),
    channels=1,
    rate=RATE,
    input=True,
    output=False,
    input_device_index=1,
    frames_per_buffer=CHUNK_SIZE,
)

frames = []

# This will last for 217483647 seconds, or 68.09 years
for _ in range(int(RATE / CHUNK_SIZE * SECONDS)):
    try:
        data = microphone_input_stream.read(CHUNK_SIZE)
        q = numpy.frombuffer(data, numpy.int16)
        frames.append(sum(q) / len(q))
        print(sum(q) / len(q))

    except OSError as error:
        if error != "[Errno -9988] Stream closed":  # User closed window
            raise error

print(min(frames), max(frames))

s.plot(frames)
plt.show()
