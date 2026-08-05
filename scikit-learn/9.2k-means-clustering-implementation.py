import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

# Step 1: Load the preloaded Iris dataset
iris = load_iris()

# Step 2: Create a DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Step 3: Select two features for clustering
X = df[['petal length (cm)', 'petal width (cm)']]

# Step 4: Create the K-Means model
model = KMeans(n_clusters=3, random_state=42, n_init=10)

# Step 5: Train the model and predict clusters
df['Cluster'] = model.fit_predict(X)

# Step 6: Get centroids
centroids = model.cluster_centers_

# Step 7: Plot the clusters
plt.figure(figsize=(7,5))

for cluster in df['Cluster'].unique():
    cluster_data = df[df['Cluster'] == cluster]
    plt.scatter(cluster_data['petal length (cm)'],
                cluster_data['petal width (cm)'],
                label=f'Cluster {cluster}')

# Plot centroids
plt.scatter(centroids[:,0], centroids[:,1], # Take all rows from column 0 & 1
            marker='X',
            s=200,
            color='black',
            label='Centroids')

plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("K-Means Clustering on Iris Dataset")
plt.legend()
plt.grid(True)
plt.show()

# Display first 10 rows
print(df.head(10))

# The best value of K is chosen using the Elbow Method,
# where the graph forms an "elbow" (a sharp bend),
# indicating that adding more clusters gives only a small improvement.

