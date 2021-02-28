from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
from AddMenu import *
# Add your own database name and password here to reflect in the code
mypass = ""
mydatabase = "julibeedb"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

# Enter Table Names here
menuTable = "menu"  # Book Table


def deleteMenu():
    code = Info1.get()

    deleteSql = "delete from " + menuTable + " where code = '" + code + "'"
    try:
        cur.execute(deleteSql)
        con.commit()
        messagebox.showinfo('Success', "Meal in Menu Deleted Successfully")
    except:
        messagebox.showinfo("Please check Meal Code")

    print(code)

    Info1.delete(0, END)
    root.destroy()


def delete():
    global Info1, Info2, Info3, Canvas1, con, cur, menuTable, root

    root = Tk()
    root.title("Julibee")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="red", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete", bg='white', fg='red', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='white')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)


    lb2 = Label(labelFrame, text="Meal Code : ", bg='white', fg='red')
    lb2.place(relx=0.05, rely=0.5)

    Info1 = Entry(labelFrame)
    Info1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='red', fg='white', command=deleteMenu)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='red', fg='white', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()