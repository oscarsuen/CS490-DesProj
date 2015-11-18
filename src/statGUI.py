from tkinter import *
import tkinter.ttk as ttk
from statistic import searchstat


def func(self):
	text = search.get()
	result = searchstat(text)

	table.delete(*table.get_children())

	for i in result:
		table.insert("", "end", values=i)

root = Tk()

search = Entry(root, width=50)
search.grid(row=0,column=0)

enter = Button(root, text="Search")
enter.bind('<Button-1>', func)
enter.grid(row=0,column=1)

root.bind("<Return>", func)

table = ttk.Treeview(root, columns=("code", "table", "long"), show="headings")
table.column("code", width=150, anchor="e")
table.heading("code", text="Code")
table.column("table", width=350, anchor="w")
table.heading("table", text="Topic")
table.column("long", width=400, anchor="w")
table.heading("long", text="Indicator Name")

table.grid(row=1, column=0, columnspan=2)

def sGUI():
	root.mainloop()

sGUI()
