import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from tkinter import *

from graph import generate
from countryGUI import CountryDialog
from statGUI import StatDialog

class MainApplication:
	def __init__(self, master):
		self.master = master
		self.master.wm_title("Graph Test")
		self.initcanvas()
		self.initsidebar()

	def opencountrydialog(self):
		self.newwindow = Toplevel(self.master)
		coundia = CountryDialog(self.newwindow, self)

	def openstatdialog(self):
		self.newwindow2 = Toplevel(self.master)
		statdia = StatDialog(self.newwindow2, self)

	def gengraph(self):
		b = self.beginscale
		e = self.endscale
		info = [b.get(), e.get(), self.ccode, self.scode]
		print(info)
		self.f.clf()
		self.f = Figure(figsize=(8, 6), dpi=100)
		self.a = self.f.add_subplot(111)
		generate("line", info, self.a)
		self.canvas = FigureCanvasTkAgg(self.f, master=self.master)
		self.canvas.show()
		self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
		
		self.canvas._tkcanvas.grid(row=0, column=1, rowspan=3)
	
	def initcanvas(self):
		self.f = Figure(figsize=(8, 6), dpi=100)
		self.a = self.f.add_subplot(111)
		
		self.canvas = FigureCanvasTkAgg(self.f, master=self.master)
		self.canvas.show()
		self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
		
		self.canvas._tkcanvas.grid(row=0, column=1, rowspan=3)
	
	def initsidebar(self):
		frame = Frame(self.master)
		frame.grid(row=0, column=0)
		
		beginlabel = Label(frame, text="Begin Year")
		self.beginscale = Scale(frame, from_=1960, to=2015, orient=HORIZONTAL)
		self.beginscale.set(1960)
		beginlabel.pack()
		self.beginscale.pack()

		endlabel = Label(frame, text="End Year")
		self.endscale = Scale(frame, from_=1960, to=2015, orient=HORIZONTAL)
		self.endscale.set(2015)
		endlabel.pack()
		self.endscale.pack()

		countrybutton = Button(frame, text="Select Country", command=self.opencountrydialog)
		self.country = StringVar()
		countrylabel = Label(frame, textvariable=self.country)
		countrybutton.pack()
		countrylabel.pack()

		statbutton = Button(frame, text="Select Statistic", command=self.openstatdialog)
		self.stat = StringVar()
		statlabel = Label(frame, textvariable=self.stat)
		statbutton.pack()
		statlabel.pack()

		graphbutton = Button(frame, text="Graph!", command=self.gengraph)
		graphbutton.pack()

def main(): 
	root = Tk()
	app = MainApplication(root)
	root.mainloop()

if __name__ == '__main__':
	main()