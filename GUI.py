import tkinter
from tkinter import *

root = Tk()

logo = PhotoImage(file="graphs/image.gif")
w1 = Label(master = root, image=logo).grid(row=1, column=0)
explanation = "Hello World"

def test():
	print("hi")

w2 = Button(master=root, 
           justify=LEFT,
           padx = 10, 
           text=explanation,
           command = test).grid(row=0, column=0)

searchbox = Tk()

csearch = Label(master = searchbox, text = "Search for a country").grid(row =1, column=1) #what is the command
ssearch = Label(master = searchbox, text = "Search for a statistic" ).grid(row =2, column=1)


root.mainloop()

