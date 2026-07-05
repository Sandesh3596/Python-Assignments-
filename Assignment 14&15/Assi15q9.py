from functools import reduce

D = lambda No1, No2: No1 * No2

def main():
    Data = [2,4,3,1]

    RData = reduce(D,Data)

    print("The data after reduce is: ",RData)

if __name__ == "__main__":
    main()