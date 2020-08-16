from tkinter import *

window = None
txtCapacity = None 
inpIntEntry = None 
canvas = None
lbl_Error = None

#defaults 
fontName = "Courier New"
capacity = 10
front = -1
rear = -1

x1 = 100
y1 = 100

arr_data = [[None,None]] * 10
arr_x1 = []

arr_front = []
arr_rear = []

def initSimpleQueue():
    global window, txtCapacity, inpIntEntry, canvas, lbl_Error

    window = Tk()
    window.title("Visual Simple Queue")
    w, h = window.winfo_screenwidth(), window.winfo_screenheight() - 20
    window.geometry("%dx%d+0+0" % (w, h))

    try:
        window.state("zoomed")
    except TclError:
        print("Linux Error")

    # Label: Queue
    Label(
        window,
        text="Simple Queue : ",
        font=(fontName, 15, "bold"),
        padx=15,
        pady=10,
    ).pack(anchor=W)

    # Label: Queue Definition Text
    Label(
        window,
        padx=15,
        font=(fontName, 10),
        text="• Simple queue defines the simple operation of queue in which insertion occurs at the rear of the list\n  and deletion occurs at the front of the list.",
        justify=LEFT
    ).pack(anchor=W)
    
    Label(
        window,
        padx=15,
        font=(fontName, 10),
        text="• It is so called linear because it resembles to a straight line where the elements are positioned one after the other.",
        justify=LEFT
    ).pack(anchor=W)

    Label(
        window,
        padx=15,
        font=(fontName, 10),
        text="• The drawback with this queue is that it tends to be full even after some elements\n  are removed because the rear end is still at the last position.",
        justify=LEFT
    ).pack(anchor=W)

    # Frame Containing Integer Input, Button Enqueue, Button Dequeue
    frame1 = Frame(window)

    inpIntEntry = Entry(frame1)
    inpIntEntry.pack(fill=BOTH, padx=5, side=LEFT)

    Button(
        frame1,
        text="Enqueue (Insert)",
        command=insert,
        font=(fontName, 10, "bold")
    ).pack(fill=BOTH, padx=5, side=LEFT)

    Button(
        frame1,
        text="Dequeue (Delete)",
        font=(fontName, 10, "bold"),
        command=delete
    ).pack(fill=BOTH, padx=5, side=LEFT)

    Button(
        frame1,
        text="Reset Queue",
        command=reset,
        font=(fontName, 10, "bold")
    ).pack(fill=BOTH, padx=5, side=LEFT)

    frame1.pack(anchor=W, padx=15, pady=15)

    txtCapacity = Label(window, padx=15, font=(fontName, 10, "bold"), text="• Current Queue Capacity : " + str(capacity),justify=LEFT)
    txtCapacity.pack(anchor=W)

    lbl_Error = Label(
        window,
        padx=15,
        font=(fontName, 10, "bold"),
        text="• Error : ",
        justify=LEFT,
        foreground="#dd2c00"
    )
    lbl_Error.pack(anchor=W)

    #----- Canvas Start ------#
    canvas = Canvas(window, width=500, height=800, bg="#FFF")
    canvas.pack(fill=BOTH, expand=True, anchor=W, padx=15, pady=15)

    emptyQueue()

    scrollbar = Scrollbar(canvas, orient="horizontal", command=canvas.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    canvas.configure(xscrollcommand=scrollbar.set)
    #----- Canvas End -------#

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

def dataBox(inp):
    global arr_data

    data = []
    data.append(canvas.create_rectangle(x1 + 10, y1 + 10, x1 + 80, y1 + 70, fill="#ffd28c"))
    data.append(canvas.create_text(x1 + 45, y1 + 40, text=str(inp)))
    
    return data

def deleteBox(box):
    canvas.delete(box[0])
    canvas.delete(box[1])

def emptyQueue():
    x = x1
    for i in range(10):
        canvas.create_rectangle(x, y1, x + 90, y1 + 80, width=2)
        x += 90

def txtFront():
    try:
        f = arr_front[0]
        canvas.delete(f)
        arr_front.pop(0)
    except IndexError:
        print(end="")

    arr_front.append(canvas.create_text(arr_x1[front] + 45, y1 + 120, text="Front ( Head )"))

def txtRear():
    try:
        r = arr_rear[0]
        canvas.delete(r)
        arr_rear.pop(0)
    except IndexError:
        print(end="")

    arr_rear.append(canvas.create_text(arr_x1[rear] + 45, y1 + 100, text="Rear ( Tail )"))

def incX1():
    global x1
    x1 += 90

def decX1():
    global x1
    x1 -= 90

def incCapacity():
    global txtCapacity, capacity
    capacity += 1
    txtCapacity.config(text="• Current Queue Capacity : " + str(capacity))

def decCapacity():
    global txtCapacity, capacity
    capacity -= 1
    txtCapacity.config(text="• Current Queue Capacity : " + str(capacity))

def setError(err):
    lbl_Error.config(text="• Error : "+str(err))

def isEmpty():
    if front == -1 and rear == -1:
        return True
    else:
        return False

def isFull():
    if rear == 9:
        return True
    else:
        return False

def getInpData():
    try:
        inp = str(int(inpIntEntry.get()))
        if len(inp) > 4:
            inp = inp[0:4]
            inp += ".."
            return inp
        else:
            return inp
    except ValueError:
        return False

def insert():
    global front, rear

    setError("")

    if not isFull():
        if getInpData():
            
            if front == -1 and rear == -1:
                front = 0
                rear = 0

                arr_data[rear] = dataBox(str(getInpData()))

                decCapacity()
                arr_x1.append(x1)
                incX1()

                txtFront()
                txtRear()

            elif front < 10:
                rear += 1

                arr_data[rear] = dataBox(str(getInpData()))

                decCapacity()
                arr_x1.append(x1)
                incX1()

                txtFront()
                txtRear()
        else:
            setError("Only integer value is accepted.")
    else:
        setError("Queue is Full.")

def delete():
    global front, rear, x1

    setError("")

    if not isEmpty():
        if front < 10:
            
            deleteBox(arr_data[front])
            arr_data[front] = [None,None]
            front += 1

            try:
                x1 = arr_x1[front]
                txtFront()
            except IndexError:
                print(end="")

            x1 = arr_x1[len(arr_x1) - 1]
            incX1()
    else:
        setError("Queue is empty.")

def resetValues():
    g = globals()

    g['window'] = None
    g['txtCapacity'] = None 
    g['inpIntEntry'] = None 
    g['canvas'] = None
    g['lbl_Error'] = None

    g['capacity'] = 10
    g['front'] = -1
    g['rear'] = -1

    g['x1'] = 100
    g['y1'] = 100

    g['arr_data'] = [[None,None]] * 10
    g['arr_x1'] = []

    g['arr_front'] = []
    g['arr_rear'] = []

def reset():
    window.destroy()
    resetValues()
    initSimpleQueue()
    
def on_closing():
    window.destroy()
    resetValues()