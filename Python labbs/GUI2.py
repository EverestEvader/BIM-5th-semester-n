import tkinter as tk
from tkinter import messagebox

# Function to perform multiplication
def multiply_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

# Function to perform division
def divide_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = num1 / num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")
    except ZeroDivisionError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Multiplication and Division")

# Create input labels and entry boxes
label1 = tk.Label(root, text="Enter first number:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter second number:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Create buttons for multiplication and division
multiply_button = tk.Button(root, text="Multiply", command=multiply_numbers)
multiply_button.pack()

divide_button = tk.Button(root, text="Divide", command=divide_numbers)
divide_button.pack()

# Label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Run the application
root.mainloop()
