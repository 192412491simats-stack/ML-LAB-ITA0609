# Compare Linear Regression and Polynomial Regression

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# Sample Dataset
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([2, 5, 10, 17, 26, 37, 50, 65, 82, 101])

# Linear Regression
linear = LinearRegression()
linear.fit(X, y)
y_linear = linear.predict(X)

# Polynomial Regression (Degree = 2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly, y)
y_poly = poly_model.predict(X_poly)

# Display Results
print("Actual Values:")
print(y)

print("\nLinear Regression Predictions:")
print(y_linear)

print("\nPolynomial Regression Predictions:")
print(y_poly)

print("\nLinear Regression R2 Score:")
print(r2_score(y, y_linear))

print("\nPolynomial Regression R2 Score:")
print(r2_score(y, y_poly))
