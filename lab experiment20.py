# Future Sales Prediction using Linear Regression

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample Dataset
data = {
    "Month": [1,2,3,4,5,6,7,8,9,10,11,12],
    "Sales": [120,135,150,165,180,195,210,225,240,255,270,285]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and Target
X = df[["Month"]]
y = df["Sales"]

# Create Model
model = LinearRegression()

# Train Model
model.fit(X, y)

# Predict Existing Sales
y_pred = model.predict(X)

# Display Results
print("========== Future Sales Prediction ==========\n")

print("Actual Sales:")
print(list(y))

print("\nPredicted Sales:")
print([round(value, 2) for value in y_pred])

print("\nMean Squared Error:")
print(round(mean_squared_error(y, y_pred), 2))

print("\nR2 Score:")
print(round(r2_score(y, y_pred), 2))

# Predict Future Sales
future_month = pd.DataFrame({"Month": [13]})

future_sales = model.predict(future_month)

print("\nPredicted Sales for Month 13:")
print(round(future_sales[0], 2))
