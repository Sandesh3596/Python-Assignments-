Divide = lambda no: no % 5 == 0

def main():
    Value = int(input("Enter a number: "))

    print("The Number is divisible by 5: ",Divide(Value))

if __name__ =="__main__":
    main()