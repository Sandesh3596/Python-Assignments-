def main():
    Value = int(input("Enter a number: "))
    Ans = 0

    while Value > 0:
        Data = Value % 10
        Ans = Ans * 10 + Data
        Value = Value // 10

    print("The reversed value is:", Ans)

if __name__ == "__main__":
    main()