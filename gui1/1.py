from tkinter import *

root = Tk()

button1 = Button(root, text = "LEFT", fg="green")
button1.pack(side = LEFT)
button2 = Button(root, text = "RIGHT", fg="black")
button2.pack(side = RIGHT)
button3 = Button(root, text = "TOP", fg="blue")
button3.pack(side = TOP)
button4 = Button(root, text = "Bottom", fg="red")
button4.pack(side = BOTTOM)





root.mainloop()