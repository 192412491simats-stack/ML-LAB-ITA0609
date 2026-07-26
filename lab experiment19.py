# Bank Loan Prediction using Naive Bayes

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Sample Dataset
data = {
    "Age": [25,35,45,23,52,40,60,48,33,29,31,55,42,27,38],
    "Income": [30000,50000,70000,25000,90000,65000,100000,85000,45000,38000,42000,95000,68000,32000,55000],
    "LoanAmount": [5000,10000,15000,3000,20000,12000,25000,18000,8000,6000,7000,22000,14000,4000,11000],
    "LoanApproved": [
        "No","Yes","Yes","No","Yes",
        "Yes","Yes","Yes","No","No",
        "No","Yes","Yes","No","Yes"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and Target
X = df[["Age", "Income", "LoanAmount"]]
y = df["LoanApproved"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# Create Model
model = GaussianNB()

# Train Model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Display Results
print("========== Bank Loan Prediction ==========\n")

print("Actual Values:")
print(list(y_test))

print("\nPredicted Values:")
print(list(y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")

# Predict New Customer
new_customer = pd.DataFrame({
    "Age": [35],
    "Income": [60000],
    "LoanAmount": [10000]
})

prediction = model.predict(new_customer)

print("\nLoan Prediction for New Customer:")
print(prediction[0])
