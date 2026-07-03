def Num(no):
    Sum = 0
    for i in range(1,no):
        if no % i == 0:
         Sum += i

    if Sum == no:
        return Sum  

def main():
    Value = int(input("Enter a Number: "))

    if Num(Value):
        print(Value, "is Perfect Number")
    else:
        print(Value, "is not Perfect Number")

if __name__ == "__main__":
    main()