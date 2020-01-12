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

# import smtplib
#
# def send_email(subject, content):
#     try:
#         server = smtplib.SMTP('smtp.gmail.com:587')
#         server.ehlo()
#         server.starttls()
#         server.login("gp2ulondon@gmail.com", "gooddoctor")
#         message = f'Subject: {subject}\n\n{content}'
#         server.sendmail("gp2ulondon@gmail.com", "gp2ulondon@gmail.com", message)
#         server.quit()
#         print("Works")
#     except:
#         print("fail")
#
# subject = "test subject"
# content = "how are you today"
# send_email(subject, content)