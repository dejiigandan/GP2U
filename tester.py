import sqlite3


conn = sqlite3.connect("ptdatabase.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM confirmed_patients ")
#cursor.execute("""DROP table gp_table""")
print(cursor.fetchall())
conn.commit()
conn.close()


#SELECT * FROM patient_details
#SELECT * FROM gp_table
#('Mrs', 357, 'jay', 'y', '198', 'Male', 'oihjn', '357', 'aga', 'adga', 'Jay', 'y')

