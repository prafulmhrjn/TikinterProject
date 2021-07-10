from tkinter import *

root = Tk()

name = Label(root,text = "Name").grid(row=0, column = 0)
e1 = Entry(root).grid(row = 0, column = 1)
password = Label(root,text = "password").grid(row=2,column=0)
e2 = Entry(root).grid(row=2, column = 1)

submit = Button(root, text = "Submit").grid(row = 4,column=1)
root.mainloop()