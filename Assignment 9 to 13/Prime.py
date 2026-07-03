def Prime(no):
    if no <= 1:
        print(no, "is not a Prime Number")
        return
    
    for i in range(2, no):
        if no % i == 0:
            print(no, "is not a Prime Number")
            return

    print(no, "is a Prime Number")

def main():
    Value = int(input("Enter a number: "))
    Prime(Value)

if __name__ == "__main__":
    main()