def main():

    No = int(input("Enter a number: "))

    Add = 0

    for i in range(1, No+1):
        if No % i == 0:
            Add = Add + i

    print("Addition of factors is:", Add)

if __name__ == "__main__":
    main()