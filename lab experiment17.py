# Mobile Price Prediction using Decision Tree Classifier

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Sample Dataset
data = {
    "RAM": [2, 3, 4, 4, 6, 6, 8, 8, 12, 12],
    "Storage": [32, 32, 64, 128, 128, 256, 256, 512, 512, 512],
    "Battery": [3000, 3500, 4000, 4500, 4500, 5000, 5000, 6000, 6000, 6500],
    "Price_Range": [
        "Low", "Low", "Medium", "Medium", "High",
        "High", "Premium", "Premium", "Premium", "Premium"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and Target
X = df[["RAM", "Storage", "Battery"]]
y = df["Price_Range"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.4,
    random_state=42,
    stratify=y
)

# Create Model
model = DecisionTreeClassifier(random_state=42)

# Train Model
model.fit(X_train, y_train)

# Predict Test Data
y_pred = model.predict(X_test)

# Display Results
print("========== Mobile Price Prediction ==========\n")

print("Actual Price Range:")
print(list(y_test))

print("\nPredicted Price Range:")
print(list(y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nAccuracy:")
print(round(accuracy_score(y_test, y_pred) * 100, 2), "%")

# Predict New Mobile Price Range
new_mobile = pd.DataFrame({
    "RAM": [8],
    "Storage": [256],
    "Battery": [5000]
})

prediction = model.predict(new_mobile)

print("\nPredicted Price Range for New Mobile:")
print(prediction[0])
