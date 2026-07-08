import threading

def Max(lst):
    print("Maximum element:", max(lst))

def Min(lst):
    print("Minimum element:", min(lst))

def main():
    n = int(input("Enter the number of elements: "))
    lst = []

    for i in range(n):
        lst.append(int(input()))

    t1 = threading.Thread(target=Max, args=(lst,))
    t2 = threading.Thread(target=Min, args=(lst,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()