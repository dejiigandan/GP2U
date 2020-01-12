import sqlite3
import tkinter
import tkinter.messagebox

def ptDatabase():
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS patient_details(nhs_number INTEGER PRIMARY KEY, Firstname TEXT, Surname TEXT, DOB TEXT, \
                Gender TEXT, Address TEXT, Contact number TEXT, Allergies TEXT, Medical history TEXT, username TEXT, password VARCHAR)""")
    conn.commit()                                                                                       # commits the transaction
    conn.close()

def new_patient(title, nhs_number, Firstname, Surname, DOB, Gender, Address, Contact_number, Allergies, Medical_history, username, password):
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS patient_details(title TEXT, nhs_number INTEGER PRIMARY KEY, Firstname TEXT, Surname TEXT, DOB TEXT, \
                    Gender TEXT, Address TEXT, Contact number TEXT, Allergies TEXT, Medical history TEXT, username TEXT, password VARCHAR)""")
    conn.commit()
    cursor.execute("""INSERT INTO patient_details VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                   (title, nhs_number, Firstname, Surname, DOB, Gender, Address, Contact_number, Allergies, Medical_history, username, password))
    conn.commit()
    conn.close()

def new_gp(title, Firstname, Surname, DOB, Gender, Address, Contact_number, username, password):
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS gp_table(title TEXT, Firstname TEXT, Surname TEXT, DOB TEXT, \
                    Gender TEXT, Address TEXT, Contact number TEXT, username TEXT, password VARCHAR)""")
    conn.commit()
    cursor.execute("""INSERT INTO gp_table VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                   (title, Firstname, Surname, DOB, Gender, Address, Contact_number, username, password))
    conn.commit()
    conn.close()


def confirm_pt_registration(pttitle, ptnhs_number, ptFirstname, ptSurname, ptDOB, ptGender, ptAddress,
                            ptContact_number, ptAllergies, ptMedical_history, ptusername, ptpassword):
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS confirmed_patients(title TEXT, nhs_number TEXT, Firstname TEXT, Surname TEXT, DOB TEXT, \
                     Gender TEXT, Address TEXT, Contact_number TEXT, Allergies TEXT, Medical_history TEXT, username TEXT, password TEXT)""")
    conn.commit()
    cursor.execute("INSERT INTO confirmed_patients VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (pttitle, ptnhs_number, ptFirstname, ptSurname, ptDOB, ptGender, ptAddress, ptContact_number,
                    ptAllergies, ptMedical_history, ptusername.title(), ptpassword))
    conn.commit()
    conn.close()

# def delete_patient(nhs_number):
#     conn = sqlite3.connect("ptdatabase.db")
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM patient_details WHERE nhs_number=?", (nhs_number,))
#     conn.commit()
#     conn.close()

# def update_patient_details(pttitle, ptnhs_number, ptFirstname, ptSurname, ptDOB, ptGender, ptAddress,
#                             ptContact_number, ptAllergies, ptMedical_history, ptusername, ptpassword):
#     conn = sqlite3.connect("ptdatabase.db")
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO confirmed_patients VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
#                    (pttitle, ptnhs_number, ptFirstname, ptSurname, ptDOB, ptGender, ptAddress, ptContact_number,
#                     ptAllergies, ptMedical_history, ptusername, ptpassword))
#     conn.commit()
#     conn.close()

def update_patient_details(pttitle, ptnhs_number, ptFirstname, ptSurname, ptDOB, ptGender, ptAddress,
                            ptContact_number, ptAllergies, ptMedical_history, ptusername, ptpassword, another):
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute(""" UPDATE confirmed_patients SET title=(?), nhs_number=(?), Firstname=(?), Surname=(?), DOB=(?), Gender=(?), Address=(?), Contact_number=(?),
                    Allergies=(?), Medical_history=(?), username=(?), password=(?) WHERE nhs_number=(?) """,
                   (pttitle, ptnhs_number, ptFirstname, ptSurname, ptDOB, ptGender, ptAddress,
                    ptContact_number, ptAllergies, ptMedical_history, ptusername, ptpassword, another))
    conn.commit()
    conn.close()


def delete_a_gp(username):
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM gp_table WHERE username='%s'" %username)
    conn.commit()
    conn.close()

#------------------------------------- FOR GP AVAILABILITY------------------------------

def list_avail():
    conn = sqlite3.connect("appointments.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM availabilities")
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

def add_new_availability(newdate, newtime, docname):
    conn = sqlite3.connect("appointments.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS availabilities (date_available TEXT, time_available TEXT, doc TEXT)")
    conn.commit()
    cursor.execute("INSERT into availabilities VALUES (?, ?, ?)", (newdate, newtime, docname))
    conn.commit()
    conn.close()

def delete_availability(x, y, z):
    conn = sqlite3.connect("appointments.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM availabilities WHERE date_available='%s' AND time_available='%s'AND doc='%s'" %(x, y, z))
    conn.commit()
    conn.close()

def list_of_requests():
    conn = sqlite3.connect("appointments.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointment_requests")
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

def confirm_appointment(a, b, c, d):
    conn=sqlite3.connect("appointments.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS confirmed_appointments(NHS_NUMBER TEXT, apptmtdate TEXT, apptmttime TEXT, apptmtdoc TEXT)")
    conn.commit()
    cursor.execute("INSERT INTO confirmed_appointments VALUES (?, ?, ?, ?)", (a, b, c, d))
    conn.commit()
    conn.close()
#
#----------------------------- TO BOOK APPOINTMENTS ------------------------------------------

def request_apptmt(ptnhsno, lastname, adate, atime):
    conn = sqlite3.connect("appointments.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS appointment_requests(NHS_NUMBER TEXT, lastname TEXT, apptmtdate TEXT, apptmttime TEXT)")
    conn.commit()
    cursor.execute("INSERT INTO appointment_requests VALUES (?, ?, ?, ?)", (ptnhsno, lastname, adate, atime))
    conn.commit()
    conn.close()

def list_mypt_bookings(nhsno):
    conn = sqlite3.connect("appointments.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM confirmed_appointments WHERE NHS_NUMBER='%s'" %nhsno)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

def del_apptmt(mynhs, mydate, mytime):
    conn = sqlite3.connect("appointments.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM confirmed_appointments WHERE NHS_NUMBER='%s'AND apptmtdate='%s'AND apptmttime='%s'" %(mynhs, mydate, mytime))
    conn.commit()
    conn.close()


