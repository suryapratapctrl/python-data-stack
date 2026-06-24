import matplotlib.pyplot as plt
import numpy as np

# scatter graphs helps to show relationship between two variables
# to identify a  correlation between them is positive or negative

x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8]) #hours studied
y1 = np.array([55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87]) # grades

x2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
y2 = np.array([20, 28, 35, 40, 47, 55, 62, 70, 76, 83, 90])


plt.scatter(x1, y1, color="blue", alpha=0.7, s=200, label="class A")

plt.scatter(x2, y2, color="RED", alpha=0.7, s=200, label="class B")

plt.title("test scores")
plt.xlabel("hours studied")
plt.ylabel("grade")
plt.legend()
plt.show()