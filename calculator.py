#calculator application

from tkinter import *



root = Tk()
root.title("Calculator")


def end():
    root.destroy()

def inp(digit):
    if display["text"] == "0":
        display["text"] = str(digit)
    else:
        display["text"] = display["text"] + str(digit)

def operation(sign):
    if display["text"] != "0":
        display["text"] = display["text"] + sign


def clear():
    display["text"] = "0"

def square():
    v1 = display["text"]
    result = float(v1) ** 2
    display["text"] = str(result)

def sroot():
    v1 = display["text"]
    result = float(v1) ** (1/2)
    display["text"] = str(result)

def enter():
    try:
        solution = eval(display["text"])
        display["text"] = str(solution)
    except:
        display["text"] = "ERROR"

def dot():
    display["text"] = display["text"] + "."


display =  Label(root, text = "0", borderwidth = 1)
display.pack()

r1 = Frame(root)
r1.pack(fill = X, expand = True)

clear = Button(r1, text = "CA", command = clear)
clear.grid(row=0, column=0)
square = Button(r1, text = "^2", command = square)
square.grid(row = 0, column = 1)
sroot = Button(r1, text = "^1/2", command = sroot)
sroot.grid(row = 0, column = 2)
divide =  Button(r1, text = "/", command = lambda: operation("/"))
divide.grid(row = 0, column = 3)

seven =  Button(r1, text = "7", command = lambda: inp(7))
seven.grid(row=1, column=0)
eight =  Button(r1, text = "8", command = lambda: inp(8))
eight.grid(row = 1, column = 1)
nine =  Button(r1, text = "9", command = lambda: inp(9))
nine.grid(row = 1, column = 2)
multiply =  Button(r1, text = "X", command = lambda: operation("*"))
multiply.grid(row = 1, column = 3)

four =  Button(r1, text = "4", command = lambda: inp(4))
four.grid(row=2, column=0)
five =  Button(r1, text = "5", command = lambda: inp(5))
five.grid(row = 2, column = 1)
six =  Button(r1, text = "6", command = lambda: inp(6))
six.grid(row = 2, column = 2)
subtract =  Button(r1, text = "-", command = lambda: operation("-"))
subtract.grid(row = 2, column = 3)

one =  Button(r1, text = "1", command = lambda: inp(1))
one.grid(row = 3, column=0)
two =  Button(r1, text = "2", command = lambda: inp(2))
two.grid(row = 3, column = 1)
three =  Button(r1, text = "3", command = lambda: inp(3))
three.grid(row = 3, column = 2)
add =  Button(r1, text = "+", command = lambda: operation("+"))
add.grid(row = 3, column = 3)

zero =  Button(r1, text = "0", command = lambda: inp(0))
zero.grid(row = 4, column=0)
point =  Button(r1, text = ".", command = dot)
point.grid(row = 4, column = 1)

enter =  Button(r1, text = "=", command = enter)
enter.grid(row = 4, column = 3)

endB =  Button(root, text = "Quit", command = end)
endB.pack()



root.mainloop()

