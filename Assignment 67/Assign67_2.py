import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


def Marvellous_Neural_Network(X,Y):

    print("---Marvellous Loan Approval Prediction---")
    print('-'* 40)

    print("Features are:")
    print("[Income, Credit Score, Loan Amount, Existing EMI, Employment Status]")
    print('-'* 40)

    # Split Dataset
    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42,
        stratify=Y
    )

    print("Training Data Size: ",X_train.shape)
    print("Testing Data Size: ",X_test.shape)
    print('-'* 40)

    # Feature Scaling
    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print("Feature Scaling Completed")
    print('-'* 40)

    # Create Neural Network
    model = MLPClassifier(
        hidden_layer_sizes=(10,5),
        activation='relu',
        max_iter=2000,
        random_state=42
    )

    # Train Model
    model.fit(X_train,Y_train)

    print("FNN Model Training Completed")
    print('-'* 40)

    # Prediction
    Y_pred = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(Y_test,Y_pred)

    print("Actual Output: ",Y_test)
    print("Predicted Output: ",Y_pred)
    print('-'* 40)

    print("Accuracy: ",accuracy)
    print('-'* 40)

    return model,scaler


def main():

    print("=== Loan Approval Prediction ===")
    print()

    # Features:
    # Applicant Income
    # Credit Score
    # Loan Amount
    # Existing EMI
    # Employment Status

    X = np.array([
        [25000, 600, 200000, 10000, 0],
        [40000, 700, 300000, 8000, 1],
        [60000, 750, 500000, 12000, 1],
        [20000, 550, 150000, 15000, 0],
        [80000, 800, 700000, 1000, 1],
        [35000, 650, 250000, 9000, 1],
        [18000, 500, 100000, 12000, 0],
        [90000, 850, 800000, 1500, 1],
        [30000, 580, 200000, 14000, 0],
        [70000, 780, 600000, 10000, 1]
    ])

    # 0 = Loan rejected
    # 1 = Loan approved

    Y = np.array([
        0,
        1,
        1,
        0,
        1,
        1,
        0,
        1,
        0,
        1
    ])

    print("Dataset Loaded Successfully")
    print('-'* 40)

    model,scaler = Marvellous_Neural_Network(X,Y)

    # Test Applicant
    new_applicant = np.array([
        [55000, 720, 400000, 10000, 1]
    ])

    print("Test Input:")
    print(new_applicant)
    print('-'* 40)

    # Scale Test Data
    new_applicant_scaled = scaler.transform(new_applicant)

    # Predict
    prediction = model.predict(new_applicant_scaled)

    print("Prediction: ",prediction)
    print('-'* 40)

    if prediction[0] == 0:
        print("Prediction: Loan Rejected")
    else:
        print("Prediction: Loan Approved")

    print('-'* 40)


if __name__ == "__main__":
    main()