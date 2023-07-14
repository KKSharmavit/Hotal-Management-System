from tkinter import*
import tkinter
from tkinter import ttk
from tkinter import messagebox
import datetime
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import mysql.connector
import random


class Info_details():
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1121x533+234+215")
        self.root.wm_iconbitmap('icon.ico')

        ################ Title ##################
        lbl_title = Label(self.root,text="STAFF INFORMATION",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1121,height=35)

        ################## Logo ######################
        img4 = Image.open(r"images\logohotel.png")
        img4 = img4.resize((100, 32), Image.ANTIALIAS)
        self.photoimage4 = ImageTk.PhotoImage(img4)
        lblimg4 = Label(self.root, image=self.photoimage4, borderwidth=0)
        # lblimg2.place(x=690,y=0,width=220,height=140)
        lblimg4.place(x=5, y=2, width=100, height=32)

        ##################  info ###########################
        img3 = Image.open("images\REPORTS.PNG")
        img3 = img3.resize((1100,417),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1 = Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=35,width=1120,height=418)


if __name__ == "__main__":
    root=Tk()
    Obj=Info_details(root)
    root.mainloop()