import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay

border = "-" * 50

############################
# Step 1 : Load Dataset
############################

print(border)
print("Step 1 : Load Dataset")
print(border)

df = pd.read_csv("student_performance_ml.csv")

print("Dataset Loaded Successfully")
print(df.head())

############################
# Step 2 : Data Analysis
############################

print(border)
print("Step 2 : Data Analysis")
print(border)

print("Shape :", df.shape)
print("Columns :", list(df.columns))
print("Missing Values")
print(df.isnull().sum())

############################
# Step 3 : Visualization
############################

print(border)
print("Step 3 : Visualization")
print(border)

plt.hist(df["Study Hours"], edgecolor="black")
plt.title("Study Hours Histogram")
plt.xlabel("Study Hours")
plt.ylabel("Frequency")
plt.show()

############################
# Step 4 : Train-Test Split
############################

print(border)
print("Step 4 : Train Test Split")
print(border)

feature_cols = ["Study Hours","Attendance","Previous Score","Assignments Completed","Sleep Hours"]
X = df[feature_cols]
Y = df["Final Result"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

print("Training and Testing data created successfully.")

############################
# Step 5 : Train Model
############################

print(border)
print("Step 5 : Train Model")
print(border)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

print("Model Trained Successfully")

############################
# Step 6 : Prediction
############################

print(border)
print("Step 6 : Prediction")
print(border)

Y_pred = model.predict(X_test)

print("Actual Values")
print(Y_test.values)

print("Predicted Values")
print(Y_pred)

############################
# Step 7 : Accuracy
############################

print(border)
print("Step 7 : Accuracy")
print(border)

accuracy = accuracy_score(Y_test, Y_pred)

print("Accuracy = {:.2f}%".format(accuracy * 100))

############################
# Step 8 : Confusion Matrix
############################

print(border)
print("Step 8 : Confusion Matrix")
print(border)

ConfusionMatrixDisplay.from_estimator(model, X_test, Y_test)

plt.show()

############################
# Step 9 : Final Conclusion
############################

print(border)
print("Step 9 : Final Conclusion")
print(border)

print("Decision Tree model trained and evaluated successfully.")
print("Accuracy of the model is {:.2f}%".format(accuracy * 100))