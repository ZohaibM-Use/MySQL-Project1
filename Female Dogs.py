import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Zohaib123",
    db='menagerie'
)
cursor=connection.cursor()
cursor.execute("SELECT * FROM pet WHERE species = 'dog' AND sex = 'f';")
query = cursor.fetchall()
for info in query:
    print(info)

cursor.close()
connection.close()