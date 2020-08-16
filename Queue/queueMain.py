from tkinter import *
from Queue.simpleQueue import initSimpleQueue
from Queue.circularQueue import initCircularQueue
from Queue.dequeue import initDequeue

fontName = "Courier New"

def initQueueWindow():
    window = Tk()
    window.title("Array")
    window.geometry("1000x400+200+200")

    # Label: Queue
    Label(
        window,
        text="Queue : ",
        font=(fontName, 15, "bold"),
        padx=15,
        pady=10,
    ).pack(anchor=W)

    # Label: Queue Definition Text
    Label(
        window,
        padx=15,
        text="• Queue is a linear data structure where the first element is\n   inserted from one end called REAR and "
             "deleted from the other end called as FRONT.",
        font=(fontName, 10),
        justify=LEFT
    ).pack(anchor=W)

    # Label: Queue Definition Text
    Label(
        window,
        padx=15,
        text="• Front points to the beginning of the queue and Rear points to the end of the queue.",
        justify=LEFT,
        font=(fontName, 10)
    ).pack(anchor=W)

    # Label: Queue Definition Text
    Label(
        window,
        padx=15,
        text="• Queue follows the FIFO (First - In - First Out) structure.",
        font=(fontName, 10),
        justify=LEFT
    ).pack(anchor=W)

    # Label: Queue Definition Text
    Label(
        window,
        padx=15,
        text="• According to its FIFO structure, element inserted first will also be removed first.",
        justify=LEFT,
        font=(fontName, 10)
    ).pack(anchor=W)

    # Label: Queue Definition Text
    Label(
        window,
        padx=15,
        text="• In a queue, one end is always used to insert data (enqueue) and the other is\n  used to delete data ("
             "dequeue), because queue is open at both its ends. ",
        justify=LEFT,
        font=(fontName, 10)
    ).pack(anchor=W)

    # Label: Queue Definition Text
    Label(
        window,
        padx=15,
        text="• The enqueue() and dequeue() are two important functions used in a queue.",
        justify=LEFT,
        font=(fontName, 10)
    ).pack(anchor=W)

    # Label: Queue Definition Text
    Label(
        window,
        padx=15,
        pady=20,
        text="Types of Queue.",
        justify=LEFT,
        font=(fontName, 10, "bold")
    ).pack(anchor=W)

    # Frame Containing buttons Array,Stack,Queue,Linked List
    left_frame1 = Frame(window)

    # Button Simple Queue
    Button(
        left_frame1,
        text="Simple Queue",
        command=initSimpleQueue,
        font=(fontName, 10)
    ).pack(padx=5, side=LEFT)

    # Button Circular Queue
    Button(
        left_frame1,
        text="Circular Queue",
        command=initCircularQueue,
        font=(fontName, 10)
    ).pack(padx=5, side=LEFT)

    # Button Dequeue (Double Ended Queue)
    Button(
        left_frame1,
        text="Dequeue (Double Ended Queue)",
        command=initDequeue,
        font=(fontName, 10)
    ).pack(padx=5, side=LEFT)

    # End of buttons frame 1.
    left_frame1.pack(padx=10, anchor=W)

    window.mainloop()
