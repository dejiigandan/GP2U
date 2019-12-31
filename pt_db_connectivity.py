import sqlite3

def ptDatabase():
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS patient_details(nhs_number INTEGER PRIMARY KEY, Firstname TEXT, Surname TEXT, DOB TEXT, \
                Gender TEXT, Address TEXT, Contact number TEXT, Allergies TEXT, Medical history TEXT, username TEXT, password TEXT)""")
    conn.commit()                                                                                       # commits the transaction
    conn.close()

def new_patient(title, nhs_number, Firstname, Surname, DOB, Gender, Address, Contact_number, Allergies, Medical_history, username, password):
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS patient_details(title TEXT, nhs_number INTEGER PRIMARY KEY, Firstname TEXT, Surname TEXT, DOB TEXT, \
                    Gender TEXT, Address TEXT, Contact number TEXT, Allergies TEXT, Medical history TEXT, username TEXT, password TEXT)""")
    conn.commit()
    cursor.execute("""INSERT INTO patient_details VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                   (title, nhs_number, Firstname, Surname, DOB, Gender, Address, Contact_number, Allergies, Medical_history, username, password))
    conn.commit()
    conn.close()

def confirm_pt_registration(title, nhs_number, Firstname, Surname, DOB, Gender, Address, Contact_number, Allergies, Medical_history, username, password):
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS confirmed_patients(title TEXT, nhs_number INTEGER PRIMARY KEY, Firstname TEXT, Surname TEXT, DOB TEXT, \
                    Gender TEXT, Address TEXT, Contact number TEXT, Allergies TEXT, Medical history TEXT, username TEXT, password TEXT)""")
    conn.commit()
    cursor.execute("""INSERT INTO confirmed_patients VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                   (title, nhs_number, Firstname, Surname, DOB, Gender, Address, Contact_number, Allergies, Medical_history, username, password))
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

def pull_info():
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patient_details")
    conn.close()
    row = cursor.fetchall()                                                                                # returns rows as a list
    return row

def delete_patient(ptId):
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute("DELETE * FROM patient_details WHERE ptId=?", (ptId,))
    conn.commit()
    conn.close()

def update_patient_details(ptId, title="", nhs_number="", Firstname="", Surname="", DOB="", Gender="", Address="", Contact_number="", Allergies="", Medical_history="", username="", password=""):
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE pt_details SET title=?, nhs_number=?, Firstname=?, Surname=?, DOB=?, Gender=?, Address=?, Contact_number=?, Allergies=?, Medical_history=?, username=?, password=?, WHERE ptID=?", \
                (title, nhs_number, Firstname, Surname, DOB, Gender, Address, Contact_number, Allergies, Medical_history, username, password, ptId))
    conn.commit()
    conn.close()

def search_patient(title="", nhs_number="", Firstname="", Surname="", DOB="", Gender="", Address="", Contact_number="", username=""):
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patient_details WHERE nhs_number=? OR Firstname=?, Surname=? OR DOB=?, Gender=? OR Address=? OR Contact_number=? OR username=? ",\
                (title, nhs_number, Firstname, Surname, DOB, Gender, Address, Contact_number, Allergies, Medical_history, username))
    row = cursor.fetchall()
    conn.close()
    return row


