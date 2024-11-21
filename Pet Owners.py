import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Zohaib123",
    db='menagerie'
)
cursor=connection.cursor()
cursor.execute("SELECT owner FROM pet;")
data = cursor.fetchall()
print(data)
cursor.close()
connection.close()