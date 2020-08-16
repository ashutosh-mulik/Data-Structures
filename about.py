from tkinter import *
from PIL import ImageTk, Image
import os

fontName = "Courier New"

def initAboutWindow():
    window = Tk()
    window.geometry("900x520+500+200")
    window.title("About Visual Data Structures")

    img = Image.open("about.png")
    img = img.resize((900, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img, master = window)
    
    Label(
        window,
        image=img
    ).pack(anchor=W)
    
    window.resizable(0,0)
    window.mainloop()