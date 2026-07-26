# Linear Regression

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load California Housing Dataset
housing = fetch_california_housing()
X = housing.data
y = housing.target

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Linear Regression Model
model = LinearRegression()

# Train the Model
model.fit(X_train, y_train)

# Predict Test Data
y_pred = model.predict(X_test)

# Display Results
print("First 10 Predicted Values:")
print(y_pred[:10])

print("\nMean Squared Error (MSE):")
print(mean_squared_error(y_test, y_pred))

print("\nR2 Score:")
print(r2_score(y_test, y_pred))
