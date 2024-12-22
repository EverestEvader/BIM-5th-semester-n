import sqlite3
import os

class StudentDatabase:
    def __init__(self, db_name='students.db'):
        """
        Initialize database connection and create students table if not exists
        """
        # Ensure database is in a writable directory
        self.db_path = os.path.join(os.getcwd(), db_name)
        
        # Establish database connection
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        
        # Create students table with comprehensive schema
        self.create_table()
    
    def create_table(self):
        """
        Create students table with specified columns
        Primary key is auto-incrementing ID for unique identification
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                level TEXT,
                program TEXT,
                email TEXT UNIQUE
            )
        ''')
        self.conn.commit()
    
    def insert_student(self, name, age, level, program, email):
        """
        Insert a new student record into the database
        """
        try:
            self.cursor.execute('''
                INSERT INTO students (name, age, level, program, email) 
                VALUES (?, ?, ?, ?, ?)
            ''', (name, age, level, program, email))
            self.conn.commit()
            print(f"Student {name} added successfully!")
        except sqlite3.IntegrityError:
            print(f"Error: Email {email} already exists!")
    
    def update_student(self, student_id, **kwargs):
        """
        Update student details by ID
        Supports updating multiple fields dynamically
        """
        update_fields = ', '.join([f"{key} = ?" for key in kwargs.keys()])
        query = f"UPDATE students SET {update_fields} WHERE id = ?"
        
        try:
            self.cursor.execute(query, list(kwargs.values()) + [student_id])
            self.conn.commit()
            print(f"Student with ID {student_id} updated successfully!")
        except sqlite3.Error as e:
            print(f"Update failed: {e}")
    
    def delete_student(self, student_id):
        """
        Delete a student record by ID
        """
        try:
            self.cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
            self.conn.commit()
            print(f"Student with ID {student_id} deleted successfully!")
        except sqlite3.Error as e:
            print(f"Deletion failed: {e}")
    
    def search_students(self, **kwargs):
        """
        Search students based on various criteria
        Supports multiple search parameters
        """
        conditions = ' AND '.join([f"{key} LIKE ?" for key in kwargs.keys()])
        query = f"SELECT * FROM students WHERE {conditions}"
        
        search_params = [f"%{value}%" for value in kwargs.values()]
        
        try:
            self.cursor.execute(query, search_params)
            results = self.cursor.fetchall()
            
            if results:
                print("Search Results:")
                for student in results:
                    print(student)
            else:
                print("No matching students found.")
        except sqlite3.Error as e:
            print(f"Search failed: {e}")
    
    def display_all_students(self):
        """
        Display all students in the database
        """
        try:
            self.cursor.execute('SELECT * FROM students')
            students = self.cursor.fetchall()
            
            print("\nAll Students:")
            for student in students:
                print(student)
        except sqlite3.Error as e:
            print(f"Display failed: {e}")
    
    def close_connection(self):
        """
        Close database connection
        """
        self.conn.close()
        print("Database connection closed.")

def main():
    # Initialize database
    db = StudentDatabase()
    
    # Insert students individually
    student_data = [
        ("Nilesh Karmacharya", 23, " 5th Sem", "BIM", "nilesh@Gmail.com"),
        ("Pratyush Suwal", 21, " 5th Sem", "BIM", "pratyush@Gmail.com"),
        ("Aakriti Prajapati", 22, " 5th Sem", "BIM", "aakriti@Gmail.com"),
        ("Sashin Chawal", 21, " 5th Sem", "BIM", "sashin@Outlook.com"),
        ("Pragya Shrestha", 22, " 5th Sem", "BIM", "pragya@Outlook.com"),
        ("Sanim Dware", 23, " 5th Sem", "BIM", "sanim@Gmail.com"),
        ("Ronish Karmacharya", 21, " 5th Sem", "BIM", "ronishk@Gmail.com"),
        ("Ronish Kayastha", 22, " 5th Sem", "BIM", "ronishka@Gmail.com"),
        ("Spandan Pokharel", 21, " 5th Sem", "BIM", "spandan@Gmail.com"),
        ("Ujwal Parajuli", 22, " 5th Sem", "BIM", "ujwal@Outlook.com"),
        ("Aaisha Awal", 29, " 5th Sem", "BIM", "aaisha@Outlook.com"),
        ("Prajwal Maka", 21, " 5th Sem", "BIM", "prajwal@Outlook.com"),
        ("KP Sharma Oli", 22, " 5th Sem", "BIM", "kpoli@Yahoo.com"),
        ("Pushpa Kamal Dahal", 23, " 5th Sem", "BIM", "pushpa@Yahoo.com")
    ]
    
    # Insert students one by one
    for student in student_data:
        db.insert_student(*student)
    
    # Display all students
    db.display_all_students()
    
    # Demonstrate search functionality
    print("\nSearching for students with name containing 'Ronish':")
    db.search_students(name="Ronish")
    
    # Update a student (assuming first student's ID is 1)
    db.update_student(1, email="new_nilesh@Yahoo.com")
    
    # Delete a student (assuming last student's ID is 14)
    db.delete_student(14)
    
    # Display updated student list
    db.display_all_students()
    
    # Close database connection
    db.close_connection()

if __name__ == "__main__":
    main()