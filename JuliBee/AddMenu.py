from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql


def menuRegister():
    code = info1.get()
    name = info2.get()
    price = info3.get()



    insertMenu = "insert into " + menuTable + " values('NULL','" + code + "','" + name + "','" + price + "')"
    try:
        cur.execute(insertMenu)
        con.commit()
        messagebox.showinfo('Success', "Meal added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")

    print(code)
    print(name)
    print(price)

    root.destroy()


def addMenu():
    global info1, info2, info3, Canvas1, con, cur, menuTable, root

    root = Tk()
    root.title("Julibee")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = ""
    mydatabase = "julibeedb"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    menuTable = "menu"  # menu Table

    Canvas1 = Canvas(root)

    Canvas1.config(bg="White")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="red", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Menu", bg='white', fg='red', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='white', bd=5)
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Code
    lb1 = Label(labelFrame, text="Code : ", bg='white', fg='red')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    info1 = Entry(labelFrame)
    info1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Name
    lb2 = Label(labelFrame, text="Name : ", bg='white', fg='red')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    info2 = Entry(labelFrame)
    info2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # price
    lb3 = Label(labelFrame, text="Price : ", bg='white', fg='red')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    info3 = Entry(labelFrame)
    info3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='red', fg='white', command=menuRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='red', fg='white', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()