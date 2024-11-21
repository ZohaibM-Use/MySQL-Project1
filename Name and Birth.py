import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Zohaib123",
    db='menagerie'
)
cursor=connection.cursor()
cursor.execute("Select name, birth FROM pet;")
data = cursor.fetchall()
for info in data:
    print(info)
cursor.close()
connection.close()