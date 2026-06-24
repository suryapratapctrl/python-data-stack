import matplotlib.pyplot as plt

import pandas as pd


df = pd.read_csv("pokemon.csv")


type_count = df["Type1"].value_counts(ascending=True)

plt.barh(type_count.index, type_count.values, color="lightgreen", edgecolor="black")

plt.title("# of pokemon by primary type")
plt.xlabel("count")
plt.ylabel("type")
plt.tight_layout()
plt.show()
