def chkNum(no):

    if no > 0:

        print("Positive Number")

    elif no < 0:

        print("Negative Number")

    else:
        
        print("Zero")

def main():

    Value = int(input("Enter a number: "))

    chkNum(Value)

if __name__ == "__main__":
    main()