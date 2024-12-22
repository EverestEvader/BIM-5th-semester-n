import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Create first array with 10 random numbers between 1 and 20
array1 = np.random.randint(1, 20, size=10)

# Create second array with squares of first array
array2 = np.square(array1)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot both arrays
plt.scatter(array1, array2, color='blue', s=100, alpha=0.6, label='Data Points')
plt.plot(array1, array2, color='red', linestyle='--', alpha=0.5, label='Trend Line')

# Add labels and title
plt.xlabel('Random Numbers', fontsize=12)
plt.ylabel('Square of Random Numbers', fontsize=12)
plt.title('Random Numbers vs Their Squares', fontsize=14, pad=20)

# Add grid
plt.grid(True, linestyle=':', alpha=0.6)

# Add legend
plt.legend()

# Display the arrays
print("Original Array:", array1)
print("Squared Array:", array2)

# Show the plot
plt.tight_layout()
plt.show()
