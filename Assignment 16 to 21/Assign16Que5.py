from MarvellousNum import ChkPrime

def ListPrime(Data):

    Sum = 0

    for No in Data:
        if ChkPrime(No):
            Sum = Sum + No

    return Sum

def main():

    Count = int(input("Enter number of elements: "))

    Data = []

    print("Enter the elements:")

    for i in range(Count):

        Value = int(input())
        
        Data.append(Value)

    Result = ListPrime(Data)

    print("Input Elements: ", Data)

    print("Addition of prime numbers:", Result)

if __name__ == "__main__":
    main()