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

# Using the model trained above
hours_to_predict = np.array([[6]])
predicted_marks = model.predict(hours_to_predict)

print("Predicted marks for 6 study hours:", predicted_marks[0])