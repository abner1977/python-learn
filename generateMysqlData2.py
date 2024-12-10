import random
import string
import mysql.connector

cnx = mysql.connector.connect(user='root', password='ht1qaz', host='localhost', database='localdb')


cursor = cnx.cursor()

for i in range(10000000):
    name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    age = random.randint(18, 60)
    address = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    path = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    query = "INSERT INTO student (name,age,adress,path) VALUES (%s,%s,%s,%s)"
    values = (name, age, address, path)
    cursor.execute(query, values)

cnx.commit()

cursor.close()
cnx.close()
