def pattern(no):
    for i in range(no):
        for j in range(1, no + 1):
            print(j, end="\t")
        print()

def main():
    Value = int(input("Enter a number: "))
    pattern(Value)

if __name__ == "__main__":
    main()