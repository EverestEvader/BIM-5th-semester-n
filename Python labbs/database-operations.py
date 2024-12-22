import sqlite3

def create_connection():
    """Create a database connection and return the connection object"""
    try:
        conn = sqlite3.connect('employee.db')
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table(conn):
    """Create employees table"""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                salary REAL
            )
        ''')
        conn.commit()
        print("Table created successfully")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def insert_records(conn):
    """Insert three sample records"""
    try:
        cursor = conn.cursor()
        records = [
            (1, 'John Smith', 'IT', 75000.00),
            (2, 'Sarah Johnson', 'HR', 65000.00),
            (3, 'Michael Brown', 'Finance', 80000.00)
        ]
        
        cursor.executemany('INSERT INTO employees VALUES (?,?,?,?)', records)
        conn.commit()
        print("Records inserted successfully")
    except sqlite3.Error as e:
        print(f"Error inserting records: {e}")

def update_record(conn):
    """Update salary for John Smith"""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE employees 
            SET salary = 78000.00 
            WHERE name = 'John Smith'
        ''')
        conn.commit()
        print("Record updated successfully")
    except sqlite3.Error as e:
        print(f"Error updating record: {e}")

def delete_record(conn):
    """Delete record for Sarah Johnson"""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM employees 
            WHERE name = 'Sarah Johnson'
        ''')
        conn.commit()
        print("Record deleted successfully")
    except sqlite3.Error as e:
        print(f"Error deleting record: {e}")

def display_records(conn):
    """Display all records in the table"""
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM employees')
        records = cursor.fetchall()
        
        print("\nCurrent Employee Records:")
        print("-------------------------")
        print("ID  |  Name           |  Department  |  Salary")
        print("----+----------------+-------------+---------")
        for record in records:
            print(f"{record[0]:<4}|  {record[1]:<14}|  {record[2]:<11}|  ${record[3]:,.2f}")
    except sqlite3.Error as e:
        print(f"Error displaying records: {e}")

def main():
    # Create database connection
    conn = create_connection()
    if conn is None:
        return
    
    # Create table
    create_table(conn)
    
    # Insert records
    insert_records(conn)
    
    # Display initial records
    print("\nInitial Records:")
    display_records(conn)
    
    # Update a record
    update_record(conn)
    
    # Delete a record
    delete_record(conn)
    
    # Display final results
    print("\nAfter Update and Delete:")
    display_records(conn)
    
    # Close connection
    conn.close()

if __name__ == "__main__":
    main()
