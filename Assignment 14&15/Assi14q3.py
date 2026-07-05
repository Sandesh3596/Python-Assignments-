Max = lambda no1, no2: no1 if no1 > no2 else no2

def main():
    Value1 = int(input("Enter first number: "))

    Value2 = int(input("Enter second Number: "))

    print("The max Number is: ",Max(Value1, Value2))

if __name__ == "__main__":
    main()