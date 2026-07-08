from functools import reduce

def fun(No):
    return No >= 70

def Increment(No):
    return No + 10

def Multiply(No1, No2):
    return No1 * No2

def main():
    Data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    print("The input Data is: ", Data)

    FData = list(filter(fun, Data))

    print("The data after filter: ", FData)

    MData = list(map(Increment,FData))

    print("The data after Map:",MData)

    RData = reduce(Multiply,MData)

    print("The data after reduce is: ",RData)

if __name__ == "__main__":
    main()