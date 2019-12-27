import sqlite3

def ptDatabase():
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS patient_details(nhs_number INTEGER PRIMARY KEY, Firstname TEXT, Surname TEXT, DOB TEXT, \
                Gender TEXT, Address TEXT, Contact number TEXT, Allergies TEXT, Medical history TEXT, username TEXT, password TEXT)""")
    conn.commit()                                                                                       # commits the transaction
    conn.close()

def new_patient(nhs_number, Firstname, Surname, DOB, Gender, Address, Contact_number, Allergies, Medical_history, username, password):
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS patient_details(nhs_number INTEGER PRIMARY KEY, Firstname TEXT, Surname TEXT, DOB TEXT, \
                    Gender TEXT, Address TEXT, Contact number TEXT, Allergies TEXT, Medical history TEXT, username TEXT, password TEXT)""")
    conn.commit()  # commits the transaction
    cursor.execute("""INSERT INTO patient_details VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                   (nhs_number, Firstname, Surname, DOB, Gender, Address, Contact_number, Allergies, Medical_history, username, password))
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

def update_patient_details(ptId, nhs_number="", Firstname="", Surname="", DOB="", Gender="", Address="", Contact_number="", Allergies="", Medical_history="", username="", password=""):
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE pt_details SET nhs_number=?, Firstname=?, Surname=?, DOB=?, Gender=?, Address=?, Contact_number=?, Allergies=?, Medical_history=?, username=?, password=?, WHERE ptID=?", \
                (nhs_number, Firstname, Surname, DOB, Gender, Address, Contact_number, Allergies, Medical_history, username, password, ptId))
    conn.commit()
    conn.close()

def search_patient(nhs_number="", Firstname="", Surname="", DOB="", Gender="", Address="", Contact_number="", username=""):
    conn = sqlite3.connect("ptdatabase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patient_details WHERE nhs_number=? OR Firstname=?, Surname=? OR DOB=?, Gender=? OR Address=? OR Contact_number=? OR username=? ",\
                (nhs_number, Firstname, Surname, DOB, Gender, Address, Contact_number, Allergies, Medical_history, username))
    row = cursor.fetchall()
    conn.close()
    return row


