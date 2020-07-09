
from tkinter import *

master = Tk()

def soma():
    fp = open(r'C:\Users\BEAST\Desktop\plans.txt', 'r')
    print(fp.read())

readFile = Button(master, text = 'Read Document', command=soma)
readFile.pack()

mainloop()

