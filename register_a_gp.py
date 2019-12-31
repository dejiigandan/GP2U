from tkinter import *
import pt_db_connectivity
import tkinter.messagebox
from tkinter import ttk

root = Tk()
frame = Frame(root)
frame.pack()

actionsframe = Frame(frame, width=500, height=40, padx=8, pady=6, relief=RIDGE)
actionsframe.pack(side=BOTTOM)
formframe = Frame(frame, bd=1, height=700, padx=15, pady=25, relief=RIDGE)
formframe.pack(side=TOP)

title = StringVar()
Firstname = StringVar()
Surname = StringVar()
DOB = StringVar()
Gender = StringVar()
Address = StringVar()
Contact_number = StringVar()

username = StringVar()
password = StringVar()

def add_gp():
    title = Label(formframe, font=('calibri', 20, 'bold'), text="Title:", padx=2, pady=2)
    title.grid(row=0, column=0, sticky=W)
    droptitle = ttk.Combobox(formframe, textvariable=title, font=('calibri', 20, 'bold'), width=29)

    droptitle['value'] = ('Select your title', 'Master', 'Miss', 'Mr', 'Mrs', 'Other')
    droptitle.current(0)
    droptitle.grid(row=0, column=1)

    labelfirstname = Label(formframe, font=('calibri', 20, 'bold'), text="First name:", padx=2, pady=2)
    labelfirstname.grid(row=2, column=0, sticky=W)
    entryfirstname = Entry(formframe, font=('calibri', 20, 'bold'), textvariable=Firstname, width=30)
    entryfirstname.grid(row=2, column=1)

    labelsurname = Label(formframe, font=('calibri', 20, 'bold'), text="Surname:", padx=2, pady=2)
    labelsurname.grid(row=3, column=0, sticky=W)
    entrysurname = Entry(formframe, font=('calibri', 20, 'bold'), textvariable=Surname, width=30)
    entrysurname.grid(row=3, column=1)

    labelgender = Label(formframe, font=('calibri', 20, 'bold'), text="Gender:", padx=2, pady=2)
    labelgender.grid(row=4, column=0, sticky=W)
    dropgender = ttk.Combobox(formframe, textvariable=Gender, font=('calibri', 20, 'bold'), width=29)

    dropgender['value'] = ('Select your gender', 'Male', 'Female', 'Non-binary', 'Other')
    dropgender.current(0)
    dropgender.grid(row=4, column=1)

    labeladdress = Label(formframe, font=('calibri', 20, 'bold'), text="Address:", padx=2, pady=2)
    labeladdress.grid(row=5, column=0, sticky=W)
    entryaddress = Entry(formframe, font=('calibri', 20, 'bold'), textvariable=Address, width=30)
    entryaddress.grid(row=5, column=1)

    labelcontact = Label(formframe, font=('calibri', 20, 'bold'), text="Contact number:", padx=2, pady=2)
    labelcontact.grid(row=6, column=0, sticky=W)
    entrycontact = Entry(formframe, font=('calibri', 20, 'bold'), textvariable=Contact_number, width=30)
    entrycontact.grid(row=6, column=1)

    labeldob = Label(formframe, font=('calibri', 20, 'bold'), text="Date of Birth:", padx=2, pady=2)
    labeldob.grid(row=7, column=0, sticky=W)
    entrydob = Entry(formframe, font=('calibri', 20, 'bold'), textvariable=DOB, width=30)
    entrydob.grid(row=7, column=1)

    labelusername = Label(actionsframe, font=('calibri', 12, 'bold'), text="Select a username:", padx=2,
                               pady=2)
    labelusername.grid(row=1, column=0, sticky=W)
    entryusername = Entry(actionsframe, font=('calibri', 12, 'bold'), textvariable=username, width=25)
    entryusername.grid(row=1, column=1)

    labelpassword = Label(actionsframe, font=('calibri', 12, 'bold'), text="  Select a password:", padx=2,
                               pady=2)
    labelpassword.grid(row=1, column=2, sticky=W)
    entrypassword = Entry(actionsframe, font=('calibri', 12, 'bold'), textvariable=password, width=25,
                               show="*")
    entrypassword.grid(row=1, column=3)


# ------------------------------------------------------------------------------------------------------

x = add_gp()

root.mainloop()