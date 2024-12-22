import numpy as np 
 
# generate an array of 5 random numbers in range 2,11 
arr1 = np.linspace(2,11,5) 
print("np.linspace(2,11,5) =",arr1) 
 
arr2 = np.linspace(2,11,5, endpoint = False) 
print("np.linspace(2,11,5) with endpoint false =",arr2) 
 
arr3 = np.linspace(2,11,5, endpoint = False,retstep = True) 
print("np.linspace(2,11,5 with endpoint and retstep) =",arr3) 