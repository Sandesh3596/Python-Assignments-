Even = lambda No: (No % 2 == 0)

def main():
    Data = [1,2,3,4,5]

    Fdata = list(filter(Even,Data))

    print("The Filter Data is: ",Fdata)

if __name__ == "__main__":
    main()