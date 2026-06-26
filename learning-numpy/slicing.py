import numpy as np

array=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

#array[start:end:step]
#select row
print(array[1:4])

print("-"*50)

print(array[0:4:2]) # this is same as array[::2]

print("-"*50)

print(array[::-1]) # reverse

#select column 

print(array[:,0]) # select all rows column zero

print(array[:,0 :3]) # this will print first three column 

