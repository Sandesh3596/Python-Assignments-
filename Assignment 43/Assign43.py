import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


def Marvellousclassifier(DataPath):

    border = "_" * 50

    # Step 1: Get Data

    print(border)
    print("Step 1: Get Data")
    print(border)

    df = pd.read_csv(DataPath)

    print("Some entries from Dataset: ")
    print(df.head())
    print(border)


    # Step 2: Clean, Prepare and Manipulate Data

    print(border)
    print("Step 2: Clean, Prepare and Manipulate Data")
    print(border)

    WetherEncoder = LabelEncoder()
    TemperatureEncoder = LabelEncoder()
    PlayEncoder = LabelEncoder()

    df["Wether"] = WetherEncoder.fit_transform(df["Wether"])
    df["Temperature"] = TemperatureEncoder.fit_transform(df["Temperature"])
    df["Play"] = PlayEncoder.fit_transform(df["Play"])

    print("Data converted into numerical format")
    print(df)
    print(border)


    # Step 3: Train Data

    print(border)
    print("Step 3: Train Data")
    print(border)

    X = df[["Wether", "Temperature"]]
    Y = df["Play"]

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X, Y)

    print("Model training completed")
    print(border)


    # Step 4: Test Data

    print(border)
    print("Step 4: Test Data")
    print(border)

    Wether = input("Enter Wether: ")
    Temperature = input("Enter Temperature: ")

    WetherValue = WetherEncoder.transform([Wether])
    TemperatureValue = TemperatureEncoder.transform([Temperature])

    TestData = [[WetherValue[0], TemperatureValue[0]]]

    Result = model.predict(TestData)

    Result = PlayEncoder.inverse_transform(Result)

    print("Result is: ", Result[0])
    print(border)


    # Step 5: Calculate Accuracy

    CheckAccuracy(df)


def CheckAccuracy(df):

    border = "_" * 50

    print(border)
    print("Step 5: Calculate Accuracy")
    print(border)

    X = df[["Wether", "Temperature"]]
    Y = df["Play"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.5, random_state=42
    )

    for K in range(1, 10):

        model = KNeighborsClassifier(n_neighbors=K)

        model.fit(X_train, Y_train)

        Y_pred = model.predict(X_test)

        Accuracy = accuracy_score(Y_test, Y_pred)

        print("K =", K, "Accuracy =", Accuracy * 100)

    print(border)


def main():

    Marvellousclassifier("MarvellousInfosystems_PlayPredictor.csv")


if __name__ == "__main__":
    main()