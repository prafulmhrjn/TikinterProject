from tkinter import *
root = Tk()
def show():
    myLabel=Label(root, text=var.get()).pack()

var = StringVar()

checkButton = Checkbutton(root, text="Check this box!",variable = var,onvalue="on", offvalue="off")

checkButton.deselect()
checkButton.pack()

myButton = Button(root, text="Show Selection", command = show).pack()
root.mainloop()
