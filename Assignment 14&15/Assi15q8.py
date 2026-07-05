D = lambda No: (No % 3 == 0) and (No % 5 == 0)

def main():
    Data = [10,15,30,40,45]

    FData = list(filter(D,Data))

    print("The data after filter is: ",FData)

if __name__ == "__main__":
    main()