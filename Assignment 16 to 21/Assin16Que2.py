from functools import reduce

Max = lambda No1, No2: No1 if No1 > No2 else No2

def main():

    data = int(input("Enter the number of elements: "))

    Data = []

    print("Enter the elements: ")

    for i in range(data):

        value = int(input())

        Data.append(value)

    print("Input Elements are:", Data)

    RData = reduce(Max, Data)

    print("The Maximum number in element is: ", RData)

if __name__ == "__main__":
    main()