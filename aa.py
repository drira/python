from tkinter import*
from timeit import default_timer

def updateTime():
    now = default_timer() - start
    minutes, seconds = divmod(now, 60)
    hours, minutes = divmod(minutes, 60)
    str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
    canvas.itemconfigure(text_clock, text=str_time)
    Fenetre.after(1000, updateTime)

start = default_timer()
text_clock = Canvas.create_text(40, 20)

updateTime()