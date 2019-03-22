import numpy as np
from sklearn.cluster import KMeans

data = np.array([5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215])

data = data.reshape(-1, 1)

kmeans = KMeans(n_clusters=3).fit(data)

print(kmeans.labels_)