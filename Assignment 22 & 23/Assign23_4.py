import os
import multiprocessing

def OddCount(no):
    Sum = 0

    for i in range(1, no + 1):
        if i % 2 != 0:
            Sum = Sum + 1

    print(f"The Process ID: {os.getpid()}")
    print("The input number: ", no)
    print("The Even number count is: ", Sum)

    return Sum

def main():

    Data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()

    Ret = p.map(OddCount, Data)

    p.close()
    p.join()

    print("The output is: ", Ret)

if __name__ == "__main__":
    main()