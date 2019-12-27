from tkinter import *
import pt_db_connectivity
import tkinter.messagebox

class for_pt():
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("750x450+770+200")

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
                pt_db_connectivity.new_patient(nhs_number.get(), Firstname.get(), Surname.get(), DOB.get(), Gender.get(),
                Address.get(), Contact_number.get(), Allergies.get(), Medical_history.get())
                pt_list.insert(END, (nhs_number.get(), Firstname.get(), Surname.get(), DOB.get(), Gender.get(),
                Address.get(), Contact_number.get(), Allergies.get(), Medical_history.get()))
            user_name = username.get()
            pass_word = password.get()
            file = open("login_info.txt", "w")
            file.write(user_name + "\n")
            file.write(pass_word + "\n")
            file.close()
            # entryusername.delete(0, END)
            # entrypassword.delete(0, END)
            confirm_box = tkinter.messagebox.showinfo(message="Registration successful")
            return confirm_box


        def show_pt():
            pt_list.delete(0, END)
            for i in pt_db_connectivity.pull_info():
                st_list.insert(END, i, str(""))


        # def update_details():
        #     if len((nhs_number.get()) != 0):
        #         pt_db_connectivity.update_patient_details(sd[0])

        frame = Frame(self.root)
        frame.pack()

        pagetitle = Frame(frame)
        pagetitle.pack(side=TOP)

        self.lbltit = Label(pagetitle, font=('calibri', 28, 'bold'), text="Registration page")
        self.lbltit.grid()

        formframe = Frame(frame, bd=1, height=700, padx=15, pady=25, relief=RIDGE)
        formframe.pack(side=TOP)

        actionsframe = Frame(frame, width=500, height=40, padx=8, pady=6, relief=RIDGE)
        actionsframe.pack(side=BOTTOM)

#-------------------- FORM ENTRIES ------------------------------

        self.labelnhs_number = Label(formframe, font=('calibri', 20, 'bold'), text="NHS number:", padx=2, pady=2)
        self.labelnhs_number.grid(row=0, column=0, sticky=W)
        self.entrynhs_number = Entry(formframe, font=('calibri', 20, 'bold'), textvariable=nhs_number, width=30)
        self.entrynhs_number.grid(row=0, column=1)

        self.labelfirstname = Label(formframe, font=('calibri', 20, 'bold'), text="First name:", padx=2, pady=2)
        self.labelfirstname.grid(row=1, column=0, sticky=W)
        self.entryfirstname = Entry(formframe, font=('calibri', 20, 'bold'), textvariable=Firstname, width=30)
        self.entryfirstname.grid(row=1, column=1)

        self.labelsurname = Label(formframe, font=('calibri', 20, 'bold'), text="Surname:", padx=2, pady=2)
        self.labelsurname.grid(row=2, column=0, sticky=W)
        self.entrysurname = Entry(formframe, font=('calibri', 20, 'bold'), textvariable=Surname, width=30)
        self.entrysurname.grid(row=2, column=1)

        self.labeldob = Label(formframe, font=('calibri', 20, 'bold'), text="Date of Birth:", padx=2, pady=2)
        self.labeldob.grid(row=3, column=0, sticky=W)
        self.entrydob = Entry(formframe, font=('calibri', 20, 'bold'), textvariable=DOB, width=30)
        self.entrydob.grid(row=3, column=1)

        self.labelgender = Label(formframe, font=('calibri', 20, 'bold'), text="Gender:", padx=2, pady=2)
        self.labelgender.grid(row=4, column=0, sticky=W)
        self.entrygender = Entry(formframe, font=('calibri', 20, 'bold'), textvariable=Gender, width=30)
        self.entrygender.grid(row=4, column=1)

        self.labeladdress = Label(formframe, font=('calibri', 20, 'bold'), text="Address:", padx=2, pady=2)
        self.labeladdress.grid(row=5, column=0, sticky=W)
        self.entryaddress = Entry(formframe, font=('calibri', 20, 'bold'), textvariable=Address, width=30)
        self.entryaddress.grid(row=5, column=1)

        self.labelcontact = Label(formframe, font=('calibri', 20, 'bold'), text="Contact number:", padx=2, pady=2)
        self.labelcontact.grid(row=6, column=0, sticky=W)
        self.entrycontact= Entry(formframe, font=('calibri', 20, 'bold'), textvariable=Contact_number, width=30)
        self.entrycontact.grid(row=6, column=1)

        self.labelallergies = Label(formframe, font=('calibri', 20, 'bold'), text="Allergies:", padx=2, pady=2)
        self.labelallergies.grid(row=7, column=0, sticky=W)
        self.entryallergies = Entry(formframe, font=('calibri', 20, 'bold'), textvariable=Allergies, width=30)
        self.entryallergies.grid(row=7, column=1)

        self.labelmedhis = Label(formframe, font=('calibri', 20, 'bold'), text="Medical history:", padx=2, pady=2)
        self.labelmedhis.grid(row=8, column=0, sticky=W)
        self.entrymedhis = Entry(formframe, font=('calibri', 20, 'bold'), textvariable=Medical_history, width=30)
        self.entrymedhis.grid(row=8, column=1)

        self.labelusername = Label(actionsframe, font=('calibri', 12, 'bold'), text="Select a username:", padx=2, pady=2)
        self.labelusername.grid(row=1, column=0, sticky=W)
        self.entryusername = Entry(actionsframe, font=('calibri', 12, 'bold'), textvariable=username, width=25)
        self.entryusername.grid(row=1, column=1)

        self.labelpassword = Label(actionsframe, font=('calibri', 12, 'bold'), text="  Select a password:", padx=2, pady=2)
        self.labelpassword.grid(row=1, column=2, sticky=W)
        self.entrypassword = Entry(actionsframe, font=('calibri', 12, 'bold'), textvariable=password, width=25)
        self.entrypassword.grid(row=1, column=3)



# ----------------  Actions to form -----------------------------

        self.add_details_btn = Button(actionsframe, text="Confirm registration", font=('arial', 12, 'bold'), height=1, width=18, relief=RAISED, command=add_pt)
        self.add_details_btn.grid(row=1, column=4)

        # self.up_details_btn = Button(actionsframe, text="Update details", font=('arial', 8, 'bold'), height=1, width=15)
        # self.up_details_btn.grid(row=9, column=2)

root = Tk()
x = for_pt(root)

root.mainloop()