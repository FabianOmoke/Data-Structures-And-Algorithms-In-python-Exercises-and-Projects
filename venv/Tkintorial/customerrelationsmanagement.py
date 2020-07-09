from tkinter import *
from PIL import ImageTk, Image
import mysql.connector

root = Tk()
root.title("Customer Relations")
root.geometry("400x400")

mydb = mysql.connector.connect(
    host = "",
    user = ""

)