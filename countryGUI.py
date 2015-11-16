from tkinter import *
import tkinter.ttk as ttk
from country import searchcountry


def func(self):
	text = search.get()
	result = searchcountry(text)

	table.delete(*table.get_children())

	for i in result:
		table.insert("", "end", values=i)

root = Tk()

search = Entry(root)
search.pack()

root.bind("<Return>", func)

table = ttk.Treeview(root, columns=("code", "table", "long"), show="headings")
table.column("code", width=50, anchor="e")
table.heading("code", text="Code")
table.column("table", width=200, anchor="w")
table.heading("table", text="Name")
table.column("long", width=400, anchor="w")
table.heading("long", text="Long Name")

table.pack()

root.mainloop()
