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

        self.new_button = Button(self.root, text="User Login", bg="lawn green")
        self.new_button.bind("<Button-1>", self.login_verification)
        self.new_button.grid(row=9, column=7, padx=4, pady=10)

        self.admin_button = Button(self.root, text="Admin Login", bg="gray85")
        self.admin_button.bind("<Button-1>", self.login_verification)
        self.admin_button.grid(row=9, column=8, padx=4, pady=10)

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

    def login_verification(self, event):
        global checkuser
        checkuser = self.user_entry.get() + ".txt"
        checkpass = self.pass_entry.get()
        my_files = os.listdir()
        if checkuser in my_files:
            open_user = open(checkuser, "r")
            open_pass = open_user.read().splitlines()
            if (checkuser == "admin.txt") and (checkpass == "1234"):
                self.upon_admin_Login()
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

    def upon_admin_Login(self):

        acc_wind = Toplevel(self.root)
        frame2 = Frame(acc_wind)
        frame2.pack(side=TOP)

        button4 = Button(frame2, text="Manage GP accounts", fg="black", width=28)
        button4.bind("<Button-1>", register_a_gp.add_gp)
        button5 = Button(frame2, text="Manage bookings", fg="black", width=28)
        button6 = Button(frame2, text="Manage patient account", fg="black", width=28)

        button4.pack(side=LEFT)
        button5.pack(side=LEFT)
        button6.pack(side=LEFT)

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
        self.root.title("GP2U Login")
        self.root.geometry("750x600+770+200")


root = Tk()
a = main(root)












# new_button = Button(root, text= "Login",)
# new_button.bind("<Button-1>", Login)
# new_button.pack()

# def leftclick(event):
#     print("left")
#
# def middleclick(event):
#     print("Middle")
#
# def rightclick(event):
#     print("right")
#
# frame = Frame(root, width=300, height=250)
# frame.bind("<Button-1>", leftclick)
# frame.bind("<Button-2>", middleclick)
# frame.bind("<Button-3>", rightclick)
# frame.pack()


root.mainloop()


