from tkinter import *
import tkinter.ttk as ttk
from country import searchcountry


def func(self):
	text = search.get()
	result = searchcountry(text)

	table.delete(*table.get_children())

	for i in result:
		table.insert("", "end", values=i)

def cGUI():
	root.mainloop()

root = Tk()

search = Entry(root, width=50)
search.grid(row=0,column=0)

enter = Button(root, text="Search")
enter.bind('<Button-1>', func)
enter.grid(row=0,column=1)

root.bind("<Return>", func)

table = ttk.Treeview(root, columns=("code", "table", "long"), show="headings")
table.column("code", width=50, anchor="e")
table.heading("code", text="Code")
table.column("table", width=200, anchor="w")
table.heading("table", text="Name")
table.column("long", width=400, anchor="w")
table.heading("long", text="Long Name")

table.grid(row=1, column=0, columnspan=2)

#cGUI()