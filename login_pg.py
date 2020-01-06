from tkinter import *
import tkinter.messagebox
import pt_db_connectivity
from tkinter import ttk
import os
import sqlite3


class main():
    def __init__(self, root):
        self.root = root
        self.root.title("GP2U Login")
        self.root.geometry("750x600+770+200")

        self.username = Label(self.root, text="Username")
        self.password = Label(self.root, text="Password")
        self.username.grid(row=8, column=4)
        self.password.grid(row=9, column=4)

        self.user_entry = Entry(self.root)
        self.pass_entry = Entry(self.root, show="*")
        self.user_entry.grid(row=8, column=5)
        self.pass_entry.grid(row=9, column=5)

        self.new_button = Button(self.root, text="Login", bg="lawn green", command=self.login_verification)
        self.new_button.bind("<Button-1>")
        self.new_button.grid(row=9, column=7, padx=4, pady=10)

        # self.admin_button = Button(self.root, text="Admin Login", bg="gray85", command=self.login_verification)
        # self.admin_button.bind("<Button-1>")
        # self.admin_button.grid(row=9, column=8, padx=4, pady=10)

        self.register_here = Label(self.root, text=" to register if unregistered")
        self.register_here.grid(row=10, column=5)

        self.register_button = Button(self.root, text="Click here", bg="gray85")
        self.register_button.bind("<Button-1>")
        self.register_button.grid(row=10, column=4, padx=4, pady=10)


##########################################################################################################
        #
        # self.account = Menu(menu)                                               # creates a submenu within menu
        # menu.add_cascade(label="Account", menu=self.account)
        # self.account.add_command(label="Profile", command=self.viewProfile)
        # self.account.add_command(label="Logout", command=self.logout)
        # self.account.add_command(label="Logout and close window", command=self.logout_and_close_window)
        #
        # # self.account.add_separator()
        #
        # self.managepts = Menu(menu)
        # menu.add_cascade(label="Manage patients", menu=self.managepts)
        # self.managepts.add_command(label="Search for a patient", command=self.listOfPatients)

    def login_verification(self):
        global checkuser
        checkuser = self.user_entry.get().lower() + ".txt"
        checkpass = self.pass_entry.get()
        my_files = os.listdir()
        if checkuser in my_files:
            open_user = open(checkuser, "r")
            open_pass = open_user.read().splitlines()
            if (checkuser == "admin.txt") and (checkpass == "1234"):
                admin_login(root)
            elif checkuser == "admin.txt" and (checkpass != "1234"):
                wrong_pass_mess = tkinter.messagebox.showinfo(message="Password does not match our records. Please try again.")
                return wrong_pass_mess
            elif (checkuser + ".gp") == (self.user_entry.get().lower() + ".txt.gp") and (checkpass in open_pass):
                GPPage(root)
            elif checkpass in open_pass:
                """ This section of the function logs user in """
                #succ_login_mess = tkinter.messagebox.showinfo(message="Login Successful")
                self.upon_login()
            else:
                wrong_pass_mess = tkinter.messagebox.showinfo(message="Password does not match our records. Please try again.")
                return wrong_pass_mess
        elif (checkuser + ".gp") in my_files:
            open_user = open((checkuser + ".gp"), "r")
            open_pass = open_user.read().splitlines()
            if checkpass in open_pass:
                GPPage(root)
            else:
                wrong_pass_mess = tkinter.messagebox.showinfo(message="Password does not match our records. Please try again.")
                return wrong_pass_mess
        else:
            unreg_mess = tkinter.messagebox.INFO(message="User account not found in our records. Please register")
            return unreg_mess

    def upon_login(self):

        self.root = root
        self.root.title(f"GP2U - {checkuser}")
        self.root.geometry("750x450+770+200")

        acc_wind = Toplevel(self.root)
        frame2 = Frame(acc_wind)
        frame2.pack(side=TOP)

        button1 = Button(frame2, text="View bookings", fg="black", width=28)
        button2 = Button(frame2, text="Book an appointment", fg="black", width=28)
        button3 = Button(frame2, text="Cancel an appointment", fg="black", width=28)
        button4 = Button(frame2, text="View Profile", fg="black", width=28)

        button1.pack(side=LEFT)
        button2.pack(side=LEFT)
        button3.pack(side=LEFT)
        button4.pack(side=LEFT)

        menubar = Menu(self.root)                                               # creates a submenu within menu
        self.root.config(menu=menubar)
        my_menu = Menu(menubar)
        submenu = Menu(my_menu)
        submenu.add_cascade(label="Account", menu=menubar)
        submenu.add_command(label="Profile", command=self.viewProfile)
        submenu.add_command(label="Logout", command=self.logout)
        submenu.add_command(label="Logout and close window", command=self.logout_and_close_window)


    def logout(self):
        print("You have been logged out")
        y = Label(text="You have been logged out")
        y.pack()

    def logout_and_close_window(self):
        frame=Frame(root)
        frame.quit()
        print("You have been logged out")

    def viewProfile(self):
        print("View profile")


    def donothing(self):
        print("nothing's been done")

class admin_login():
    def __init__(self, root):
        self.root = root
        self.root.title("Admin")
        self.root.geometry("750x600+770+200")

        frame2 = Toplevel(self.root)
        frame2.grid()

        leftframe = Frame(frame2, bd=2, width=420, height=400, padx=50, pady=10, relief=GROOVE)
        leftframe.pack(side=LEFT)

        middleframe = Frame(frame2, bd=2, width=420, height=400, padx=50, pady=10, relief=GROOVE)
        middleframe.pack(side=LEFT)

        rightframe = Frame(frame2, bd=2, width=420, height=400, padx=20, pady=10, relief=GROOVE)
        rightframe.pack(side=LEFT)

#-------------------------------  some functions-----------------------------------

        def confirm_pt():
            pt_db_connectivity.confirm_pt_registration(pttitle.get(), right_nhs.get(), ptFirstname.get(), ptSurname.get(), ptGender.get(), ptAddress.get(),
            ptContact_number.get(), ptDOB.get(), ptAllergies.get(), ptMedical_history.get(), right_user.get().title(), ptpassword.get())

        def reggp():
            if len(entryusername.get()) != 0:
                pt_db_connectivity.new_gp(droptitle.get(),
                        entryfirstname.get(), entrysurname.get(), dropgender.get(), entryaddress.get(), entrycontact.get(), entrydob.get(),
                        entryusername.get(), entrypassword.get())
            gpuser = entryusername.get()
            gppass = entrypassword.get()
            file = open(f"{gpuser}.txt.gp", "w")
            file.write(gpuser + "\n")
            file.write(gppass + "\n")
            file.close()

        def delgp():
            pt_db_connectivity.delete_a_gp(entryusername.get())

        def uppt():
            pt_db_connectivity.update_patient_details(pttitle.get(), right_nhs.get(), ptFirstname.get(), ptSurname.get(), ptGender.get(), ptAddress.get(),
                    ptContact_number.get(), ptDOB.get(), ptAllergies.get(), ptMedical_history.get(), right_user.get().title(), ptpassword.get())


#----------------------- GP DETAILS---------------------------------
        Title = StringVar()
        self.Title = Title

        Firstname = StringVar()
        self.Firstname = Firstname

        Surname = StringVar()
        self.Surname = Surname

        DOB = StringVar()
        self.DOB = DOB

        Gender = StringVar()
        self.Gender = Gender

        Address = StringVar()
        self.Address = Address

        Contact_number = StringVar()
        self.Contact_number = Contact_number

        username = StringVar()
        self.username = username

        password = StringVar()
        self.password = password
#-----------------------Patient details-------------------------------------

        pttitle = StringVar()
        self.pttitle = pttitle

        right_nhs = StringVar()
        self.right_nhs = right_nhs

        ptFirstname = StringVar()
        self.ptFirstname = ptFirstname

        ptSurname = StringVar()
        self.ptSurname = ptSurname

        ptDOB = StringVar()
        self.ptDOB = ptDOB

        ptGender = StringVar()
        self.ptGender = ptGender

        ptAddress = StringVar()
        self.ptAddress = ptAddress

        ptContact_number = StringVar()
        self.ptContact_number = ptContact_number

        ptAllergies = StringVar()
        self.ptAllergies = ptAllergies

        ptMedical_history = StringVar()
        self.ptMedical_history = ptMedical_history

        right_user = StringVar()
        self.right_user = right_user

        ptpassword = StringVar()
        self.ptpassword = ptpassword
# --------------------------- HEADERS FOR EACH FRAME ---------------------------------------
        addgp_heading = Label(leftframe, font=('calibri', 22, 'bold'), text="Add new GP:", padx=25, pady=2)
        addgp_heading.grid(row=0, column=1)

        view_avail_heading = Label(middleframe, font=('calibri', 22, 'bold'), text="View availabilities:", padx=25, pady=2)
        view_avail_heading.grid(row=0, column=1)

        man_acc = Label(rightframe, font=('calibri', 22, 'bold'), text="Manage User", padx=25, pady=2)
        man_acc.grid(row=0, columnspan=2)

#------------------------ TEXT BOX SHOWING AVAILABILITIES ---------------------------------------------------

        avail_box = tkinter.Text(middleframe, font=('calibri', 12), height=13, width=40, padx=10, pady=30, relief=GROOVE)
        avail_box.grid(row=1, column=1)
        notebox = Label(middleframe, text="Doctors' Availabilities", font=('calibri', 12, 'bold'))
        notebox.grid(row=2, column=1)
#-----------------------------------PATIENT SEARCH BOX -------------------------------------------------------------

        global searchboxentry
        searchboxentry = Entry(rightframe, font=('calibri', 12, 'bold'), width=20)
        searchboxentry.grid(row=1, column=1)

        search_btn = Button(rightframe, text="Search", font=('calibri', 12), height=1, width=6, relief=RAISED, command=self.search_user)
        search_btn.grid(row=1, column=2, sticky=W)

        searchtext = Label(rightframe, font=('calibri', 12), text="Search NHS number:", padx=2, pady=2)
        searchtext.grid(row=1, column=0, sticky=W)

        labelrighttitle = Label(rightframe, font=('calibri', 12, 'bold'), text="Title", padx=2, pady=2)
        labelrighttitle.grid(row=2, column=0, sticky=W)
        entryrighttitle = Entry(rightframe, font=('calibri', 12, 'bold'), textvariable=self.pttitle, width=20)
        entryrighttitle.grid(row=2, column=1)

        labelnhs_right = Label(rightframe, font=('calibri', 12, 'bold'), text="NHS number:", padx=2, pady=2)
        labelnhs_right.grid(row=3, column=0, sticky=W)
        entrynhs_right = Entry(rightframe, font=('calibri', 12, 'bold'), textvariable=self.right_nhs, width=20)
        entrynhs_right.grid(row=3, column=1)

        labelfirstnameright = Label(rightframe, font=('calibri', 12, 'bold'), text="First name", padx=2, pady=2)
        labelfirstnameright.grid(row=4, column=0, sticky=W)
        entryfirstnameright = Entry(rightframe, font=('calibri', 12, 'bold'), textvariable=self.ptFirstname, width=20)
        entryfirstnameright.grid(row=4, column=1)

        labellastnameright = Label(rightframe, font=('calibri', 12, 'bold'), text="Last name", padx=2, pady=2)
        labellastnameright.grid(row=5, column=0, sticky=W)
        entrylastnameright = Entry(rightframe, font=('calibri', 12, 'bold'), textvariable=self.ptSurname, width=20)
        entrylastnameright.grid(row=5, column=1)

        labelgenderright = Label(rightframe, font=('calibri', 12, 'bold'), text="Gender", padx=2, pady=2)
        labelgenderright.grid(row=6, column=0, sticky=W)
        entrygenderright = Entry(rightframe, font=('calibri', 12, 'bold'), textvariable=self.ptGender, width=20)
        entrygenderright.grid(row=6, column=1)

        labeladdressright = Label(rightframe, font=('calibri', 12, 'bold'), text="Address", padx=2, pady=2)
        labeladdressright.grid(row=7, column=0, sticky=W)
        entryaddressright = Entry(rightframe, font=('calibri', 12, 'bold'), textvariable=self.ptAddress, width=20)
        entryaddressright.grid(row=7, column=1)

        labelcontactright = Label(rightframe, font=('calibri', 12, 'bold'), text="Contact", padx=2, pady=2)
        labelcontactright.grid(row=8, column=0, sticky=W)
        entrycontactright = Entry(rightframe, font=('calibri', 12, 'bold'), textvariable=self.ptContact_number, width=20)
        entrycontactright.grid(row=8, column=1)

        labeldobright = Label(rightframe, font=('calibri', 12, 'bold'), text="DOB", padx=2, pady=2)
        labeldobright.grid(row=9, column=0, sticky=W)
        entrydobright = Entry(rightframe, font=('calibri', 12, 'bold'), textvariable=self.ptDOB, width=20)
        entrydobright.grid(row=9, column=1)

        labelallerright = Label(rightframe, font=('calibri', 12, 'bold'), text="Allergies", padx=2, pady=2)
        labelallerright.grid(row=10, column=0, sticky=W)
        entryallerright = Entry(rightframe, font=('calibri', 12, 'bold'), textvariable=self.ptAllergies, width=20)
        entryallerright.grid(row=10, column=1)

        labelmed = Label(rightframe, font=('calibri', 12, 'bold'), text="Medical history", padx=2, pady=2)
        labelmed.grid(row=11, column=0, sticky=W)
        entrymed = Entry(rightframe, font=('calibri', 12, 'bold'), textvariable=self.ptMedical_history, width=20)
        entrymed.grid(row=11, column=1)

        labeluser_right = Label(rightframe, font=('calibri', 12, 'bold'), text="Username:", padx=2, pady=2)
        labeluser_right.grid(row=12, column=0, sticky=W)
        entryuser_right = Entry(rightframe, font=('calibri', 12, 'bold'), textvariable=self.right_user, width=20)
        entryuser_right.grid(row=12, column=1)

        labelpass_right = Label(rightframe, font=('calibri', 12, 'bold'), text="Password:", padx=2, pady=2)
        labelpass_right.grid(row=13, column=0, sticky=W)
        entrypass_right = Entry(rightframe, font=('calibri', 12, 'bold'), textvariable=self.ptpassword, width=20)
        entrypass_right.grid(row=13, column=1)

        confirmregbtn = Button(rightframe, text="Confirm registration", font=('calibri', 14, 'bold'), height=1, width=20,
                       relief=RAISED, command=confirm_pt)
        confirmregbtn.grid(row=14, column=0, sticky=W)

        update_pt_btn = Button(rightframe, text="Update patient details", font=('calibri', 14, 'bold'), height=1, width=20,
                               relief=RAISED, command=uppt)
        update_pt_btn.grid(row=14, column=1, sticky=E)


#-----------------------------------GP HANDLING-------------------------------------------------------------

        title = Label(leftframe, font=('calibri', 16, 'bold'), text="Title:", padx=2, pady=2)
        title.grid(row=1, column=0, sticky=W)
        droptitle = ttk.Combobox(leftframe, textvariable=self.Title, font=('calibri', 16, 'bold'), width=25)

        droptitle['value'] = ('Select your title', 'Dr', 'Miss', 'Mr', 'Mrs', 'Other')
        droptitle.current(0)
        droptitle.grid(row=1, column=1)

        labelfirstname = Label(leftframe, font=('calibri', 16, 'bold'), text="First name:", padx=2, pady=2)
        labelfirstname.grid(row=2, column=0, sticky=W)
        entryfirstname = Entry(leftframe, font=('calibri', 16, 'bold'), textvariable=self.Firstname, width=25)
        entryfirstname.grid(row=2, column=1)

        labelsurname = Label(leftframe, font=('calibri', 16, 'bold'), text="Surname:", padx=2, pady=2)
        labelsurname.grid(row=3, column=0, sticky=W)
        entrysurname = Entry(leftframe, font=('calibri', 16, 'bold'), textvariable=self.Surname, width=25)
        entrysurname.grid(row=3, column=1)

        labelgender = Label(leftframe, font=('calibri', 16, 'bold'), text="Gender:", padx=2, pady=2)
        labelgender.grid(row=4, column=0, sticky=W)
        dropgender = ttk.Combobox(leftframe, textvariable=self.Gender, font=('calibri', 16, 'bold'), width=25)

        dropgender['value'] = ('Select your gender', 'Male', 'Female', 'Non-binary', 'Other')
        dropgender.current(0)
        dropgender.grid(row=4, column=1)

        labeladdress = Label(leftframe, font=('calibri', 16, 'bold'), text="Address:", padx=2, pady=2)
        labeladdress.grid(row=5, column=0, sticky=W)
        entryaddress = Entry(leftframe, font=('calibri', 16, 'bold'), textvariable=self.Address, width=25)
        entryaddress.grid(row=5, column=1)

        labelcontact = Label(leftframe, font=('calibri', 16, 'bold'), text="Contact number:", padx=2, pady=2)
        labelcontact.grid(row=6, column=0, sticky=W)
        entrycontact = Entry(leftframe, font=('calibri', 16, 'bold'), textvariable=self.Contact_number, width=25)
        entrycontact.grid(row=6, column=1)

        labeldob = Label(leftframe, font=('calibri', 16, 'bold'), text="Date of Birth:", padx=2, pady=2)
        labeldob.grid(row=7, column=0, sticky=W)
        entrydob = Entry(leftframe, font=('calibri', 16, 'bold'), textvariable=self.DOB, width=25)
        entrydob.grid(row=7, column=1)

        labelusername = Label(leftframe, font=('calibri', 16, 'bold'), text="Select a username:", padx=2, pady=2)
        labelusername.grid(row=8, column=0, sticky=W)
        entryusername = Entry(leftframe, font=('calibri', 16, 'bold'), textvariable=self.username, width=25)
        entryusername.grid(row=8, column=1)

        labelpassword = Label(leftframe, font=('calibri', 16, 'bold'), text="Select a password:", padx=2, pady=2)
        labelpassword.grid(row=9, column=0, sticky=W)
        entrypassword = Entry(leftframe, font=('calibri', 16, 'bold'), textvariable=self.password, width=25, show="*")
        entrypassword.grid(row=9, column=1)

        labelalterna = Label(leftframe, font=('calibri', 16, 'bold'), text="Search for GP below", padx=2, pady=2)
        labelalterna.grid(row=12, sticky=W)


        add_gp_btn = Button(leftframe, text="Confirm registration", font=('arial', 12, 'bold'), height=1, width=18, relief=RAISED, command=reggp)
        add_gp_btn.grid(row=10, column=1)

        delete_gp_btn = Button(leftframe, text="Delete GP", font=('arial', 12, 'bold'), height=1, width=18, relief=RAISED, command=delgp)
        delete_gp_btn.grid(row=11, column=1)

        global gpsearchbox
        gpsearchbox = Entry(leftframe, font=('calibri', 12, 'bold'), width=20)
        gpsearchbox.grid(row=14, column=0)

        gp_search_btn = Button(leftframe, text="Search", font=('calibri', 12), height=1, width=6, relief=RAISED, command=self.search_gp)
        gp_search_btn.grid(row=14, column=1, sticky=W)

        searchtext = Label(leftframe, font=('calibri', 12), text="Search GP username:", padx=2, pady=2)
        searchtext.grid(row=13, column=0, sticky=W)
#----------------------------------------------------------------------------------------------------------------------
    def donothing(self):
        print("nothing's been done")

    def search_user(self):
        try:
            conn = sqlite3.connect("ptdatabase.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM patient_details WHERE nhs_number='%s'" %searchboxentry.get().title())
            conn.commit()
            row = cursor.fetchone()
            self.pttitle.set(row[0])
            self.right_nhs.set(row[1])
            self.ptFirstname.set(row[2])
            self.ptSurname.set(row[3])
            self.ptGender.set(row[4])
            self.ptAddress.set(row[5])
            self.ptContact_number.set(row[6])
            self.ptDOB.set(row[7])
            self.ptAllergies.set(row[8])
            self.ptMedical_history.set(row[9])
            self.right_user.set(row[10])
            self.ptpassword.set(row[11])
            conn.commit()
            conn.close()
        except:
             tkinter.messagebox.showinfo(title="No user error", message="User account not found in our records")

    def search_gp(self):
        try:
            conn = sqlite3.connect("ptdatabase.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM gp_table WHERE username='%s'" %gpsearchbox.get())
            conn.commit()
            row = cursor.fetchone()
            self.Title.set(row[0])
            self.Firstname.set(row[1])
            self.Surname.set(row[2])
            self.Gender.set(row[3])
            self.Address.set(row[4])
            self.Contact_number.set(row[5])
            self.DOB.set(row[6])
            self.username.set(row[7])
            self.password.set(row[8])
            conn.commit()
            conn.close()
        except:
            tkinter.messagebox.showinfo(title="No user error", message="User account not found in our records")



class GPPage:
    def __init__(self, root):
        self.root = root
        self.root.title("GP")
        self.root.geometry("750x600+770+200")

        frame3 = Toplevel(self.root)
        frame3.grid()

        leftframe = Frame(frame3, bd=2, width=420, height=400, padx=50, pady=10, relief=GROOVE)
        leftframe.pack(side=LEFT)

        middleframe = Frame(frame3, bd=2, width=420, height=400, padx=50, pady=10, relief=GROOVE)
        middleframe.pack(side=LEFT)

        rightframe = Frame(frame3, bd=2, width=420, height=400, padx=20, pady=10, relief=GROOVE)
        rightframe.pack(side=LEFT)

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
            global selected
            item = avail_box.curselection()
            selected = avail_box.get(item)

        def del_avail():
            pt_db_connectivity.delete_availability(selected[0])
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

        # placetittle = Label(scriptbox, text=entryrighttitle.get())
        # placetittle.place(x=250, y=10)
        #
        # placedobage = Label(scriptbox, text=entrydobage.get())
        # placedobage.place(x=150, y=10)

#----------------------------------------   MIDDLE FRAME   ----------------------------------------------------------------

        middlebox = LabelFrame(middleframe, bd)

        middlebox = LabelFrame(middleframe, bd=1, width=400, height=500, relief=GROOVE, font=('calibri', 18, 'bold'), text="Appointment requests", padx=2, pady=2)
        middlebox.pack(side=TOP)

        global request_box
        request_box = Listbox(middlebox, height=25, width=55)
        request_box.grid(row=0, column=0)





root=Tk()
a = main(root)
root.mainloop()


