from sklearn.linear_model import LinearRegression
import numpy as np

# Data
X = np.array([
    [1, 7],
    [2, 6],
    [3, 7],
    [4, 6],
    [5, 8]
])
y = np.array([50, 55, 60, 65, 70])

# Train model
model = LinearRegression()
model.fit(X, y)

# Print coefficients and intercept
print("Coefficients (StudyHours, SleepHours):", model.coef_)
print("Intercept:", model.intercept_)