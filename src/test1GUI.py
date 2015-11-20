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
		self.curr = 1
		self.newwindow2 = Toplevel(self.master)
		statdia = StatDialog(self.newwindow2, self)

	def openstat2dialog(self):
		self.curr = 2
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

	def genscatter(self):
		info = [self.beginscale.get(), self.scode, self.scode2]
		print (info)
		self.f.clf()
		self.f = Figure(figsize=(8, 6), dpi=100)
		self.a = self.f.add_subplot(111)
		generate("scatteryear", info, self.a) 
		self.canvas = FigureCanvasTkAgg(self.f, master=self.master)
		self.canvas.show()
		self.canvas._tkcanvas.grid(row=0, column=1, rowspan=3)

	def gencountryscatter(self):
		info = [self.ccode, self.scode, self.scode2]
		print (info)
		self.f.clf()
		self.f = Figure(figsize=(8, 6), dpi=100)
		self.a = self.f.add_subplot(111)
		generate("scattercountry", info, self.a) 
		self.canvas = FigureCanvasTkAgg(self.f, master=self.master)
		self.canvas.show()
		self.canvas._tkcanvas.grid(row=0, column=1, rowspan=3)
	
	def initcanvas(self):
		self.f = Figure(figsize=(8, 6), dpi=100)
		self.a = self.f.add_subplot(111)
		
		self.canvas = FigureCanvasTkAgg(self.f, master=self.master)
		self.canvas.show()
		self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
		
		self.canvas._tkcanvas.grid(row=0, column=1, rowspan=3)
	
	def initlinewindow(self):
		self.linewindow = Toplevel(self.master)

		frame1 = Frame(master = self.linewindow)

		frame1.grid(row=0, column=0)

		beginlabel = Label(frame1, text="Begin Year")
		self.beginscale = Scale(frame1, from_=1960, to=2015, orient=HORIZONTAL)
		self.beginscale.set(1960)
		beginlabel.pack()
		self.beginscale.pack()

		endlabel = Label(frame1, text="End Year",)
		self.endscale = Scale(frame1, from_=1960, to=2015, orient=HORIZONTAL)
		self.endscale.set(2015)
		endlabel.pack()
		self.endscale.pack()

		countrybutton = Button(frame1, text="Select Country", command=self.opencountrydialog)
		self.country = StringVar()
		countrylabel = Label(frame1, textvariable=self.country)
		countrybutton.pack()
		countrylabel.pack()

		statbutton = Button(frame1, text="Select Statistic", command=self.openstatdialog)
		self.stat = StringVar()
		statlabel = Label(frame1, textvariable=self.stat)
		statbutton.pack()
		statlabel.pack()

		graphbutton = Button(frame1, text="Graph!", command=self.gengraph)
		graphbutton.pack()

		

	def initscatterwindow(self):

		self.scatterwindow = Toplevel(self.master)

		frame2 = Frame(master = self.scatterwindow)

		beginlabel1 = Label(frame2, text="Year")
		self.beginscale = Scale(frame2, from_=1960, to=2015, orient=HORIZONTAL)
		self.beginscale.set(1960)
		beginlabel1.pack()
		self.beginscale.pack()

		countrybutton1 = Button(frame2, text="Select Statistic 1", command=self.openstatdialog)
		self.stat = StringVar()
		countrylabel1 = Label(frame2, textvariable=self.stat)
		countrybutton1.pack()
		countrylabel1.pack()

		statbutton1 = Button(frame2, text="Select Statistic 2", command=self.openstat2dialog)
		self.stat2 = StringVar()
		statlabel1 = Label(frame2, textvariable=self.stat2)
		statbutton1.pack()
		statlabel1.pack()

		graphbutton = Button(frame2, text="Graph!", command=self.genscatter)
		graphbutton.pack()

		frame2.grid(row=0, column=0)

	def initcountryscatterwindow(self):

		self.scatterwindow = Toplevel(self.master)

		frame3 = Frame(master = self.scatterwindow)

		countrybutton = Button(frame3, text="Select Country", command=self.opencountrydialog)
		self.country = StringVar()
		countrylabel = Label(frame3, textvariable=self.country)
		countrybutton.pack()
		countrylabel.pack()

		countrybutton1 = Button(frame3, text="Select Statistic 1", command=self.openstatdialog)
		self.stat = StringVar()
		countrylabel1 = Label(frame3, textvariable=self.stat)
		countrybutton1.pack()
		countrylabel1.pack()

		statbutton1 = Button(frame3, text="Select Statistic 2", command=self.openstat2dialog)
		self.stat2 = StringVar()
		statlabel1 = Label(frame3, textvariable=self.stat2)
		statbutton1.pack()
		statlabel1.pack()

		graphbutton = Button(frame3, text="Graph!", command=self.gencountryscatter)
		graphbutton.pack()

		frame3.grid(row=0, column=0)



	def initsidebar(self):
		frame = Frame(self.master)
		frame.grid(row=0, column=0)

		graphbutton = Button(frame, text="Line Graph", command=self.initlinewindow)
		graphbutton.pack()

		scatterbutton = Button(frame, text="Scatter Year", command=self.initscatterwindow)
		scatterbutton.pack()

		scattercountrybutton = Button(frame, text="Scatter Country", command=self.initcountryscatterwindow)
		scattercountrybutton.pack()

		scattertotalbutton = Button(frame, text="Scatter Total", command=self.gengraph)
		scattertotalbutton.pack()

def main(): 
	root = Tk()
	app = MainApplication(root)
	root.mainloop()

if __name__ == '__main__':
	main()