import os
import time
import multiprocessing

def PrimeCount(No):
    print(f"The PID of PrimeCount: {os.getpid()} PPID of PrimeCount : {os.getppid()}")

    Count = 0

    for i in range(2, No + 1):
        Prime = True

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                Prime = False
                break

        if Prime:
            Count = Count + 1

    print("Input Number is: ",No)
    print("Total Prime Count :", Count)

    return Count

def main():
    print(f"PID of main: {os.getpid()} PPID of main : {os.getppid()}")

    start_time = time.perf_counter()

    Value = [10000, 20000, 30000, 40000]

    p = multiprocessing.Pool()

    Ret = p.map(PrimeCount, Value)

    p.close()
    p.join()

    print("The final output is: ",Ret)

    end_time = time.perf_counter()

    print(f"Time required is : {end_time - start_time:.4f}")

if __name__ == "__main__":
    main()