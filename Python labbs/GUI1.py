import tkinter as tk
from tkinter import messagebox

# Function to perform addition
def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

# Function to perform subtraction
def subtract_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Addition and Subtraction")

# Create input labels and entry boxes
label1 = tk.Label(root, text="Enter first number:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter second number:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Create buttons for addition and subtraction
add_button = tk.Button(root, text="Add", command=add_numbers)
add_button.pack()

subtract_button = tk.Button(root, text="Subtract", command=subtract_numbers)
subtract_button.pack()

# Label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Run the application
root.mainloop()
