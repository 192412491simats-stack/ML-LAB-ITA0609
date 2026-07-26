import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample Dataset
data = {
    "Year": [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024],
    "Kilometers_Driven": [80000,70000,60000,50000,40000,30000,25000,20000,15000,10000],
    "Price": [500000,550000,600000,650000,700000,750000,800000,850000,900000,950000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and Target
X = df[["Year", "Kilometers_Driven"]]
y = df["Price"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction on Test Data
y_pred = model.predict(X_test)

print("===== Car Price Prediction =====")

print("\nActual Prices:")
print(y_test.values)

print("\nPredicted Prices:")
print(y_pred)

print("\nMean Squared Error:")
print(mean_squared_error(y_test, y_pred))

print("\nR2 Score:")
print(r2_score(y_test, y_pred))

# Predict New Car Price
new_car = pd.DataFrame({
    "Year": [2022],
    "Kilometers_Driven": [18000]
})

predicted_price = model.predict(new_car)

print("\nPredicted Price for New Car:")
print(round(predicted_price[0], 2))
