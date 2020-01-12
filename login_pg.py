from tkinter import *
import tkinter.messagebox
from tkinter import Menu
import pt_db_connectivity
from tkinter import ttk
import os
import sqlite3
import smtplib

class main():
    """The main page. Patient/Admin/GP can navigate the software from this page"""
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

        self.register_here = Label(self.root, text=" to register if unregistered")
        self.register_here.grid(row=10, column=5)

        self.register_button = Button(self.root, text="Click here", bg="gray85", command=self.taketoregister)
        self.register_button.bind("<Button-1>")
        self.register_button.grid(row=10, column=4, padx=4, pady=10)


    def taketoregister(self):
        return for_pt(root)
##########################################################################################################
        # self.account = Menu(menu)                                               # creates a submenu within menu
        # menu.add_cascade(label="Account", menu=self.account)
        # self.account.add_command(label="Logout", command=self.logout)
        # self.account.add_command(label="Logout and exit", command=self.logout_and_close_window)


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
            # elif (checkuser + ".gp") == (self.user_entry.get().lower() + ".txt.gp") and (checkpass in open_pass):
            #     GPPage(root)
            elif checkpass in open_pass:
                """ This section of the function logs user in """
                succ_login_mess = tkinter.messagebox.showinfo(message="Login Successful")
                PatientPage(root)
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
        self.root.title(f"GP2U")
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

    def donothing(self):
        print("nothing's been done")

    #TODO Add regiser button and register class to login page
    #todo add logout button to each page


class for_pt():
    """This allows the user to register"""
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("750x600+770+200")
        frame = Toplevel(self.root)
        frame.grid()

        title = StringVar()
        nhs_number = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DOB = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Contact_number = StringVar()
        Allergies = StringVar()
        Medical_history = StringVar()

        username = StringVar()
        password = StringVar()

        def add_pt():
            if len(nhs_number.get()) != 0:
                pt_db_connectivity.new_patient(title.get(), nhs_number.get(), Firstname.get(), Surname.get(),  Gender.get(),
                Address.get(), Contact_number.get(), DOB.get(), Allergies.get(), Medical_history.get(), username.get().title(), password.get())
            user_name = username.get()
            pass_word = password.get()
            file = open(f"{user_name}.txt", "w")
            file.write(user_name + "\n")
            file.write(pass_word + "\n")
            file.close()
            confirm_box = tkinter.messagebox.showinfo(message="Your details have been forwarded to our administration team who will confirm your registration")
            return confirm_box
            #TODO add message box to show message if selected NHS number is not unique

        pagetitle = Frame(frame)
        pagetitle.pack(side=TOP)

        lbltit = Label(pagetitle, font=('calibri', 28, 'bold'), text="Registration page")
        lbltit.grid()

        formframe = Frame(frame, bd=1, height=700, padx=15, pady=25, relief=RIDGE)
        formframe.pack(side=TOP)

        actionsframe = Frame(frame, width=500, height=40, padx=8, pady=6, relief=RIDGE)
        actionsframe.pack(side=TOP)

#-------------------- FORM ENTRIES ------------------------------

        title = Label(formframe, font=('calibri', 20, 'bold'), text="Title:", padx=2, pady=2)
        title.grid(row=0, column=0, sticky=W)
        droptitle = ttk.Combobox(formframe, textvariable=title, font=('calibri', 20, 'bold'), width=29)

        droptitle['value'] = ('Select your title', 'Master', 'Miss', 'Mr', 'Mrs', 'Other')
        droptitle.current(0)
        droptitle.grid(row=0, column=1)

        labelnhs_number = Label(formframe, font=('calibri', 20, 'bold'), text="NHS number:", padx=2, pady=2)
        labelnhs_number.grid(row=1, column=0, sticky=W)
        entrynhs_number = Entry(formframe, font=('calibri', 20, 'bold'), textvariable=nhs_number, width=30)
        entrynhs_number.grid(row=1, column=1)

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
        entrycontact= Entry(formframe, font=('calibri', 20, 'bold'), textvariable=Contact_number, width=30)
        entrycontact.grid(row=6, column=1)

        labeldob = Label(formframe, font=('calibri', 20, 'bold'), text="Date of Birth:", padx=2, pady=2)
        labeldob.grid(row=7, column=0, sticky=W)
        entrydob = Entry(formframe, font=('calibri', 20, 'bold'), textvariable=DOB, width=30)
        entrydob.grid(row=7, column=1)

        labelallergies = Label(formframe, font=('calibri', 20, 'bold'), text="Allergies:", padx=2, pady=2)
        labelallergies.grid(row=8, column=0, sticky=W)
        entryallergies = Entry(formframe, font=('calibri', 20, 'bold'), textvariable=Allergies, width=30)
        entryallergies.grid(row=8, column=1)

        labelmedhis = Label(formframe, font=('calibri', 20, 'bold'), text="Medical history:", padx=2, pady=2)
        labelmedhis.grid(row=9, column=0, sticky=W)
        entrymedhis = Entry(formframe, font=('calibri', 20, 'bold'), textvariable=Medical_history, width=30)
        entrymedhis.grid(row=9, column=1)

        labelusername = Label(actionsframe, font=('calibri', 12, 'bold'), text="Select a username:", padx=2, pady=2)
        labelusername.grid(row=1, column=0, sticky=W)
        entryusername = Entry(actionsframe, font=('calibri', 12, 'bold'), textvariable=username, width=25)
        entryusername.grid(row=1, column=1)

        labelpassword = Label(actionsframe, font=('calibri', 12, 'bold'), text="  Select a password:", padx=2, pady=2)
        labelpassword.grid(row=1, column=2, sticky=W)
        entrypassword = Entry(actionsframe, font=('calibri', 12, 'bold'), textvariable=password, width=25, show="*")
        entrypassword.grid(row=1, column=3)



# ----------------  Actions to form -----------------------------

        add_details_btn = Button(actionsframe, text="Confirm registration", font=('arial', 12, 'bold'), height=1, width=18, relief=RAISED, command=add_pt)
        add_details_btn.grid(row=1, column=4)


class admin_login(main):
    """Admin staff are taken here and can add new GP, delete GP or confirm patient registration"""
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Admin")
        self.root.geometry("750x600+770+200")

        global frame2
        frame2 = Toplevel(self.root)
        frame2.grid()

        adminnotebook = ttk.Notebook(frame2)
        adminnotebook.pack()

        leftframe = ttk.Frame(adminnotebook)
        leftframe.pack(side=LEFT)

        middleframe = ttk.Frame(adminnotebook)
        middleframe.pack(side=LEFT)

        rightframe = ttk.Frame(adminnotebook)
        rightframe.pack(side=LEFT)

        adminnotebook.add(leftframe, text="Add new GP")
        adminnotebook.add(middleframe, text="View available appointments")
        adminnotebook.add(rightframe, text="Manage patients")

        menubar = Menu(frame2)
        frame2.config(menu=menubar)
        mymenu = Menu(menubar, tearoff=0)
        mymenu.add_command(label="Logout", command=self.quitframe2)
        menubar.add_cascade(label="Account", menu=mymenu)

#-------------------------------  some functions-----------------------------------

        def confirm_pt():
            pt_db_connectivity.confirm_pt_registration(pttitle.get(), right_nhs.get(), ptFirstname.get(), ptSurname.get(), ptGender.get(), ptAddress.get(),
            ptContact_number.get(), ptDOB.get(), ptAllergies.get(), ptMedical_history.get(), right_user.get().title(), ptpassword.get())

            def send_email(subject, content):
                """Sends a confirmation email to the newly registered patient"""
                try:
                    server = smtplib.SMTP('smtp.gmail.com:587')
                    server.ehlo()
                    server.starttls()
                    server.login("gp2ulondon@gmail.com", "gooddoctor")
                    message = f'Subject: {subject}\n\n{content}'
                    server.sendmail("gp2ulondon@gmail.com", ptContact_number.get(), message)
                    server.quit()
                    print("Works")
                except:
                    print("fail")

            subject = "test subject"
            content = "how are you today"
            send_email(subject, content)

        def reggp():
            """Function to register a GP"""
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
            ptContact_number.get(), ptDOB.get(), ptAllergies.get(), ptMedical_history.get(), right_user.get().title(), ptpassword.get(), right_nhs.get())
            tkinter.messagebox.showinfo(title="update", message="User details updated")

        def admin_fill_list():
            avail_box.delete(0, END)
            for row in pt_db_connectivity.list_avail():
                avail_box.insert(END, row)


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

        avail_box = Listbox(middleframe, height=25, width=55)
        avail_box.grid(row=1, column=1)
        admin_fill_list()


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


    def quitframe2(self):
        _1exit = tkinter.messagebox.askyesno(title="Logout?", message="Do you wish to logout")
        if _1exit > 0:
            frame2.destroy()
        else:
            pass



class GPPage(main):
    """The GP Page allows GP to manage patients as well as manage appointments/availabilities"""
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title(f"GP")
        self.root.geometry("750x600+770+200")

        global frame3
        frame3 = Toplevel(self.root)
        frame3.grid()

        notebook = ttk.Notebook(frame3)
        notebook.pack()

        leftframe = ttk.Frame(notebook)
        leftframe.pack(side=LEFT)

        middleframe = ttk.Frame(notebook)
        middleframe.pack(side=LEFT)

        rightframe = ttk.Frame(notebook)
        rightframe.pack(side=LEFT)

        notebook.add(leftframe, text="Manage availabilities")
        notebook.add(middleframe, text="Requests")
        notebook.add(rightframe, text="Prescriptions")

        menubar = Menu(frame3)
        frame3.config(menu=menubar)
        mymenu = Menu(menubar, tearoff=0)
        mymenu.add_command(label="Logout", command=self.quitframe3)
        menubar.add_cascade(label="Account", menu=mymenu)

        # -----------------------------FUNCTIONS-------------------------------------------------
        def fill_list():
            availabilities_box.delete(0, END)
            for row in pt_db_connectivity.list_avail():
                availabilities_box.insert(END, row)

        def fillrequestbox():
            requestsbox.delete(0, END)
            for i in pt_db_connectivity.list_of_requests():
                requestsbox.insert(END, i)

        def add_myavails():
            if (len(apdate_entry.get()) != 0) and (len(apttime_entry.get()) != 0) and (len (name_show_entry.get()) != 0):
                pt_db_connectivity.add_new_availability(apdate_entry.get(), apttime_entry.get(), name_show_entry.get())
                availabilities_box.delete(0, END)
                availabilities_box.insert(END, (apdate_entry.get(), apttime_entry.get(), name_show_entry.get()))
                fill_list()
            else:
                tkinter.messagebox.showinfo(title="Error", message="Please ensure all fields are complete")

        def selectitem(command):
            try:
                global selected
                datesel = availabilities_box.curselection()[0]
                selected = availabilities_box.get(datesel)
            except IndexError:
                pass

        def del_avail():
            pt_db_connectivity.delete_availability(selected[0], selected[1], selected[2])
            fill_list()

        def selectrequest(anothercommand):
            try:
                global myselect
                itemselected = requestsbox.curselection()[0]
                myselect = requestsbox.get(itemselected)
            except IndexError:
                pass

        def confirm_appointment():
            pt_db_connectivity.confirm_appointment(myselect[0], myselect[1], myselect[2], myselect[3])
            tkinter.messagebox.showinfo(title="Confirmed", message="Appointment confirmed")
            fillrequestbox()

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

# ---------------------availabilities and requests listboxes------------------------------------------------
        global availabilities_box
        availabilities_box = Listbox(leftframe, height=25, width=55)
        availabilities_box.grid(row=4, column=0)

        scrollbar = Scrollbar(leftframe)
        scrollbar.grid(row=4, column=1)
        availabilities_box.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=availabilities_box)

        availabilities_box.bind('<<ListboxSelect>>', selectitem)

        fill_list()

# ------------------------------------MIDDLE FRAME----------------------------------------------------------------

        middlebox = LabelFrame(middleframe, bd=1, width=400, height=500, relief=GROOVE, font=('calibri', 18, 'bold'), text="Appointment requests", padx=2, pady=2)
        middlebox.grid()

        global requestsbox
        requestsbox = Listbox(middleframe, height=27, width=60)
        requestsbox.grid(row=0, column=0)

        confirm_button = Button(middleframe, text="Confirm appointment", font=('calibri', 12), height=1, width=18, relief=RAISED, command=confirm_appointment)
        confirm_button.grid(row=1, column=0, sticky=W)

        requestsbox.bind('<<ListboxSelect>>', selectrequest)


        fillrequestbox()

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

    def quitframe3(self):
        _exit = tkinter.messagebox.askyesno(title="Logout?", message="Do you wish to logout")
        if _exit > 0:
            frame3.destroy()
        else:
            pass



class PatientPage(main):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title(f"Patient")
        self.root.geometry("750x700+780+160")

        global frame4
        frame4 = Toplevel(self.root)
        frame4.grid()

        def sendrequest():
            if (len(entryptnhsno.get()) != 0) and (len(entryptsurname.get()) != 0) and (
                    len(entryptdate.get()) != 0) and (len(entrypttime.get()) != 0):
                pt_db_connectivity.request_apptmt(entryptnhsno.get(), entryptsurname.get(), entryptdate.get(),
                                                  entrypttime.get())
                tkinter.messagebox.showinfo(title="Request sent", message="Request sent")

            else:
                tkinter.messagebox.showinfo(title="Error", message="Please fill all fields")

        def selecter(mycommand):
            try:
                global myselection
                selectappmt = ptbookings_box.curselection()[0]
                myselection = ptbookings_box.get(selectappmt)
            except IndexError:
                pass

        def delete_appointment_pt():
            pt_db_connectivity.del_apptmt(myselection[0], myselection[1], myselection[2])
            fill_pt_bookings()



        # ---------------------------------  NOTEBOOK ---------------------------------

        ptnotebook = ttk.Notebook(frame4)
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

        menubar = Menu(frame4)
        frame4.config(menu=menubar)
        mymenu = Menu(menubar, tearoff=0)
        mymenu.add_command(label="Logout", command=self.quitframe4)
        menubar.add_cascade(label="Account", menu=mymenu)

        # --------------------------------- LEFT FRAME   -----------------------------------------------

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
                entryptdate.insert(END, selectedTimeslot[
                    0])  # fills the entry boxes in the middle tab with the chosen timeslot and time
                entrypttime.delete(0, END)
                entrypttime.insert(END, selectedTimeslot[1])
            except IndexError:
                pass

        def fill_pt_bookings():
            ptbookings_box.delete(0, END)
            for i in pt_db_connectivity.list_mypt_bookings(ptenternhs.get()):
                ptbookings_box.insert(END, i)

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

        ptsearch_btn = Button(ptmiddleframe, text="Search", font=('calibri', 12), height=1, width=8, relief=RAISED,
                              command=self.ptsearch_user)
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

        request_aptmt_btn = Button(ptmiddleframe, text="Request appointment", font=('calibri', 12), height=1, width=20,
                                   relief=RAISED, command=sendrequest)
        request_aptmt_btn.grid(row=5, column=1, sticky=E)

        # --------------------------------------------- RIGHT FRAME-------------------------------------------------------

        this_user_nhsno = StringVar()
        self.this_user_nhsno = this_user_nhsno

        newone = StringVar()
        self.newone = newone

        global ptbookings_box
        ptbookings_box = Listbox(ptrightframe, height=25, width=55, font=('calibri', 13, 'bold'))
        ptbookings_box.grid(row=3, column=0)

        deletebutton = Button(ptrightframe, text="Delete appointment", font=('calibri', 12), height=1, width=18, relief=RAISED,
                              command=delete_appointment_pt)
        deletebutton.grid(row=4, column=0, sticky=E)

        #fill_pt_bookings()

        rightframetit = Label(ptrightframe, font=('calibri', 16, 'bold'), text="Confirmed appointments", padx=2, pady=2)
        rightframetit.grid(row=0, column=0)

        rightsearchtext = Label(ptrightframe, font=('calibri', 16, 'bold'), text="Enter NHS no:", padx=2, pady=2)
        rightsearchtext.grid(row=1, column=0, sticky=W)

        global ptenternhs
        ptenternhs = Entry(ptrightframe, font=('calibri', 16, 'bold'), textvariable=self.this_user_nhsno, width=16)
        ptenternhs.grid(row=1, column=0, sticky=E)

        ptsearch_btn2 = Button(ptrightframe, text="Search", font=('calibri', 12), height=1, width=8, relief=RAISED,
                              command=self.search_usertwo)
        ptsearch_btn2.grid(row=2, column=0, sticky=E)

        ptbookings_box.bind('<<ListboxSelect>>', selecter)


        # -------------------------------------------SOME FUNCTIONS------------------------------------------------------

    def ptsearch_user(self):
        try:
            conn = sqlite3.connect("ptdatabase.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM confirmed_patients WHERE nhs_number='%s'" % pt_searchby_nhsentry.get().title())
            conn.commit()
            row = cursor.fetchone()
            self.pt_nhs_no.set(row[1])
            self.ptSurname.set(row[2])
            conn.commit()
            conn.close()
        except:
            tkinter.messagebox.showinfo(title="No user error", message="User account not found in our records")


    def search_usertwo(self):
        conn = sqlite3.connect("ptdatabase.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM confirmed_patients WHERE username='%s'" %ptenternhs.get())
        conn.commit()
        #row = cursor.fetchone()
        #print(row)
        #self.newone.set(row[1])
        conn.commit()
        conn.close()

        ptbookings_box.delete(0, END)
        for i in pt_db_connectivity.list_mypt_bookings(ptenternhs.get()):
            ptbookings_box.insert(END, i)
            print(i)

    def quitframe4(self):
        _ptexit = tkinter.messagebox.askyesno(title="Logout?", message="Do you wish to logout")
        if _ptexit > 0:
            frame4.destroy()
        else:
            pass


root=Tk()
a = main(root)
root.mainloop()


