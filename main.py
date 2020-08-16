from Array.arrayMain import *
from Stack.stack import *
from Queue.queueMain import *
from LinkedList.listMain import *
from about import initAboutWindow

from PIL import ImageTk, Image
import os

window = Tk()
window.geometry("900x500+300+200")
window.title("Visual Data Structures")

fontName = "Courier New"

menubar = Menu(window)

arrayMenu = Menu(menubar, tearoff=0)
arrayMenu.add_command(label="What is Array?", command=initArrayWindow)
arrayMenu.add_separator()
arrayMenu.add_command(label="Static Array", command=initStatArray)
arrayMenu.add_command(label="Dynamic Arrary", command=initDynamicArray)
menubar.add_cascade(label="Array", menu=arrayMenu)

stackMenu = Menu(menubar, tearoff=0)
stackMenu.add_command(label="Stack", command=initStackWindow)
menubar.add_cascade(label="Stack", menu=stackMenu)

queueMenu = Menu(menubar, tearoff=0, )
queueMenu.add_command(label="What is Queue?", command=initQueueWindow)
queueMenu.add_separator()
queueMenu.add_command(label="Simple Queue", command=initSimpleQueue)
queueMenu.add_command(label="Circular Queue", command=initCircularQueue)
queueMenu.add_command(label="Double Ended Queue", command=initDequeue)
menubar.add_cascade(label="Queue", menu=queueMenu)

listMenu = Menu(menubar, tearoff=0, )
listMenu.add_command(label="What is Linked List?", command=initList)
listMenu.add_separator()
listMenu.add_command(label="Singly Linked List", command=initSinglyList)
listMenu.add_command(label="Doubly Linked List", command=initDoublyList)
listMenu.add_command(label="Circular Linked List", command=initCircularList)
menubar.add_cascade(label="Linked List", menu=listMenu)

aboutMenu = Menu(menubar, tearoff=0)
aboutMenu.add_command(label="About", command=initAboutWindow)
menubar.add_cascade(label="About", menu=aboutMenu)

icon = Image.open("icon.png")
icon = ImageTk.PhotoImage(icon, master = window)

window.iconphoto(False,icon)

# Label Data Structures
Label(
    window,
    text="Data Structure : ",
    font=(fontName, 15, "bold"),
    padx=15,
    pady=10,
).pack(anchor=W)

# Data Structures Definition Text
Label(
    window,
    padx=15,
    text="• Data Structure is a way of collecting and organising data in such a way that we can\n  perform operations on these data in an effective way.",
    font=(fontName, 10),
    justify=LEFT
).pack(anchor=W)

Label(
    window,
    padx=15,
    text="• More precisely, a data structure is a collection of data values,\n  the relationships among them, and the functions or operations that can be applied to the data.",
    font=(fontName, 10),
    justify=LEFT
).pack(anchor=W)

Label(
    window,
    padx=15,
    text="• Data Structures is about rendering data elements in terms of some relationship,\n  for better organization and storage.",
    font=(fontName, 10),
    justify=LEFT
).pack(anchor=W)

Label(
    window,
    padx=15,
    text="• The idea is to reduce the space and time complexities of different tasks.",
    font=(fontName, 10)
).pack(anchor=W)

Label(
    window,
    padx=15,
    text="• Data structures serve as the basis for abstract data types (ADT). ",
    font=(fontName, 10)
).pack(anchor=W)

Label(
    window,
    padx=15,
    text="• The ADT defines the logical form of the data type.",
    font=(fontName, 10)
).pack(anchor=W)

# Label Linear Data Structures
lbl_linear = Label(
    window,
    text="• Visual Data Structures",
    padx=15,
    pady=15,
    font=(fontName, 11, "bold")
).pack(anchor=W)

# Frame Containing buttons Array,Stack,Queue,Linked List
left_frame1 = Frame(window)

# Button Array
Button(left_frame1, text="Array", font=(fontName, 10, "bold"), command=initArrayWindow, width=10).pack(padx=5, side=LEFT)

# Button Stack
Button(left_frame1, text="Stack", font=(fontName, 10, "bold"), command=initStackWindow, width=10).pack(padx=5, side=LEFT)

# Button Queue
Button(left_frame1, text="Queue", font=(fontName, 10, "bold"), command=initQueueWindow, width=10).pack(padx=5, side=LEFT)

# Button Linked List
Button(left_frame1, text="Linked List", font=(fontName, 10, "bold"), command=initList, width=15).pack(padx=5, side=LEFT)

# End of buttons frame 1.
left_frame1.pack(padx=10, anchor=W)

def on_closing():
    window.destroy()

window.config(menu=menubar)
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
