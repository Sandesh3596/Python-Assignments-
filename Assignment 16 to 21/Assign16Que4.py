def main():

    Data = int(input("Enter the number of elements: "))

    data = []

    print("Enter the elements:")

    for i in range(Data):

        value = int(input())

        data.append(value)

    freq = int(input("Element to search: "))

    frequency = data.count(freq)

    print("Input Elements:", data)

    print("Frequency of", freq, "is:", frequency)

if __name__ == "__main__":
    main()