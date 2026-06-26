import numpy as np

ages=np.array([[21,17,19,20,16,30,18,65],
               [39,22,15,99,18,19,20,21]])

teenagers=ages[ages<18] # this flaten the source array
adults=ages[(ages>=18) & (ages<65)]
seniors=ages[ages>=65]
evens=ages[ages%2==0]


print(teenagers)


adults1=np.where(ages>=18,ages,0) # this used to preserve the original shape and 0 is used to fill in those values

print(adults1)