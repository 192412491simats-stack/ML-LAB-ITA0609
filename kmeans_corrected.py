from sklearn.cluster import KMeans
import numpy as np

X = np.array([
    [1,2],
    [2,3],
    [3,4],
    [10,10],
    [11,11],
    [12,12]
])

# Bug: Wrong number of clusters
kmeans = KMeans(n_clusters=2, random_state=0)

kmeans.fit(X)

print(kmeans.labels_)
