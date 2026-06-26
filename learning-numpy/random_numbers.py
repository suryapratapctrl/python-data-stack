import numpy as np 

rng=np.random.default_rng() # we can set seed to produce same results

print(rng.integers(low=1,high=101,size=3))# second number is exclusive


#floating point number

print(np.random.uniform(low=-1,high=1,size=(3,2)))


array=np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)


fruits=np.array(['apple','orange','banana','coconut','pineapple'])
fruits=rng.choice(fruits,size=(3,3))
print(fruits)