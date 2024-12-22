import sqlite3

# Step 1: Connect to SQLite database (creates the file if it doesn't exist)
connection = sqlite3.connect("example.db")

# Step 2: Create a cursor object
cursor = connection.cursor()

# Step 3: Write the SQL command to create a table
# The table 'users' has three columns: id (integer), name (text), and age (integer)
sql_command = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
);
"""

# Step 4: Execute the SQL command
cursor.execute(sql_command)

# Step 5: Commit the changes
connection.commit()

# Step 6: Close the connection
connection.close()

print("Table 'users' created successfully.")
