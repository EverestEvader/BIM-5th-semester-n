import numpy as np 
 
# create a 2-D array  
array1 = np.array([[2, 4, 6], 
                  [1, 3, 5]]) 
 
# check the dimension of array1 
print("Dimension = ",array1.ndim)  
# return total number of elements in array1 
print("\n Array Size = ",array1.size) 
# return a tuple that gives size of array in each dimension 
print("\n Array Shape = ",array1.shape) 
# check the data type of array1 
print("\n Data Type = ",array1.dtype) 
# use of itemsize to determine size of each array element of array1  
 
print("\n Size of each data = ",array1.itemsize) 
#print memory address of array1 data 
print("\nData of array1 is: ",array1.data)