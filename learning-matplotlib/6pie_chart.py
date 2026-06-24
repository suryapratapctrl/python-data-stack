import matplotlib.pyplot as plt


categories = ["freshmen", "sophomores", "juniors", "seniors"]
values = [300, 250, 275, 225]
colors = ["red", "yellow", "blue", "green"]

plt.pie(
    values,
    labels=categories,
    autopct="%1.1f%%",
    colors=colors,
    explode=[0, 0, 0, 0.1],
    shadow=True,
)  # autopct displays percentages on the pie chart and 1.1 means one digit after decimal

plt.title("collge name")

plt.show()
