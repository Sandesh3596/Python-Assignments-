from functools import reduce

Max = lambda No1,No2: No1 if No1 > No2 else No2

def main():
    Data = [1,2,3,4,5]

    RData = reduce(Max,Data)

    print("The Max number after reduce is: ",RData)

if __name__ == "__main__":
    main()