import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


def Marvellous_Neural_Network(X,Y):

    print("---Marvellous Customer Churn Prediction---")
    print('-'* 40)

    print("Features are:")
    print("[Age, Monthly Charges, Tenure, Complaints, Support Calls]")
    print('-'* 40)

    # Split Dataset
    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
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

    print("=== Customer Churn Prediction ===")
    print()

    # Features:
    # Age
    # Monthly Charges
    # Tenure
    # Complaints
    # Support Calls

    X = np.array([
        [250, 500, 12, 1, 2],
        [30, 700, 24, 0, 1],
        [45, 1200, 6, 5, 8],
        [150, 1500, 5, 6, 10],
        [280, 600, 18, 1, 11],
        [35, 800, 30, 0, 1],
        [48, 1400, 4, 7, 9],
        [52, 1600, 3, 8, 12],
        [27, 550, 20, 0, 1],
        [42, 1300, 8, 4, 7]
    ])

    # 0 = Customer will stay
    # 1 = Customer will leave

    Y = np.array([
        0,
        1,
        1,
        0,
        1,
        0,
        1,
        1,
        0,
        1
    ])

    print("Dataset Loaded Successfully")
    print('-'* 40)

    model,scaler = Marvellous_Neural_Network(X,Y)

    # Test Customer
    new_customer = np.array([
        [46,1450,5,6,9]
    ])

    print("Test Input:")
    print(new_customer)
    print('-'* 40)

    # Scale Test Data
    new_customer_scaled = scaler.transform(new_customer)

    # Predict
    prediction = model.predict(new_customer_scaled)

    print("Prediction: ",prediction)
    print('-'* 40)

    if prediction[0] == 0:
        print("Prediction: Customer will stay")
    else:
        print("Prediction: Customer will leave")

    print('-'* 40)


if __name__ == "__main__":
    main()