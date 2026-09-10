import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

Border = "=" * 75
#--------------------------------
# 1. Read the Data from CSV
#--------------------------------

print("1. Read the Data from CSV")

data = pd.read_csv("Employee_Attrition.csv")

print("Complete Dataset: ")
print(data)

print(Border)
#--------------------------------
# 2. Data Analysis
#--------------------------------

print("2. Data Analysis")

print("First 5 Rows: ")
print(data.head())

print("Column Names: ")
print(data.columns)

print("Shape of Dataset: ")
print(data.shape)

print("Statistical Summary: ")
print(data.describe())

print("Dataset Information: ")
print(data.info())
print(Border)

#--------------------------------
# 3. Check Missing Values
#--------------------------------

print("3. Check Missing Values")

print(data.isnull().sum())
print(Border)

#--------------------------------
# 4. Convert Categorical Features
#--------------------------------

print("4. Convert Categorical Features")

# OverTime : Yes/No
data["OverTime"] = data["OverTime"].map(
    {
        "Yes": 1,
        "No": 0
    }
)

# Attrition : Yes/No -> Target
data["Attrition"] = data["Attrition"].map(
    {
        "Yes": 1,
        "No": 0
    }
)

print("Dataset After Conversion: ")
print(data.head())

print(Border)
#--------------------------------
# 5. Define Input and Target Data
#--------------------------------

print("5. Define Input and Target Data")

X = data[
    [
        "Age",
        "MonthlyIncome",
        "YearsAtCompany",
        "TotalWorkingYears",
        "DistanceFromHome",
        "JobSatisfaction",
        "WorkLifeBalance",
        "OverTime",
        "NumCompaniesWorked",
        "TrainingTimesLastYear"
    ]
]

Y = data["Attrition"]

print("Input Features: ")
print(X.head())

print("Target Data: ")
print(Y.head())
print(Border)

#--------------------------------
# 6. Train Test Split
#--------------------------------

print("6. Train Test Split")

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.3,
    random_state=42
)

print("Training Input Shape: ", X_train.shape)
print("Testing Input Shape: ", X_test.shape)

print("Training Output Shape: ", Y_train.shape)
print("Testing Output Shape: ", Y_test.shape)
print(Border)

#--------------------------------
# 7. Feature Scaling
#--------------------------------

print("7. Feature Scaling")

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)

# Important:
# Use transform() for testing data
# Do not use fit_transform() on test data
X_test_scaled = scalar.transform(X_test)

print("Scaled Training Data: ")
print(X_train_scaled[:5])
print(Border)

#--------------------------------
# 8. MLP Model Training
#--------------------------------

print("8. MLP Model Training")

model = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

print(model)

print("Train the Model")

model.fit(X_train_scaled, Y_train)

print("Model Training Completed")
print(Border)

#--------------------------------
# 9. Model Evaluation
#--------------------------------

print("9. Model Evaluation")

Y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(Y_test, Y_pred)

print("Accuracy is: ", accuracy)

cm = confusion_matrix(Y_test, Y_pred)

print("Confusion Matrix: ")
print(cm)
print(Border)

#--------------------------------
# 10. Display Confusion Matrix
#--------------------------------

print("10. Display Confusion Matrix")

plt.imshow(cm)

plt.title("Employee Attrition Confusion Matrix")

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.xticks([0, 1], ["No Attrition", "Attrition"])

plt.yticks([0, 1], ["No Attrition", "Attrition"])

plt.colorbar()

plt.show()
print(Border)

#--------------------------------
# 11. Predict the Probability
#--------------------------------

print("11. Predict the Probability")

Y_prob = model.predict_proba(X_test_scaled)

print(Y_prob[:5])
print(Border)

#--------------------------------
# 12. Model Preserve
#--------------------------------

print("12. Model Preserve")

joblib.dump(
    model,
    "employee_attrition_mlp_model.pkl"
)

joblib.dump(
    scalar,
    "employee_attrition_scalar.pkl"
)

print("Model & Scalar gets dumped successfully")
print(Border)

#--------------------------------
# 13. Model Loading
#--------------------------------

print("13. Model Loading")

loaded_model = joblib.load(
    "employee_attrition_mlp_model.pkl"
)

loaded_scalar = joblib.load(
    "employee_attrition_scalar.pkl"
)

print("Model gets loaded successfully")
print(Border)

#--------------------------------
# 14. Test Unseen Data
#
# Age:                     30
# MonthlyIncome:           50000
# YearsAtCompany:          3
# TotalWorkingYears:       5
# DistanceFromHome:        10
# JobSatisfaction:         3
# WorkLifeBalance:         3
# OverTime:                1
# NumCompaniesWorked:      2
# TrainingTimesLastYear:   3
#--------------------------------

print("14. Test Unseen Data")


new_employee = pd.DataFrame(
    [
        [
            30,
            50000,
            3,
            5,
            10,
            3,
            3,
            1,
            2,
            3
        ]
    ],

    columns=[
        "Age",
        "MonthlyIncome",
        "YearsAtCompany",
        "TotalWorkingYears",
        "DistanceFromHome",
        "JobSatisfaction",
        "WorkLifeBalance",
        "OverTime",
        "NumCompaniesWorked",
        "TrainingTimesLastYear"
    ]
)


print("New Employee Data: ")

print(new_employee)
print(Border)

#--------------------------------
# 15. Scale Unseen Data
#--------------------------------

new_employee_scaled = loaded_scalar.transform(
    new_employee
)
print(Border)

#--------------------------------
# 16. Predict Unseen Data
#--------------------------------

new_pred = loaded_model.predict(
    new_employee_scaled
)
print(Border)

#--------------------------------
# 17. Predict Probability
#--------------------------------

new_prob = loaded_model.predict_proba(
    new_employee_scaled
)

print("Prediction Probability: ")

print(new_prob)
print(Border)

#--------------------------------
# 18. Display Final Prediction
#--------------------------------

if new_pred[0] == 1:

    print(
        "Prediction: Employee is likely to leave the company"
    )

else:

    print(
        "Prediction: Employee is likely to stay in the company"
    )
print(Border)

#--------------------------------
# 19. Explanation
#--------------------------------

print(
    "This MLPClassifier model predicts employee attrition "
    "based on employee age, income, experience, distance "
    "from home, job satisfaction, work-life balance, "
    "overtime and training history."
)
print(Border)