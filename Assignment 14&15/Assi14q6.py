Odd = lambda no: no  % 2 != 0 

def main():
    Value = int(input("Enter a number: "))

    print("The Value is: ", Odd(Value))

if __name__ =="__main__":
    main()

