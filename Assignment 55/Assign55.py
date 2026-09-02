import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

#---------------------------------------
# Step 1 : Load the dataset
#---------------------------------------

df = pd.read_csv("Customer_Loan_Approval.csv")

print("Shape of dataset : ", df.shape)

print("First few records : ")
print(df.head())

#---------------------------------------
# Step 2 : Check for missing values
#---------------------------------------

print("Missing values : ")
print(df.isnull().sum())

#---------------------------------------
# Step 3 : Separate input and output variables
#---------------------------------------

X = df.drop("LoanApproved", axis=1)
Y = df["LoanApproved"]

print("X shape : ", X.shape)
print("Y shape : ", Y.shape)

#---------------------------------------
# Step 4 : Split dataset into training and testing data
#---------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(
                                            X,
                                            Y,
                                            test_size=0.2,
                                            random_state=42
                                            )

#---------------------------------------
# Step 5 : Train Logistic Regression
#---------------------------------------

scalar = StandardScaler()

X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

model_log = LogisticRegression(max_iter=1000)

model_log.fit(X_train, Y_train)

Y_pred_log = model_log.predict(X_test)

#---------------------------------------
# Step 6 : Train Decision Tree
#---------------------------------------

model_det = DecisionTreeClassifier(random_state=42)

model_det.fit(X_train, Y_train)

Y_pred_det = model_det.predict(X_test)

#---------------------------------------
# Step 7 : Train KNN
#---------------------------------------

model_knn = KNeighborsClassifier(n_neighbors=5)

model_knn.fit(X_train, Y_train)

Y_pred_knn = model_knn.predict(X_test)

#---------------------------------------
# Step 8 : Calculate individual accuracy
#---------------------------------------

accuracy_log = accuracy_score(Y_test, Y_pred_log)

accuracy_det = accuracy_score(Y_test, Y_pred_det)

accuracy_knn = accuracy_score(Y_test, Y_pred_knn)

print("Logistic Regression Accuracy : ", accuracy_log)

print("Decision Tree Accuracy : ", accuracy_det)

print("KNN Accuracy : ", accuracy_knn)

#---------------------------------------
# Step 9 : Create Hard Voting Classifier
#---------------------------------------

model_hard = VotingClassifier(
    estimators=[
        ('logistic', LogisticRegression(max_iter=1000)),
        ('decision_tree', DecisionTreeClassifier(random_state=42)),
        ('knn', KNeighborsClassifier(n_neighbors=5))
    ],
    voting='hard'
)

#---------------------------------------
# Step 10 : Calculate Hard Voting accuracy
#---------------------------------------

model_hard.fit(X_train, Y_train)

Y_pred_hard = model_hard.predict(X_test)

accuracy_hard = accuracy_score(Y_test, Y_pred_hard)

print("Hard Voting Accuracy : ", accuracy_hard)

#---------------------------------------
# Step 11 : Create Soft Voting Classifier
#---------------------------------------

model_soft = VotingClassifier(
    estimators=[
        ('logistic', LogisticRegression(max_iter=1000)),
        ('decision_tree', DecisionTreeClassifier(random_state=42)),
        ('knn', KNeighborsClassifier(n_neighbors=5))
    ],
    voting='soft'
)

#---------------------------------------
# Step 12 : Calculate Soft Voting accuracy
#---------------------------------------

model_soft.fit(X_train, Y_train)

Y_pred_soft = model_soft.predict(X_test)

accuracy_soft = accuracy_score(Y_test, Y_pred_soft)

print("Soft Voting Accuracy : ", accuracy_soft)

#---------------------------------------
# Step 13 : Compare all models
#---------------------------------------

print("\nModel Accuracy Comparison")

print("Logistic Regression : ", accuracy_log)

print("Decision Tree       : ", accuracy_det)

print("KNN                 : ", accuracy_knn)

print("Hard Voting         : ", accuracy_hard)

print("Soft Voting         : ", accuracy_soft)