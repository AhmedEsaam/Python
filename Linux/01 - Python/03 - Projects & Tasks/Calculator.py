from tkinter import *
import tkinter.font as font
import string

root = Tk()

root.title("Calculator")

root.geometry('285x310')

myFont = font.Font(size=15)

exp = StringVar()
exp.set("0")

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    exp.set(expression)

def equal():
    try:
        global expression
        total = str(eval(expression))
        exp.set(total)
        expression = ""
    except:
        exp.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    exp.set("")
 

# Label(text="Position 1", bg="#FFF111", fg="black", width=10).grid(row=0, column=0)
field = Entry(root, bd= 5, textvariable =exp, font= myFont)
field.grid(columnspan=4, ipadx=28)
Button(root, text = "7", font= myFont, bd='5', width=5, height=2, command=lambda: press(7)).grid(row=1, column=0);
Button(root, text = "8", font= myFont, bd='5', width=5, height=2, command=lambda: press(8)).grid(row=1, column=1);
Button(root, text = "9", font= myFont, bd='5', width=5, height=2, command=lambda: press(9)).grid(row=1, column=2);
Button(root, text = "/", font= myFont, bd='5', width=5, height=2, command=lambda: press('/')).grid(row=1, column=3);
Button(root, text = "4", font= myFont, bd='5', width=5, height=2, command=lambda: press(4)).grid(row=2, column=0);
Button(root, text = "5", font= myFont, bd='5', width=5, height=2, command=lambda: press(5)).grid(row=2, column=1);
Button(root, text = "6", font= myFont, bd='5', width=5, height=2, command=lambda: press(6)).grid(row=2, column=2);
Button(root, text = "x", font= myFont, bd='5', width=5, height=2, command=lambda: press('*')).grid(row=2, column=3);
Button(root, text = "1", font= myFont, bd='5', width=5, height=2, command=lambda: press(1)).grid(row=3, column=0);
Button(root, text = "2", font= myFont, bd='5', width=5, height=2, command=lambda: press(2)).grid(row=3, column=1);
Button(root, text = "3", font= myFont, bd='5', width=5, height=2, command=lambda: press(3)).grid(row=3, column=2);
Button(root, text = "-", font= myFont, bd='5', width=5, height=2, command=lambda: press('-')).grid(row=3, column=3);
Button(root, text = ".", font= myFont, bd='5', width=5, height=2, command=lambda: press('.')).grid(row=4, column=0);
Button(root, text = "0", font= myFont, bd='5', width=5, height=2, command=lambda: press(0)).grid(row=4, column=1);
Button(root, text = "=", font= myFont, bd='5', width=5, height=2, command=equal).grid(row=4, column=2);
Button(root, text = "+", font= myFont, bd='5', width=5, height=2, command=lambda: press('+')).grid(row=4, column=3);

root.mainloop()