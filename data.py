import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Zohaib123",
    db='menagerie',
    allow_local_infile=True
)
cursor=connection.cursor()
query = """
LOAD DATA LOCAL INFILE 'pet.txt'
INTO TABLE pet
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
(name, owner, species, sex, birth, death);
"""
cursor.execute(query)
connection.commit()

cursor.execute('SELECT * FROM pet;')
data = cursor.fetchall()
for info in data:
    print(info)
cursor.close()
connection.close()