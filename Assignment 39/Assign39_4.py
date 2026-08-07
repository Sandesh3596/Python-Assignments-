import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import ConfusionMatrixDisplay

df = pd.read_csv("student_performance_ml.csv")

feature_cols = ["Study Hours","Attendance","Previous Score","Assignments Completed","Sleep Hours"]

X = df[feature_cols]
Y = df["Final Result"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

ConfusionMatrixDisplay.from_estimator(model, X_test, Y_test)

plt.show()