import numpy as np

# broadcasting allowa numpy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape.

#the dimensions have the same size
#OR
#One of the dimensions has a size of 1.

array1=np.array([[1,2,3,4]])

array2=np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)

print(array1*array2)

#exercise 

arr1=np.array([[1,2,3,4,5,6,7,8,9,10]])
arr2=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(arr1.shape)
print(arr2.shape)

print(arr1*arr2)

