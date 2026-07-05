Square = lambda No: No * No

def main():
    Data = [1,2,3,4,5]

    print("Enter a data: ", Data)

    Map = list(map(Square,Data))

    print("Data after Map:",Map)

if __name__ == "__main__":
    main()