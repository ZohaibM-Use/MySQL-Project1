import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Zohaib123"
)
cursor = connection.cursor()
cursor.execute('CREATE DATABASE menagerie')
cursor.execute('USE menagerie')
cursor.execute('CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20),'
               'species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);')

cursor.execute('DESCRIBE pet')
structure = cursor.fetchall()
for describe in structure:
    print(describe)

cursor.close()
connection.close()