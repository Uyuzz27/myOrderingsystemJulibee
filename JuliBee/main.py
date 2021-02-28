from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from Admin import *
from Customer import *


#thinker
root = Tk()
root.title("Welcome to Julius Ordering System")
root.minsize(width=400,height=400)
root.geometry("1200x1000")

# Take n greater than 0.25 and less than 5
same=True
n=0.25
Canvas1 = Canvas(root)


#the windows main
headingFrame1 = Frame(root,bg="red",bd=5)
headingFrame1.place(relx=0.2,rely=0,relwidth=0.6,relheight=0.15)
headingLabel = Label(headingFrame1, text="Welcome to \n Julibee", bg='white', fg='red', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
adminPic = PhotoImage(file = r"C:\Users\Julius kieth estrell\PycharmProjects\JuliBee\Julibee\begining\admin2.png")
btn1 = Button(root, image=adminPic,bg='White', fg='red', command=adminWin)
btn1.place(relx=0.1, rely=0.15,relwidth=0.4, relheight=0.8)
orderPic = PhotoImage(file = r"C:\Users\Julius kieth estrell\PycharmProjects\JuliBee\Julibee\begining\order1.png")
btn2 = Button(root, image=orderPic,bg='white', fg='red', command=intname)
btn2.place(relx=0.5, rely=0.15, relwidth=0.4, relheight=0.8)


root.mainloop()