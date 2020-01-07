from tkinter import *
import pt_db_connectivity
import tkinter.messagebox
import sqlite3
from tkinter import ttk

class PatientPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient")
        self.root.geometry("750x600+770+200")
        #frame4 = Toplevel(self.root)
        #frame4.grid()

        ptleftframe = Frame(self.root, bd=2, width=420, height=400, padx=50, pady=10, relief=GROOVE)
        ptleftframe.pack(side=LEFT)

        ptmiddleframe = Frame(self.root, bd=2, width=420, height=400, padx=50, pady=10, relief=GROOVE)
        ptmiddleframe.pack(side=LEFT)

        ptrightframe = Frame(self.root, bd=2, width=420, height=400, padx=20, pady=10, relief=GROOVE)
        ptrightframe.pack(side=LEFT)

        def pt_fill_list():
            """This lists the available appointments in the middle box"""
            avail_box.delete(0, END)
            for row in pt_db_connectivity.list_avail():
                avail_box.insert(END, row)

        avail_box = Listbox(ptmiddleframe, height=25, width=55, font=('calibri', 13, 'bold'))
        avail_box.grid(row=0, column=0)

        pt_fill_list()








root=Tk()
a = PatientPage(root)
root.mainloop()

