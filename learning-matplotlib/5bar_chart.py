import matplotlib.pyplot as plt
import numpy as np

categories=np.array(['grain','fruits','veges','protine','dairy','sweets'])
values=np.array([4,3,2,5,3,1])

plt.bar(categories,values,color='green')
#plt.barh(categories,values,color='green') this used to show horizontal bars in the chart

plt.title('daily consumptions')
plt.xlabel('food')
plt.ylabel('quantity')

plt.show()