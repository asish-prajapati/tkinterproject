from tkinter import *
from PIL import ImageTk,Image
def welcome(root):
    global welcomeframe
    welcomeframe=Frame(root,width=900,height=400)
    welcomeframe.pack(side=RIGHT,fill=Y)

    image = Image.open('welcomeimage.jpg')
    global img
    img = ImageTk.PhotoImage(image)
    Label(welcomeframe, image=img).place(x=0, y=0)
    Label(welcomeframe, text='welcomeframe', font=('arial', 5), ).place(x=0, y=0)

def welcomedest():
    welcomeframe.destroy()