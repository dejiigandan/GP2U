import sqlite3


conn = sqlite3.connect("ptdatabase.db")
cursor = conn.cursor()
cursor.execute("""SELECT * FROM patient_details""")
print(cursor.fetchone())
conn.commit()
conn.close()


#SELECT * FROM patient_details
#('Mrs', 357, 'jay', 'y', '198', 'Male', 'oihjn', '357', 'aga', 'adga', 'Jay', 'y')