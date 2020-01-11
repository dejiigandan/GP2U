from tkinter import *
import pt_db_connectivity
import tkinter.messagebox
import sqlite3
from tkinter import ttk

class PatientPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient")
        self.root.geometry("750x700+780+160")
        #frame4 = Toplevel(self.root)
        #frame4.grid()

        # ptleftframe = Frame(self.root, bd=2, width=420, height=400, padx=50, pady=10, relief=GROOVE)
        # ptleftframe.pack(side=LEFT)
        #
        # ptmiddleframe = Frame(self.root, bd=2, width=420, height=400, padx=50, pady=10, relief=GROOVE)
        # ptmiddleframe.pack(side=LEFT)
        #
        # ptrightframe = Frame(self.root, bd=2, width=420, height=400, padx=20, pady=10, relief=GROOVE)
        # ptrightframe.pack(side=LEFT)

        def sendrequest():
            if (len(entryptnhsno.get()) != 0) and (len(entryptsurname.get()) != 0) and (len(entryptdate.get()) != 0) and (len(entrypttime.get()) != 0):
                pt_db_connectivity.request_apptmt(entryptnhsno.get(), entryptsurname.get(), entryptdate.get(), entrypttime.get())
                tkinter.messagebox.showinfo(title="Request sent", message="Request sent")

            else:
                tkinter.messagebox.showinfo(title="Error", message="Please fill all fields")

        #---------------------------------  NOTEBOOK ---------------------------------

        ptnotebook = ttk.Notebook(root)
        ptnotebook.pack()

        ptleftframe = ttk.Frame(ptnotebook)
        ptleftframe.pack(side=LEFT)

        ptmiddleframe = ttk.Frame(ptnotebook)
        ptmiddleframe.pack(side=LEFT)

        ptrightframe = ttk.Frame(ptnotebook)
        ptrightframe.pack(side=LEFT)

        ptnotebook.add(ptleftframe, text="Appointment availabilities")
        ptnotebook.add(ptmiddleframe, text="Book an appointment")
        ptnotebook.add(ptrightframe, text="Cancel an appointment")

#--------------------------------- LEFT FRAME   -----------------------------------------------


        def pt_fill_list():
            """This lists the available appointments in the leftmost tab"""
            ptavail_box.delete(0, END)
            for row in pt_db_connectivity.list_avail():
                ptavail_box.insert(END, row)


        def cursorselect(event):
            try:
                global selectedTimeslot
                timeslot = ptavail_box.curselection()[0]
                selectedTimeslot = ptavail_box.get(timeslot)

                entryptdate.delete(0, END)
                entryptdate.insert(END, selectedTimeslot[0])        # fills the entry boxes in the middle tab with the chosen timeslot and time
                entrypttime.delete(0, END)
                entrypttime.insert(END, selectedTimeslot[1])
            except IndexError:
                pass

        global ptavail_box
        ptavail_box = Listbox(ptleftframe, height=25, width=55, font=('calibri', 13, 'bold'))
        ptavail_box.grid(row=0, column=0)

        pt_fill_list()

        ptavail_box.bind('<<ListboxSelect>>', cursorselect)

##--------------------------------- MIDDLE FRAME ------------------------------------------------

        pt_nhs_no = StringVar()
        self.pt_nhs_no = pt_nhs_no

        ptSurname = StringVar()
        self.ptSurname = ptSurname

        ptappdate = StringVar()
        self.ptappdate = ptappdate

        ptapptime = StringVar()
        self.ptapptime = ptapptime


        searchbytext = Label(ptmiddleframe, text="Enter NHS number:", font=('calibri', 12), padx=2, pady=2)
        searchbytext.grid(row=0, column=0, sticky=W)

        global pt_searchby_nhsentry
        pt_searchby_nhsentry = Entry(ptmiddleframe, font=('calibri', 12, 'bold'), width=22)
        pt_searchby_nhsentry.grid(row=0, column=1, sticky=W)

        ptsearch_btn = Button(ptmiddleframe, text="Search", font=('calibri', 12), height=1, width=8, relief=RAISED, command=self.ptsearch_user)
        ptsearch_btn.grid(row=0, column=1, sticky=E)

        labelptnhsno = Label(ptmiddleframe, font=('calibri', 16, 'bold'), text="NHS No:", padx=2, pady=2)
        labelptnhsno.grid(row=1, column=0, sticky=W)
        entryptnhsno = Entry(ptmiddleframe, font=('calibri', 16, 'bold'), textvariable=self.pt_nhs_no, width=25)
        entryptnhsno.grid(row=1, column=1)

        labelptsurname = Label(ptmiddleframe, font=('calibri', 16, 'bold'), text="Surname:", padx=2, pady=2)
        labelptsurname.grid(row=2, column=0, sticky=W)
        entryptsurname = Entry(ptmiddleframe, font=('calibri', 16, 'bold'), textvariable=self.ptSurname, width=25)
        entryptsurname.grid(row=2, column=1)

        labelptdate = Label(ptmiddleframe, font=('calibri', 16, 'bold'), text="Enter date:", padx=2, pady=2)
        labelptdate.grid(row=3, column=0, sticky=W)
        entryptdate = Entry(ptmiddleframe, font=('calibri', 16, 'bold'), textvariable=self.ptappdate, width=25)
        entryptdate.grid(row=3, column=1)

        labelpttime = Label(ptmiddleframe, font=('calibri', 16, 'bold'), text="Enter time:", padx=2, pady=2)
        labelpttime.grid(row=4, column=0, sticky=W)
        entrypttime = Entry(ptmiddleframe, font=('calibri', 16, 'bold'), textvariable=self.ptapptime, width=25)
        entrypttime.grid(row=4, column=1)

        request_aptmt_btn = Button(ptmiddleframe, text="Request appointment", font=('calibri', 12), height=1, width=20, relief=RAISED, command=sendrequest)
        request_aptmt_btn.grid(row=5, column=1, sticky=E)

# --------------------------------------------- RIGHT FRAME-------------------------------------------------------

        global pbookings_box
        pbookings_box = Listbox(ptrightframe, height=25, width=55, font=('calibri', 13, 'bold'))
        pbookings_box.grid(row=1, column=0)

        rightframetit = Label(ptrightframe, font=('calibri', 16, 'bold'), text="Confirmed appointments", padx=2, pady=2)
        rightframetit.grid(row=0, column=0)


#-------------------------------------------SOME FUNCTIONS------------------------------------------------------
    def ptsearch_user(self):
        try:
            conn = sqlite3.connect("ptdatabase.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM patient_details WHERE nhs_number='%s'" %pt_searchby_nhsentry.get().title())
            conn.commit()
            row = cursor.fetchone()
            self.pt_nhs_no.set(row[1])
            self.ptSurname.set(row[2])
            conn.commit()
            conn.close()
        except:
             tkinter.messagebox.showinfo(title="No user error", message="User account not found in our records")










root=Tk()
a = PatientPage(root)
root.mainloop()

