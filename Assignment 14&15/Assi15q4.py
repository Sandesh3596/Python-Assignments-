from functools import reduce

Sum = lambda No1, No2: No1 + No2

def main():
    Data = [1,2,3,4,5]

    RData = reduce(Sum,Data)

    print("The Addition after reduce is: ",RData)

if __name__ == "__main__":
    main()

