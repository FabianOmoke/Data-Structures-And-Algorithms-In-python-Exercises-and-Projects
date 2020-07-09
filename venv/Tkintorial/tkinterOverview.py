from tkinter import *

root = Tk() #creating the root widget

e = Entry(root, bg="black", fg="white")
e.insert(0,"Your Name?")
e.grid(row=0, column=0)

def showMe():
    myLabel1 = Label(root, text="Hello World")
    myLabel2 = Label(root, text="Do you know who I am?")
    myLabel3 = Label(root, text=e.get())
    myLabel3.grid(row=3, column=0)
    myLabel1.grid(row=1, column=0)
    myLabel2.grid(row=2, column=0)


# initializing a Button in root with identifier Text whose state is DISABLED
myButton = Button(root, text="Click Me", command=showMe)


#Shove it to the screen and according to its current size
## myLabel1.pack()

#Using the grid system

myButton.grid(row=2, column=1)

root.mainloop()