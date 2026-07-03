def main():
    Value = int(input("Enter a number: "))

    Ans = 0

    while Value > 0:
        Ans = Ans + (Value % 10)
        Value = Value // 10

    print("Sum of digits is:", Ans)

if __name__ == "__main__":
    main()