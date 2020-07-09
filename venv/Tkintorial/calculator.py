from tkinter import *

calculator = Tk()
calculator.title("Simple Calculator")

inputScreen = Entry(calculator, borderwidth=5, width= 35)
inputScreen.grid(row=0, column=0, columnspan=3, padx=10, pady= 10)

# ARITHMETIC FUNCTIONS
def button_click(number):
    # inputScreen.delete(0,END) # initially for testing purposes
    # inputScreen.insert(0,number) # inserts from the front(0)
    inputScreen.insert(END, number)

def button_clear():
    inputScreen.delete(0, END)

def button_add():
    fnum = inputScreen.get()
    global firstNumber
    global math
    math = "addition"
    firstNumber = int(fnum)
    inputScreen.delete(0,END)

def button_equals():
    seconnd_num = inputScreen.get()
    inputScreen.delete(0,END)

    if math == "addition":
        inputScreen.insert(0, int(seconnd_num) + int(firstNumber))
    if math == "multiplication":
        inputScreen.insert(0, int(seconnd_num) * int(firstNumber))
    if math == "division":
        inputScreen.insert(0, int(firstNumber) / int(seconnd_num))
    if math == "subtraction":
        inputScreen.insert(0, int(firstNumber)- int(seconnd_num))





def button_multiply():
    fnum = inputScreen.get()
    global firstNumber
    global math
    math = "multiplication"
    firstNumber = int(fnum)
    inputScreen.delete(0, END)


def button_division():
    fnum = inputScreen.get()
    global firstNumber
    global math
    math = "division"
    firstNumber = int(fnum)
    inputScreen.delete(0, END)


def button_subtract():
    fnum = inputScreen.get()
    global firstNumber
    global math
    math = "subtraction"
    firstNumber = int(fnum)
    inputScreen.delete(0, END)


# Button declarations grouped as they will appear
buttonOne = Button(calculator, text = "1", padx=40, pady=20, command = lambda: button_click(1))
buttonTwo = Button(calculator, text = "2", padx=40, pady=20, command = lambda: button_click(2))
buttonThree = Button(calculator, text = "3", padx=40, pady=20, command = lambda: button_click(3))

buttonFour = Button(calculator, text = "4", padx=40, pady=20, command = lambda: button_click(4))
buttonFive = Button(calculator, text = "5", padx=40, pady=20, command = lambda: button_click(5))
buttonSix = Button(calculator, text = "6", padx=40, pady=20, command = lambda: button_click(6))

buttonSeven = Button(calculator, text = "7", padx=40, pady=20, command = lambda: button_click(7))
buttonEight = Button(calculator, text = "8", padx=40, pady=20, command = lambda: button_click(8))
buttonNine = Button(calculator, text = "9", padx=40, pady=20, command = lambda: button_click(9))

buttonZero = Button(calculator, text = "0", padx=40, pady=20, command = lambda: button_click(0))

buttonAdd = Button(calculator, text = "+", padx=40, pady=20, command = button_add)
buttonEquals= Button(calculator, text = "=", padx=90, pady=20, command = button_equals)
buttonClear= Button(calculator, text = "Clear", padx=80, pady=20, command = button_clear)

buttonMultiply = Button(calculator, text = "x", padx=42, pady=20, command = button_multiply)
buttonDivide = Button(calculator, text = "/", padx=40, pady=20, command = button_division)
buttonSubtract = Button(calculator, text = "-", padx=42, pady=20, command = button_subtract)




# Button positioning on the Grid
buttonOne.grid(row=3, column=0)
buttonTwo.grid(row=3, column=1)
buttonThree.grid(row=3, column=2)

buttonFour.grid(row=2, column=0)
buttonFive.grid(row=2, column=1)
buttonSix.grid(row=2, column=2)

buttonSeven.grid(row=1, column=0)
buttonEight.grid(row=1, column=1)
buttonNine.grid(row=1, column=2)

buttonZero.grid(row=4, column=0)

buttonAdd.grid(row=5, column=0)
buttonEquals.grid(row=5,column=1, columnspan=2) #spans 2 columns
buttonClear.grid(row=4, column=1, columnspan=2)  #spans 2 columns
buttonSubtract.grid(row=6, column=0)
buttonMultiply.grid(row=6, column=1)
buttonDivide.grid(row=6, column=2)






calculator.mainloop()