# Import Modules
from tkinter import *
from time import strftime
from PIL import ImageTk, Image


# time function

def time():
    current_time = strftime('%H:%M:%S')
    current_date = strftime('%a, %d %b')
    canvas.itemconfig(date_text, text=current_date)
    canvas.itemconfig(time_text, text = current_time)
    window.after(1000, time)

# Window Settings
window = Tk()
window.title("Digital Clock")
window.config(padx=10, pady=10, bg="#EBD5D5")

canvas = Canvas(width=320, height=460, highlightthickness=0,bg="#EBD5D5")
img_clock = ImageTk.PhotoImage(Image.open("clock.png"))
canvas.create_image(0,60,anchor=NW, image=img_clock)
date_text = canvas.create_text(90, 40, font=("Courier", 20, "bold"))
time_text = canvas.create_text(160, 270,font=("Courier", 35, "bold"))
canvas.pack()

time()
window.mainloop()