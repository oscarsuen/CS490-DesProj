from tkinter import *

root = Tk()

logo = PhotoImage(file="graphs/image.gif")
w1 = Label(root, image=logo).pack(side="right")
explanation = "Hello World"
w2 = Label(root, 
           justify=LEFT,
           padx = 10, 
           text=explanation).pack(side="left")
root.mainloop()

