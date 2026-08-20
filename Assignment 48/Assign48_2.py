import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Dataset
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)   
Y = np.array([3, 4, 2, 4, 5])

# --- Split into train/test sets ---
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.5, random_state=42
)

print("X_train:\n", X_train)
print("X_test:\n", X_test)
print("Y_train:", Y_train)
print("Y_test:", Y_test)

# --- Train model on training data only ---
model = LinearRegression()
model.fit(X_train, Y_train)

print("\nSlope (m):", model.coef_[0])
print("Intercept (c):", model.intercept_)

# --- Predict on test data ---
Y_pred = model.predict(X_test)
print("\nY_test (actual):", Y_test)
print("Y_pred (predicted):", Y_pred)

# --- Evaluate on test data ---
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)
print("\nMSE (on test data):", mse)
print("R2 Score (on test data):", r2)

# --- Predict for a new value
new_pred = model.predict([[6]])
print("\nPrediction for X=6:", new_pred[0])

