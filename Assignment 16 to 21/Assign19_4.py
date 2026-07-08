from functools import reduce

def CheckEven(No):
    return (No % 2 ==0)

def Increment(No):
    return No * No

def Addition(No1, No2):
    return No1 + No2

def main():
    Data = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

    print("Input data is :",Data)

    FData = list(filter(CheckEven,Data))
    print("Data after filter: ",FData)

    MData = list(map(Increment,FData))
    print("Data after Map:",MData)

    RData = reduce(Addition,MData)
    print("Data after reduce:",RData)


if __name__ == "__main__":
    main()