from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk
root1=Tk()
root1.config(bg="white")
root1.title("help")
photo = PhotoImage(file = "logo.png")
root1.iconphoto(False,photo)
root1.geometry("200x200+500+300")
root1.maxsize(200,200)
root1.minsize(200,200)
root1.mainloop()