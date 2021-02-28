from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddMenu import *
from Menu import *
from DeleteMenu import *

def adminWin():
    #thinker
    root = Tk()
    root.title("Welcome to Julius Ordering System")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Take n greater than 0.25 and less than 5
    same=True
    n=0.25

    # Adding a background image
    background_image =Image.open("Jobi.png")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth * n)
    if same:
        newImageSizeHeight = int(imageSizeHeight * n)
    else:
        newImageSizeHeight = int(imageSizeHeight / n)

    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)

    Canvas1.config(bg="White")
    Canvas1.pack(expand=True, fill=BOTH)

    #mysql
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

    btn2 = Button(root, text="Delete Menu", bg='white', fg='red', command=delete)
    btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    btn3 = Button(root, text="View Menu List", bg='white', fg='red', command=View)
    btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

    quitBtn = Button(root, text="Back", bg='red', fg='white', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

