import sqlite3

# Step 1: Establish a connection to the database
connection = sqlite3.connect("students.db")

# Step 2: Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Step 3: Drop the existing table if it exists (this ensures a clean slate)
cursor.execute("DROP TABLE IF EXISTS students")

# Step 4: Create the students table with exact column names
cursor.execute('''
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    level TEXT NOT NULL,
    program TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')
print("Table 'students' created successfully.")

# Step 5: Insert data into the students table
students_data = [
    ("Nilesh Karmacharya", 22, "5th semester", "BIM", "nilesh.karmacharya@gmail.com"),
    ("Pratyush Suwal", 21, "5th semester", "BIM", "pratyush.suwal@gmail.com"),
    ("Aakriti Prajapati", 22, "5th semester", "BIM", "aakriti.prajapati@gmail.com"),
    ("Sashin Chawal", 21, "5th semester", "BIM", "sashin.chawal@outlook.com"),
    ("Pragya Shrestha", 22, "5th semester", "BIM", "pragya.shrestha@outlook.com"),
    ("Sanim Dware", 23, "5th semester", "BIM", "sanim.dware@gmail.com"),
    ("Ronish Karmacharya", 21, "5th semester", "BIM", "ronish.karmacharya@gmail.com"),
    ("Ronish Kayastha", 21, "5th semester", "BIM", "ronish.kayastha@gmail.com"),
    ("Spandan Pokharel", 21, "5th semester", "BIM", "spandan.pokharel@gmail.com"),
    ("Ujwal Parajuli", 22, "5th semester", "BIM", "ujwal.parajuli@gmail.com"),
    ("Aaisha Awal", 26, "5th semester", "BIM", "aaisha.awal@gmail.com"),
    ("Prajwal Maka", 21, "5th semester", "BIM", "prajwal.maka@gmail.com"),
    ("KP Sharma Oli", 70, "5th semester", "BIM", "kp.sharma.oli@yahoo.com"),
    ("Pushpa Kamal Dahal", 68, "5th semester", "BIM", "pushpa.kamal.dahal@gmail.com")
]

# Step 6: Insert data using executemany
cursor.executemany('''
INSERT INTO students (name, age, level, program, email)
VALUES (?, ?, ?, ?, ?)
''', students_data)
print("Data inserted successfully.")

# Step 7: Display all students
def display_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

print("\nStudents data:")
display_students()

# Step 8: Update a student's details
cursor.execute('''
UPDATE students
SET age = 23
WHERE name = "Nilesh Karmacharya"
''')
print("\nUpdated age for Nilesh Karmacharya.")
display_students()

# Step 9: Delete a student's record
cursor.execute('''
DELETE FROM students
WHERE name = "KP Sharma Oli"
''')
print("\nDeleted KP Sharma Oli's record.")
display_students()

# Step 10: Commit changes and close the connection
connection.commit()
connection.close()
print("\nDatabase operations completed.")