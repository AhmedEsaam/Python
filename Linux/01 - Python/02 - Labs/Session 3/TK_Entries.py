from tkinter import *

root = Tk()

root.geometry('500x500')

name_ = StringVar()
passw_= StringVar()
name_.set("Enter Name")
passw_.set("Enter Pass")

def submit():
    name= name_.get()
    passw= passw_.get()
    
    lbl3 = Label(root, text = name)
    lbl3.pack(side = TOP)

    lbl4 = Label(root, text = passw)
    lbl4.pack(side = TOP)

lbl1 = Label(root, text = "name")
lbl1.pack(side = LEFT)

username = Entry(root, bd= 5, textvariable= name_)
username.pack(side = LEFT)

lbl2 = Label(root, text = "password")
lbl2.pack(side = LEFT)

Pass = Entry(root, bd= 5, textvariable =passw_, show='*')
Pass.pack(side = LEFT)

b1 = Button(root, text = "submit", bd='5', command = submit)
b1.pack(side = BOTTOM)

root.mainloop()