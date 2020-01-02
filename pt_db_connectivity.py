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

# def confirm_pt_registration(title, nhs_number, Firstname, Surname, DOB, Gender, Address, Contact_number, Allergies, Medical_history, username, password):
#     conn = sqlite3.connect("ptdatabase.db")
#     cursor = conn.cursor()
#     cursor.execute("""CREATE TABLE IF NOT EXISTS confirmed_patients(title TEXT, nhs_number INTEGER PRIMARY KEY, Firstname TEXT, Surname TEXT, DOB TEXT, \
#                     Gender TEXT, Address TEXT, Contact number TEXT, Allergies TEXT, Medical history TEXT, username TEXT, password TEXT)""")
#     conn.commit()
#     cursor.execute("""INSERT INTO confirmed_patients VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
#                    (title, nhs_number, Firstname, Surname, DOB, Gender, Address, Contact_number, Allergies, Medical_history, username, password))
#     conn.commit()
#     conn.close()

def confirm_pt_registration(self, pttitle, ptnhs_number, ptFirstname, ptSurname, ptDOB, ptGender, ptAddress, ptContact_number, ptAllergies, ptMedical_history, ptusername, ptpassword):
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS confirmed_patients(title TEXT, nhs_number INTEGER PRIMARY KEY, Firstname TEXT, Surname TEXT, DOB TEXT, \
                    Gender TEXT, Address TEXT, Contact_number TEXT, Allergies TEXT, Medical_history TEXT, username TEXT, password TEXT)""")
    conn.commit()
    cursor.execute("INSERT INTO confirmed_patients VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
               (pttitle, ptnhs_number, ptFirstname, ptSurname, ptDOB, ptGender, ptAddress, ptContact_number, ptAllergies,
                ptMedical_history, ptusername, ptpassword))
    conn.commit()
    conn.close()



def confirm_gp():
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS list_of_gps(title TEXT, Firstname TEXT, Surname TEXT,  Gender TEXT,  \
                    Address TEXT, Contact number TEXT, DOB TEXT, username INTEGER PRIMARY KEY TEXT, password TEXT)""")
    conn.commit()
    cursor.execute("""INSERT INTO list_of_gps VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                   (title, Firstname, Surname,  Gender, Address, Contact_number, DOB, username, password))
    conn.commit()
    conn.close()


def delete_patient(nhs_number):
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute("DELETE * FROM patient_details WHERE nhs_number=?", (nhs_number,))
    conn.commit()
    conn.close()

def update_patient_details(ptId, title="", nhs_number="", Firstname="", Surname="", DOB="", Gender="", Address="", Contact_number="", Allergies="", Medical_history="", username="", password=""):
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE pt_details SET title=?, nhs_number=?, Firstname=?, Surname=?, DOB=?, Gender=?, Address=?, Contact_number=?, Allergies=?, Medical_history=?, username=?, password=?, WHERE ptID=?", \
                (title, nhs_number, Firstname, Surname, DOB, Gender, Address, Contact_number, Allergies, Medical_history, username, password, ptId))
    conn.commit()
    conn.close()

# def search_user(nhs_number="", Firstname="", Surname="", DOB="", Address="", Contact_number="", username=""):
#     try:
#         conn = sqlite3.connect("ptdatabase.db")
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM patient_details AND list_of_gps WHERE nhs_number=? OR Firstname=?, Surname=? OR DOB=?, OR Address=? OR Contact_number=? OR username=? ",\
#                     (nhs_number, Firstname, Surname, DOB, Address, Contact_number, username))
#         row = cursor.fetchone()
#         nhs_number.set(row[])
#         conn.close()
#         return row
#
#     except:
#         tkinter.messagebox.INFO(message="User account not found in our records")


