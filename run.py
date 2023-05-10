import sys
import os
from tkinter import *
from tkinter import *
from PIL import ImageTk, Image
window = Tk()

canv = Canvas(window, width=1240, height=720)
canv.grid(row=0, column=0)

# img = ImageTk.PhotoImage(Image.open("mine.jpg"))  # PIL solution
# canv.create_image(0, 0, anchor=NW, image=img)

window.title("Running Python Script")
window.geometry('550x200')

def run():
    os.system('python -u track.py --classes 0 --source 0')

btn = Button(window, text="Run your Code!", bg="blue", fg="white",command=run)
btn.grid(column=0, row=0)

window.mainloop()
