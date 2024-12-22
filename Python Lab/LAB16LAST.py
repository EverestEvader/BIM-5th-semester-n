import sqlite3

# Step 1: Establish a connection to the database
connection = sqlite3.connect("employees.db")

# Step 2: Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Step 3: Drop the existing table if it exists (this ensures a clean slate)
cursor.execute("DROP TABLE IF EXISTS employees")

# Step 4: Create the employees table with exact column names
cursor.execute('''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    job_title TEXT NOT NULL,
    post TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')
print("Table 'employees' created successfully.")

# Step 5: Insert data into the employees table
employees_data = [
    ("Nilesh Karmacharya", 22, "Graphic Designer", "Senior Designer", "nilesh.karmacharya@gmail.com"),
    ("Pratyush Suwal", 21, "Data Analyst", "Assistant Manager", "pratyush.suwal@gmail.com"),
    ("Aakriti Prajapati", 22, "Software Engineer", "Manager", "aakriti.prajapati@gmail.com"),
    ("Sashin Chawal", 21, "Web Developer", "Team Lead", "sashin.chawal@outlook.com"),
    ("Pragya Shrestha", 22, "Content Writer", "Content Manager", "pragya.shrestha@outlook.com"),
    ("Sanim Dware", 23, "System Administrator", "IT Head", "sanim.dware@gmail.com"),
    ("Ronish Karmacharya", 21, "Digital Marketer", "SEO Specialist", "ronish.karmacharya@gmail.com"),
    ("Ronish Kayastha", 21, "Network Engineer", "Support Lead", "ronish.kayastha@gmail.com"),
    ("Spandan Pokharel", 21, "HR Officer", "HR Manager", "spandan.pokharel@gmail.com"),
    ("Ujwal Parajuli", 22, "Business Analyst", "Analyst Lead", "ujwal.parajuli@gmail.com"),
    ("Aaisha Awal", 26, "Accountant", "Finance Head", "aaisha.awal@gmail.com"),
    ("Prajwal Maka", 21, "UX Designer", "Creative Head", "prajwal.maka@gmail.com"),
    ("Ram Bahadur", 30, "CEO", "Director", "bahadurramey@yahoo.com"),
    ("Rajesh Hamal", 38, "COO", "Executive Director", "rajeshdai@gmail.com")
]

# Step 6: Insert data using executemany
cursor.executemany('''
INSERT INTO employees (name, age, job_title, post, email)
VALUES (?, ?, ?, ?, ?)
''', employees_data)
print("Data inserted successfully.")

# Step 7: Display all employees
def display_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

print("\nEmployees data:")
display_employees()

# Step 8: Update an employee's details
cursor.execute('''
UPDATE employees
SET age = 23
WHERE name = "Nilesh Karmacharya"
''')
print("\nUpdated age for Nilesh Karmacharya.")
display_employees()

# Step 9: Delete an employee's record
cursor.execute('''
DELETE FROM employees
WHERE name = "Ram Bahadur"
''')
print("\nDeleted Ram Bahadur's record.")
display_employees()

# Step 10: Commit changes and close the connection
connection.commit()
connection.close()
print("\nDatabase operations completed.")