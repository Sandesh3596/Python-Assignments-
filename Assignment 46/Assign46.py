import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def MachineLearning():
    # Step 1: Load the Data
    df = pd.read_csv("Advertising.csv")

    # Step 2: Clean, Prepare & Manipulate Data
    X = df[['TV', 'radio', 'newspaper']]
    Y = df['sales']

    # Step 3: Train Data
    X_train = X.iloc[:100]
    Y_train = Y.iloc[:100]

    model = LinearRegression()
    model.fit(X_train, Y_train)

    # Step 4: Test Data
    X_test = X.iloc[100:]
    Y_test = Y.iloc[100:]

    # Step 5: Predict the Data
    predicted = model.predict(X_test)

    print('-' * 40)
    print("Expected Values: \n")
    print(Y_test.values)
    print('-' * 40)

    print('-' * 40)
    print("Predicted Values: \n")
    print(predicted)
    print('-' * 40)

def main():
    MachineLearning()

if __name__ == "__main__":
    main()