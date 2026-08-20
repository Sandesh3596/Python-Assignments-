import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Dataset
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
Y = np.array([20000, 25000, 30000, 35000, 40000])

# --- Split into train/test sets ---
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
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
Y_pred_test = model.predict(X_test)
print("\nY_test (actual):", Y_test)
print("Y_pred (predicted):", Y_pred_test)

# --- Evaluate on test data ---
mse = mean_squared_error(Y_test, Y_pred_test)
r2 = r2_score(Y_test, Y_pred_test)
print("\nMSE (on test data):", mse)
print("R2 Score (on test data):", r2)

# --- Predict salary for 6 years experience ---
pred_6 = model.predict([[6]])
print("\nPredicted salary for 6 years experience:", pred_6[0])

# --- Plot ---
plt.scatter(X_train, Y_train, color='blue', label='Training data')
plt.scatter(X_test, Y_test, color='orange', label='Testing data', s=100, marker='o')
x_line = np.linspace(1, 6, 100).reshape(-1, 1)
plt.plot(x_line, model.predict(x_line), color='red', label='Regression line')
plt.scatter([6], pred_6, color='green', s=150,
            label=f'Prediction (6 yrs) = {pred_6[0]:.0f}')
plt.xlabel('Experience (years)')
plt.ylabel('Salary')
plt.title('Salary vs Experience - Train/Test Split')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()