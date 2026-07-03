def CheckGreater(no1, no2):
    if no1 > no2:
        return no1
    else:
        return no2

def main():
    Value1 = int(input("Enter First Number: "))
    Value2 = int(input("Enter Second Number: "))

    Ans = CheckGreater(Value1, Value2)

    print("The greater value is: ", Ans)

if __name__ == "__main__":
    main()