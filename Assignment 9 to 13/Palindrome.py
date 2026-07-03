def main():
    Value = int(input("Enter a number: "))
    no = Value
    Ans = 0

    while Value > 0:
        digit = Value % 10
        Ans = Ans * 10 + digit
        Value = Value // 10

    if no == Ans:
        print("This is Palindrome Number")
    else:
        print("This is not a Palindrome Number")

if __name__ == "__main__":
    main()