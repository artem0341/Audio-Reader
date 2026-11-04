import pyaudiowpatch

def audio_read(data, frame_count, time_info, status):
    global buffer
    buffer += data
    return (data, pyaudiowpatch.paContinue)

chunk = 2048
sample_format = pyaudiowpatch.paInt16
channels = 2
p = pyaudiowpatch.PyAudio()
buffer = b""

pyaudio = p.get_default_wasapi_loopback()

stream = p.open(format=sample_format,
channels=channels,
rate=int(pyaudio["defaultSampleRate"]),
frames_per_buffer=chunk,
input_device_index=pyaudio["index"],
input=True,
stream_callback=audio_read,
start=False
)