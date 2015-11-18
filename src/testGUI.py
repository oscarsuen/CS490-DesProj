import matplotlib
matplotlib.use('TkAgg')

import sys

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import tkinter as Tk

from line import linegraph
from scatter import scatterplotyear
from scattercountry import scatterplotcountry
from scattertotal import scatterplottotal


def destroy(e):
    sys.exit()

root = Tk.Tk()
root.wm_title("Embedding in TK")


f = Figure(figsize=(7, 6), dpi=100)
a = f.add_subplot(111)

info = [1960, 2014, "USA", "NY.GDP.MKTP.KD"]
linegraph(info, a)



#t = arange(0.0, 3.0, 0.01)
#s = sin(2*pi*t)
"""
a.plot(t, s)
a.set_title('Tk embedding')
a.set_xlabel('X axis label')
a.set_ylabel('Y label')
"""

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().grid(row=1,column=1, padx=2, pady=2, rowspan=5, columnspan=5)
#canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
buttonpanel = Tk.Frame(master=root).grid(row=0,column=0)

canvas._tkcanvas.grid(row=1,column=0,padx=2, pady=2, rowspan=5, columnspan=5)
#canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

button = Tk.Button(master=buttonpanel, text='Quit', command=sys.exit)
button.grid(row=0,column=0, padx=2, pady=2)

def test():
	print("hi")


w2 = Tk.Button(master=buttonpanel, 
           padx = 5, 
           text="ey",
           command = test).grid(row=0, column=1)

Tk.mainloop()