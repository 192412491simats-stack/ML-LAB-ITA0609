import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Sample Dataset
data = {
    "Age": [25,35,45,23,52,40,60,48,33,29,31,55,42,27,38],
    "Income": [30000,50000,70000,25000,90000,65000,100000,85000,45000,38000,42000,95000,68000,32000,55000],
    "Loan": [5000,10000,15000,3000,20000,12000,25000,18000,8000,6000,7000,22000,14000,4000,11000],
    "CreditScore": [
        "Low","Medium","High","Low","High",
        "High","High","High","Medium","Low",
        "Medium","High","High","Low","Medium"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and Target
X = df[["Age", "Income", "Loan"]]
y = df["CreditScore"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# Train Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Results
print("Actual Values:")
print(list(y_test))

print("\nPredicted Values:")
print(list(y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))
