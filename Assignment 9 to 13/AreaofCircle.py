Area = lambda no: 3.14 *no * no

def Circle():
    Value = float(input("Enter a radius of circle: "))

    print("The Area of Circle is: ",Area(Value))

if __name__ == "__main__":
    Circle()