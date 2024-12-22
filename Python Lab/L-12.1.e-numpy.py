import numpy as np

# Step 1: Create a NumPy array
array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])

print("Original Array:")
print(array)

# Step 2: Accessing specific elements (Indexing)
print("\nElement at row 1, column 2:", array[1, 2])  # Element at 2nd row, 3rd column
print("Element at row 0, column 3:", array[0, 3])  # Element at 1st row, 4th column

# Step 3: Slicing the array (Rows and Columns)
print("\nSliced Array (All rows, column 1 to 2):")
print(array[:, 1:3])  # Slicing columns 2 and 3 from all rows

print("\nSliced Array (First two rows, last two columns):")
print(array[0:2, 2:4])  # Slicing first two rows and last two columns

# Step 4: Modifying an element using indexing
array[1, 2] = 100
print("\nArray after modifying element at row 1, column 2:")
print(array)

# Step 5: Slicing and modifying part of the array
array[0:2, 2:4] = [[50, 60], [70, 80]]
print("\nArray after modifying a slice (First two rows, last two columns):")
print(array)