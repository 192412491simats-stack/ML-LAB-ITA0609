# House Price Prediction using Linear Regression

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample Dataset
data = {
    "Area": [1000,1200,1500,1800,2000,2200,2500,2800,3000,3500],
    "Bedrooms": [2,2,3,3,3,4,4,4,5,5],
    "Age": [15,12,10,8,7,5,4,3,2,1],
    "Price": [2000000,2500000,3000000,3500000,4000000,
              4500000,5000000,5500000,6000000,7000000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and Target
X = df[["Area", "Bedrooms", "Age"]]
y = df["Price"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Model
model = LinearRegression()

# Train Model
model.fit(X_train, y_train)

# Predict Test Data
y_pred = model.predict(X_test)

# Display Results
print("========== House Price Prediction ==========\n")

print("Actual Prices:")
print(y_test.values)

print("\nPredicted Prices:")
print(y_pred)

print("\nMean Squared Error:")
print(mean_squared_error(y_test, y_pred))

print("\nR2 Score:")
print(r2_score(y_test, y_pred))

# Predict Price for New House
new_house = pd.DataFrame({
    "Area": [2400],
    "Bedrooms": [4],
    "Age": [3]
})

predicted_price = model.predict(new_house)

print("\nPredicted Price for New House:")
print(round(predicted_price[0], 2))
