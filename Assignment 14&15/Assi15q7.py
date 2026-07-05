Length = lambda No: len(No) > 5

def main():
    Data = ["Ram","Shyam","Marvellous","Infosystem"]

    FData = list(filter(Length,Data))

    print("The data after filter is: ",FData)

if __name__ == "__main__":
    main()