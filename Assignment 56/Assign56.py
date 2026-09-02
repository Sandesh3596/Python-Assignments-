import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier

#---------------------------------------
# Step 1 : Load the dataset
#---------------------------------------

df = pd.read_csv("Fraudulent_Transaction_Detection.csv")

print("Shape of dataset : ", df.shape)

print("First few records : ")
print(df.head())

#---------------------------------------
# Step 2 : Check for missing values
#---------------------------------------

print("Missing values : ")
print(df.isnull().sum())

#---------------------------------------
# Step 3 : Encode categorical variables
#---------------------------------------

encoder = LabelEncoder()

for column in df.columns:
    if df[column].dtype == "object":
        df[column] = encoder.fit_transform(df[column])

#---------------------------------------
# Step 4 : Separate features and labels
#---------------------------------------

X = df.drop("Fraud", axis=1)
Y = df["Fraud"]

print("X shape : ", X.shape)
print("Y shape : ", Y.shape)

#---------------------------------------
# Step 5 : Split dataset for training and testing
#---------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(
                                            X,
                                            Y,
                                            test_size=0.2,
                                            random_state=42
                                            )

#---------------------------------------
# Step 6 : Create Decision Tree
#---------------------------------------

model_det = DecisionTreeClassifier(random_state=42)

model_det.fit(X_train, Y_train)

Y_pred_det = model_det.predict(X_test)

#---------------------------------------
# Step 7 : Create Bagging Classifier
#---------------------------------------

model_bag = BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=10,
    random_state=42
)

model_bag.fit(X_train, Y_train)

Y_pred_bag = model_bag.predict(X_test)

#---------------------------------------
# Step 8 : Create Random Forest Classifier
#---------------------------------------

model_rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model_rf.fit(X_train, Y_train)

Y_pred_rf = model_rf.predict(X_test)

#---------------------------------------
# Step 9 : Create AdaBoost Classifier
#---------------------------------------

model_ada = AdaBoostClassifier(
    n_estimators=50,
    random_state=42
)

model_ada.fit(X_train, Y_train)

Y_pred_ada = model_ada.predict(X_test)

#---------------------------------------
# Step 10 : Create Voting Classifier
#---------------------------------------

model_vote = VotingClassifier(
    estimators=[
        ('decision_tree', DecisionTreeClassifier(random_state=42)),
        ('random_forest', RandomForestClassifier(n_estimators=100, random_state=42)),
        ('adaboost', AdaBoostClassifier(n_estimators=50, random_state=42))
    ],
    voting='hard'
)

model_vote.fit(X_train, Y_train)

Y_pred_vote = model_vote.predict(X_test)

#---------------------------------------
# Step 11 : Calculate Accuracy
#---------------------------------------

accuracy_det = accuracy_score(Y_test, Y_pred_det)

accuracy_bag = accuracy_score(Y_test, Y_pred_bag)

accuracy_rf = accuracy_score(Y_test, Y_pred_rf)

accuracy_ada = accuracy_score(Y_test, Y_pred_ada)

accuracy_vote = accuracy_score(Y_test, Y_pred_vote)

print("Decision Tree Accuracy : ", accuracy_det)

print("Bagging Accuracy : ", accuracy_bag)

print("Random Forest Accuracy : ", accuracy_rf)

print("AdaBoost Accuracy : ", accuracy_ada)

print("Voting Accuracy : ", accuracy_vote)

#---------------------------------------
# Step 12 : Calculate Precision
#---------------------------------------

precision_det = precision_score(Y_test, Y_pred_det, zero_division=0)

precision_bag = precision_score(Y_test, Y_pred_bag, zero_division=0)

precision_rf = precision_score(Y_test, Y_pred_rf, zero_division=0)

precision_ada = precision_score(Y_test, Y_pred_ada, zero_division=0)

precision_vote = precision_score(Y_test, Y_pred_vote, zero_division=0)

#---------------------------------------
# Step 13 : Calculate Recall
#---------------------------------------

recall_det = recall_score(Y_test, Y_pred_det, zero_division=0)

recall_bag = recall_score(Y_test, Y_pred_bag, zero_division=0)

recall_rf = recall_score(Y_test, Y_pred_rf, zero_division=0)

recall_ada = recall_score(Y_test, Y_pred_ada, zero_division=0)

recall_vote = recall_score(Y_test, Y_pred_vote, zero_division=0)

#---------------------------------------
# Step 14 : Calculate F1 Score
#---------------------------------------

f1_det = f1_score(Y_test, Y_pred_det, zero_division=0)

f1_bag = f1_score(Y_test, Y_pred_bag, zero_division=0)

f1_rf = f1_score(Y_test, Y_pred_rf, zero_division=0)

f1_ada = f1_score(Y_test, Y_pred_ada, zero_division=0)

f1_vote = f1_score(Y_test, Y_pred_vote, zero_division=0)

#---------------------------------------
# Step 15 : Display Model Comparison
#---------------------------------------

print("\nModel Comparison")

print("Decision Tree : ")
print("Accuracy  : ", accuracy_det)
print("Precision : ", precision_det)
print("Recall    : ", recall_det)
print("F1 Score  : ", f1_det)

print("\nBagging : ")
print("Accuracy  : ", accuracy_bag)
print("Precision : ", precision_bag)
print("Recall    : ", recall_bag)
print("F1 Score  : ", f1_bag)

print("\nRandom Forest : ")
print("Accuracy  : ", accuracy_rf)
print("Precision : ", precision_rf)
print("Recall    : ", recall_rf)
print("F1 Score  : ", f1_rf)

print("\nAdaBoost : ")
print("Accuracy  : ", accuracy_ada)
print("Precision : ", precision_ada)
print("Recall    : ", recall_ada)
print("F1 Score  : ", f1_ada)

print("\nVoting : ")
print("Accuracy  : ", accuracy_vote)
print("Precision : ", precision_vote)
print("Recall    : ", recall_vote)
print("F1 Score  : ", f1_vote)

#---------------------------------------
# Step 16 : Confusion Matrix
#---------------------------------------

print("\nDecision Tree Confusion Matrix : ")
print(confusion_matrix(Y_test, Y_pred_det))

print("\nBagging Confusion Matrix : ")
print(confusion_matrix(Y_test, Y_pred_bag))

print("\nRandom Forest Confusion Matrix : ")
print(confusion_matrix(Y_test, Y_pred_rf))

print("\nAdaBoost Confusion Matrix : ")
print(confusion_matrix(Y_test, Y_pred_ada))

print("\nVoting Confusion Matrix : ")
print(confusion_matrix(Y_test, Y_pred_vote))