import tkinter as tk
root = tk.Tk()
root.title("display a website image")
photo = tk.PhotoImage(file= r"~/Desktop/Github/CS490-DesProj/graphs/image.gif")
cv = tk.Canvas()
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(10, 10, image=photo, anchor='nw')
root.mainloop()
