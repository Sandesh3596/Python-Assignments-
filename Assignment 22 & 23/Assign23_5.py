import os
import time
import multiprocessing

def Factorial(no):
    Fact = 1

    for i in range(1, no + 1):
        Fact = Fact * i

    print(f"Process ID : {os.getpid()}")
    print("Input Number: ", no)
    print("Factorial: ", Fact)

    return Fact

def main():
    start_time = time.perf_counter()

    Data = [10, 15, 20, 25]

    p = multiprocessing.Pool()

    Ret = p.map(Factorial, Data)

    p.close()
    p.join()

    print("Output :", Ret)

    end_time = time.perf_counter()

    print(f"Time required is: {end_time - start_time:.4f}")

if __name__ == "__main__":
    main()