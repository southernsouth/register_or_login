import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import json
from tkinter import filedialog



def button1():
    w.minsize(width=200, height=135)
    w.maxsize(width=200, height=135)

    f1.pack_forget()
    f2.pack()

def button2():
    w.minsize(width=200, height=135)
    w.maxsize(width=200, height=135)

    f1.pack_forget()
    f3.pack()

def ex_button3(login, passworld):
    cursor.execute('SELECT * FROM res_log')
    data = cursor.fetchall()

    for i in range(len(data)):
        if login in data[i] and passworld == (data[i])[2]:
            return True
    
    return False
        
def button3():    
    login = e1.get()
    passworld = e2.get()
    
    if ex_button3(login, passworld) == True:
        f2.pack_forget()
        f4.pack()
    else:
        messagebox.showwarning('Information', 'Wrong login or password.')

def ex_button4(login):
    cursor.execute('SELECT * FROM res_log')
    data = cursor.fetchall()

    for i in range(len(data)):
        if login in data[i]:
            return True

    return False

def button4():
    login = e3.get()
    passworld = e4.get()
    
    if login != '' and passworld != '' and ex_button4(login) == False:
        e4.pack_forget()
        b4.pack_forget()
        
        l5['text'] = 'Re-password:'
        e5.pack()
        b5.pack()
    else:
        messagebox.showwarning('Information', 'Login busy or invalid input.')

def button5():
    login = e3.get()
    passworld = e4.get()
    passworld2 = e5.get()

    if passworld == passworld2:
        cursor.execute('INSERT INTO res_log (login, passworld) VALUES ("{}", "{}")'.format(login, passworld))
        con.commit()

        f3.pack_forget()
        f2.pack()
    else:
        messagebox.showwarning('Information', 'Passwords do not match.')

def ex_button_json1(x):
    cursor.execute('SELECT * FROM res_log')
    data = cursor.fetchall()

    for i in range(len(data)):
        if x in (data[i])[1]:
            return True
    return False

def button_json1():
    dlg = tk.filedialog.askopenfilename()
    name = os.path.basename(r'{}'.format(dlg))
    
    with open(os.path.join(str(dlg.rstrip(name)), name), 'r') as f:
        x = json.load(f)
    
    for i in range(len(x)):
        if ex_button_json1((x[i])[0]) == False:
            cursor.execute('INSERT INTO res_log (login, passworld) VALUES ("{}", "{}")'.format((x[i])[0], (x[i])[1]))
            con.commit()

def button_json2():
    cursor.execute('SELECT * FROM res_log')
    data = cursor.fetchall()
    x = []

    for i in range(len(data)):
        x.append([(data[i])[1], (data[i])[2]])

    with open(os.path.join('database.json'), 'w') as f:
        json.dump(x, f)


login = ''
passworld = ''
passworld2 = ''

w = tk.Tk()
w.title('Login or register')
w.minsize(width=200, height=162)
w.maxsize(width=200, height=162)

f1 = tk.Frame(w)
f1.pack()

l1 = tk.Label(f1, text='')
l1.pack()

b1 = tk.Button(f1, text='Login', command=button1)
b1.pack()

b2 = tk.Button(f1, text='Register', command=button2)
b2.pack()

b_json1 = tk.Button(f1, text='Import json', command=button_json1)
b_json1.pack()

b_json2 = tk.Button(f1, text='Export json', command=button_json2)
b_json2.pack()


f2 = tk.Frame(w)

l2 = tk.Label(f2, text='Login:')
l2.pack()

e1 = tk.Entry(f2)
e1.pack()

l3 = tk.Label(f2, text='Passworld:')
l3. pack()

e2 = tk.Entry(f2)
e2.pack()

b3 = tk.Button(f2, text='Login', command=button3)
b3.pack()


f3 = tk.Frame(w)

l4 = tk.Label(f3, text='Login:')
l4.pack()

e3 = tk.Entry(f3)
e3.pack()

l5 = tk.Label(f3, text='Passworld:')
l5.pack()

e4 = tk.Entry(f3)
e4.pack()

b4 = tk.Button(f3, text='Register', command=button4)
b4.pack()

e5 = tk.Entry(f3)

b5 = tk.Button(f3, text='Register', command=button5)


f4 = tk.Frame(w)

l_1 = tk.Label(f4, text='')
l_1.pack()

l_2 = tk.Label(f4, text='Successful login.')
l_2.pack()

con = mysql.connector.connect(host='localhost',
                                database='res_log',
                                user='south',
                                password='21199')

cursor = con.cursor()

w.mainloop()

cursor.close()
