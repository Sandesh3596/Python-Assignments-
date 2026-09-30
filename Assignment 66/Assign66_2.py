import numpy as np
import math
import matplotlib.pyplot as plt


def sigmaid(z):

    return 1 / (1 + np.exp(-z))


def ReLU(z):

    return np.maximum(0,z)


def Tanh(z):

    return np.tanh(z)


def Marvellous_Activation_Function():

    inputs = np.linspace(-10,10,100)

    sigmoid_output = sigmaid(inputs)
    relu_output = ReLU(inputs)
    tanh_output = Tanh(inputs)

    plt.plot(inputs,sigmoid_output,label="Sigmoid")
    plt.plot(inputs,relu_output,label="ReLU")
    plt.plot(inputs,tanh_output,label="Tanh")

    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.title("Activation Functions")

    plt.legend()
    plt.grid()

    plt.show()


def main():

    print("---Marvellous Activation Functions---")

    Marvellous_Activation_Function()


if __name__ == "__main__":
    main()