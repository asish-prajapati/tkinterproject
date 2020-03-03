from tkinter import *
import registrationForm,studentData
def main(root):
    global mainframe
    mainframe=Frame(root,width=900,height=400,bg='#1d1d1d')
    mainframe.pack(side=RIGHT, fill=Y)
    Label(mainframe,text='mainframe',font=('arial',5)).place(x=0,y=0)
    Button(mainframe,text='New Registration',font=('Helvetica',20),bg='#333333',foreground='#e7e7ea',activebackground='#453D3D',activeforeground='#eff4ff',command=lambda :regaction(root)).place(x=150,y=170)
    Button(mainframe, text='  Students Data  ', font=('Helvetica', 20), bg='#333333',foreground='#e7e7ea',activebackground='#453D3D', activeforeground='#eff4ff',command=lambda :studataaction(root)).place(x=500, y=170)
def regaction(root):
    mainframedest()
    registrationForm.registration(root)

def studataaction(root):
    mainframedest()
    studentData.studentdata(root)
def mainframedest():
    mainframe.destroy()