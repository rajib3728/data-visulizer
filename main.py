from tkinter import *
from PIL import ImageTk
import winsound
splash_root=Tk()
splash_root.geometry("500x300+500+200")
splash_root.overrideredirect(True)
bg=ImageTk.PhotoImage(file="Splash.png")
bglb=Label(splash_root,image=bg)
bglb.place(x=0,y=0,relheight=1,relwidth=1)
def main_window():
    winsound.PlaySound("song2.wav",winsound.SND_FILENAME)
    splash_root.destroy()
    import login
splash_root.after(1000,main_window)
mainloop()
