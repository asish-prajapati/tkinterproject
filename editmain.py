from tkinter import *
import editaskid,sqlite3
import tkinter.messagebox as msgbox
def edit(root,idgot,l):
        global editmainframe
        editmainframe = Frame(root, width=900, height=400)
        editmainframe.pack(side=RIGHT, fill=Y)
        Label(editmainframe, text='editmain', font=('arial', 5)).place(x=0, y=0)

        j = list(l[0])
        Label(editmainframe, text='Student Name').place(x=200, y=30)
        editNameEntry = Entry(editmainframe, textvariable=StringVar())
        editNameEntry.place(x=400, y=30)
        editNameEntry.insert(0, j[1])

        Label(editmainframe, text='Father Name').place(x=200, y=80)
        editFatherEntry = Entry(editmainframe, textvariable=StringVar())
        editFatherEntry.place(x=400, y=80)
        editFatherEntry.insert(0, j[2])

        Label(editmainframe, text='Hometown').place(x=200, y=130)
        editHomeEntry = Entry(editmainframe, textvariable=StringVar())
        editHomeEntry.place(x=400, y=130)
        editHomeEntry.insert(0, j[3])

        Label(editmainframe, text='Mobile No').place(x=200, y=180)
        editMobEntry = Entry(editmainframe, textvariable=StringVar())
        editMobEntry.place(x=400, y=180)
        editMobEntry.insert(0, j[4])

        Label(editmainframe, text='Course').place(x=200, y=230)
        variable = StringVar(editmainframe)
        variable.set(j[5])
        course = OptionMenu(editmainframe, variable, 'SSC JEN', "PATWAR", "SBI PO", "IBPS PO", "RAILWAY",
                            "INFORMATIC ASSISTANT", "STENO")
        course.config(width="20", bd=2)
        course.place(x=400, y=230)

        Label(editmainframe, text='Course Fee').place(x=200, y=280)
        editFeeEntry = Entry(editmainframe, textvariable=StringVar())
        editFeeEntry.place(x=400, y=280)
        editFeeEntry.insert(0, j[6])

        Label(editmainframe, text='Fee Deposit').place(x=200, y=330)
        editFeeDepEntry = Entry(editmainframe, textvariable=StringVar())
        editFeeDepEntry.place(x=400, y=330)
        editFeeDepEntry.insert(0, j[7])

        Button(editmainframe,text='Back',bg='red',command=lambda:backaction4(root)).place(x=300,y=370)
        Button(editmainframe, text='Submit Change', bg='red',command=lambda :submitchangeaction(editNameEntry,editFatherEntry,editHomeEntry,editMobEntry,variable,editFeeEntry,editFeeDepEntry,idgot,root)).place(x=430, y=370)
def editmainframedest():
    if 'editmainframe' in globals():
        editmainframe.destroy()
    else:
        pass
def backaction4(root):
    editmainframedest()
    editaskid.askid(root)

def submitchangeaction(editNameEntry,editFatherEntry,editHomeEntry,editMobEntry,variable ,editFeeEntry,editFeeDepEntry,idgot,root):
    a=editNameEntry.get()
    b=editFatherEntry.get()
    c=editHomeEntry.get()
    dv=editMobEntry.get()
    e=variable.get()
    fv=editFeeEntry.get()
    gv=editFeeDepEntry.get()
    if not editNameEntry.get():
        msgbox.showinfo('error','Student Name can not be empty')
    elif a.isspace() :
        msgbox.showinfo('error','All Space not allowed')
    elif not editFatherEntry.get():
        msgbox.showinfo('error','Father Name can not be empty')
    elif b.isspace() :
        msgbox.showinfo('error','All Space not allowed')
    elif not editHomeEntry.get():
        msgbox.showinfo('error','HomeTown can not be empty')
    elif c.isspace() :
        msgbox.showinfo('error','All Space not allowed')
    elif not editMobEntry.get():
        msgbox.showinfo('error','Mobile No can not be empty')
    elif not dv.isdigit():
        msgbox.showinfo('error','Only Digits Allowed in Mobile No')
    elif dv.isspace() :
        msgbox.showinfo('error','All Space not allowed')

    elif not editFeeEntry.get():
        msgbox.showinfo('error','Course Fee can not be empty')
    elif not fv.isdigit():
        msgbox.showinfo('error','Only Digits Allowed in Fee Course Fee')
    elif fv.isspace() :
        msgbox.showinfo('error','All Space not allowed')
    elif not editFeeEntry.get():
        msgbox.showinfo('error','Fee Deposit can not be empty')
    elif not fv.isdigit():
        msgbox.showinfo('error','Only Digits Allowed in Fee Deposit')
    elif fv.isspace() :
        msgbox.showinfo('error','All Space not allowed')
    else:
        d = int(dv)
        f = int(fv)
        g = int(gv)
        con=sqlite3.connect('PARAMOUNT')
        con.execute("UPDATE studenttable SET Student_Name='{}',Father_Name='{}',Hometown='{}',Mobile_No='{}',Course='{}',Course_Fee='{}',Fee_Deposit='{}',Remaining_Fee='{}' WHERE Reg_No = '{}'".format(a,b,c,d,e,f,g,f-g,idgot))
        con.commit()
        con.close()
        msgbox.showinfo('Success','Data Updated')
        editmainframedest()
        editaskid.askid(root)



