import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score


def MarvellousPredictor():
    # Load the Data

    Data = load_breast_cancer()

    X = Data.data
    Y = Data.target

    print("Independent Variables are: ", X)
    print("Dependent Variable are: ", Y)

    print("Number of Records: ", X.shape[0])
    print("Number of Features: ", X.shape[1])

    # Create DataFrame

    df = pd.DataFrame(X, columns=Data.feature_names)

    print("\nFirst 5 Records:")
    print(df.head())

    # Summary Statistics

    print("\nSummary Statistics:")
    print(df.describe())

    # Check Missing Values

    print("\nMissing Values: ")
    print(df.isnull().sum())

    # Feature Correlation

    print("\n Feature Correlation: ")
    print(df.corr())

    plt.figure(figsize=(12, 10))
    plt.imshow(df.corr(), cmap="coolwarm")
    plt.colorbar()
    plt.title("Feature Correlation")
    plt.show()

    # Split the Data into Training and Testing

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("\nTraining Data: ", X_train.shape)
    print("Testing Data: ", X_test.shape)

    # Normalize / Scale Features

    Scaler = StandardScaler()

    X_train = Scaler.fit_transform(X_train)
    X_test = Scaler.transform(X_test)

    # Build Machine Learning Model

    Model = LogisticRegression(max_iter=1000)

    # Train the Model

    Model.fit(X_train, Y_train)

    print("\nModel Training Completed")

    # Test the Model

    Y_Predicted = Model.predict(X_test)

    print("\nActual Values: ", Y_test)
    print("Predicted Values: ", Y_Predicted)

    # Calculate Accuracy

    Accuracy = accuracy_score(Y_test, Y_Predicted)

    print("\nAccuracy of Model: ", Accuracy)

    # Calculate Confusion Matrix

    ConfusionMatrix = confusion_matrix(Y_test, Y_Predicted)

    print("\nConfusion Matrix: ")
    print(ConfusionMatrix)

    # Calculate Precision

    Precision = precision_score(Y_test, Y_Predicted)

    print("\nPrecision: ", Precision)

    # Calculate Recall

    Recall = recall_score(Y_test, Y_Predicted)

    print("Recall: ", Recall)

    # Calculate F1 Score

    F1Score = f1_score(Y_test, Y_Predicted)

    print("F1 Score: ", F1Score)

    # Display Confusion Matrix

    plt.figure(figsize=(6, 5))
    plt.imshow(ConfusionMatrix, cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted Values")
    plt.ylabel("Actual Values")
    plt.colorbar()
    plt.show()


def main():
    MarvellousPredictor()


if __name__ == "__main__":
    main()