from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox as msgbox
import mainFrame,welcomeFrame,logOut,signupwindow,sqlite3


def adminlogin(root):
    global loginframe
    loginframe = Frame(root, width=300,height=400,borderwidth=0)
    loginframe.pack(side=LEFT,fill=Y)
    image = Image.open('loginimage.jpg')
    global  img
    img = ImageTk.PhotoImage(image)
    Label(loginframe, image=img).place(x=0, y=0)
    Label(loginframe, text='adminLogin', font=('Helvetica', 5), fg='#7F0000').place(x=0,y=0)
    userLabel=Label(loginframe,text='ADMIN',font=('Helvetica',11,'bold'),fg='#7F0000')
    userLabel.place(x=20,y=120)
    userEntry=Entry(loginframe,textvariable=StringVar())
    userEntry.place(x=120,y=120)
    passLabel = Label(loginframe,text='PASSWORD',font=('Helvetica',11,'bold'),fg='#7F0000')
    passLabel.place(x=20, y=180)
    passEntry = Entry(loginframe, textvariable=StringVar(),show='*')
    passEntry.place(x=120, y=180)

    Button(loginframe,text='  Login  ',cursor='hand2',bg='#4F5BDB',fg='white',command=lambda:loginaction(userEntry,passEntry,root)).place(x=190,y=220)
    Button(loginframe,text=' Sign Up ',cursor='hand2',bg='#4F5BDB',fg='white',command=lambda:signupaction()).place(x=120,y=220)
def loginaction(userEntry,passEntery,root):
    con = sqlite3.connect('PARAMOUNT')
    a=userEntry.get()
    b=passEntery.get()  #userentry and passentry are Entryobject
    idlist = []
    passlist = []
    idholder = con.execute("select admin_id from admindetail")
    for idtuple in idholder:
        for idstring in idtuple:
            idlist.append(idstring)
    passholder = con.execute("select password from admindetail")
    for passtuple in passholder:
        for passstring in passtuple:
            passlist.append(passstring)
    if (a in idlist) and (b in passlist):

        msgbox.showinfo('True','Successfully Logged IN')
        welcomeFrame.welcomedest()
        mainFrame.main(root)
        adminlogindest()
        logOut.logout(root)

    else:
        msgbox.showinfo('False','Wrong ID/PASS')
def signupaction():
    signupwindow.signup()

def adminlogindest():
    loginframe.destroy()