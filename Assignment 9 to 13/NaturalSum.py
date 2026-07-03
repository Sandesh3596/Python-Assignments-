def main():
    n = int(input("Enter a number: "))

    i = 1
    Sum = 0

    while i <= n:
        Sum = Sum + i
        i = i + 1

    print("Sum of first", n, "natural numbers is:", Sum)

if __name__ == "__main__":
    main()