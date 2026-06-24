import matplotlib.pyplot as plt
import numpy as np

scores =np.random.normal(loc=80,scale=10,size=100) 
scores=np.clip(scores,0,100)

plt.hist(scores,bins=10,
         color='lightgreen',
         edgecolor='black')


plt.title('exam scores')
plt.xlabel('scores')
plt.ylabel("# of students")

plt.show()


# Histogram:
# A histogram shows the distribution of numerical data.
# Instead of plotting each value individually, it groups values into ranges called bins.
# The x-axis represents the value ranges (bins).
# The y-axis represents the frequency (count) of values in each range.
# Taller bars mean more values fall within that range.
#
# np.random.normal(loc=80, scale=10, size=100):
# loc=80   -> mean (average) score is 80
# scale=10 -> standard deviation; controls how spread out the scores are
# size=100 -> generates 100 random scores
#
# np.clip(scores, 0, 100):
# Restricts all scores to the range 0-100.
# Values below 0 become 0 and values above 100 become 100.