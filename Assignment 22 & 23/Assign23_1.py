import os
import multiprocessing

def SumEven(no):
    Sum = 0

    for i in range(2, no + 1, 2):
        Sum = Sum + i

    print(f"The Process ID: {os.getpid()}")
    print("The input number: ", no)
    print("The sum of Even numbers are: ", Sum)

    return Sum

def main():   
    Data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()

    Ret = p.map(SumEven, Data)

    p.close()
    p.join()

    print("The Sum is: ", Ret)
 
if __name__ == "__main__":
    main()