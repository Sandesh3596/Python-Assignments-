import threading

def EvenFactor(No):
    Sum = 0

    print("Even Factors are:")
    for i in range(1, No + 1):
        if No % i == 0:
            if i % 2 == 0:
                print(i)
                Sum = Sum + i

    print("Sum of Even Factors:", Sum)


def OddFactor(No):
    Sum = 0

    print("Odd Factors are:")
    for i in range(1, No + 1):
        if No % i == 0:
            if i % 2 != 0:
                print(i)
                Sum = Sum + i

    print("Sum of Odd Factors:", Sum)


def main():
    No = int(input("Enter a number: "))

    t1 = threading.Thread(target=EvenFactor, args=(No,), name="EvenFactor")
    t2 = threading.Thread(target=OddFactor, args=(No,), name="OddFactor")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()