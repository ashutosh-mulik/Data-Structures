from tkinter import *


# Globals
capacity = 10
front = 10
rear = -1
size = 9

x, x1, x2 = 90, 60, 120
y, y1, y2 = 150, 60, 120

f_x, f_x1, f_x2 = 810 ,780, 840
f_y, f_y1, f_y2 = 150, 60, 120

# Global Widgets
window = None
lbl_capacity = None
canvas = None
lbl_error = None
inp_get_txt = None

lbl_front = []
lbl_rear = []

arr_box = [None] * 10
arr_inp_txt = [None] * 10

arr_f_box = [None] * 10
arr_f_inp_txt = [None] * 10

fontName = "Courier New"

def initDequeue():
    g = globals()
    global window
    window = Tk()
    window.title("Visual Double Ended Queue")
    w, h = window.winfo_screenwidth(), window.winfo_screenheight() - 20
    window.geometry("%dx%d+0+0" % (w, h))

    try:
        window.state("zoomed")
    except TclError:
        print("Linux Error")

    # Label: Queue
    Label(
        window,
        text="Double Ended Queue : ",
        font=(fontName, 15, "bold"),
        padx=15,
        pady=10,
    ).pack(anchor=W)

    # Label: Queue Definition Text
    Label(
        window,
        padx=15,
        font=(fontName, 10),
        text="• Double ended queue is a more generalized form of queue data structure which \n  allows insertion and removal of elements from both the ends, i.e , front and back.",
        justify=LEFT
    ).pack(anchor=W)

    g['lbl_capacity'] = Label(window, padx=15, font=(fontName, 10, "bold"), text="• Current Queue Capacity : " + str(capacity), justify=LEFT)
    g['lbl_capacity'].pack(anchor=W)

    # Frame Containing Integer Input, Button Enqueue, Button Dequeue
    frame1 = Frame(window)

    g['inp_get_txt'] = Entry(frame1)
    g['inp_get_txt'].pack(fill=BOTH, padx=5, side=LEFT)

    Button(
        frame1,
        text="PUSH Front",
        command=PushBoxFront
    ).pack(fill=BOTH, padx=5, side=LEFT)

    Button(
        frame1,
        text="POP Front",
        command=popBoxFront
    ).pack(fill=BOTH, padx=5, side=LEFT)

    Button(
        frame1,
        text="PUSH Rear",
        command=PushBoxRear
    ).pack(fill=BOTH, padx=5, side=LEFT)

    Button(
        frame1,
        text="POP Rear",
        command=popBoxRear
    ).pack(fill=BOTH, padx=5, side=LEFT)

    Button(
        frame1,
        text="Reset Queue",
        command=reset
    ).pack(fill=BOTH, padx=5, side=LEFT)

    frame1.pack(anchor=W, padx=15, pady=15)

    g['lbl_error'] = Label(window, padx=15, font=(fontName , 10, "bold"), text="• Error : ", justify=LEFT, foreground="#dd2c00")
    g['lbl_error'].pack(anchor=W)

    g['canvas'] = Canvas(window, width=1200, height=300, bg="#FFF")

    emptyQueueBorder()

    g['canvas'].pack(fill=BOTH, expand=True, padx=15, pady=15)

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

def getText():
    global inp_get_txt
    try:
        op = int(inp_get_txt.get())
        op = str(op)

        if len(op) > 4:
            op = op[0:4] + ".."
            return op
        else:
            return op

    except ValueError:
        return False

def emptyQueueBorder():
    global canvas

    x1, x2 = 50, 130
    y1, y2 = 50, 130

    canvas.create_line(x1 + 35, y1 + 130, x1 + 35, y1 + 190, arrow=FIRST, width=2)
    canvas.create_text(x1 + 35, y1 + 200, text="Rear", font=(fontName, 11, "bold"))

    for i in range(10):
        canvas.create_rectangle(x1, y1, x2, y2, width=2)
        x1 += 80
        x2 += 80

    canvas.create_line(x1 - 40, y1 + 130, x1 - 40, y1 + 190, arrow=FIRST, width=2)
    canvas.create_text(x1 - 40, y1 + 200, text="Front", font=(fontName, 11, "bold"))

def createBox(txt,x1, y1, x2, y2):
    global canvas
    rect_id = canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="#ffd28c")
    txt_id = canvas.create_text(x1+30, y1+30, text=txt)
    return rect_id,txt_id

def PushBoxRear():
    global x1, x2, rear, capacity

    if isFull():
        setError("Queue is full.")
    else:
        if rear < size:
            setError("")
            decCapacity()
            rear += 1
            box = createBox(getText(),x1,y1,x2,y2)
            arr_box[rear] = box[0]
            arr_inp_txt[rear] = box[1]
            incRearLbl()
            x1 += 80
            x2 += 80

def popBoxRear():
    global canvas, x1, x2, rear

    if isEmpty():
        setError("Queue is empty.")
    elif rear == -1:
        setError("No element at Rear.")
    else:
        setError("")
        incCapacity()
        canvas.delete(arr_box[rear])
        canvas.delete(arr_inp_txt[rear])
        rear -= 1
        x1 -= 80
        x2 -= 80
        decRearLbl()

def PushBoxFront():
    global f_x1, f_x2, front

    if isFull():
        setError("Queue is full.")
    else:
        if front > 0:
            setError("")
            decCapacity()
            front -= 1
            box = createBox(getText(),f_x1,f_y1,f_x2,f_y2)
            arr_f_box[front] = box[0]
            arr_f_inp_txt[front] = box[1]
            incFrontLbl()
            f_x1 -= 80
            f_x2 -= 80
    
def popBoxFront():
    global front, canvas, f_x1, f_x2

    if isEmpty():
        setError("Queue is empty.")
    elif front == 10:
        setError("No element at Front.")
    else:
        setError("")
        incCapacity()
        canvas.delete(arr_f_box[front])
        canvas.delete(arr_f_inp_txt[front])
        front += 1
        f_x1 += 80
        f_x2 += 80
        decFrontLbl()

def incRearLbl():
    global canvas, x, lbl_rear

    try:
        canvas.delete(lbl_rear[0])
        lbl_rear.pop(0)
    except IndexError:
        print(end="")

    id = canvas.create_text(x, y, text="Rear")
    lbl_rear.append(id)

    x += 80

def decRearLbl():
    global canvas, x, lbl_rear

    try:
        canvas.delete(lbl_rear[0])
        lbl_rear.pop(0)
    except IndexError:
        print(end="")

    x -= 160
    id = canvas.create_text(x, y, text="Rear")
    lbl_rear.append(id)
    x += 80

    if rear == -1:
        try:
            canvas.delete(lbl_rear[0])
            lbl_rear.pop(0)
        except IndexError:
            print(end="")

def incFrontLbl():
    global canvas, f_x, lbl_front

    try:
        canvas.delete(lbl_front[0])
        lbl_front.pop(0)
    except IndexError:
        print(end="")

    id = canvas.create_text(f_x, f_y, text="Front")
    lbl_front.append(id)

    f_x -= 80

def decFrontLbl():
    global canvas, f_x, lbl_front

    try:
        canvas.delete(lbl_front[0])
        lbl_front.pop(0)
    except IndexError:
        print(end="")

    f_x += 160
    id = canvas.create_text(f_x, f_y, text="Front")
    lbl_front.append(id)
    f_x -= 80

    if front == 10:
        try:
            canvas.delete(lbl_front[0])
            lbl_front.pop(0)
        except IndexError:
            print(end="")

def isFull():
    if rear == size or front == 0 or front == rear + 1:
        return True

def isEmpty():
    if front == 10 and rear == -1:
        return True

def setError(error):
    global lbl_error
    lbl_error.config(text="• Error : "+str(error))

def incCapacity():
    global capacity, lbl_capacity
    capacity += 1
    lbl_capacity.config(text="• Current Queue Capacity : "+str(capacity))

def decCapacity():
    global capacity, lbl_capacity
    capacity -= 1
    lbl_capacity.config(text="• Current Queue Capacity : "+str(capacity))

def reset():
    window.destroy()
    resertValues()
    initDequeue()

def resertValues():
    g = globals()

    # Globals
    g['capacity'] = 10
    g['front'] = 10
    g['rear'] = -1
    g['size'] = 9

    g['x'], g['x1'], g['x2'] = 90, 60, 120
    g['y'], g['y1'], g['y2'] = 150, 60, 120

    g['f_x'], g['f_x1'], g['f_x2'] = 810 ,780, 840
    g['f_y'], g['f_y1'], g['f_y2'] = 150, 60, 120

    # Global Widgets
    g['window'] = None
    g['lbl_capacity'] = None
    g['canvas'] = None
    g['lbl_error'] = None
    g['inp_get_txt'] = None

    g['lbl_front'] = []
    g['lbl_rear'] = []

    g['arr_box'] = [None] * 10
    g['arr_inp_txt'] = [None] * 10

    g['arr_f_box'] = [None] * 10
    g['arr_f_inp_txt'] = [None] * 10

def on_closing():
    window.destroy()
    resertValues()
