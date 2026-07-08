import threading

def IsPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True


def Prime(Data):
    print("Prime Numbers are:")
    for i in Data:
        if IsPrime(i):
            print(i)


def NonPrime(Data):
    print("Non-Prime Numbers are:")
    for i in Data:
        if not IsPrime(i):
            print(i)


def main():
    Size = int(input("Enter number of elements: "))

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        No = int(input())
        Data.append(No)

    t1 = threading.Thread(target=Prime, args=(Data,), name="Prime")
    t2 = threading.Thread(target=NonPrime, args=(Data,), name="NonPrime")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()