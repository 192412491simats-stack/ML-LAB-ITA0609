# Iris Flower Classification using Naive Bayes

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load Iris Dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Naive Bayes Model
model = GaussianNB()

# Train Model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Display Results
print("========== Iris Flower Classification using Naive Bayes ==========\n")

print("Actual Values:")
print(y_test)

print("\nPredicted Values:")
print(y_pred)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
