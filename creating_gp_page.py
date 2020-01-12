from tkinter import *
import pt_db_connectivity
import tkinter.messagebox
import sqlite3
from tkinter import ttk

class GPPage:
    def __init__(self, root):
        self.root = root
        self.root.title("GP")
        self.root.geometry("750x600+770+200")
        #frame3 = Toplevel(self.root)
        #frame3.grid()

        # leftframe = Frame(self.root, bd=2, width=420, height=400, padx=50, pady=10, relief=GROOVE)
        # leftframe.pack(side=LEFT)
        #
        # middleframe = Frame(self.root, bd=2, width=420, height=400, padx=50, pady=10, relief=GROOVE)
        # middleframe.pack(side=LEFT)
        #
        # rightframe = Frame(self.root, bd=2, width=420, height=400, padx=20, pady=10, relief=GROOVE)
        # rightframe.pack(side=LEFT)
################################# NOTEBOOK######################################################

        notebook = ttk.Notebook(root)
        notebook.pack()

        leftframe = ttk.Frame(notebook)
        leftframe.pack(side=LEFT)

        middleframe = ttk.Frame(notebook)
        middleframe.pack(side=LEFT)

        rightframe = ttk.Frame(notebook)
        rightframe.pack(side=LEFT)

        notebook.add(leftframe, text="Manage availabilities")
        notebook.add(middleframe, text="Bookings")
        notebook.add(rightframe, text="Prescriptions")


################################################################################################
        # -----------------------------FUNCTIONS-------------------------------------------------
        def fill_list():
            avail_box.delete(0, END)
            for row in pt_db_connectivity.list_avail():
                avail_box.insert(END, row)

        def add_myavails():
            if (len(apdate_entry.get()) != 0) and (len(apttime_entry.get()) != 0) and (len (name_show_entry.get()) != 0):
                pt_db_connectivity.add_new_availability(apdate_entry.get(), apttime_entry.get(), name_show_entry.get())
                avail_box.delete(0, END)
                avail_box.insert(END, (apdate_entry.get(), apttime_entry.get(), name_show_entry.get()))
                fill_list()
            else:
                tkinter.messagebox.showinfo(title="Error", message="Please ensure all fields are complete")

        def selectitem(command):
            try:
                global selected
                datesel = avail_box.curselection()[0]
                selected = avail_box.get(datesel)
            except IndexError:
                pass


        def del_avail():
            pt_db_connectivity.delete_availability(selected[0], selected[1], selected[2])
            fill_list()


#----------------- Entry boxes in leftframre--------------------------

        enteredapt = StringVar
        self.enteredapt = enteredapt

        enteredtime = StringVar
        self.enteredtime =enteredtime

        # aptdate = StringVar
        # aptime = StringVar

        name_show = StringVar
        self.name_show = name_show

        aptdate_label = Label(leftframe, text="Date", font=('calibri', 12, 'bold'), padx=2, pady=2)
        aptdate_label.grid(row=0, column=0, sticky=W)
        apdate_entry = Entry(leftframe, font=('calibri', 12, 'bold'), textvariable=self.enteredapt, width=20)
        apdate_entry.grid(row=0, column=0, sticky=E)

        apttime_label = Label(leftframe, text="Time", font=('calibri', 12, 'bold'), padx=2, pady=2)
        apttime_label.grid(row=1, column=0, sticky=W)
        apttime_entry = Entry(leftframe, font=('calibri', 12, 'bold'), textvariable=self.enteredtime, width=20)
        apttime_entry.grid(row=1, column=0, sticky=E)

        name_show_label = Label(leftframe, text="Name", font=('calibri', 12, 'bold'), padx=2, pady=2)
        name_show_label.grid(row=2, column=0, sticky=W)
        name_show_entry = Entry(leftframe, font=('calibri', 12, 'bold'), textvariable=self.name_show, width=20)
        name_show_entry.grid(row=2, column=0, sticky=E)


        add_btn = Button(leftframe, text="Add availability", font=('calibri', 12), height=1, width=16, relief=RAISED, command=add_myavails)
        add_btn.grid(row=3, column=0, sticky=W)

        delete_btn = Button(leftframe, text="Delete availability", font=('calibri', 12), height=1, width=16, relief=RAISED, command=del_avail)
        delete_btn.grid(row=3, column=0, sticky=E)

# ---------------------availabilities listbox------------------------------------------------
        global avail_box
        avail_box = Listbox(leftframe, height=25, width=55)
        avail_box.grid(row=4, column=0)

        scrollbar = Scrollbar(leftframe)
        scrollbar.grid(row=4, column=1)
        avail_box.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=avail_box)

        avail_box.bind('<<ListboxSelect>>', selectitem)

        fill_list()
#---------------------------------------- RIGHT FRAME------------------------------------------------------------------

        presbox = LabelFrame(rightframe, bd=1, width=400, height=300, relief=RIDGE, font=('calibri', 18, 'bold'), text="Create a prescription", padx=2, pady=2)
        presbox.pack(side=TOP)

        labelrighttitle = Label(presbox, font=('calibri', 15), text="Title, name & address", padx=2, pady=2)
        labelrighttitle.grid(row=1, column=0, sticky=W)
        entryrighttitle = Entry(presbox, font=('calibri', 15), width=20)
        entryrighttitle.grid(row=1, column=1)

        labeldobage = Label(presbox, font=('calibri', 15), text="Date of Birth & Age", padx=2, pady=2)
        labeldobage.grid(row=2, column=0, sticky=W)
        entrydobage = Entry(presbox, font=('calibri', 15), width=20)
        entrydobage.grid(row=2, column=1)

        labeldrugname = Label(presbox, font=('calibri', 15), text="Drug name", padx=2, pady=2)
        labeldrugname.grid(row=3, column=0, sticky=W)
        entrydrugname = Entry(presbox, font=('calibri', 15), width=20)
        entrydrugname.grid(row=3, column=1)

        labeldrugstrength = Label(presbox, font=('calibri', 15), text="Drug strength", padx=2, pady=2)
        labeldrugstrength.grid(row=4, column=0, sticky=W)
        entrydrugstrength = Entry(presbox, font=('calibri', 15), width=20)
        entrydrugstrength.grid(row=4, column=1)

        labeldrugquantity = Label(presbox, font=('calibri', 15), text="Quntity", padx=2, pady=2)
        labeldrugquantity.grid(row=5, column=0, sticky=W)
        entrydrugquantity = Entry(presbox, font=('calibri', 15), width=20)
        entrydrugquantity.grid(row=5, column=1)

        labelformulation = Label(presbox, font=('calibri', 15), text="Formulation", padx=2, pady=2)
        labelformulation.grid(row=6, column=0, sticky=W)
        entryformulation = Entry(presbox, font=('calibri', 15), width=20)
        entryformulation.grid(row=6, column=1)

        labeldosage = Label(presbox, font=('calibri', 15), text="Dosage", padx=2, pady=2)
        labeldosage.grid(row=7, column=0, sticky=W)
        entrydosage = Entry(presbox, font=('calibri', 15), width=20)
        entrydosage.grid(row=7, column=1)

        labelsignature = Label(presbox, font=('calibri', 15), text="Electronic signature & GMC number", padx=2, pady=2)
        labelsignature.grid(row=8, column=0, sticky=W)
        entrysignature = Entry(presbox, font=('calibri', 15), width=20)
        entrysignature.grid(row=8, column=1)

        labeladdress = Label(presbox, font=('calibri', 15), text="Address (of surgery/Hospital)", padx=2, pady=2)
        labeladdress.grid(row=9, column=0, sticky=W)
        entryaddress = Entry(presbox, font=('calibri', 15), width=20)
        entryaddress.grid(row=9, column=1)
                    #------------------------------------------------------------------------#

        scriptbox = LabelFrame(rightframe, bd=1, width=400, height=300, relief=RIDGE, font=('calibri', 18, 'bold'), text="Sample prescription", padx=2, pady=2)
        scriptbox.pack(side=BOTTOM)

        placetittle = Label(scriptbox, text="great")#entryrighttitle.get()
        placetittle.place(x=250, y=10)

        placedobage = Label(scriptbox, text=entrydobage.get())
        placedobage.place(x=150, y=10)

#-------------------------------------------------------------------------------------------------------------------------------------

        middlebox = LabelFrame(middleframe, bd=1, width=400, height=500, relief=GROOVE, font=('calibri', 18, 'bold'), text="Appointment requests", padx=2, pady=2)
        middlebox.pack(side=TOP)

        global request_box
        request_box = Listbox(middlebox, height=25, width=55)
        request_box.grid(row=0, column=0)

        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        mymenu = Menu(menubar, tearoff=0)
        mymenu.add_command(label="New", command=self.donothing)
        menubar.add_cascade(label="File", menu=mymenu)


    def donothing(self):
        self.root.destroy()

root=Tk()
a = GPPage(root)
root.mainloop()

