from tkinter import *
from Array.widget import *
import time

# Globals
canvas = None
inpUpdateElement = None
inpElement = None
inpDelIndex = None
inpUpdateIndex = None
error = None
program = None
window = None

rect_empty_box = []
rect_data = []
txt_index = []
txt_data = []

index = -1
arr_elements = []

x1 = 100
y1 = 80

arr_x1 = []

def initDynamicArray():
    global canvas,inpUpdateElement,inpElement,inpDelIndex,inpUpdateIndex,error,program,window

    window = Tk()
    window.title("Visual Static Array")
    w, h = window.winfo_screenwidth(), window.winfo_screenheight() - 20
    window.geometry("%dx%d+0+0" % (w, h))

    try:
        window.state("zoomed")
    except TclError:
        print("Linux Error")

    lbl_heading(window, "Dynamic Array : ")
    lbl_text(window, "A dynamic array has memory allocated at run time.")
    lbl_text(window, "Run time is when the program is actually running.")
    lbl_text(window, "The elements of the dynamic array are stored contiguously at the start of the underlying array,")
    lbl_text(window, "and the remaining positions towards the end of the underlying array are reserved, or unused.")

    #----- Frame 1 Start -----#
    frame1 = Frame(window)

    #------- Section InsertAtEnd -------#
    entry_text(frame1, "• Element :")
    inpElement = entry(frame1, 10)
    btn_in_frame(frame1, "Insert",insert)

    #------- Section Update ------------#
    entry_text(frame1, "Index :")
    inpUpdateIndex = entry(frame1, 10)
    entry_text(frame1, "Element :")
    inpUpdateElement = entry(frame1, 10)
    btn_in_frame(frame1, "Update",update)

    entry_text(frame1, " | ")

    #------ Section Delete --------#
    entry_text(frame1, "Index :")
    inpDelIndex = entry(frame1, 10)
    btn_in_frame(frame1, "Delete",delete)

    entry_text(frame1, " | ")

    btn_in_frame(frame1, "Reset",reset)

    frame1.pack(anchor=W, pady=15)
    #----- Frame 1 End -------#

    error = lbl_error(window, "")
    program = Label(window, text="• Program : ",font=("Courier New", 10, 'bold'))
    program.pack(anchor=W, padx=15, pady=10)

    #----- Canvas Start ------#
    canvas = Canvas(window, width=500, height=800, bg="#FFF")
    canvas.pack(fill=BOTH, expand=True, anchor=W, padx=15, pady=15)

    scrollbar = Scrollbar(canvas, orient="horizontal", command=canvas.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    canvas.configure(xscrollcommand=scrollbar.set)

    #----- Canvas End -------#
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

def element(text,index):
    global rect_data,rect_empty_box,txt_data,txt_index

    id_rect_empty_box = canvas.create_rectangle(x1, y1, x1+90, y1+80, width=2)
    id_txt_index = canvas.create_text(x1+40, y1+100, text=str(index))
    id_rect_data = canvas.create_rectangle(x1+10, y1 + 10, x1 + 80, y1 + 70, fill="#ffd28c")
    id_txt_data = canvas.create_text(x1+45, y1+40, text=str(text))

    rect_empty_box.append(id_rect_empty_box)
    rect_data.append(id_rect_data)
    txt_index.append(id_txt_index)
    txt_data.append(id_txt_data)

    return id_rect_data, id_txt_data, id_rect_empty_box, id_txt_index

def incX1():
    global x1
    x1 += 90

def incIndex():
    global index
    index += 1

def getDelIndex():
    try:
        inp = int(inpDelIndex.get())
        return str(inp)
    except ValueError:
        return False

def getInsertText():
    try:
        inp = str(int(inpElement.get()))
        if len(inp) > 4:
            inp = inp[0:4]
            inp += ".."
            return inp
        else:
            return inp
    except ValueError:
        return False

def getUpdateText():
    try:
        inp = str(int(inpUpdateElement.get()))
        if len(inp) > 4:
            inp = inp[0:4]
            inp += ".."
            return inp
        else:
            return inp
    except ValueError:
        return False

def insert():
    updateProgram("")
    if getInsertText():
        setError("")
        incIndex()
        updateProgram("array["+str(index)+"] = "+str(inpElement.get())+";")
        element(getInsertText(),index)
        arr_elements.append(getInsertText())
        arr_x1.append(x1)
        incX1()
        canvas.configure(scrollregion=canvas.bbox("all"))
    else:
        setError("Only integer value is accepted.")

def getUpdateIndex():
    try:
        inp = int(inpUpdateIndex.get())
        return str(inp)
    except ValueError:
        return False

def update():
    updateProgram("")
    if getUpdateIndex():
        setError("")
        if getUpdateText():
            try:
                i = int(getUpdateIndex())
                txt = getUpdateText()
                updateProgram("array["+str(i)+"] = "+str(inpUpdateElement.get())+";")
                arr_elements[i] = txt
                canvas.itemconfig(txt_data[i], text=str(txt))
            except IndexError:
                if index == -1:
                    setError("Array is empty.")
                    updateProgram("Java Exception : IndexOutOfBoundsException | Python Exception : IndexError")
                else:
                    setError("Enter value between 0 to "+str(index)+".")
                    updateProgram("Java Exception : IndexOutOfBoundsException | Python Exception : IndexError")
        else:
            setError("Element value must be Numeric.")
    else:
        setError("Index must be Numeric.")

def setError(err):
    global error
    error.config(text=str("• Error : "+err))

def reCreateElement(i):
    try:
        element = str(arr_elements[i])
        x = arr_x1[i]
        id_rect_data = canvas.create_rectangle(x+10, y1 + 10, x + 80, y1 + 70, fill="#ffd28c")
        id_txt_data = canvas.create_text(x+45, y1+40, text=element)

        rect_data[i] = id_rect_data
        txt_data[i] = id_txt_data
    except IndexError:
        arr_x1.pop(i)

def delete():
    setError("")
    updateProgram("")
    if getDelIndex():
        inpIndex = int(getDelIndex())
        if index == -1:
            setError("Array is empty.")
            updateProgram("Java Exception : IndexOutOfBoundsException | Python Exception : IndexError")
        elif inpIndex < 0 or inpIndex > index:
            try: 
                data = rect_empty_box[inpIndex]
                updateProgram("array["+str(inpIndex)+"] = null;  srinkArray();")
            except IndexError:
                setError("Enter value between 0 to "+str(index)+".")
                updateProgram("Java Exception : IndexOutOfBoundsException | Python Exception : IndexError")
        else:
            arr_elements.pop(inpIndex)

            updateProgram("array["+str(inpIndex)+"] = null; srinkArray();")

            for i in range(inpIndex,index+1):
                deleteDataBox(i)
                reCreateElement(i)

            rect_data.pop(i)
            txt_data.pop(i)

            decX1()
            decIndex()

    else:
        setError("Index must be Numeric.")

def deleteDataBox(i):
    canvas.delete(txt_data[i])
    canvas.delete(rect_data[i])

def decX1():
    global x1
    x1 -= 90

def decIndex():
    global index
    index -= 1

def updateProgram(data):
    program.config(text="• Program : "+str(data))

def reset():
    window.destroy()
    resetValues()
    initDynamicArray()

def resetValues():
    g = globals()
    g['canvas'] = None
    g['inpUpdateElement'] = None
    g['inpElement'] = None
    g['inpDelIndex'] = None
    g['inpUpdateIndex'] = None
    g['error'] = None
    g['program'] = None
    g['window'] = None

    g['rect_empty_box'] = []
    g['rect_data'] = []
    g['txt_index'] = []
    g['txt_data'] = []

    g['index'] = -1
    g['arr_elements'] = []

    g['x1'] = 100
    g['y1'] = 80

    g['arr_x1'] = []

def on_closing():
    window.destroy()
    resetValues()