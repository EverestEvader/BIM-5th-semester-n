import tkinter as tk
from tkinter import messagebox

# Function to find the maximum number
def find_maximum():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        result = max(num1, num2, num3)
        result_label.config(text=f"Maximum: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

# Function to find the minimum number
def find_minimum():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        result = min(num1, num2, num3)
        result_label.config(text=f"Minimum: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Maximum and Minimum Finder")

# Create input labels and entry boxes
label1 = tk.Label(root, text="Enter first number:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter second number:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="Enter third number:")
label3.pack()
entry3 = tk.Entry(root)
entry3.pack()

# Create buttons for finding max and min
max_button = tk.Button(root, text="Find Maximum", command=find_maximum)
max_button.pack()

min_button = tk.Button(root, text="Find Minimum", command=find_minimum)
min_button.pack()

# Label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Run the application
root.mainloop()
