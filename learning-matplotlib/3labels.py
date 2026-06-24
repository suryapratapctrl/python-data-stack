import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])

y1 = np.array([15, 25, 30, 20])

y2 = np.array([17, 20, 38, 40])

y3 = np.array([7, 28, 18, 30])

plt.title("class size", fontsize=20, family="Arial", fontweight="bold", color="#2d4cfc")

plt.xlabel("Year" ,fontsize=20, family="Arial", fontweight="bold", color="#13dcf2")

plt.ylabel("Students" ,fontsize=20, family="Arial", fontweight="bold", color="#13dcf2")

plt.tick_params(axis='both',
                colors='blue')

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.xticks(x)

plt.show()
