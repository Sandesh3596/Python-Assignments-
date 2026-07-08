from functools import reduce

Add = lambda No1, No2: No1 + No2

def main():

    data = int(input("Enter the number of elements: "))

    Data = []

    print("Enter the elements: ")

    for i in range(data):
        value = int(input())
        Data.append(value)

    print("Input Elements are:", Data)

    RData = reduce(Add, Data)

    print("Addition of all elements:", RData)

if __name__ == "__main__":
    main()