def checkeven(No):
    
    print("The Even Numbers Are: ")

    for i in range(1, No + 1):

        if(i % 2 ==0):
         print(i)


def main():
    value = int(input("Enter Number: "))

    checkeven(value)

if __name__ =="__main__":
    main()