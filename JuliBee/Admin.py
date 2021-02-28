from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from adminwindow import *
from AddMenu import *
from Menu import *
from DeleteMenu import *

def popmesage():
    popup=ttk

    popup.wm_title("!")
    label=ttk.Label(popup, text="msg",)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="proced", command=adminWin)
    B1.pack()
    popup.mainloop

def login():
    #database
    mypass = ""
    mydatabase = "julibeedb"
    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()
    #table
    admin="admin"

    name = Username.get()
    passw = password.get()

    user1="select user_name from "+admin+" where id='1'"
    cur.execute(user1)
    user2=cur.fetchone()
    pass1="select pass from "+admin+" where id='1'"
    cur.execute(pass1)
    pass2=cur.fetchone()

    if name !=0:
        name == user2
        if passw !=0:
            passw == pass2

            def adminWin():
                # thinker
                root = Tk()
                root.title("Welcome to Julius Ordering System")
                root.minsize(width=400, height=400)
                root.geometry("600x500")

                Canvas1 = Canvas(root)

                Canvas1.config(bg="White")
                Canvas1.pack(expand=True, fill=BOTH)

                # mysql
                mypass = ""
                mydatabase = "julibeedb"
                con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
                cur = con.cursor()

                # the windows main
                headingFrame1 = Frame(root, bg="Red", bd=5)
                headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

                headingLabel = Label(headingFrame1, text="Welcome \n Admin", bg='white', fg='red', font=('Courier', 15))
                headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

                btn1 = Button(root, text="Add Meal Details", bg='white', fg='red', command=addMenu)
                btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

                btn2 = Button(root, text="Delete Book", bg='white', fg='red', command=delete)
                btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

                btn3 = Button(root, text="View Menu List", bg='white', fg='red', command=View)
                btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

                quitBtn = Button(root, text="Back", bg='red', fg='white', command=root.destroy)
                quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

                root.mainloop()



def loginadmin():
    global Username, password, Canvas1, con, cur, admin, root
    #thinkter
    root = Tk()
    root.title("Julibee")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="red", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Welcome Admin", bg='White', fg='red', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='red')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Code
    lb1 = Label(labelFrame, text="Name ", bg='white', fg='red')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    Username = Entry(labelFrame)
    Username.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Name
    lb2 = Label(labelFrame, text="Password : ", bg='white', fg='red')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)
    password = Entry(labelFrame)
    password.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=login)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()