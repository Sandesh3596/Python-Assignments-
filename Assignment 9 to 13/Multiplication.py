def main():
    Value = int(input("Enter a number: "))

    i = 1

    for i in range(1,11):
        print(Value, "x", i, "=", Value * i)
        i = i + 1

if __name__ == "__main__":
    main()