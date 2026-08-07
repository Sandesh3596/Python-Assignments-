import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("student_performance_ml.csv")

feature_cols = ["Study Hours","Attendance","Previous Score","Assignments Completed","Sleep Hours"]

X = df[feature_cols]
Y = df["Final Result"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=42
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

student = pd.DataFrame([[6, 85, 66, 7, 7]], columns=feature_cols)

prediction = model.predict(student)

print("The Prediction is:", prediction[0])

if prediction[0] == 1:
    print("The student will Pass.")
else:
    print("The student will Fail.")