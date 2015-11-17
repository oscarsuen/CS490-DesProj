import tkinter
#from graph import generate
from tkinter import *

root = Tk()

logo = PhotoImage(file="../graphs/image.gif")
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

#generate(type=line, scatteryear, scattercountry, scattertotal; data)


csearch = Label(master = searchbox, text = "Search for a country").grid(row =1, column=1)
ssearch = Label(master = searchbox, text = "Search for a statistic" ).grid(row =2, column=1)
e1 = Entry(master = searchbox).grid(row=1, column=2)
e2 = Entry(master = searchbox).grid(row=2, column=2)


root.mainloop()

