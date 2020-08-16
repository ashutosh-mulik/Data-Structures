from tkinter import *

font = "Courier New"


def lbl_heading(parent, txt):
    lbl = Label(parent, text=str(txt), font=(
        font, 15, "bold"), padx=15, pady=10)
    lbl.pack(anchor=W)

    return lbl


def lbl_text(parent, txt):
    lbl = Label(parent, text=str("• "+txt), font=(font, 10), padx=15)
    lbl.pack(anchor=W)

    return lbl


def lbl_error(parent, error):
    lbl = Label(parent, text=str("• Error : "+error),font=(font, 10, "bold"), padx=15, foreground="#dd2c00")
    lbl.pack(anchor=W)

    return lbl


def entry_text(parent, txt):
    lbl = Label(parent, text=str(txt), font=(font, 10), padx=15)
    lbl.pack(fill=BOTH, side=LEFT)

    return lbl


def entry(parent, width):
    entry = Entry(parent, width=width)
    entry.pack(fill=BOTH, side=LEFT)

    return entry

def btn_in_frame(parent, text, command):
    btn = Button(parent, text=str(text), command=command)
    btn.pack(fill=BOTH, padx=5, side=LEFT)

    return btn