import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("student_performance_ml.csv")

feature_cols = ["Study Hours","Attendance","Previous Score","Assignments Completed","Sleep Hours"]

X = df[feature_cols]
Y = df["Final Result"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

depths = [1,3,None]

for d in depths:

    model = DecisionTreeClassifier(max_depth=d, random_state=42)

    model.fit(X_train,Y_train)

    accuracy = model.score(X_test,Y_test)

    print("Max Depth = ",d," Accuracy = {:.2f}%".format(accuracy*100))