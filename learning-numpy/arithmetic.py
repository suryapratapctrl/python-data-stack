import numpy as np

array=np.array([1.01,2.5,3.99])

print(array+1) # this will add one to each digit 

print(np.sqrt(array)) # this will give square root of array

print(np.floor(array))

print(np.ceil(array))

print(np.round(array))

#EXERCISE

radii=np.array([1,2,3])

print(np.pi * radii ** 2)


#element wise arithmetic

array1=np.array([1,2,3])
array2=np.array([4,5,6])

print(array1 +  array2)
print(array1 ** array2)

#comparison operators

scores=np.array([91,55,100,73,82,64])

print(scores==100)

scores[scores<60]=0

print(scores)