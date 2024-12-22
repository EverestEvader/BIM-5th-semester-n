import mysql.connector
#mydb = mysql.connector.connect(host = "localhost", user = "Nilesh", password = "nilesh123")
mydb = mysql.connector.connect(user='root', password='nilesh123', database='nilesh' )
mycursor = mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print (i)