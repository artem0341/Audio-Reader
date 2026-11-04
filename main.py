import io
import tkinter
from PIL import Image, ImageTk
import base64
import functions
import audio_device
import assets

t = tkinter.Tk()
t.geometry("400x400")
t.title("Audio Reader")
img = Image.open(io.BytesIO(base64.b64decode(assets.image)))
image1 = ImageTk.PhotoImage(img)
t.iconphoto(False, image1)
label = tkinter.Label(t, text="")
label.pack()
info = tkinter.Label(t, text="Введите название файла")
info.pack(pady=5)
entry = tkinter.Entry(t)
entry.pack()
Read = tkinter.Button(t, text="Запись", command=functions.start_audio_read)
Read.pack()
Pause = tkinter.Button(t, text="Пауза", command=functions.pause)
Pause.pack()
Resume = tkinter.Button(t, text="Продолжить", command=functions.resume)
Resume.pack()
Stop = tkinter.Button(t, text="Стоп", command=functions.stop)
Stop.pack()
Pause.config(state="disabled")
Resume.config(state="disabled")
Stop.config(state="disabled")

functions.array["label"] = label
functions.array["entry"] = entry
functions.array["info"] = info
functions.array["Read"] = Read
functions.array["Pause"] = Pause
functions.array["Resume"] = Resume
functions.array["Stop"] = Stop

t.mainloop()

audio_device.stream.stop_stream()
audio_device.stream.close()
audio_device.p.terminate()