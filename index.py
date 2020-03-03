from tkinter import *
import adminLogin
import welcomeFrame


root=Tk()
root.geometry('1200x400')
root.title('Paramount Coaching')
root.resizable(0,0)



adminLogin.adminlogin(root)
welcomeFrame.welcome(root)

root.mainloop()