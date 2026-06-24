import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])

y1 = np.array(
    [15, 25, 30, 20]
)  # here we are using numpy array Because Matplotlib works much better with numerical data stored as NumPy arrays

y2 = np.array([17, 20, 38, 40])

y3 = np.array([7, 28, 18, 30])

line_style = dict(
    marker=".",
    ms=20,  # here ms is markersize
    markerfacecolor="cyan",  # we can also use hex code also
    markeredgecolor="cyan",
    linestyle="solid",
    linewidth=3,
)

plt.plot(
    x,
    y1,
    marker=".",
    ms=20,
    markerfacecolor="cyan",
    markeredgecolor="cyan",
    linestyle="solid",
    linewidth=3,
    color="#05f6f6",
)


plt.plot(x, y2, color="#f6ee05", **line_style)

plt.plot(x, y3, color="#05f631", **line_style)


plt.show()
