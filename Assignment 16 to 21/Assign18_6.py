def pattern(no):
    for i in range(no, 0, -1):
        for j in range(i):
            print("*", end="\t")
        print()

def main():
    Value = int(input("Enter a number: "))
    pattern(Value)

if __name__ == "__main__":
    main()