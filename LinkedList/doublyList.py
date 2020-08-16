from tkinter import *
from random import randint
import asyncio

fontName = "Courier New"
window = None
inpData = None
inpInsNode = None
inpDelNode = None
canvas = None
errorText = None

arr_Nodes = []
arr_arrow_prev = []
arr_arrow_next = []

arr_x1 = []
index = 0 
x1 = 100
y1 = 100

head_txt = []
head_arrow = []

def initDoublyList():
    global window, inpData, inpInsNode, inpDelNode, canvas, errorText

    window = Tk()
    window.title("Visual Doubly Linked List")
    w, h = window.winfo_screenwidth(), window.winfo_screenheight() - 20
    window.geometry("%dx%d+0+0" % (w, h))

    try:
        window.state("zoomed")
    except TclError:
        print("Linux Error")
        
    Label(
        window,
        text="Doubly Linked List : ",
        font=(fontName, 15, "bold"),
        padx=15,
        pady=10,
    ).pack(anchor=W)

    Label(
        window,
        padx=15,
        font=(fontName, 10),
        text="• Doubly linked list is a type of linked list in which each node apart from storing its data has two links.",
        justify=LEFT
    ).pack(anchor=W)

    Label(
        window,
        padx=15,
        font=(fontName, 10),
        text="• The first link points to the previous node in the list and the second link points to the next node in the list. ",
        justify=LEFT
    ).pack(anchor=W)

    Label(
        window,
        padx=15,
        font=(fontName, 10),
        text="• The first node of the list has its previous link pointing to NULL similarly the last node of the list has its next node pointing to NULL.",
        justify=LEFT
    ).pack(anchor=W)

    Label(
        window,
        padx=15,
        font=(fontName, 10),
        text="• The two links help us to traverse the list in both backward and forward direction. But storing an extra link requires some extra space.",
        justify=LEFT
    ).pack(anchor=W)

    #------ Frame 1 Start------#
    frame1 = Frame(window)

    Label(
        frame1,
        text="Data : ",
        font=(fontName, 10, "bold")
    ).pack(fill=BOTH, padx=5, side=LEFT)

    inpData = Entry(frame1)
    inpData.pack(fill=BOTH, padx=5, side=LEFT)

    Label(
        frame1,
        text=" | ",
        font=(fontName, 10, "bold")
    ).pack(fill=BOTH, padx=5, side=LEFT)

    Button(
        frame1,
        text="Add Front",
        command=insertAtFront
    ).pack(fill=BOTH, padx=5, side=LEFT)

    Button(
        frame1,
        text="Add End",
        command=insertAtEnd
    ).pack(fill=BOTH, padx=5, side=LEFT)

    Label(
        frame1,
        text=" | ",
        font=(fontName, 10, "bold")
    ).pack(fill=BOTH, padx=5, side=LEFT)

    Label(
        frame1,
        text="Node : ",
        font=(fontName, 10, "bold")
    ).pack(fill=BOTH, padx=5, side=LEFT)

    inpInsNode = Entry(frame1, width=5)
    inpInsNode.pack(fill=BOTH, padx=5, side=LEFT)

    Button(
        frame1,
        text="Add After",
        command=insertAfter
    ).pack(fill=BOTH, padx=5, side=LEFT)

    Button(
        frame1,
        text="Add Before",
        command=insertBefore
    ).pack(fill=BOTH, padx=5, side=LEFT)
    
    Label(
        frame1,
        text=" | ",
        font=(fontName, 10, "bold")
    ).pack(fill=BOTH, padx=5, side=LEFT)

    Label(
        frame1,
        text="Node : ",
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
    #------ Frame 1 End ------#

    errorText = Label(
        window,
        padx=15,
        font=(fontName, 10, "bold"),
        text="• Error : ",
        justify=LEFT,
        foreground="#dd2c00"
    )
    errorText.pack(anchor=W)

    #------- Canvas Start ------#
    canvas = Canvas(window, width=500, height=800, bg="#FFF")

    canvas.pack(fill=BOTH, expand=True, anchor=W, padx=15, pady=15)
    scrollbar = Scrollbar(canvas, orient="horizontal", command=canvas.xview)
    scrollbar.pack(side=BOTTOM, fill=X)

    canvas.configure(xscrollcommand=scrollbar.set)
    #------- Canvas End --------#

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

def visualNode(prev = "Null",data = "Null",next = "Null",i = "0"):
    Node = [[[], []], [[], []], [[], []], None, None]

    #Box Prev
    Node[0][0] = canvas.create_rectangle(x1,y1,x1+80,y1+60,fill="#F6F4F4")
    #box Data
    Node[1][0] = canvas.create_rectangle(x1+80,y1,x1+160,y1+60,fill="#ffd28c")
    #box Next
    Node[2][0] = canvas.create_rectangle(x1+160,y1,x1+240,y1+60,fill="#F6F4F4")
    
    #Text Prev
    Node[0][1] = canvas.create_text(x1 + 40,y1 + 30,text=str(prev))
    #Text Data
    Node[1][1] = canvas.create_text(x1 + 120,y1 + 30,text=str(data))
    #Text Next
    Node[2][1] = canvas.create_text(x1 + 200,y1 + 30,text=str(next))

    #Text Address
    address = randint(1111, 9999)
    Node[3] = canvas.create_text(x1 + 120,y1 + 90,text=str(address))

    #Text Node Index
    Node[4] = canvas.create_text(x1 + 120,y1 + 110,text="Node : "+str(i))

    canvas.configure(scrollregion=canvas.bbox("all"))
    return Node

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
            head_txt.append(canvas.create_text(220, 340, text="HEAD", font=(fontName, 10, "bold")))
            head_arrow.append(canvas.create_line(220, 240, 220, 330, arrow=FIRST))
    except IndexError:
        print("")

def updateNodePosition(node,x):

    canvas.coords(node[0][0],x,y1,x+80,y1+60) #Box Prev
    canvas.coords(node[1][0],x+80,y1,x+160,y1+60) #Box Data
    canvas.coords(node[2][0],x+160,y1,x+240,y1+60) #Text Next

    canvas.coords(node[0][1],x + 40,y1 + 30) #Text Prev
    canvas.coords(node[1][1],x + 120,y1 + 30) #Text Data    
    canvas.coords(node[2][1],x + 200,y1 + 30) #Text Next

    canvas.coords(node[3], x + 120,y1 + 90) #Text Address
    canvas.coords(node[4], x + 120,y1 + 110) #Text Node Index

def updateArrow(i,x):
    arrNext = arr_arrow_next[i]
    arrPrev = arr_arrow_prev[i]
    canvas.coords(arrPrev, x-110, y1+20, x, y1+20)
    canvas.coords(arrNext, x-110, y1+40, x, y1+40)

def arrowPrev():
    return canvas.create_line(x1-110,y1+20,x1,y1+20,arrow=FIRST,width=2)

def arrowNext():
    return canvas.create_line(x1-110,y1+40,x1,y1+40,arrow=LAST, width=2)

def incX1():
    global x1
    x1 += 350

def decX1():
    global x1
    x1 -= 350

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

def getInpInsNode():
    try:
        inp = int(inpInsNode.get())
        return str(inp)
    except ValueError:
        return False

def setError(err):
    errorText.config(text="• Error : "+str(err))

def incIndex():
    global index
    index += 1

def decIndex():
    global index
    index -= 1

def insertAtEnd():
    setError("")
    try:
        if getInpData():
            lastNode = arr_Nodes[index - 1]
            newNode = visualNode(getItemText(lastNode[3]),getInpData(),"Null",index)
            setItemText(lastNode[2][1],getItemText(newNode[3]))
            arr_arrow_prev.append(arrowPrev())
            arr_arrow_next.append(arrowNext())
            arr_Nodes.append(newNode)
            arr_x1.append(x1)
            incIndex()
            incX1()
            canvas.configure(scrollregion=canvas.bbox("all"))
        else:
            setError("Only integer value is accepted.")

    except IndexError:

        if getInpData():
            newNode = visualNode("Null",getInpData(),"Null",index)
            arr_Nodes.append(newNode)
            arr_x1.append(x1)
            incIndex()
            incX1()
            canvas.configure(scrollregion=canvas.bbox("all"))
        else:
            setError("Only integer value is accepted.")
    lblHead()

def getItemText(itemId):
    return str(canvas.itemcget(itemId,"text"))

def setItemText(itemId,text):
    canvas.itemconfig(itemId, text=str(text))

def delete():
    setError("")
    if getDelNode():
        i = int(getDelNode())
        if i <= 0 and i < index:
            if deleteNode(i):
                arr_x1.pop()

                for j in range(i,len(arr_x1)):
                    node = arr_Nodes[j]
                    updateNodePosition(node,arr_x1[j])
                    setItemText(node[4],"Node : "+str(j))
                
                deleteArrowNext(len(arr_arrow_next) - 1)
                deleteArrowPrev(len(arr_arrow_prev) - 1)

                try:
                    currNewNode = arr_Nodes[i]
                    try:
                        prNode = arr_Nodes[i - 1]
                        lastNode = arr_Nodes[len(arr_Nodes) - 1]
                        if prNode[0][1] == lastNode[0][1]:
                            setItemText(currNewNode[0][1],"Null")
                        else:
                            setItemText(prNode[2][1],getItemText(currNewNode[3]))
                            setItemText(currNewNode[0][1],getItemText(prNode[3]))
                    except IndexError:
                        print("")
                except IndexError:
                    try:
                        prNode = arr_Nodes[i - 1]
                        setItemText(prNode[2][1],"Null")
                    except IndexError:
                        print()

                decIndex()
                decX1()
            else:
                setError("List is empty.")
        else:
            if index == 0:
                setError("Enter value between 0 to 0.")
            else:
                setError("Enter value between 0 to "+str(index - 1)+".")
    else:
        setError("Only integer value is accepted.")
    lblHead()

def deleteNode(i):
    try:
        node = arr_Nodes[i]
        canvas.delete(node[0][0])
        canvas.delete(node[0][1])
        canvas.delete(node[1][0])
        canvas.delete(node[1][1])
        canvas.delete(node[2][0])
        canvas.delete(node[2][1])
        canvas.delete(node[3])
        canvas.delete(node[4])
        arr_Nodes.pop(i)
        return True
    except IndexError:
        return False

def deleteArrowNext(i):
    try:
        arrowNext = arr_arrow_next[i]
        canvas.delete(arrowNext)
        arr_arrow_next.pop(i)
        return True
    except IndexError:
        return False

def deleteArrowPrev(i):
    try:
        arrowPrev = arr_arrow_prev[i]
        canvas.delete(arrowPrev)
        arr_arrow_prev.pop(i)
        return True
    except IndexError:
        return False

def insertAtFront():
    global arr_Nodes,arr_arrow_next,arr_arrow_prev,x1
    lblHead()
    if getInpData():
        try:
            currFirstNode = arr_Nodes[0]
            arr_x1.append(x1)
            x1 = arr_x1[0]

            for i in range(len(arr_Nodes)):
                node = arr_Nodes[i]
                setItemText(node[4],"Node : "+str(i + 1))
                updateNodePosition(node,arr_x1[i+1])
            
            for i in range(len(arr_arrow_next)):
                updateArrow(i,arr_x1[i+2])

            newFirstNode = visualNode("Null",getInpData(),getItemText(currFirstNode[3]),"0")

            setItemText(currFirstNode[0][1],getItemText(newFirstNode[3]))

            x1 = arr_x1[1]

            arr_Nodes.insert(0,newFirstNode)
            arr_arrow_prev.insert(0,arrowPrev())
            arr_arrow_next.insert(0,arrowNext())

            x1 = arr_x1[len(arr_x1)-1]
            incX1()
            incIndex()
            canvas.configure(scrollregion=canvas.bbox("all"))
        except IndexError:
            newNode = visualNode("Null",getInpData(),"Null",index)
            arr_Nodes.append(newNode)
            arr_x1.append(x1)
            incIndex()
            incX1()
            lblHead()
            canvas.configure(scrollregion=canvas.bbox("all"))
    else:
        setError("Only integer value is accepted.")
    setError("")

def insertAfter():
    global arr_Nodes,arr_arrow_next,arr_arrow_prev,x1
    setError("")
    if getInpData():
        if getInpInsNode():
            if int(getInpInsNode()) >= 0 and int(getInpInsNode()) < index:
                try:
                    if int(getInpInsNode()) + 1 < index and int(getInpInsNode()) >= 0:

                        loc = int(getInpInsNode())
                        arr_x1.append(x1)
                        x1 = arr_x1[loc+2]

                        currNode = arr_Nodes[loc]
                        nodeAfterNew = arr_Nodes[loc+1]
                        newNode = visualNode(getItemText(currNode[3]),getInpData(),getItemText(nodeAfterNew[3]),loc+1)

                        setItemText(nodeAfterNew[0][1],getItemText(newNode[3]))
                        arr_Nodes.insert(loc+1,newNode)

                        nodeVal = loc + 2
                        for node in arr_Nodes[loc + 2:]:
                            updateNodePosition(node,x1)
                            setItemText(node[4],"Node : "+str(nodeVal))
                            nodeVal += 1
                            incX1()
                        
                        x1 = arr_x1[loc+2]
                        for parrow in arr_arrow_prev[loc:]:
                            canvas.coords(parrow, x1-110, y1+20, x1, y1+20)
                            incX1()
                        
                        x1 = arr_x1[loc+2]
                        for narrow in arr_arrow_next[loc:]:
                            canvas.coords(narrow, x1-110, y1+40, x1, y1+40)
                            incX1()
                        
                        x1 = arr_x1[loc +1]
                        arr_arrow_prev.insert(loc,arrowPrev())
                        arr_arrow_next.insert(loc,arrowNext())

                        x1 = arr_x1[len(arr_x1) - 1]
                        updateNodePosition(newNode,arr_x1[loc+1])

                        incX1()
                        incIndex()
                        canvas.configure(scrollregion=canvas.bbox("all"))
                    else:
                        insertAtEnd()
                except IndexError:
                    newNode = visualNode("Null",getInpData(),"Null",index)
                    arr_Nodes.append(newNode)
                    arr_x1.append(x1)
                    incIndex()
                    incX1()
                    lblHead()
                    canvas.configure(scrollregion=canvas.bbox("all"))
            else:
                if index > 0:
                    setError("Enter value between 0 to "+str(index - 1)+".")
                else:
                    setError("List is empty.")
        else:
            setError("Only integer value is accepted.")
    else:
        setError("Only integer value is accepted.")
    lblHead()

def insertBefore():
    global arr_Nodes,arr_arrow_next,arr_arrow_prev,x1
    setError("")
    if getInpData():
        if getInpInsNode():
            if int(getInpInsNode()) >= 0 and int(getInpInsNode()) < index:
                try:
                    if int(getInpInsNode()) < index and int(getInpInsNode()) > 0:

                        loc = int(getInpInsNode())
                        arr_x1.append(x1)
                        x1 = arr_x1[loc]

                        currNode = arr_Nodes[loc]
                        nodeBeforeNew = arr_Nodes[loc-1]
                        newNode = visualNode(getItemText(nodeBeforeNew[3]),getInpData(),getItemText(currNode[3]),loc+1)

                        setItemText(nodeBeforeNew[2][1],getItemText(newNode[3]))
                        setItemText(currNode[0][1],getItemText(newNode[3]))
                        arr_Nodes.insert(loc,newNode)

                        nodeVal = loc
                        for node in arr_Nodes[loc:]:
                            updateNodePosition(node,x1)
                            setItemText(node[4],"Node : "+str(nodeVal))
                            nodeVal += 1
                            incX1()
                        
                        x1 = arr_x1[loc+2]
                        for parrow in arr_arrow_prev[loc:]:
                            canvas.coords(parrow, x1-110, y1+20, x1, y1+20)
                            incX1()
                        
                        x1 = arr_x1[loc+2]
                        for narrow in arr_arrow_next[loc:]:
                            canvas.coords(narrow, x1-110, y1+40, x1, y1+40)
                            incX1()
                        
                        x1 = arr_x1[loc +1]
                        arr_arrow_prev.insert(loc,arrowPrev())
                        arr_arrow_next.insert(loc,arrowNext())

                        x1 = arr_x1[len(arr_x1) - 1]

                        incX1()
                        incIndex()
                        canvas.configure(scrollregion=canvas.bbox("all"))
                    else:
                        insertAtFront()
                except IndexError:
                    newNode = visualNode("Null",getInpData(),"Null",index)
                    arr_Nodes.append(newNode)
                    arr_x1.append(x1)
                    incIndex()
                    incX1()
                    lblHead()
                    canvas.configure(scrollregion=canvas.bbox("all"))
            else:
                if index > 0:
                    setError("Enter value between 0 to "+str(index - 1)+".")
                else:
                    setError("List is empty.")
        else:
            setError("Only integer value is accepted.")
    else:
        setError("Only integer value is accepted.")
    lblHead()

def resetValues():
    g = globals()

    g['window'] = None
    g['inpData'] = None
    g['inpInsNode'] = None
    g['inpDelNode'] = None
    g['canvas'] = None
    g['errorText'] = None

    g['arr_Nodes'] = []
    g['arr_arrow_prev'] = []
    g['arr_arrow_next'] = []

    g['arr_x1'] = []
    g['index'] = 0 
    g['x1'] = 100
    g['y1'] = 100

    g['head_txt'] = []
    g['head_arrow'] = []

def on_closing():
    window.destroy()
    resetValues()

def reset():
    window.destroy()
    resetValues()
    initDoublyList()
