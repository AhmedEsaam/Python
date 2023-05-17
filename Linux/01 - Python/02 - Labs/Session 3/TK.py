from tkinter import *



window = Tk()

window.title("My Program")

lbl1 = Label(window, text = "Name: Ahmed Essam\n Faculty: Engineering Ain Shams")
lbl1.pack(side = TOP)
window.geometry('500x500')

def PrintName():
    lbl2= Label(window, text = "Ahmed Essam")
    lbl2.pack(side = TOP)

b1 = Button(window, text = "Destroy", bd='5', command=window.destroy)
b1.pack(side = LEFT)
b2 = Button(window, text = "Print Name", bd='5', command=PrintName)
b2.pack(side = LEFT)
# b3 = Button(window, text = "Bottom")
# b3.pack(side = BOTTOM)
# b4 = Button(window, text = "Top")
# b4.pack(side = TOP)

photo = PhotoImage(file="img.png")
photo = photo.subsample(2,2)

b3 = Button(window, image=photo)
b3.pack(side = TOP)

b3 = Button(window, text = "Linux Debian", bg="orange", fg="white", font=('times', 20))
b3.pack(side = TOP)




window.mainloop()
