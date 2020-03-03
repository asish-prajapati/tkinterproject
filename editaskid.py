from tkinter import *
import studentData,editmain,sqlite3
import tkinter.messagebox as msgbox
def askid(root):
    global askidframe
    askidframe=Frame(root,width=900,height=400)
    askidframe.pack(side=RIGHT,fill=Y)
    Label(askidframe, text='search', font=('arial', 5)).place(x=0, y=0)
    Label(askidframe,text='ENTER REG ID').place(x=250,y=200)
    askidentry=Entry(askidframe,textvariable=StringVar())
    askidentry.place(x=350,y=200)
    askidbutton=Button(askidframe,text='Edit',bg='red',command=lambda :editaction(root,askidentry))
    askidbutton.place(x=500,y=200)

    back4=Button(askidframe,text='Back',bg='brown',command=lambda :back4action(root))
    back4.place(x=350,y=350)


def askidframedest():
    if 'askidframe' in globals():
        askidframe.destroy()
    else:
        pass

def back4action(root):
    askidframedest()
    studentData.studentdata(root)

def editaction(root,askidentry):
    idgot=askidentry.get()

    askidframedest()
    con = sqlite3.connect('PARAMOUNT')
    result = con.execute('select * from studenttable where Reg_No="{}"'.format(idgot))
    l = list(result)
    if len(l)==0 : # TRUR FALSE
        msgbox.showinfo('Error','Enter Valid Reg No.')
        askidframedest()
        askid(root)
    else:
        editmain.edit(root,idgot,l)