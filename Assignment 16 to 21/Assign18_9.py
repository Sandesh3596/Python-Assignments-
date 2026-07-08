def countDigits(no):
    Sum = 0

    while no > 0:
        Sum += 1
        no = no // 10

    return Sum

def main():

    No = int(input("Enter a number: "))

    Ret = countDigits(No)

    print("Number of digits:", Ret)

if __name__ == "__main__":
    main()