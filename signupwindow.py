from tkinter import *
import sqlite3,time
import tkinter.messagebox as msgbox
def signup():
    signuproot=Tk()
    signuproot.call("wm", "attributes", ".", "-topmost", "true")
    # signuproot.transient()
    signuproot.geometry('400x300')
    signuproot.title('Sign Up')
    signuproot.resizable(0,0)
    signupframe=Frame(signuproot,width=400,height=300,bg='#2C3539')
    signupframe.pack(fill=X)
    Label(signupframe,text='Admin Id',bg='#2C3539',fg='#B6B6B4',font=('Helvetica',11)).place(x=40,y=60)
    adminid= Entry(signupframe, font=('Helvetica', 11), textvariable=StringVar())
    adminid.place(x=200, y=60)
    Label(signupframe, text='Password',bg='#2C3539',fg='#B6B6B4', font=('Helvetica', 11)).place(x=40, y=120)
    password= Entry(signupframe,show='*', font=('Helvetica', 11), textvariable=StringVar())
    password.place(x=200, y=120)
    Label(signupframe, text='Confirm Password',bg='#2C3539',fg='#B6B6B4', font=('Helvetica', 11)).place(x=40, y=180)
    confirmpassword = Entry(signupframe,show="*", font=('Helvetica', 11), textvariable=StringVar())
    confirmpassword.place(x=200, y=180)

    Label(signupframe, text='**space not allowed', bg='#2C3539', fg='yellow', font=('Helvetica', 10)).place(x=100,
                                                                                                      y=250)
    Button(signupframe,bg='#2C3539', text='  Register  ', cursor='hand2', fg='white',command=lambda :regaction(adminid,password,confirmpassword,signuproot,signupframe)).place(x=300, y=250)



    signuproot.mainloop()

def regaction(adminid,password,confirmpassword,signuproot,signupframe):
    id = adminid.get()
    ps = password.get()
    cnfps = confirmpassword.get()
    if (id.isalnum()):
        if (ps == cnfps):
            if (ps.isalnum()):
                con = sqlite3.connect("PARAMOUNT")
                # cur=con.cursor()
                con.execute("create table if not exists admindetail (admin_id[10],password char[10])")
                query = "insert into admindetail (admin_id,password) values('{}','{}')".format(id, ps)

                con.execute(query)
                con.commit()
                m = con.execute("select * from admindetail")
                print(list(m))
                con.close()
                signuproot.destroy()

            else:
                msgbox.showinfo("error", "space not allowed in ps")
                confirmpassword.delete(0, END)
                password.delete(0, END)
        else:
            Label(signupframe, text='Password mismatch', bg='#2C3539', fg='red', font=('Helvetica', 8)).place(x=250,
                                                                                                              y=220)
            confirmpassword.delete(0, END)
    else:

        msgbox.showinfo("error", "space not allowed in id")
        adminid.delete(0, END)













