import os
import multiprocessing

def SumOdd(no):
    Sum = 0

    for i in range(1, no + 1, 2):
        Sum = Sum + i

    print(f"The Process ID: {os.getpid()}")
    print("The input number: ", no)
    print("The sum of Odd numbers are: ", Sum)

    return Sum

def main():   
    Data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()

    Ret = p.map(SumOdd, Data)

    p.close()
    p.join()

    print("The Sum of Odd is: ", Ret)
 
if __name__ == "__main__":
    main()