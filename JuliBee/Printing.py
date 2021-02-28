from tkinter import *
from tkinter import ttk
import time


def printing():
    root = Tk()
    root.title("Julibee")
    root.minsize(width=50, height=50)
    root.geometry("200x150")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)


    labelFrame = Frame(root, bg='white')
    labelFrame.place(relx=0.0, rely=0.0, relwidth=0.8, relheight=0.5)

    Label(labelFrame, text="Printing Reciept....", bg='red', fg='white').place(
    relx=0.07, rely=0.1)


    Label(labelFrame, text="Finish Printing", bg='red', fg='white').place(
        relx=0.07, rely=0.5)
    quitBtn = Button(root, text="Finish", bg='red', fg='white', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.7, relwidth=0.18, relheight=0.15)


    root.mainloop()