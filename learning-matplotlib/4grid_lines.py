import matplotlib.pyplot as plt

#grid() = helps make plots easier to read by adding reference lines

x=[1,2,3,4,5]

y=[5,10,15,20,25]

plt.grid(linewidth=1,color="blue",linestyle="dotted")

plt.plot(x,y)
plt.show()