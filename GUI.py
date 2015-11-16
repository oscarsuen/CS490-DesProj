import tkinter
from tkinter import *

root = Tk()

logo = PhotoImage(file="graphs/image.gif")
w1 = Label(master = root, image=logo).grid(row=0, column=0)
explanation = "Hello World"

def test():
	print("hi")

w2 = Button(master=root, 
           justify=LEFT,
           padx = 10, 
           text=explanation,
           command = test).grid(row=1, column=0)

#searchbox = Tk()



root.mainloop()

