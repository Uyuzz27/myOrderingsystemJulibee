from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

mypass = ""
mydatabase = "julibeedb"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

menuTable = "menu"


def View():
    root = Tk()
    root.title("Julibee")
    root.minsize(width=400, height=400)
    root.geometry("600x600")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="red", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Menu", bg='white', fg='red', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='white')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    #scroll
    mycanvas=Canvas(labelFrame, bg='red')
    mycanvas.pack(side=LEFT ,fill="both" , expand="yes")
    yscrollbar=ttk.Scrollbar(labelFrame, orient="vertical", command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT, fill="y")

    myframe=Frame(mycanvas, bg='white')
    myframe.pack()
    Label(labelFrame, text="%-10s%-50s%-40s" % ('Code', 'Name', 'Price'), bg='red', fg='white').place(
        relx=0.07, rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------", bg='red',
          fg='white').place(relx=0.05, rely=0.2)
    getMenu = "select * from " + menuTable
    try:
        cur.execute(getMenu)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-50s%-40s" % (i[1], i[2], i[3]), bg='red', fg='white').place(
                relx=0.07, rely=y)
            y += 0.05
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root, text="Quit", bg='red', fg='white', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()