from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk
import mysql.connector
from matplotlib import pyplot as plt
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import webbrowser
def work():
    try:
        mydb=mysql.connector.connect(host=e4.get(),user=e2.get(),password=e3.get(),database=e1.get())
        f2.config(bg="greenyellow")
        mycursor=mydb.cursor()
        sql1="select "+e5.get()+" from "+e7.get()
        mycursor.execute(sql1)
        myresult=mycursor.fetchall()
        l1=[]
        for i in myresult:
            x=list(i)
            l1.extend(x)
        sql2="select "+e6.get()+" from "+e7.get()
        mycursor.execute(sql2)
        myresult2=mycursor.fetchall()
        l2=[]
        for i in myresult2:
            x=list(i)
            l2.extend(x)
        style.use("ggplot")
        figure1 = plt.Figure(figsize=(7,5), dpi=60)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().place(x=1080,y=140)
        ax1.scatter(l1,l2)
        ax1.set_xlabel(e5.get())
        ax1.set_ylabel(e6.get())
        ax1.set_title(e5.get()+' vs '+e6.get()+" scatter plot")

        figure2 = plt.Figure(figsize=(7,5), dpi=60)
        ax2 = figure2.add_subplot(111)
        bar2 = FigureCanvasTkAgg(figure2, root)
        bar2.get_tk_widget().place(x=1080,y=450)
        ax2.bar(l1,l2)
        ax2.set_xlabel(e5.get())
        ax2.set_ylabel(e6.get())
        ax2.set_title(e5.get()+' vs '+e6.get()+" bar plot")
        
        sql3="select * from "+e7.get()
        mycursor.execute(sql3)
        res=mycursor.fetchall()
        if len(res)>=0 and len(res)<=10:
            slider.set(1)
        elif len(res)>=11 and len(res)<=100:
            slider.set(2)
        elif len(res)>=101 and len(res)>=1000:
            slider.set(3)
        else:
            slider.set(4)
        mydb.close()
    except:
        f2.config(bg="red")
        messagebox.showinfo("info","give correct input for successful connection")
def vt():
    try:
        db1 = mysql.connector.connect(host=e4.get(), user=e2.get(), password=e3.get(), database=e1.get())
        mycursor1 = db1.cursor()
        sql="select "+e5.get()+","+e6.get()+" from "+e7.get()
        mycursor1.execute(sql)
        rows=mycursor1.fetchall()
        if len(rows)!=0:
            medtab.delete(*medtab.get_children())
        for row in rows:
            medtab.insert('',END,values=row)
        #db1.commit()
        db1.close()
    except:
        messagebox.showinfo("info","sorry some error occured")
def help():
    messagebox.showinfo("info","opening in your default browser")
    webbrowser.open("index.html")
    
def other():
    if clicked.get()=="Line plot":
        try:
            db2 = mysql.connector.connect(host=e4.get(), user=e2.get(), password=e3.get(), database=e1.get())
            mycursor2 = db2.cursor()
            sql1="select "+e5.get()+" from "+e7.get()
            mycursor2.execute(sql1)
            myresult=mycursor2.fetchall()
            l1=[]
            l2=[]
            for i in myresult:
                x=list(i)
                l1.extend(x)
            sql2="select "+e6.get()+" from "+e7.get()
            mycursor2.execute(sql2)
            myresult2=mycursor2.fetchall()
            for i in myresult2:
                y=list(i)
                l2.extend(y)
            style.use("ggplot")
            plt.plot(l1,l2)
            plt.title("Line plot")
            plt.xlabel(e5.get())
            plt.ylabel(e6.get())
            plt.show()
        except:
            messagebox.showinfo("info","some error occured")
    elif clicked.get()=="Histogram plot":
        try:
            db2 = mysql.connector.connect(host=e4.get(), user=e2.get(), password=e3.get(), database=e1.get())
            mycursor2 = db2.cursor()
            sql1="select "+e5.get()+" from "+e7.get()
            mycursor2.execute(sql1)
            myresult=mycursor2.fetchall()
            l1=[]
            for i in myresult:
                x=list(i)
                l1.extend(x)

            sql2="select "+e6.get()+" from "+e7.get()
            mycursor2.execute(sql2)
            myresult2=mycursor2.fetchall()
            l2=[]
            for i in myresult2:
                y=list(i)
                l2.extend(y)
        
            style.use("ggplot")
            
            plt.subplot(1, 2, 1)
            plt.hist(l1,bins=5)
            
            plt.subplot(1, 2, 2)
            plt.hist(l2,bins=5)
            plt.title("Histogram plot")
            plt.xlabel(e5.get())
            plt.ylabel(e6.get())
            plt.show()
        except:
            messagebox.showinfo("info","some error occured")
    else:
        try:
            db2 = mysql.connector.connect(host=e4.get(), user=e2.get(), password=e3.get(), database=e1.get())
            mycursor2 = db2.cursor()
            sql1="select "+e5.get()+" from "+e7.get()
            mycursor2.execute(sql1)
            myresult=mycursor2.fetchall()
            l1=[]
            for i in myresult:
                x=list(i)
                l1.extend(x)

            sql2="select "+e6.get()+" from "+e7.get()
            mycursor2.execute(sql2)
            myresult2=mycursor2.fetchall()
            l2=[]
            for i in myresult2:
                y=list(i)
                l2.extend(y)
        
            if sum(l1)==100 and sum(l2)==100:
                plt.style.use("fivethirtyeight")
                plt.subplot(1, 2, 1)
                plt.pie(l1,labels=l1)
                plt.title("pie plot")
                plt.subplot(1, 2, 2)
                plt.pie(l2,labels=l2)
                plt.title("pie plot")
                plt.show()
            else:
                messagebox.showinfo("info","all number sum should be 100")
        except:
            messagebox.showinfo("info","some error occured")
def thm():
    if clicked2.get()=="white theme":
        root.config(bg="white")
    else:
        root.config(bg="black")
root=Tk()
root.config(bg="white")
root.title("workpage")
photo = PhotoImage(file = "logo.png")
root.iconphoto(False,photo)
root.geometry("1600x900+0+0")
f1=Frame(root,bg="grey",width=270,height=900)
f1.place(x=0,y=0)
l1=Label(f1,fg="white",font=("Times", 20,"bold"),bg="black",text='''connect with data 
base''')
l1.place(x=30,y=30)
l2=Label(f1,text="database name",bg="grey")
l2.place(x=10,y=160)
l3=Label(f1,text="user name",bg="grey")
l3.place(x=10,y=200)
l4=Label(f1,text="password",bg="grey")
l4.place(x=10,y=240)
l5=Label(f1,text="host name",bg="grey")
l5.place(x=10,y=280)
bg=ImageTk.PhotoImage(file="logo2.jpg")
bglb=Label(root,image=bg)
bglb.place(x=300,y=20,height=100,width=100)
l5=Label(root,text="Data visulizer",bg="white",fg="black")
l5.place(x=310,y=128)
e1=Entry(f1)
e1.place(x=100,y=163)
e2=Entry(f1)
e2.place(x=100,y=203)
e3=Entry(f1)
e3.place(x=100,y=243)
e4=Entry(f1)
e4.place(x=100,y=283)

f2=Frame(root,highlightbackground="black", highlightthickness=2,width=20,height=20,bg="white")
f2.place(x=1400,y=30)
l6=Label(root,text="connection status",bg="white")
l6.place(x=1428,y=28)
l7=Label(f1,fg="white",font=("Times", 20,"bold"),bg="black",text='''data for draw 
graph''')
l7.place(x=40,y=340)
l8=Label(f1,text="data field1",bg="grey")
l8.place(x=10,y=440)
l9=Label(f1,text="data field2",bg="grey")
l9.place(x=10,y=480)
l11=Label(f1,text="table name",bg="grey")
l11.place(x=10,y=520)
e5=Entry(f1)
e5.place(x=100,y=443)
e6=Entry(f1)
e6.place(x=100,y=483)
e7=Entry(f1)
e7.place(x=100,y=523)
b1=Button(f1,text="connect",command=work)
b1.place(x=70,y=560)
b2=Button(f1,text="view data",command=vt)
b2.place(x=150,y=560)
detfrm=Frame(root,bd=4,relief=RIDGE,bg="grey")
detfrm.place(x=275,y=160,width=780,height=620)
tabfrm=Frame(detfrm,bd=4,relief=RIDGE,bg="lightblue")
tabfrm.place(x=10,y=10,width=750,height=590)
scrollx=Scrollbar(tabfrm,orient=HORIZONTAL)
scrolly=Scrollbar(tabfrm,orient=VERTICAL)
medtab=ttk.Treeview(tabfrm,columns=("data1","data2"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrollx.config(command=medtab.xview)
scrolly.config(command=medtab.yview)
medtab.heading("data1",text="data1")
medtab.heading("data2",text="data2")
medtab['show']="headings"
medtab.column("data1",width=200)
medtab.column("data2",width=300)
medtab.pack(fill=BOTH,expand=1)
medtab.bind("<ButtonRelease-1>",vt)

l10=Label(root,text="Copyright (c) 2023 Rajib Paul",bg="white")
l10.place(x=540,y=780)

l12=Label(root,text="do you want help?",bg="white")
l12.place(x=1270,y=28)
b3=Button(root,text="click",command=help)
b3.place(x=1300,y=65)

options = [
    "Line plot",
    "Pie plot",
    "Histogram plot",
    ] 
# datatype of menu text
clicked =StringVar()
# initial menu text
clicked.set( "Line plot" )
drop =OptionMenu( root , clicked ,*options )
drop.place(x=1130,y=28)
b4=Button(root,text="view graph",command=other)
b4.place(x=1140,y=65)

l13=Label(root,text="other select:",bg="white")
l13.place(x=1050,y=28)

def slider_changed(event):  
    print(slider.get())

slider = ttk.Scale(
    root,
    from_=4,
    to=0,
    orient='vertical',
)
slider.set(0)
slider.place(x=1000,y=28)

f3=Frame(root,width=20,height=100)
f3.place(x=970,y=28)
f4=Frame(f3,bg="red",width=20,height=20)
f4.place(x=0,y=0)
f5=Frame(f3,bg="orange",width=20,height=20)
f5.place(x=0,y=20)
f6=Frame(f3,bg="yellow",width=20,height=20)
f6.place(x=0,y=40)
f7=Frame(f3,bg="greenyellow",width=20,height=20)
f7.place(x=0,y=60)
f8=Frame(f3,bg="green",width=20,height=20)
f8.place(x=0,y=80)
l14=Label(root,text="row count:",bg="white")
l14.place(x=900,y=28)

options2 = [
   "white theme",
   "black theme",
] 
# datatype of menu text
clicked2 =StringVar()
# initial menu text
clicked2.set( "white theme" )
drop2 =OptionMenu( root , clicked2 ,*options2 )
drop2.place(x=770,y=28)
b5=Button(root,text="ok",command=thm)
b5.place(x=810,y=70)
figure1 = plt.Figure(figsize=(7,5), dpi=60)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().place(x=1080,y=140)
ax1.set_xlabel("data1")
ax1.set_ylabel("data2")
ax1.set_title('data1 vs data2') 

figure2 = plt.Figure(figsize=(7,5), dpi=60)
ax2 = figure1.add_subplot(111)
bar2 = FigureCanvasTkAgg(figure1, root)
bar2.get_tk_widget().place(x=1080,y=450)
ax2.set_xlabel("data1")
ax2.set_ylabel("data2")
ax2.set_title('data1 vs data2')

root.mainloop()