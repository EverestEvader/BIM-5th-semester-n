import numpy as np 
 
# create a 2D array with 2 rows and 4 columns 
array1 = np.array([[1, 2, 3, 4], 
    [5, 6, 7, 8]]) 
#create a 2D array using list having 3 rows and 4 columns 
list2 = [[1,2,3,4],[7,8,9,10],[11,12,13,14]] 
array2 = np.array(list2) 
 
print(f'Array 1 is \n {array1}\n') 
print(f'Array 2 is \n {array2}\n') 
#creating a 3D array using two 2D slices of size 2*3 
list3 =[[[1,2,3], 
         [4,5,6]], 
        [[7,8,9], 
         [11,12,13]]] 
array3 = np.array(list3) 
print(f'3-D Array is \n {array3}')