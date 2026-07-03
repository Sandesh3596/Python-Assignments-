def main():
    Value = int(input("Enter a number: "))

    if Value % 3 == 0 and Value % 5 == 0:
        print("The Value is Divisible by 3 & 5")

    else:
        print("The Value is not Divisible by 3 & 5")

if __name__ == "__main__":
    main()