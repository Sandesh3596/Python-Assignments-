import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)

Border = "=" * 70


# ==============================================================
# 1. Load and Understand the Dataset
# ==============================================================

print("1. Load and Understand the Dataset")

data = pd.read_csv("Loan_Default.csv")

print("Complete Dataset:")
print(data)

print("First 5 Rows:")
print(data.head())

print("Column Names:")
print(data.columns)

print("Shape of Dataset:")
print(data.shape)

print(Border)


# ==============================================================
# 2. Perform Exploratory Analysis
# ==============================================================

print("2. Perform Exploratory Analysis")

print("Statistical Summary:")
print(data.describe())

print("Dataset Information:")
data.info()

print(Border)


# ==============================================================
# 3. Find Missing Values
# ==============================================================

print("3. Find Missing Values")

print(data.isnull().sum())

print(Border)


# ==============================================================
# 4. Check Whether the Target Classes are Balanced
# ==============================================================

print("4. Check Whether the Target Classes are Balanced")

print("Default Class Distribution:")
print(data["Default"].value_counts())

print("Default Class Percentage:")
print(data["Default"].value_counts(normalize=True) * 100)

print(Border)


# ==============================================================
# 5. Encode Categorical Variables
# ==============================================================

print("5. Encode Categorical Variables")

data["PreviousDefault"] = data["PreviousDefault"].map({
    "Yes": 1,
    "No": 0
})

data["HomeOwnership"] = data["HomeOwnership"].map({
    "Rent": 0,
    "Own": 1,
    "Mortgage": 2
})

print("Dataset After Encoding:")
print(data.head())

print(Border)


# ==============================================================
# 6. Separate X and y
# ==============================================================

print("6. Separate X and y")

X = data[
    [
        "Age",
        "Income",
        "LoanAmount",
        "CreditScore",
        "EmploymentYears",
        "ExistingLoans",
        "MonthlyDebt",
        "LoanTerm",
        "PreviousDefault",
        "HomeOwnership"
    ]
]

y = data["Default"]

print("Input Features:")
print(X.head())

print("Target Data:")
print(y.head())

print(Border)


# ==============================================================
# 7. Split the Dataset into Training and Testing Data
# ==============================================================

print("7. Split the Dataset into Training and Testing Data")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

print("Training Input Shape:", X_train.shape)
print("Testing Input Shape:", X_test.shape)

print("Training Target Shape:", y_train.shape)
print("Testing Target Shape:", y_test.shape)

print(Border)


# ==============================================================
# 8. Explain Whether Stratified Splitting Should be Used
# ==============================================================

print("8. Explain Whether Stratified Splitting Should be Used")

print(
    "Stratified splitting should be used because it maintains "
    "the same proportion of Default classes in both training "
    "and testing datasets."
)

print(Border)


# ==============================================================
# 9. Scale the Features
# ==============================================================

print("9. Scale the Features")

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

print("Scaled Training Data:")
print(X_train_scaled[:5])

print(Border)


# ==============================================================
# 10. Create an MLPClassifier
# ==============================================================

print("10. Create an MLPClassifier")

model = MLPClassifier(
    hidden_layer_sizes=(32, 16),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

print(model)

print(Border)


# ==============================================================
# 11. Train the Model
# ==============================================================

print("11. Train the Model")

model.fit(
    X_train_scaled,
    y_train
)

print("Model Training Completed")

print(Border)


# ==============================================================
# 12. Calculate Accuracy
# ==============================================================

print("12. Calculate Accuracy")

y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("Accuracy:", accuracy)

print(Border)


# ==============================================================
# 13. Generate the Confusion Matrix
# ==============================================================

print("13. Generate the Confusion Matrix")

cm = confusion_matrix(
    y_test,
    y_pred
)

print("Confusion Matrix:")
print(cm)

print(Border)


# ==============================================================
# 14. Generate the Classification Report
# ==============================================================

print("14. Generate the Classification Report")

report = classification_report(
    y_test,
    y_pred
)

print("Classification Report:")
print(report)

print(Border)


# ==============================================================
# 15. Calculate Precision, Recall and F1-Score
# ==============================================================

print("15. Calculate Precision, Recall and F1-Score")

precision = precision_score(
    y_test,
    y_pred
)

recall = recall_score(
    y_test,
    y_pred
)

f1 = f1_score(
    y_test,
    y_pred
)

print("Precision:", precision)
print("Recall:", recall)
print("F1-Score:", f1)

print(Border)


# ==============================================================
# 16. Plot Training Loss
# ==============================================================

print("16. Plot Training Loss")

plt.plot(
    model.loss_curve_
)

plt.title("MLP Training Loss Curve")
plt.xlabel("Iterations")
plt.ylabel("Loss")

plt.show()

print(Border)


# ==============================================================
# 17. Test the Model on New / Unseen Data
# ==============================================================

print("17. Test the Model on New / Unseen Data")

new_customer = pd.DataFrame(
    [
        [
            35,
            600000,
            400000,
            700,
            10,
            2,
            20000,
            36,
            "No",
            "Rent"
        ]
    ],
    columns=[
        "Age",
        "Income",
        "LoanAmount",
        "CreditScore",
        "EmploymentYears",
        "ExistingLoans",
        "MonthlyDebt",
        "LoanTerm",
        "PreviousDefault",
        "HomeOwnership"
    ]
)

new_customer["PreviousDefault"] = new_customer[
    "PreviousDefault"
].map({
    "Yes": 1,
    "No": 0
})

new_customer["HomeOwnership"] = new_customer[
    "HomeOwnership"
].map({
    "Rent": 0,
    "Own": 1,
    "Mortgage": 2
})

print("New Customer Data:")
print(new_customer)

new_customer_scaled = scaler.transform(
    new_customer
)

new_prediction = model.predict(
    new_customer_scaled
)

print("Prediction:")

if new_prediction[0] == 0:

    print("0 -> Low default risk")

else:

    print("1 -> High default risk")

print(Border)


# ==============================================================
# Hyperparameter Experiment 1 - Activation
# ==============================================================

print("Hyperparameter Experiment 1 - Activation")

activation_values = [
    "identity",
    "logistic",
    "tanh",
    "relu"
]

for activation in activation_values:

    model_activation = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation=activation,
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    model_activation.fit(
        X_train_scaled,
        y_train
    )

    prediction = model_activation.predict(
        X_test_scaled
    )

    accuracy = accuracy_score(
        y_test,
        prediction
    )

    print(
        "Activation:",
        activation,
        "Accuracy:",
        accuracy
    )

print(Border)


# ==============================================================
# Hyperparameter Experiment 2 - Hidden Layers
# ==============================================================

print("Hyperparameter Experiment 2 - Hidden Layers")

hidden_layer_values = [
    (10,),
    (20, 10),
    (50, 25),
    (100, 50, 25)
]

for hidden_layers in hidden_layer_values:

    model_hidden = MLPClassifier(
        hidden_layer_sizes=hidden_layers,
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    model_hidden.fit(
        X_train_scaled,
        y_train
    )

    prediction = model_hidden.predict(
        X_test_scaled
    )

    accuracy = accuracy_score(
        y_test,
        prediction
    )

    print(
        "Hidden Layers:",
        hidden_layers,
        "Accuracy:",
        accuracy
    )

print(Border)


# ==============================================================
# Hyperparameter Experiment 3 - Learning Rate
# ==============================================================

print("Hyperparameter Experiment 3 - Learning Rate")

learning_rates = [
    0.0001,
    0.001,
    0.01,
    0.1
]

for learning_rate in learning_rates:

    model_learning = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation="relu",
        solver="adam",
        learning_rate_init=learning_rate,
        max_iter=1000,
        random_state=42
    )

    model_learning.fit(
        X_train_scaled,
        y_train
    )

    prediction = model_learning.predict(
        X_test_scaled
    )

    accuracy = accuracy_score(
        y_test,
        prediction
    )

    print(
        "Learning Rate:",
        learning_rate,
        "Accuracy:",
        accuracy
    )

print(Border)