from tkinter import *
import tkinter.messagebox
import pt_db_connectivity
from tkinter import ttk
import os


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
            elif checkpass in open_pass:
                """ This section of the function logs user in """
                #succ_login_mess = tkinter.messagebox.showinfo(message="Login Successful")
                self.upon_login()
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

        rightframe = Frame(frame2, bd=2, width=420, height=400, padx=50, pady=10, relief=GROOVE)
        rightframe.pack(side=LEFT)

        Title = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DOB = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Contact_number = StringVar()

        username = StringVar()
        password = StringVar()

# --------------------------- HEADERS FOR EACH FRAME ---------------------------------------
        addgp_heading = Label(leftframe, font=('calibri', 22, 'bold'), text="Add new GP:", padx=25, pady=2)
        addgp_heading.grid(row=0, column=1)

        view_avail_heading = Label(middleframe, font=('calibri', 22, 'bold'), text="View availabilities:", padx=25, pady=2)
        view_avail_heading.grid(row=0, column=1)

        man_acc = Label(rightframe, font=('calibri', 22, 'bold'), text="Manage accounts", padx=25, pady=2)
        man_acc.grid(row=0, column=0)

#------------------------ TEXT BOX SHOWING AVAILABILITIES ---------------------------------------------------

        avail_box = tkinter.Text(middleframe, font=('calibri', 12, 'bold'), height=13, width=40, padx=10, pady=30, relief=GROOVE)
        avail_box.grid(row=1, column=1)
        notebox = Label(middleframe, text="Doctors' Availabilities", font=('calibri', 12, 'bold'))
        notebox.grid(row=2, column=1)
#----------------------------------- SEARCH BOX -------------------------------------------------------------

        searchboxentry = Entry(rightframe, font=('calibri', 16, 'bold'), width=25)
        searchboxentry.grid(row=0, column=0)

        search_btn = Button(rightframe, text="Search", font=('arial', 16, 'bold'), height=1, width=12, relief=RAISED, command=self.donothing)
        search_btn.grid(row=0, column=1)

        labeltitle = Label(rightframe, font=('calibri', 16, 'bold'), text="Title:", padx=2, pady=2)
        labeltitle.grid(row=1, column=0, sticky=W)
        entrytitle = Entry(rightframe, font=('calibri', 16, 'bold'), width=25)
        entrytitle.grid(row=1, column=1)

        labelfirstname = Label(rightframe, font=('calibri', 16, 'bold'), text="First name:", padx=2, pady=2)
        labelfirstname.grid(row=2, column=0, sticky=W)
        entryfirstname = Entry(rightframe, font=('calibri', 16, 'bold'), textvariable=Firstname, width=25)
        entryfirstname.grid(row=2, column=1)

        labelsurname = Label(rightframe, font=('calibri', 16, 'bold'), text="Surname:", padx=2, pady=2)
        labelsurname.grid(row=3, column=0, sticky=W)
        entrysurname = Entry(rightframe, font=('calibri', 16, 'bold'), textvariable=Surname, width=25)
        entrysurname.grid(row=3, column=1)

        labelgender = Label(rightframe, font=('calibri', 16, 'bold'), text="Gender:", padx=2, pady=2)
        labelgender.grid(row=4, column=0, sticky=W)
        entrygender = Entry()
        labeladdress = Label(rightframe, font=('calibri', 16, 'bold'), text="Address:", padx=2, pady=2)
        labeladdress.grid(row=5, column=0, sticky=W)
        entryaddress = Entry(rightframe, font=('calibri', 16, 'bold'), textvariable=Address, width=25)
        entryaddress.grid(row=5, column=1)

        labelcontact = Label(rightframe, font=('calibri', 16, 'bold'), text="Contact number:", padx=2, pady=2)
        labelcontact.grid(row=6, column=0, sticky=W)
        entrycontact = Entry(rightframe, font=('calibri', 16, 'bold'), textvariable=Contact_number, width=25)
        entrycontact.grid(row=6, column=1)

        labeldob = Label(rightframe, font=('calibri', 16, 'bold'), text="Date of Birth:", padx=2, pady=2)
        labeldob.grid(row=7, column=0, sticky=W)
        entrydob = Entry(rightframe, font=('calibri', 16, 'bold'), textvariable=DOB, width=25)
        entrydob.grid(row=7, column=1)

        labelusername = Label(leftframe, font=('calibri', 16, 'bold'), text="Select a username:", padx=2, pady=2)
        labelusername.grid(row=8, column=0, sticky=W)
        entryusername = Entry(leftframe, font=('calibri', 16, 'bold'), textvariable=username, width=25)
        entryusername.grid(row=8, column=1)

        labelpassword = Label(rightframe, font=('calibri', 16, 'bold'), text="Select a password:", padx=2, pady=2)
        labelpassword.grid(row=9, column=0, sticky=W)
        entrypassword = Entry(rightframe, font=('calibri', 16, 'bold'), textvariable=password, width=25, show="*")
        entrypassword.grid(row=9, column=1)

        #------------------------------------------------------------------------------------------------

        title = Label(leftframe, font=('calibri', 16, 'bold'), text="Title:", padx=2, pady=2)
        title.grid(row=1, column=0, sticky=W)
        droptitle = ttk.Combobox(leftframe, textvariable=Title, font=('calibri', 16, 'bold'), width=25)

        droptitle['value'] = ('Select your title', 'Master', 'Miss', 'Mr', 'Mrs', 'Other')
        droptitle.current(0)
        droptitle.grid(row=1, column=1)

        labelfirstname = Label(leftframe, font=('calibri', 16, 'bold'), text="First name:", padx=2, pady=2)
        labelfirstname.grid(row=2, column=0, sticky=W)
        entryfirstname = Entry(leftframe, font=('calibri', 16, 'bold'), textvariable=Firstname, width=25)
        entryfirstname.grid(row=2, column=1)

        labelsurname = Label(leftframe, font=('calibri', 16, 'bold'), text="Surname:", padx=2, pady=2)
        labelsurname.grid(row=3, column=0, sticky=W)
        entrysurname = Entry(leftframe, font=('calibri', 16, 'bold'), textvariable=Surname, width=25)
        entrysurname.grid(row=3, column=1)

        labelgender = Label(leftframe, font=('calibri', 16, 'bold'), text="Gender:", padx=2, pady=2)
        labelgender.grid(row=4, column=0, sticky=W)
        dropgender = ttk.Combobox(leftframe, textvariable=Gender, font=('calibri', 16, 'bold'), width=25)

        dropgender['value'] = ('Select your gender', 'Male', 'Female', 'Non-binary', 'Other')
        dropgender.current(0)
        dropgender.grid(row=4, column=1)

        labeladdress = Label(leftframe, font=('calibri', 16, 'bold'), text="Address:", padx=2, pady=2)
        labeladdress.grid(row=5, column=0, sticky=W)
        entryaddress = Entry(leftframe, font=('calibri', 16, 'bold'), textvariable=Address, width=25)
        entryaddress.grid(row=5, column=1)

        labelcontact = Label(leftframe, font=('calibri', 16, 'bold'), text="Contact number:", padx=2, pady=2)
        labelcontact.grid(row=6, column=0, sticky=W)
        entrycontact = Entry(leftframe, font=('calibri', 16, 'bold'), textvariable=Contact_number, width=25)
        entrycontact.grid(row=6, column=1)

        labeldob = Label(leftframe, font=('calibri', 16, 'bold'), text="Date of Birth:", padx=2, pady=2)
        labeldob.grid(row=7, column=0, sticky=W)
        entrydob = Entry(leftframe, font=('calibri', 16, 'bold'), textvariable=DOB, width=25)
        entrydob.grid(row=7, column=1)

        labelusername = Label(leftframe, font=('calibri', 16, 'bold'), text="Select a username:", padx=2, pady=2)
        labelusername.grid(row=8, column=0, sticky=W)
        entryusername = Entry(leftframe, font=('calibri', 16, 'bold'), textvariable=username, width=25)
        entryusername.grid(row=8, column=1)

        labelpassword = Label(leftframe, font=('calibri', 16, 'bold'), text="Select a password:", padx=2, pady=2)
        labelpassword.grid(row=9, column=0, sticky=W)
        entrypassword = Entry(leftframe, font=('calibri', 16, 'bold'), textvariable=password, width=25, show="*")
        entrypassword.grid(row=9, column=1)

        add_gp_btn = Button(leftframe, text="Confirm registration", font=('arial', 12, 'bold'), height=1, width=18, relief=RAISED, command=self.donothing)
        add_gp_btn.grid(row=10, column=1)

#----------------------------------------------------------------------------------------------------------------------
    def donothing(self):
        print("nothing's been done")


root = Tk()
a = main(root)



root.mainloop()


