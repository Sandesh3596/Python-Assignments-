import math


def Mean_Squared_Error(actual,predicted):

    total = 0

    for i in range(len(actual)):

        error = actual[i] - predicted[i]

        total = total + (error * error)

    mse = total / len(actual)

    return mse


def Binary_Cross_Entropy(actual,predicted):

    total = 0

    for i in range(len(actual)):

        loss = -(actual[i] * math.log(predicted[i]) +
                 (1 - actual[i]) * math.log(1 - predicted[i]))

        total = total + loss

    bce = total / len(actual)

    return bce


def main():

    print("---Marvellous Loss Calculation---")

    actual = [1,0,1,1]
    predicted = [0.9,0.2,0.8,0.7]

    print("Actual Values: ",actual)
    print('-'* 20)

    print("Predicted Values: ",predicted)
    print('-'* 20)

    mse = Mean_Squared_Error(actual,predicted)

    print("Mean Squared Error: ",mse)
    print('-'* 20)

    bce = Binary_Cross_Entropy(actual,predicted)

    print("Binary Cross Entropy: ",bce)
    print('-'* 20)

    print("MSE is generally used for Regression.")
    print("Binary Cross Entropy is generally used for Classification.")


if __name__ == "__main__":
    main()