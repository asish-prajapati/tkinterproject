from tkinter import *
import mainFrame,sqlite3
import tkinter.messagebox as msgbox


def registration(root):
    global regframe
    regframe=Frame(root,width=900,height=400,bg='#1d1d1d')
    regframe.pack(side=RIGHT, fill=Y)
    Label(regframe, text='Registration Form', font=('Helvetica', 5), bg='#1d1d1d', fg='white').place(x=0, y=0)
    Label(regframe,text='Registration No.',font=('Helvetica',11),bg='#1d1d1d',fg='white').place(x=300,y=20)
    regno=Entry(regframe,font=('Helvetica',11),textvariable=StringVar())
    regno.place(x=450,y=20)




    con = sqlite3.connect('PARAMOUNT')
    con.execute(
        'create table if not exists studenttable (id integer primary key AUTOINCREMENT,Reg_No char[8], Student_Name char[20],Father_Name char[20],Hometown char[10],Mobile_No int[10],Course char[10],Course_Fee int[5],Fee_Deposit int[5],Remaining_Fee int[5])')
    con.commit()

    idholder1 = con.execute("select * from studenttable order by id desc limit 1")
    idlist = list(idholder1)
    idtuple = idlist[0]
    lastid= idtuple[0]
    con.close()

    regno.insert(0,'eseee{}'.format(lastid+1))


    Label(regframe, text='Student Name', font=('Helvetica', 11), bg='#1d1d1d', fg='white').place(x=300, y=55)
    studentname=Entry(regframe, font=('Helvetica', 11), textvariable=StringVar())
    studentname.place(x=450, y=55)


    Label(regframe, text='Father Name', font=('Helvetica', 11), bg='#1d1d1d', fg='white').place(x=300, y=90)
    fathername=Entry(regframe, font=('Helvetica', 11), textvariable=StringVar())
    fathername.place(x=450, y=90)


    Label(regframe, text='Hometown', font=('Helvetica', 11), bg='#1d1d1d', fg='white').place(x=300, y=125)
    hometown = Entry(regframe, font=('Helvetica', 11), textvariable=StringVar())
    hometown.place(x=450, y=125)


    Label(regframe, text='Mobile No.', font=('Helvetica', 11), bg='#1d1d1d', fg='white').place(x=300, y=160)
    mobno = Entry(regframe,textvariable=StringVar(), font=('Helvetica', 11))
    mobno.place(x=450, y=160)


    #mobno.insert(0,"")
    
    Label(regframe, text='Course', font=('Helvetica', 11), bg='#1d1d1d', fg='white').place(x=300, y=195)
    variable = StringVar(regframe)
    variable.set("SSC JEN")
    course = OptionMenu(regframe, variable,'SSC JEN', "PATWAR", "SBI PO", "IBPS PO", "RAILWAY", "INFORMATIC ASSISTANT", "STENO")
    course.config(width="20", bd=2)
    course.place(x=450, y=195)

    # course = Entry(regframe, font=('Helvetica', 11), textvariable=StringVar()).place(x=450, y=195)

    Label(regframe, text='Course Fee', font=('Helvetica', 11), bg='#1d1d1d', fg='white').place(x=300, y=234)
    coursefee = Entry(regframe,textvariable=StringVar(), font=('Helvetica', 11))
    coursefee.place(x=450, y=234)


    Label(regframe, text='Fee Deposit', font=('Helvetica', 11), bg='#1d1d1d', fg='white').place(x=300, y=269)
    feedeposit = Entry(regframe,textvariable=StringVar(), font=('Helvetica', 11))
    feedeposit.place(x=450, y=269)


    Button(regframe,text='Reset All',font=('Helvetica',11),width=11,command=lambda :resetaction(root)).place(x=300,y=340)
    Button(regframe, text='Back', font=('Helvetica', 11),width=11,command=lambda :backaction(regframe,root)).place(x=400, y=340)
    Button(regframe, text='Submit', font=('Helvetica', 11),width=11,bg='#0d3300',fg='#e0ebeb',command=lambda :submitaction(root,regno,studentname,fathername,hometown,mobno,variable,coursefee,feedeposit)).place(x=505, y=340)

def regframedest():
    if 'regframe' in globals():
        regframe.destroy()
    else:
        pass

def backaction(regframe,root):
    regframedest()
    mainFrame.main(root)
def resetaction(root):
    regframedest()
    registration(root)
def submitaction(root,regno,studentname,fathername,hometown,mobno,variable,coursefee,feedeposit):
    a=regno.get()
    b=studentname.get()
    c=fathername.get()
    d=hometown.get()
    ev=mobno.get()
    f=variable.get()
    gv=coursefee.get()
    hv=feedeposit.get()

    reglist=[]
    con = sqlite3.connect('PARAMOUNT')
    regholder = con.execute("select Reg_No from studenttable")
    for regtuple in regholder:
        for regstring in regtuple:
            reglist.append(regstring)

    if not regno.get():
        msgbox.showinfo('error','Reg No can not be empty')
    elif a.isspace() :
        msgbox.showinfo('error','All Space not allowed')
    elif a in reglist:
        msgbox.showinfo('Error','Reg No Already Exists')
    elif not studentname.get():
        msgbox.showinfo('error','Student Name can not be empty')
    elif b.isspace() :
        msgbox.showinfo('error','All Space not allowed')
    elif not fathername.get():
        msgbox.showinfo('error','Father Name can not be empty')
    elif c.isspace() :
        msgbox.showinfo('error','All Space not allowed')
    elif not hometown.get():
        msgbox.showinfo('error','Hometown can not be empty')
    elif d.isspace() :
        msgbox.showinfo('error','All Space not allowed')
    elif not mobno.get():
        msgbox.showinfo('error','Mobile No can not be empty')
    elif not ev.isdigit():
        msgbox.showinfo('error','Only Digits Allowed in Mobile No')
    elif ev.isspace() :
        msgbox.showinfo('error','All Space not allowed')
    elif not coursefee.get():
        msgbox.showinfo('error','Course Fee can not be empty')
    elif not gv.isdigit():
        msgbox.showinfo('error','Only Digits Allowed in Course Fee')
    elif gv.isspace() :
        msgbox.showinfo('error','All Space not allowed')
    elif not feedeposit.get():
        msgbox.showinfo('error','Fee Deposit can not be empty')
    elif not hv.isdigit():
        msgbox.showinfo('error','Only Digits Allowed in Fee Deposit')
    elif hv.isspace() :
        msgbox.showinfo('error','All Space not allowed')
    else:
        e = int(ev)
        g = int(gv)
        h = int(hv)

        con.execute("insert into studenttable (Reg_No,Student_Name,Father_Name,Hometown,Mobile_No,Course,Course_Fee,Fee_Deposit,Remaining_Fee) values ('{}','{}','{}','{}',{},'{}',{},{},{})".format(a,b,c,d,e,f,g,h,g-h))
        con.commit()
        con.close()
        regframedest()
        registration(root)
