def Marvellous_Weight_Update(input_value,weight,bias,target,learning_rate):

    print("Input is: ",input_value)
    print('-'* 20)

    print("Weight is: ",weight)
    print('-'* 20)

    print("Bias is: ",bias)
    print('-'* 20)

    print("Target is: ",target)
    print('-'* 20)

    print("Learning Rate is: ",learning_rate)
    print('-'* 20)

    prediction = (input_value * weight) + bias

    print("Prediction is: ",prediction)
    print('-'* 20)

    error = target - prediction

    print("Error is: ",error)
    print('-'* 20)

    gradient = error * input_value

    updated_weight = weight + (learning_rate * gradient)

    print("Gradient is: ",gradient)
    print('-'* 20)

    print("Updated Weight is: ",updated_weight)
    print('-'* 20)

    return updated_weight


def main():

    print("---Marvellous Weight Update---")

    input_value = 2.0
    weight = 0.5
    bias = 0.5
    target = 2.0
    learning_rate = 0.1

    result = Marvellous_Weight_Update(
        input_value,
        weight,
        bias,
        target,
        learning_rate
    )

    print("Old Weight: ",weight)
    print("New Weight: ",result)


if __name__ == "__main__":
    main()