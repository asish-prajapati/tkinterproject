from tkinter import *
import mainFrame,search,editaskid
import tkinter.messagebox as msgbox
def studentdata(root):
    global studataframe
    studataframe=Frame(root,width=900,height=400,bg='#1d1d1d')
    studataframe.pack(side=RIGHT, fill=Y)
    Label(studataframe,text='studentData',font=('Helvetica', 5), bg='#1d1d1d', fg='white').place(x=0,y=0)
    Label(studataframe, text='Search By ID', font=('Helvetica', 11), bg='#1d1d1d', fg='white').place(x=200, y=80)
    idquery = Entry(studataframe, font=('Helvetica', 11), textvariable=StringVar())
    idquery.place(x=350, y=80)
    idquery.insert(0,'eseee')
    Button(studataframe, text='Search', font=('Helvetica',8), width=11, bg='#3E766D', fg='#e0ebeb',command=lambda:searchaction1(root,idquery)).place(x=600, y=80)

    Label(studataframe, text='Search By Name', font=('Helvetica', 11), bg='#1d1d1d', fg='white').place(x=200, y=130)
    namequery = Entry(studataframe, font=('Helvetica', 11), textvariable=StringVar())
    namequery.place(x=350, y=130)
    Button(studataframe, text='Search', font=('Helvetica', 8), width=11, bg='#3E766D', fg='#e0ebeb',command=lambda:searchaction2(root,namequery)).place(x=600, y=130)

    Label(studataframe, text='Search By Course', font=('Helvetica', 11), bg='#1d1d1d', fg='white').place(x=200, y=180)
    coursequery = Entry(studataframe, font=('Helvetica', 11), textvariable=StringVar())
    coursequery.place(x=350, y=180)
    Button(studataframe, text='Search', font=('Helvetica', 8), width=11, bg='#3E766D', fg='#e0ebeb',command=lambda:searchaction3(root,coursequery)).place(x=600, y=180)

    Button(studataframe, text='Back', font=('Helvetica', 11), width=11, bg='#3E766D', fg='#e0ebeb',command=lambda :backaction2(root)).place(x=350, y=300)
    Button(studataframe, text='Edit Data', font=('Helvetica', 11), width=11, bg='#856363', fg='#e0ebeb',command=lambda :editdataaction(root)).place(x=600, y=300)

def studataframedest():
    if 'studataframe' in globals():
        studataframe.destroy()
    else:
        pass

def backaction2(root):
    studataframedest()
    mainFrame.main(root)

def searchaction1(root,idquery):
    y=idquery.get()
    x = 'Reg_No'
    if not idquery.get():
        msgbox.showinfo('Error','Please Enter Something')
    elif y.isspace():
        msgbox.showinfo('Error','All Spaces not Allowed')
        idquery.delete(0, END)
    else:
        studataframedest()
        search.searchfun(root,x,y)

def searchaction2(root,namequery):

    y=namequery.get()
    x = 'Student_Name'
    if not namequery.get():
        msgbox.showinfo('Error', 'Please Enter Something')
    elif y.isspace():
        msgbox.showinfo('Error', 'All Spaces not Allowed')
        namequery.delete(0,END)
    else:
        studataframedest()
        search.searchfun(root, x,y)
def searchaction3(root,coursequery):
    y=coursequery.get()
    x='Course'
    if not coursequery.get():
        msgbox.showinfo('Error', 'Please Enter Something')
    elif y.isspace():
        msgbox.showinfo('Error', 'All Spaces not Allowed')
        coursequery.delete(0,END)
    else:
        studataframedest()
        search.searchfun(root, x,y)
def editdataaction(root):
    studataframedest()
    editaskid.askid(root)
