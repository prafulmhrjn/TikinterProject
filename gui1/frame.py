from tkinter import *

root=Tk()

Frame= LabelFrame(root,text="My Frame",padx=5,pady=5)
Frame.pack(padx=10,pady=10)

mybutton=Button(Frame,text="ok then")
mybutton.pack()

root.mainloop()