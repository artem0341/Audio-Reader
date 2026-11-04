from pydub import AudioSegment
import threading
import pyaudiowpatch
import audio_device
import io

array = {}

def start_audio_read():
    audio_device.stream.start_stream()
    array["label"]["text"] = "Запись идёт..."
    array["Pause"].config(state="normal")
    array["Read"].config(state="disabled")
    array["Stop"].config(state="normal")

def stop():
    threading.Thread(target=stop1).start()

def stop1():
    audio_device.stream.stop_stream()
    array["Pause"].config(state="disabled")
    array["Resume"].config(state="disabled")
    array["Read"].config(state="normal")
    array["Stop"].config(state="disabled")
    array["label"]["text"] = "Запись остановлена"
    value = array["entry"].get()
    if not value:
        value = 1
    recording = AudioSegment.from_file(io.BytesIO(audio_device.buffer), frame_rate=int(audio_device.pyaudio["defaultSampleRate"]), channels=audio_device.channels, format="raw", sample_width=2)
    recording.export(f"{value}.wav", format="wav")
    audio_device.buffer = b""

def pause():
    audio_device.stream.stop_stream()
    array["label"]["text"] = "Запись приостановлена"
    array["Resume"].config(state="normal")
    array["Pause"].config(state="disabled")

def resume():
    audio_device.stream.start_stream()
    array["label"]["text"] = "Запись продолжается"
    array["Resume"].config(state="disabled")
    array["Pause"].config(state="normal")