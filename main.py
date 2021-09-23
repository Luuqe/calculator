"""
The goal of this project is to create a simplistic calculator providing;
Multiplication
Addition
Subtraction
Division
"""

from tkinter import *
import parser

"""
i is used to keep the position of the current number in the input field
reset is used for when = is pressed, its used so that after = is pressed the input field will be cleared if another number is attempted to be entered
"""
i = 0
reset = 0

root = Tk()
root.title('Calculator')


display = Entry(root)
display.grid(row=1, columnspan=6, sticky=N+E+S+W)


# Recieves the number based on the button pressed and displays it on the input field
def getVariables(num):
    global i
    global reset
    if reset == 1:
        clearAll()
        reset = 0
    display.insert(i, num)
    i += 1


# clears the input field
def clearAll():
    display.delete(0, END)


# recieves the operator as a parameter, which is put into the input field
# resets the reset counter to 0 as an operation has been pressed, the next number wont clear the field
def getOperation(operator):
    global i
    global reset
    reset = 0
    length = len(operator)
    display.insert(i, operator)
    i += length


# the input is retrieved from the field, the parser module is used to scan the string
# the string is then accepted into the eval function to give a result that displays in the input field
def equals():
    input = display.get()
    global reset
    reset = 1
    try:
        x = parser.expr(input).compile()
        total = eval(x)
        clearAll()
        display.insert(0, total)
    except Exception:
        clearAll()
        display.insert(0, "Error")


# GUI setup
Button(root, text=1, command=lambda: getVariables(1)).grid(row=2, column=0, sticky=N+E+S+W)
Button(root, text=2, command=lambda: getVariables(2)).grid(row=2, column=1, sticky=N+E+S+W)
Button(root, text=3, command=lambda: getVariables(3)).grid(row=2, column=2, sticky=N+E+S+W)

Button(root, text=4, command=lambda: getVariables(4)).grid(row=3, column=0, sticky=N+E+S+W)
Button(root, text=5,command=lambda: getVariables(5)).grid(row=3, column=1, sticky=N+E+S+W)
Button(root, text=6,command=lambda: getVariables(6)).grid(row=3, column=2, sticky=N+E+S+W)

Button(root, text=7, command=lambda: getVariables(7)).grid(row=4, column=0, sticky=N+E+S+W)
Button(root, text=8, command=lambda: getVariables(8)).grid(row=4, column=1, sticky=N+E+S+W)
Button(root, text=9, command=lambda: getVariables(9)).grid(row=4, column=2, sticky=N+E+S+W)

Button(root, text="C", command=lambda: clearAll()).grid(row=5, column=0, sticky=N+E+S+W)
Button(root, text=" 0", command=lambda: getVariables(0)).grid(row=5, column=1, sticky=N+E+S+W)
Button(root, text=" .", command=lambda: getVariables(".")).grid(row=5, column=2, sticky=N+E+S+W)

Button(root, text="+", command=lambda: getOperation("+")).grid(row=2, column=3, sticky=N+E+S+W)
Button(root, text="-", command=lambda: getOperation("-")).grid(row=3, column=3, sticky=N+E+S+W)
Button(root, text="*", command=lambda: getOperation("*")).grid(row=4, column=3, sticky=N+E+S+W)
Button(root, text="/", command=lambda: getOperation("/")).grid(row=5, column=3, sticky=N+E+S+W)
Button(root, text="=", command=lambda: equals()).grid(row=5, column=4, sticky=N+E+S+W)

root.mainloop()
