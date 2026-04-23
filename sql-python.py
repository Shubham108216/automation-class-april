import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="SHUBHAM18",
    password="root@123",)
print(mydb,"connected")