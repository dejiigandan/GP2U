from tkinter import *
import sqlite3

import tkinter.messagebox
# import userDB


class main():
    def __init__(self, root):
        self.root = root
        self.root.title("GP2U")
        self.root.geometry("750x450+770+200")

        self.username = Label(root, text="Username")
        self.password = Label(root, text="Password")
        self.username.place(x=200,y=150)
        self.password.place(x=200, y=180)

        self.entry_1 = Entry(root)
        self.entry_2 = Entry(root)
        self.entry_1.place(x=280, y=150)
        self.entry_2.place(x=280, y=180)

        self.new_button = Button(root, text="Login", bg="lawn green", command=self.donothing)
        self.new_button.bind("<Button-1>", self.login)
        self.new_button.place(x=420, y=180)

        self.textbox = Text(root, width=25, height=10, wrap=WORD)
        self.textbox.place(x=300, y = 250)

#- image of GP2U logo
        # self.image = PhotoImage(file="steth.png")
        # self.label=Label(root, image=self.image)
        # self.label.grid(row=10, column=6)
#

        # self.logoutbutton = Button(frame, text="Logout", command=self.logout)
        # self.logoutbutton.pack(side=LEFT)

        menu = Menu(root)
        root.config(menu=menu)                                                  # we are configuring a menu for menu

##########################################################################################################

        self.account = Menu(menu)                                               # creates a submenu within menu
        menu.add_cascade(label="Account", menu=self.account)
        self.account.add_command(label="Profile", command=self.viewProfile)
        self.account.add_command(label="Logout", command=self.logout)
        self.account.add_command(label="Logout and close window", command=self.logout_and_close_window)

        # self.account.add_separator()

        self.managepts = Menu(menu)
        menu.add_cascade(label="Manage patients", menu=self.managepts)
        self.managepts.add_command(label="Search for a patient", command=self.listOfPatients)

    def login(self, event):
        print("Logged in")

    def logout(self):
        print("You have been logged out")

    def logout_and_close_window(self):
        frame=Frame(root)
        frame.quit()
        print("You have been logged out")


    def viewProfile(self):
        print("View profile")


    def tabs(self):
        print("This is your tab")

    def listOfPatients(self):
        print("This is a list of your patients")


    def donothing(self):
        print("nothing's been done")




root = Tk()
a = main(root)











# pagehead = Frame(root)
# pagehead.pack()
# pagebottom = Frame(root)
# pagebottom.pack(side=BOTTOM)                                                    # places text at bottom of Frame instead of the default head
#
# button1 = Button(pagehead, text="Patient Search", fg="black")                   # fg:text colour    bg:tab colour
# button2 = Button(pagehead, text="Bookings", fg="black")
# button3 = Button(pagehead, text="Tab 3", fg="black")
# button4 = Button(pagehead, text="Profile", fg="black")
#
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=LEFT)

# username = Label(root, text="Username")
# password = Label(root, text="Password")
#
# entry_1 = Entry(root)
# entry_2 = Entry(root)
#
# username.grid(row=5, sticky=E)
# password.grid(row=6, sticky=W)
#
# entry_1.grid(row=5, column=1)
# entry_2.grid(row=6, column=1)


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


