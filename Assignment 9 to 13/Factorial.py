def fact(no):
    Ans = 1

    for i in range(1, no + 1):
        Ans = Ans * i

    return Ans

def main():
    Value = int(input("Enter a number: "))

    if Value > 0:
        Ret = fact(Value)
        print("Factorial of", Value, "is", Ret)


if __name__ == "__main__":
    main()