import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Zohaib123"
)
cursor=connection.cursor()
cursor.execute('DROP DATABASE IF EXISTS menagerie')
cursor.execute('SHOW DATABASES')
databases = cursor.fetchall()
for database in databases:
    print(database)

cursor.close()
connection.close()