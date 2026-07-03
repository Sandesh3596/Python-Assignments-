Add = lambda no1, no2: no1 + no2
Sub = lambda no1, no2: no1 - no2
Multiply = lambda no1, no2: no1 * no2
Divide = lambda no1, no2: no1 / no2

def main():
    Value1 = int(input("Enter first number:" ))
    Value2 = int(input("Enter second number:" ))

    print("The Addition is: ",Add(Value1, Value2))
    print("The Sub is: ",Sub(Value1, Value2))
    print("The Multiplication is: ",Multiply(Value1, Value2))
    print("The Division is: ",Divide(Value1, Value2))

if __name__ == "__main__":
    main()