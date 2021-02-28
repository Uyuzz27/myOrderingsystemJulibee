from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from Order import *

def getName():
    name = info1.get()
    total = 0

    insertMenu = "insert into customers values(' NULL ','" + name + "','" + str(total) + "')"
    cur.execute(insertMenu)
    con.commit()
    messagebox.showinfo('Success', "Please go to Order to Proceed!")

    root.mainloop()

def intname():
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

     # customers name
     lb1 = Label(labelFrame, text="Name ", bg='white', fg='red')
     lb1.place(relx=0.05, rely=0.2, relheight=0.08)

     info1 = Entry(labelFrame)
     info1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

     # Submit Button
     SubmitBtn = Button(root, text="SUBMIT", bg='red', fg='white', command=getName)
     SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

     quitBtn = Button(root, text="Quit", bg='red', fg='white', command=root.destroy)
     quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

     SubmitBtn = Button(root, text="Order", bg='red', fg='white',command= user)
     SubmitBtn.place(relx=0.78, rely=0.6, relwidth=0.18, relheight=0.08)

     root.mainloop()


