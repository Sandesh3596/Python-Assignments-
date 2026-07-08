def pattern(no):
    for i in range(1, no + 1):
        for j in range(1, i + 1):
            print(j, end="\t")
        print()

def main():
    num = int(input("Enter a number: "))
    pattern(num)

if __name__ == "__main__":
    main()