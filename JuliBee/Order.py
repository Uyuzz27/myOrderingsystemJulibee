from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from Printing import printing

def user():
    global result1, result2, result3,code, root, con, cur
    # Add your own database name and password here to reflect in the code
    root = Tk()
    root.title("Julibee")
    root.minsize(width=800, height=800)
    root.geometry("600x500")

    mypass = ""
    mydatabase = "julibeedb"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    info1="select id from customers order by id desc limit 1"
    cur.execute(info1)
    result1=cur.fetchone()
    info2="select name from customers order by id desc limit 1"
    cur.execute(info2)
    result2=cur.fetchone()
    info3="select total from customers order by id desc limit 1"
    cur.execute(info3)
    result3=cur.fetchone()

    Canvas1 = Canvas(root)

    Canvas1.config(bg="White")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="red", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    heading= "Welcome Sir/Maam "+str(result2[0])+" Enjoy!!"

    headingLabel = Label(headingFrame1, text=heading, bg='white', fg='red', font=('Courier', 10))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


    labelFrame1 = Frame(root, bg="Red", bd=5)
    labelFrame1.place(relx=0.02, rely=0.29, relwidth=0.49, relheight=0.62)

    labelFrame = Frame(root, bg='red', bd=5)
    labelFrame.place(relx=0.03, rely=0.3, relwidth=0.47, relheight=0.6)
    y = 0.15


#menu
    Label(labelFrame, text="%-10s%-30s%-30s" % ('Code', 'Name', 'Price'), bg='red', fg='white').place(
        relx=0.01, rely=0.01)
    Label(labelFrame, text="----------------------------------------------------------------------------", bg='red',
          fg='white').place(relx=0.01, rely=0.1)
    getMenu = "select * from menu"
    cur.execute(getMenu)
    con.commit()
    for i in cur:
        Label(labelFrame, text="%-10s%-30s%-20s" % (i[1], i[2], i[3]), bg='red', fg='white').place(relx=0.01, rely=y)
        btn= Button(labelFrame,  text="buy", bg='white', fg='red', command=lambda i=i:itemQty(i))
        btn.place(relx=0.9, rely=y, relwidth=0.1, relheight=0.07)
        y += 0.07



#view order
    viewFrame = Frame(root, bg='black', bd=5)
    viewFrame.place(relx=0.52, rely=0.3, relwidth=0.47, relheight=0.6)

    x = 0.15
    Label(viewFrame, text="%-10s%-40s%-40s%-10s" % ('Code', 'Name', 'Qty', 'Price'), bg='black', fg='white').place(
        relx=0.01, rely=0.01)
    Label(viewFrame, text="----------------------------------------------------------------------------", bg='black',
          fg='white').place(relx=0.01, rely=0.1)
    getMenu = "select * from orders where customers_id ='"+str(result1[0])+"'"
    try:
        cur.execute(getMenu)
        con.commit()
        for e in cur:
            Label(viewFrame, text="%-10s%-40s%-40s%-10s" % (e[3], e[4], e[5],e[6]), bg='black', fg='white').place(
                relx=0.01, rely=x)
            x += 0.05
    except:
        messagebox.showinfo("Failed to fetch files from database")
    SubmitBtn = Button(root, text="CheckOut", bg='red', fg='white', command=checkOut)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='red', fg='white', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

def checkOut():
    root2 = Tk()
    root2.title("Julibee")
    root2.minsize(width=300, height=300)
    root2.geometry("600x500")
    Canvas2 = Canvas(root2)

    Canvas2.config(bg="White")
    Canvas2.pack(expand=True, fill=BOTH)

    headingFrame2 = Frame(root2, bg="red", bd=5)
    headingFrame2.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel2 = Label(headingFrame2, text="Reciept", bg='white', fg='red', font=('Courier', 15))
    headingLabel2.place(relx=0, rely=0, relwidth=1, relheight=1)


    headingLabel3 = Label(root2, text="Thank you Sir/ Maam "+str(result2[0]), bg='white', fg='red', font=('Courier', 10))
    headingLabel3.place(relx=0.1, rely=0.25, relwidth=0.82, relheight=0.13)

    printFrame2 = Frame(root2, bg='red', bd=5)
    printFrame2.place(relx=0.09, rely=0.39, relwidth=0.82, relheight=0.42)
    printFrame2 = Frame(root2, bg='white', bd=5)
    printFrame2.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)
    x = 0.30
    Label(printFrame2, text="%-10s%-40s%-40s%-10s" % ('Code', 'Name', 'Qty', 'Price'), bg='white', fg='red').place(
        relx=0.01, rely=0.01)
    Label(printFrame2, text="----------------------------------------------------------------------------", bg='white',
          fg='black').place(relx=0.01, rely=0.15)
    getMenu = "select * from orders where customers_id ='"+str(result1[0])+"'"
    try:
        cur.execute(getMenu)
        con.commit()
        for e in cur:
            Label(printFrame2, text="%-10s%-40s%-40s%-10s" % (e[3], e[4], e[5],e[6]), bg='white', fg='red').place(
                relx=0.01, rely=x)
            x += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    total="select sum(price) from orders where customers_id ='"+str(result1[0])+"'"
    cur.execute(total)
    total1=cur.fetchone()

    Label(printFrame2, text="Total = P"+str(total1[0]),bg='white', fg='red' , font=('Courier', 15)).place(relx=0.3, rely=0.7)

    SubmitBtn = Button(root2, text="CheckOut", bg='red', fg='white', command=printing)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root2, text="Quit", bg='red', fg='white', command=root2.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)


def buy():
    global prices

    itemcode=itemid
    qty=iteminfo1.get()
    itemnames=itemname
    id=result1
    name=result2
    prices=itemprice
    total=result3
    price=int(prices)*int(qty)

    print(itemcode, qty, id, name, total,itemnames)

    orders="insert into orders values('NULL','" + str(id[0]) + "','" + str(name[0]) + "','" + itemcode + "','" + itemname + "','" + qty + "','" + str(price) + "')"
    try:
        cur.execute(orders)
        con.commit()
        messagebox.showinfo('Success', "Meal added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")

    root1.mainloop()

def itemQty(meal):
    global iteminfo1, itemid, root1, itemprice, itemname

    root1 = Tk()
    root1.title("Julibee")
    root1.minsize(width=200, height=200)
    root1.geometry("600x500")


    itemid=str(meal[1])
    itemprice=str(meal[3])
    itemname=str(meal[2])

    Canvas1 = Canvas(root1)

    Canvas1.config(bg="White")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root1, bg="red", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel1 = Label(headingFrame1, text="Add Menu", bg='white', fg='red', font=('Courier', 15))
    headingLabel1.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame1 = Frame(root1, bg='white', bd=5)
    labelFrame1.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # quantity
    quantity = Label(labelFrame1, text="Quantity: ", bg='white', fg='red')
    quantity.place(relx=0.05, rely=0.2, relheight=0.08)

    iteminfo1 = Entry(labelFrame1)
    iteminfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    addBtn = Button(root1, text="buy", bg='red', fg='white',command= buy)
    addBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
    quitBtn = Button(root1, text="Quit", bg='red', fg='white', command=root1.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    