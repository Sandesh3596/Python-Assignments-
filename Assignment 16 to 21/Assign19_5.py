from functools import reduce

def PrimeNum(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

def Increment(No):
    return No * 2

def Addition(No1, No2):
    return No1 + No2

def main():
    Data = [2, 70, 11, 10, 17, 23, 31, 77]

    print("Input data is :", Data)

    FData = list(filter(PrimeNum, Data))
    print("Data after filter:", FData)

    MData = list(map(Increment, FData))
    print("Data after map:", MData)

    RData = reduce(Addition, MData)
    print("Data after reduce:", RData)

if __name__ == "__main__":
    main()