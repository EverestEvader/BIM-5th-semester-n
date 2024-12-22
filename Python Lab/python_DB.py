import mysql.connector

# Establish a connection to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nilesh123",
    database="nilesh"
)

# Create a cursor object to execute queries
mycursor = mydb.cursor()

# Execute a query to fetch all rows
mycursor.execute("SELECT * FROM student")

# Fetch all the rows
databases = mycursor.fetchall()

for i in databases:
    print(i)