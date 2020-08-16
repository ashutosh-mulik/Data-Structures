from tkinter import *
from Array.staticArray import initStatArray
from Array.dynamicArray import initDynamicArray

fontName = "Courier New"

def initArrayWindow():
    window = Tk()
    window.title("Array")
    w, h = 1000, 300
    window.geometry("%dx%d+100+100" % (w, h))

    # Label: Array
    Label(
        window,
        text="Array : ",
        font=(fontName, 15, "bold"),
        padx=15,
        pady=10,
    ).pack(anchor=W)

    # Label: Array Definition Text
    Label(
        window,
        padx=15,
        text="• Array is a data structure used to store homogeneous elements at contiguous locations.",
        font=(fontName, 10)
    ).pack(anchor=W)

    Label(
        window,
        padx=15,
        text="• Arrays are used to store multiple values in a single variable, instead of declaring\n  separate variables for each value.",
        justify=LEFT,
        font=(fontName, 10)
    ).pack(anchor=W)

    Label(
        window,
        padx=15,
        text="• An array is a container object that holds a fixed number of values of a single type.",
        font=(fontName, 10)
    ).pack(anchor=W)

    Label(
        window,
        padx=15,
        text="• Array elements are numbered, starting with zero.",
        font=(fontName, 10)
    ).pack(anchor=W)

    Label(
        window,
        padx=15,
        text="• Types of Array : ",
        font=(fontName, 10, "bold")
    ).pack(anchor=W, pady=10)

    frame1 = Frame(window)

    Button(
        frame1,
        text="Static Array",
        font=(fontName, 10, "bold"),
        width=15,
        command=initStatArray,
    ).pack(side=LEFT)

    Button(
        frame1,
        text="Dynamic Array",
        font=(fontName, 10, "bold"),
        width=15,
        command=initDynamicArray,
    ).pack(side=LEFT,padx=5)


    frame1.pack(anchor=W, padx=15)
    

    window.mainloop()