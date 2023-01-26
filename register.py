from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
def login():
    if e1.get()=="":
        messagebox.showinfo("info","please provide username for acccount creation")
    elif e1.get()==e2.get():
        messagebox.showinfo("info","username and password should be different")
    else:
        f=open("data.txt",'a')
        f.write('\n'+e1.get())
        f.write('\n'+e2.get())
        f.close()
        root.destroy()
        messagebox.showinfo("info","account creation succuessful and open aplication again")
root=Tk()
root.geometry("1600x900+0+0")
root.title("register page")
photo = PhotoImage(file = "logo.png")
root.iconphoto(False,photo)
bg=ImageTk.PhotoImage(file="img2.jpg")
bglb=Label(root,image=bg)
bglb.place(x=0,y=0,relheight=1,relwidth=1)
f1=Frame(root,width=450,height=400,bg="black")
f1.place(x=550,y=200)
l1=Label(f1,fg="white",font=("Times", 30,"bold"),bg="black",text="register")
l1.place(x=170,y=30)
l2=Label(f1,text="create username",bg="black",fg="white",font=("Times",15,"bold"))
l2.place(x=80,y=100)
l3=Label(f1,text="create password",bg="black",fg="white",font=("Times",15,"bold"))
l3.place(x=80,y=150)
e1=Entry(f1,bg="black",fg="white")
e1.place(x=230,y=107)
e2=Entry(f1,bg="black",fg="white")
e2.place(x=230,y=157)
b1=Button(f1,text="submit",bg="grey",fg="black",command=login)
b1.place(x=210,y=200)
root.mainloop()