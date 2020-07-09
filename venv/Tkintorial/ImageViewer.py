from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")


my_img = ImageTk.PhotoImage(Image.open("me.jpg")) #Declare an Image
mylabel = Label(image=my_img) #Display it in a label
mylabel.pack()

button_quit = Button(root, text ="Exit program", command=root.quit)
button_quit.pack()

root.mainloop()