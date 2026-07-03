Area = lambda no1, no2: no1 * no2

def main():
    Value1 = float(input("Enter a length: "))
    Value2 = float(input("Enter a width: "))

    print("The Area of rectangle is: ",Area(Value1, Value2))
if __name__ == "__main__":
    main()