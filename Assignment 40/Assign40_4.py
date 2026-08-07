import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("student_performance_ml.csv")

feature_cols = ["Study Hours","Attendance","Previous Score","Assignments Completed","Sleep Hours"]

X = df[feature_cols]
Y = df["Final Result"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

students = pd.DataFrame([
    [6,85,66,7,7],
    [8,90,80,9,8],
    [4,70,55,5,6],
    [5,75,60,6,7],
    [7,88,78,8,8]
], columns=feature_cols)

prediction = model.predict(students)

students["Prediction"] = prediction

print(students)