Add = lambda No1, No2: No1 + No2
Sub = lambda No1, No2: No1 - No2
Multiply = lambda No1, No2: No1 * No2
Division = lambda No1, No2: No1 / No2

def Arithmetic():

    Value1 = int(input("Enter First Number: "))
    Value2 = int(input("Enter Second Number: "))

    print("The Addition of numbers are: ",Add(Value1, Value2))
    print("The Sub of numbers are: ",Sub(Value1, Value2))
    print("The Multiplication of numbers are: ",Multiply(Value1, Value2))
    print("The Division of numbers are: ",Division(Value1, Value2))

if __name__ == "__main__":
    Arithmetic()
