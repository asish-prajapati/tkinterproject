from tkinter import *
from PIL import ImageTk,Image
import adminLogin,welcomeFrame,mainFrame,registrationForm,studentData,search,editaskid,editmain

def logout(root):
    global logoutframe
    logoutframe = Frame(root, width=300,height=400,borderwidth=0)
    logoutframe.pack(side=LEFT,fill=Y)
    image = Image.open('loginimage.jpg')
    global  img
    img = ImageTk.PhotoImage(image)
    Label(logoutframe, image=img).place(x=0, y=0)
    Label(text='logOut', font=('Helvetica', 5)).place(x=0, y=0)
    Label(text='W',font=('Helvetica',15,'bold')).place(x=38,y=145)
    Label(text='elcome Admin',font=('Helvetica',12)).place(x=60, y=150)
    Button(logoutframe, text=' Logout ',bg='red',fg='white', command=lambda:reset(root)).place(x=190, y=220)
def reset(root):
    logoutframe.destroy()
    mainFrame.mainframedest()
    registrationForm.regframedest()
    studentData.studataframedest()
    editaskid.askidframedest()
    search.searchframedest()
    editmain.editmainframedest()
    adminLogin.adminlogin(root)
    welcomeFrame.welcome(root)

