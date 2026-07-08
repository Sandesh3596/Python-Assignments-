def sumDigits(no):
    sum = 0

    while no > 0:
        Count = no % 10
        sum = sum + Count
        no = no // 10

    return sum

def main():
    No = int(input("Enter a number: "))
    Ret = sumDigits(No)
    print("Addition of digits:", Ret)

if __name__ == "__main__":
    main()