from tkinter import *
root = Tk()
def show():
    myLabel = Label(root, text = clicked.get()).pack()
clicked = StringVar()
clicked.set("Monday")

drop = OptionMenu(root,clicked,"Monday","Tuesday","Wednesday","Thursday","Friday")
drop.pack()

myButton = Button(root,text="Show Selection",command = show).pack()
root.mainloop()
