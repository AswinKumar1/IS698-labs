import mysql.connector

conn = mysql.connector.connect(
 host="s*#*#*#*#*#*#*#**#*#*#.rds.amazonaws.com",
 user="admin",
 password="*************",
 database="University"
)

cursor = conn.cursor()

cursor.execute("INSERT INTO Students VALUES (2, 'Kush Patel', 22, 'Information Systems')")

conn.commit()

cursor.execute("SELECT * FROM Students")
for row in cursor.fetchall():
 print(row)

cursor.close()
conn.close()

