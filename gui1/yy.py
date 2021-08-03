from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title = ('Image Intersection')
root.iconbitmap('C:/Users/Prafulmhrjn/Downloads/fencees.ico')
my_image= ImageTk.PhotoImage(Image.open("C:/Users/Prafulmhrjn/Downloads/fencess.png"))
my_label= Label(image=my_image)
my_label.pack()
button_quit= Button(root, text="Exit", command=root.quit,width=20)
button_quit.pack
root.mainloop()