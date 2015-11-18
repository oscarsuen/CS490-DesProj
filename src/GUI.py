import tkinter
from tkinter import *

root = Tk()

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

def linepick():
	chooseline = Tk()
	y1p = Label(master = chooseline, text = "Beginning year").grid(row=1, column=1)
	y1 = Entry(master = chooseline).grid(row=1,column=2)
	y2p = Label(master = chooseline, text = "End year").grid(row=2, column=1)
	y2 = Entry(master = chooseline).grid(row=2,column=2)
	c = Label(master = chooseline, text = "Beginning year").grid(row=3, column=1)
	cp = Entry(master = chooseline).grid(row=3,column=2)
	d = Label(master = chooseline, text = "Beginning year").grid(row=4, column=1)
	dp = Entry(master = chooseline).grid(row=4,column=2)




#generate(type=line, scatteryear, scattercountry, scattertotal; data)


csearch = Label(master = searchbox, text = "Search for a country").grid(row =1, column=1)
ssearch = Label(master = searchbox, text = "Search for a statistic" ).grid(row =2, column=1)
e1 = Entry(master = searchbox).grid(row=1, column=2)
e2 = Entry(master = searchbox).grid(row=2, column=2)


root.mainloop()

