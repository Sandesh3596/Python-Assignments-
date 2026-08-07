import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("student_performance_ml.csv")

feature_cols = ["Study Hours","Attendance","Previous Score","Assignments Completed","Sleep Hours"]

X = df[feature_cols]
Y = df["Final Result"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train,Y_train)

importance = model.feature_importances_

for feature,value in zip(feature_cols,importance):
    print(feature,"=",value)

print("Most Important Feature :",feature_cols[importance.argmax()])

print("Least Important Feature :",feature_cols[importance.argmin()])