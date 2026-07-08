def ChkPrime(No):

    if No <= 1:
        print("It is Not a Prime Number")
        return

    for i in range(2, No):
        if No % i == 0:
            print("It is Not a Prime Number")
            return

    print("It is Prime Number")


def main():

    Value = int(input("Enter a number: "))
    ChkPrime(Value)


if __name__ == "__main__":
    main()