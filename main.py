import tkinter as tk
import pyttsx3

frame = tk.Tk()
frame.title("Text to speech")
frame.geometry("400x200")
bot = pyttsx3.init()

def TTS():
    valueTXT = inputText.get(1.0, "end-1c")
    lbl.config(text=f"{valueTXT}")
    bot.say(valueTXT)
    bot.runAndWait()

inputText = tk.Text(
    frame,
    height=5,
    width=20
)
inputText.pack()

printButton = tk.Button(
    frame,
    text="Cetak",
    command=TTS
)
printButton.pack()

lbl = tk.Label(
    frame,
    text=""
)
lbl.pack()

frame.mainloop()