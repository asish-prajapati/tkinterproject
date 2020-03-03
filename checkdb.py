import sqlite3
con=sqlite3.connect('PARAMOUNT')
reglist=[]
con = sqlite3.connect('PARAMOUNT')
regholder1 = con.execute("SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';")
print(list(regholder1))


ertjyuyttyuiuytrertg