import sqlite3

def ptDatabase():
    conn = sqlite3.connect("ptdatabase")
    cur.execute("CREATE TABLE IF NOT EXISTS patient_details(nhs number INTEGER PRIMARY KEY, Firstname TEXT, Surname TEXT, DOB TEXT, \
                Gender TEXT, Address TEXT, Contact number TEXT, Allergies TEXT, Medical history TEXT)")
    conn.commit()
    conn.close()


def new_patient(nhs_number, Firstname, Surname, DOB, Gender, Address, Contact_number, Allergies, Medical_history, username, password):
    conn = sqlite3.connect("ptdatabase")
    cur = conn.cursor()
    cur.execute("INSERT INTO patient_details VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)", nhs_number, Firstname, Surname, DOB, Gender, Address, Contact_number, Allergies, Medical_history, username, password)
    conn.commit()
    conn.close()

def pull_info():
    conn = sqlite3.connect("ptdatabase")
    cur = conn.cursor()
    cur.execute("SELECT * FROM patient_details")
    row = cur.fetchall()
    conn.close()
    return row

def delete_patient(ptId):
    conn = sqlite3.connect("ptdatabase")
    cur = conn.cursor()
    cur.execute("DELETE * FROM patient_details WHERE ptId=?", (ptId,))
    conn.commit()
    conn.close()

def update_patient_details(ptId, nhs_number="", Firstname="", Surname="", DOB="", Gender="", Address="", Contact_number="", Allergies="", Medical_history="", username="", password=""):
    conn = sqlite3.connect("ptdatabase")
    cur = conn.cursor()
    cur.execute("UPDATE pt_details SET nhs_number=?, Firstname=?, Surname=?, DOB=?, Gender=?, Address=?, Contact_number=?, Allergies=?, Medical_history=?, username=?, password=?, WHERE ptID=?", \
                (nhs_number, Firstname, Surname, DOB, Gender, Address, Contact_number, Allergies, Medical_history, username, password, ptId))
    conn.commit()
    conn.close()

def search_patient(nhs_number="", Firstname="", Surname="", DOB="", Gender="", Address="", Contact_number="", username=""):
    conn = sqlite3.connect("ptdatabase")
    cur = conn.cursor()
    cur.execute("SELECT * FROM patient_details WHERE nhs_number=? OR Firstname=?, Surname=? OR DOB=?, Gender=? OR Address=? OR Contact_number=? OR username=? ",\
                (nhs_number, Firstname, Surname, DOB, Gender, Address, Contact_number, Allergies, Medical_history, username))
    row = cur.fetchall()
    conn.close()
    return row


