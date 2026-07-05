Even = lambda no: True if no  % 2 == 0 else False

def main():
    Value = int(input("Enter a number: "))

    print("The Value is: ",Even(Value))

if __name__ =="__main__":
    main()

