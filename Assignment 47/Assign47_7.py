from sklearn.linear_model import LinearRegression
import numpy as np

# Data
study_hours = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
marks = np.array([50, 55, 60, 65, 70])

# Train model
model = LinearRegression()
model.fit(study_hours, marks)

# Print coefficient and intercept
print("Coefficient: ", model.coef_[0])
print("Intercept: ", model.intercept_)