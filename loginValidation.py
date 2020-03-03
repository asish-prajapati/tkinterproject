def loginaction(userEntry, passEntery, root):
    con = sqlite3.connect('PARAMOUNT')
    a = userEntry.get()
    b = passEntery.get()  # userentry and passentry are Entryobject
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

        msgbox.showinfo('True', 'Successfully Logged IN')
        welcomeFrame.welcomedest()
        mainFrame.main(root)
        adminlogindest()
        logOut.logout(root)

    else:
        msgbox.showinfo('False', 'Wrong ID/PASS')