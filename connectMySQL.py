import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host='localhost', user='root', password='Soumen@1234')
print(mydb.connection_id)

mydb.close()
