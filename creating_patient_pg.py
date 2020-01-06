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
        frame4 = Toplevel(self.root)
        frame4.grid()

        ptleftframe = Frame(self.root, bd=2, width=420, height=400, padx=50, pady=10, relief=GROOVE)
        ptleftframe.pack(side=LEFT)

        ptmiddleframe = Frame(self.root, bd=2, width=420, height=400, padx=50, pady=10, relief=GROOVE)
        ptmiddleframe.pack(side=LEFT)

        ptrightframe = Frame(self.root, bd=2, width=420, height=400, padx=20, pady=10, relief=GROOVE)
        ptrightframe.pack(side=LEFT)









root=Tk()
a = GPPage(root)
root.mainloop()

