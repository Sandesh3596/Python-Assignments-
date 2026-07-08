import threading

def EvenList(Data):
    Even = []
    Sum = 0

    for i in Data:
        if i % 2 == 0:
            Even.append(i)
            Sum += i

    print("Even Elements:", Even)
    print("Sum of Even Elements:", Sum)


def OddList(Data):
    Odd = []
    Sum = 0

    for i in Data:
        if i % 2 != 0:
            Odd.append(i)
            Sum += i

    print("Odd Elements:", Odd)
    print("Sum of Odd Elements:", Sum)


def main():
    Size = int(input("Enter number of elements: "))

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        No = int(input())
        Data.append(No)

    t1 = threading.Thread(target=EvenList, args=(Data,), name="EvenList")
    t2 = threading.Thread(target=OddList, args=(Data,), name="OddList")

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()