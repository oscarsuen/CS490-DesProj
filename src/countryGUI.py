from tkinter import *
import tkinter.ttk as ttk
from country import searchcountry

class CountryDialog():
	def __init__(self, master, top):
		self.master = master
		self.top = top
		self.createbox()
		self.func(0)
	
	def createbox(self):
		
		self.search = Entry(self.master, width=50)
		self.search.grid(row=0,column=0)
		
		self.enter = Button(self.master, text="Search")
		self.enter.bind('<Button-1>', self.func)
		self.enter.grid(row=0,column=1)
		
		self.master.bind("<Return>", self.func)
		
		self.table = ttk.Treeview(self.master, columns=("code", "table", "long"), show="headings")
		self.table.column("code", width=50, anchor="e")
		self.table.heading("code", text="Code")
		self.table.column("table", width=200, anchor="w")
		self.table.heading("table", text="Name")
		self.table.column("long", width=400, anchor="w")
		self.table.heading("long", text="Long Name")

		self.table.bind("<Double-1>", self.doubleclick)		
		self.table.grid(row=1, column=0, columnspan=2)

	def func(self, event):
		text = self.search.get()
		result = searchcountry(text)
	
		self.table.delete(*self.table.get_children())
	
		for i in result:
			self.table.insert("", "end", values=i)

	def doubleclick(self, event):
		item = self.table.item(self.table.focus())
		self.top.ccode=item['values'][0]
		self.top.country.set(item['values'][1])
		self.master.destroy()

#root = Tk()
#CountryDialog(root, root)
#root.mainloop()