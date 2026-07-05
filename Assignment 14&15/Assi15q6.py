from functools import reduce

Min = lambda No1,No2: No1 if No1 < No2 else No2

def main():
    Data = [0,2,3,4,5]

    RData = reduce(Min,Data)

    print("The Max number after reduce is: ",RData)

if __name__ == "__main__":
    main()