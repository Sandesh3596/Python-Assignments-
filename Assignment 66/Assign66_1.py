import numpy as np
import math

def sigmaid(z):
    return 1 / (1 + math.exp(-z))


def Neuron(inputs,weights,bias):

    print("Inputs are: ",inputs)
    print('-'* 20)

    print("Weights are: ",weights)
    print('-'* 20)

    print("bias is: ",bias)
    print('-'* 20)

    z = 0

    for i in range(len(inputs)):
        z = z + (inputs[i] * weights[i])

    z = z + bias

    print("Weighted Sum: ",z)
    print('-'* 20)

    y = sigmaid(z)

    print("Activation Output: ",y)
    print('-'* 20)

    return y


def main():

    print("---Marvellous Neural Network---")

    inputs = [2.0,3.0]
    weights = [0.4,0.6]
    bias = 0.5

    result = Neuron(inputs,weights,bias)

    print("Predicted Result: ",result)

    if result >= 0.5:
        print("Output is close to 1")
    else:
        print("Output is close to 0")


if __name__ == "__main__":
    main()