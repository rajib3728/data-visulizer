from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
def register():
    root.destroy()
    import register
def workpage():
    if e1.get()=="":
        messagebox.showinfo("info","please provide username")
    else:
        try:
            f=open("data.txt",'r')
            l=f.readlines()
            # initialize character
            char ='\n'
            # Remove character from Strings list
            # using loop + replace() + enumerate()
            for idx, ele in enumerate(l):
                l[idx] = ele.replace(char, '')
            l.remove(l[0])
            f.close()
            x=0
            y=0
            for i in range(len(l)):
                if e1.get()==l[i] :
                    x=i
                    break
            for i in range(len(l)):
                if e2.get()==l[i]:
                    y=i
                    break
            if x==y-1:
                messagebox.showinfo("info","login succussful redirect to workpage")
                root.destroy()
                import workpage
            else:
                messagebox.showinfo("info","username or password mismatch or register first")
        except:
            messagebox.showinfo("info","there is some problem or no data found")
root=Tk()
root.geometry("1600x900+0+0")
root.title("login page")
photo = PhotoImage(file = "logo.png")
root.iconphoto(False,photo)
bg=ImageTk.PhotoImage(file="img1.jpg")
bglb=Label(root,image=bg)
bglb.place(x=0,y=0,relheight=1,relwidth=1)
f1=Frame(root,width=450,height=400,bg="black")
f1.place(x=550,y=200)
l1=Label(f1,fg="white",font=("Times", 30,"bold"),bg="black",text="login")
l1.place(x=190,y=30)
l2=Label(f1,text="username",bg="black",fg="white",font=("Times",15,"bold"))
l2.place(x=100,y=100)
l3=Label(f1,text="password",bg="black",fg="white",font=("Times",15,"bold"))
l3.place(x=100,y=150)
e1=Entry(f1,bg="black",fg="white")
e1.place(x=200,y=107)
e2=Entry(f1,bg="black",fg="white",show="*")
e2.place(x=200,y=157)
b1=Button(f1,text="submit",bg="grey",fg="black",command=workpage)
b1.place(x=210,y=200)
b2=Button(f1,text="or register here",bg="black",fg="white",command=register)
b2.place(x=190,y=250)
root.mainloop()