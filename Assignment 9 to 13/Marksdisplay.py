def main():
    Value = int(input("Enter a Marks: "))

    if Value >= 75:
        print("You passed with Distinction")

    elif Value >=60:
        print("You passed with First Class")

    elif Value >=50:
        print("You passed with Second Class")

    elif Value <50:
        print("You are Fail")    

if __name__ == "__main__":
    main()