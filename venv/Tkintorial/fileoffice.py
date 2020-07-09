from tkinter import *
from tkinter import filedialog

myoffice = Tk()

def browser():

    filename = filedialog.askopenfilename(initialdir="/", title ="Select File", filetypes=
    (("Text Files", "*.txt*"),("All files","*.*")))
    if filename == "":
        label_file_explorer.configure(text="No file Opened Yet")
    else:
        label_file_explorer.configure(text="File Opened: " + filename)

    return filename

def readFile():
    filename = browser()
    fname = open(str(filename),"r")
    content = fname.read()
    label_file_explorer.configure(text=str(content))


def updateFile():
    filename = browser()
    fname = open(str(filename),"a")
    retrieve_input(fname)



def retrieve_input(fname):
    input = entry_box.get("1.0", "end")
    # get text from our textbox from the first line , 0th character and delete the automatic newline character textboxes
    # include
    fname.write("\n" +input)
    fname.close()




# Set window title
myoffice.title('File Explorer')


# Set window background color
myoffice.config(background="white")


label_file_explorer = Label(myoffice,
                            text="File Explorer using Tkinter",
                            width=100, height=4,
                            fg="blue")

label_file_update = Label(myoffice,
                            text="You Can Enter Your Update Text Below", fg="blue")

entry_box=Text(myoffice)

button_explore = Button(myoffice,
                        text="Browse Files",
                        command=browser)

button_read = Button(myoffice,
                    text="Read",
                    command=readFile)


button_update = Button(myoffice,
                    text="Update",
                    command=updateFile)


button_exit = Button(myoffice,
                    text="Exit",
                    command=exit)


# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns


label_file_explorer.grid(column=1, row=1)

label_file_update.grid(column=1, row=2)

entry_box.grid(column=1, row=3)

button_explore.grid(column=1, row=4)

button_read.grid(column=1, row=5)

button_update.grid(column=1, row=6)

button_exit.grid(column=1, row=7)

myoffice.mainloop()