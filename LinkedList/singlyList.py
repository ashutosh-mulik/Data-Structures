from tkinter import *
from random import randint

fontName = "Courier New"

window = None
canvas = None
inpData = None
lbl_Error = None
inpDelNode = None

x1,y1 = 100,100

arr_x1 = []
arr_Nodes = []
arr_arrow = []

head_arrow, head_txt = [], []

index = -1

def initSinglyList():
    global window, canvas, inpData, lbl_Error, inpDelNode

    window = Tk()
    window.title("Visual Singly Linked List")
    w, h = window.winfo_screenwidth(), window.winfo_screenheight() - 20
    window.geometry("%dx%d+0+0" % (w, h))

    try:
        window.state("zoomed")
    except TclError:
        print("Linux Error")
        
    Label(
        window,
        text="Singly Linked List : ",
        font=(fontName, 15, "bold"),
        padx=15,
        pady=10,
    ).pack(anchor=W)

    Label(
        window,
        padx=15,
        font=(fontName, 10),
        text="• It is the most common. Each node has data and a pointer to the next node. ",
        justify=LEFT
    ).pack(anchor=W)

    Label(
        window,
        padx=15,
        font=(fontName, 10),
        text="• Linear Linked list is the default linked list and a linear data structure\n"
            "  in which data is not stored in contiguous memory locations but each data node is\n  connected to the next data node via a pointer, hence forming a chain.",
        justify=LEFT
    ).pack(anchor=W)

    frame1 = Frame(window)

    Label(
        frame1,
        text="Data : ",
        font=(fontName, 10, "bold")
    ).pack(fill=BOTH, padx=5, side=LEFT)

    inpData = Entry(frame1)
    inpData.pack(fill=BOTH, padx=5, side=LEFT)

    Button(
        frame1,
        text="Insert at Front",
        command=insertAtFront
    ).pack(fill=BOTH, padx=5, side=LEFT)

    Button(
        frame1,
        text="Insert at End",
        command=insertAtEnd
    ).pack(fill=BOTH, padx=5, side=LEFT)

    Label(
        frame1,
        text=" | ",
        font=(fontName, 10, "bold")
    ).pack(fill=BOTH, padx=5, side=LEFT)

    inpDelNode = Entry(frame1, width=5)
    inpDelNode.pack(fill=BOTH, padx=5, side=LEFT)

    Button(
        frame1,
        text="Delete",
        command=delete
    ).pack(fill=BOTH, padx=5, side=LEFT)

    Label(
        frame1,
        text=" | ",
        font=(fontName, 10, "bold")
    ).pack(fill=BOTH, padx=5, side=LEFT)

    Button(
        frame1,
        text="Reset",
        command=reset
    ).pack(fill=BOTH, padx=5, side=LEFT)

    frame1.pack(anchor=W, padx=15, pady=15)

    lbl_Error = Label(
        window,
        padx=15,
        font=(fontName, 10, "bold"),
        text="• Error : ",
        justify=LEFT,
        foreground="#dd2c00"
    )
    lbl_Error.pack(anchor=W)

    canvas = Canvas(window, width=500, height=800, bg="#FFF")

    canvas.pack(fill=BOTH, expand=True, anchor=W, padx=15, pady=15)
    scrollbar = Scrollbar(canvas, orient="horizontal", command=canvas.xview)
    scrollbar.pack(side=BOTTOM, fill=X)

    canvas.configure(xscrollcommand=scrollbar.set)

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

def lblHead():
    global head_arrow, head_txt

    try:
        canvas.delete(head_txt[0])
        canvas.delete(head_arrow[0])
        head_txt.pop(0)
        head_arrow.pop(0)
    except IndexError:
        print("")

    try:
        if arr_Nodes[0]:
            head_txt.append(canvas.create_text(170, 340, text="HEAD", font=(fontName, 10, "bold")))
            head_arrow.append(canvas.create_line(170, 240, 170, 330, arrow=FIRST))
    except IndexError:
        print("")

def visualNode(data="Data", next="Next", index = "0"):
    global x1

    node = [[[],[]],[[],[]],None,None]

    node[0][0] = canvas.create_rectangle(x1, y1, x1 + 70, y1 + 50, width=2, fill="#F6F4F4")
    node[1][0] = canvas.create_rectangle(x1 + 70, y1, x1 + 140, y1 + 50, width=2, fill="#ffd28c")
    node[0][1] = canvas.create_text(x1 + 30, y1 + 25, text=str(data))
    node[1][1] = canvas.create_text(x1 + 105, y1 + 25, text=str(next), font=(fontName, 10, "bold"))
    node[2] = canvas.create_text(x1 + 70, y1 + 75, text=str(randint(1111,9999)), font=(fontName, 10, "bold"))
    node[3] = canvas.create_text(x1 + 70, y1 + 100, text="Node : "+str(index), font=(fontName, 10, "bold"))

    canvas.configure(scrollregion=canvas.bbox("all"))
    return node

def incX1():
    global x1
    x1 += 230

def decX1():
    global x1
    x1 -= 230

def incIndex():
    global index
    index += 1

def decIndex():
    global index
    index -= 1

def getInpData():
    try:
        inp = str(int(inpData.get()))
        if len(inp) > 4:
            inp = inp[0:4]
            inp += ".."
            return inp
        else:
            return inp
    except ValueError:
        return False

def getDelNode():
    try:
        inp = int(inpDelNode.get())
        return str(inp)
    except ValueError:
        return False

def getItemText(itemId):
    return str(canvas.itemcget(itemId,"text"))

def setItemText(itemId,text):
    canvas.itemconfig(itemId, text=str(text))

def setError(err):
    lbl_Error.config(text="• Error : "+str(err))

def nextArrow():
    return canvas.create_line(x1 - 100,y1 + 25,x1, y1 + 25, arrow=LAST)

def updateNodePostion(node,x):
    canvas.coords(node[0][0], x, y1, x + 70, y1 + 50)
    canvas.coords(node[1][0], x + 70, y1, x + 140, y1 + 50)
    canvas.coords(node[0][1], x + 30, y1 + 25)
    canvas.coords(node[1][1], x + 105, y1 + 25)
    canvas.coords(node[2], x + 70, y1 + 75)
    canvas.coords(node[3], x + 70, y1 + 100)

def updateArrowPosition(arrow,x):
    canvas.coords(arrow, x - 100, y1 + 25, x, y1 + 25)

def insertAtEnd():
    setError("")

    if getInpData():
        incIndex()
        arr_x1.append(x1)
        if index > 0:
            newNode = visualNode(getInpData(),"Null",index)
            prevNode = arr_Nodes[len(arr_Nodes)-1]
            setItemText(prevNode[1][1],getItemText(newNode[2]))

            arr_arrow.append(nextArrow())
            arr_Nodes.append(newNode)
        else:
            arr_Nodes.append(visualNode(getInpData(),"Null",index))
        
        incX1()
    else:
        setError("Only integer value is accepted.")
    lblHead()

def insertAtFront():
    global x1
    setError("")

    if getInpData():
        
        if index >= 0:
            arr_x1.append(x1)
            i = 1
            for node in arr_Nodes:
                updateNodePostion(node,arr_x1[i])
                setItemText(node[3],"Node : "+str(i))
                i += 1
            
            if index >= 1:
                i = 0
                for arrow in arr_arrow:
                    updateArrowPosition(arrow,arr_x1[i + 2])
                    i += 1  
            
            x1 = arr_x1[0]
            currFirstNode = arr_Nodes[0]
            newNode = visualNode(getInpData(),getItemText(currFirstNode[2]),"0")
            arr_Nodes.insert(0,newNode)

            x1 = arr_x1[1]
            newArrow = nextArrow()
            arr_arrow.insert(0,newArrow)
            
            x1 = arr_x1[len(arr_x1) - 1]
            incX1()
            incIndex()
        else:
            insertAtEnd()
    else:
        setError("Only integer value is accepted.")
    lblHead()

def deleteNode(i):
    node = arr_Nodes[i]

    canvas.delete(node[0][0])
    canvas.delete(node[0][1])
    canvas.delete(node[1][0])
    canvas.delete(node[1][1])
    canvas.delete(node[2])
    canvas.delete(node[3])
    
    try:
        arrow = arr_arrow[i]
        canvas.delete(arrow)
    except IndexError:
        print("")

def delete():
    global x1, index, x1, y1, arr_x1, arr_Nodes, arr_arrow
    setError("")

    if index >= 0:

        if getDelNode():

            if int(getDelNode()) >= 0 and int(getDelNode()) <= index:
            
                try:
                    if int(getDelNode()) == index:
                        try:
                            prNode = arr_Nodes[int(getDelNode()) - 1]
                            setItemText(prNode[1][1],"Null")

                            deleteNode(int(getDelNode()))
                            arr_Nodes.pop(int(getDelNode()))

                            try:
                                canvas.delete(arr_arrow[int(getDelNode()) - 1])
                                arr_arrow.pop(int(getDelNode()) - 1)
                            except IndexError:
                                print()

                            arr_x1.pop()

                            x1 = arr_x1[len(arr_x1) - 1]
                            incX1()
                            decIndex()
                        except IndexError:
                            if index == 0:
                                x1,y1 = 100,100
                                arr_x1 = []
                                arr_Nodes = []
                                arr_arrow = []

                                index = -1
                    else:
                        prNode = arr_Nodes[int(getDelNode()) - 1]
                        nxtNode = arr_Nodes[int(getDelNode()) + 1]
                        setItemText(prNode[1][1],getItemText(nxtNode[2]))

                        deleteNode(int(getDelNode()))
                        arr_Nodes.pop(int(getDelNode()))

                        try:
                            arr_arrow.pop(int(getDelNode()))
                        except IndexError:
                            print()

                        arr_x1.pop()

                        x1 = arr_x1[0]

                        i = 0
                        for node in arr_Nodes:
                            updateNodePostion(node,arr_x1[i])
                            setItemText(node[3],"Node : "+str(i))
                            i += 1
                        
                        if index >= 1:
                            i = 0
                            for arrow in arr_arrow:
                                updateArrowPosition(arrow,arr_x1[i + 1])
                                i += 1  

                        lastNode = arr_Nodes[len(arr_Nodes) - 1]
                        setItemText(lastNode[1][1],"Null")
                        x1 = arr_x1[len(arr_x1) - 1]
                        incX1()
                        decIndex()

                except IndexError:
                    deleteNode(int(getDelNode()))
                    arr_Nodes.pop(int(getDelNode()))     
            else:
                setError("Enter value between 0 to "+str(index)+".")
        else:
            setError("Only integer value is accepted.")
    else:
        setError("List is empty.")
    lblHead()

def resetValues():
    g = globals()

    g['window'] = None
    g['canvas'] = None
    g['inpData'] = None
    g['lbl_Error'] = None
    g['inpDelNode'] = None

    g['x1'], g['y1'] = 100,100

    g['arr_x1'] = []
    g['arr_Nodes'] = []
    g['arr_arrow'] = []

    g['index'] = -1

    g['head_arrow'], g['head_txt'] = [], []

def on_closing():
    window.destroy()
    resetValues()

def reset():
    window.destroy()
    resetValues()
    initSinglyList()
