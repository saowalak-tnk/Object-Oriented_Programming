import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "9395",
    database = "shop"
)
print(mydb)