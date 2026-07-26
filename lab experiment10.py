# Expectation Maximization (EM) Algorithm

from sklearn.datasets import load_iris
from sklearn.mixture import GaussianMixture
from sklearn.metrics import accuracy_score
import numpy as np

# Load Iris Dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create Gaussian Mixture Model
model = GaussianMixture(n_components=3, random_state=42)

# Train the Model
model.fit(X)

# Predict Cluster Labels
y_pred = model.predict(X)

# Map Clusters to Actual Labels
labels = np.zeros_like(y_pred)
for i in range(3):
    mask = (y_pred == i)
    labels[mask] = np.bincount(y[mask]).argmax()

# Display Results
print("Predicted Labels:")
print(labels)

print("\nActual Labels:")
print(y)

print("\nAccuracy:")
print(accuracy_score(y, labels))
