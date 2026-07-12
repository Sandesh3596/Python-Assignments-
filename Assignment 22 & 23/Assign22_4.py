import os
import time
import multiprocessing

def Power(No):
    print(f"The PID of Power is: {os.getpid()} PPID of SumPower5 : {os.getppid()}")

    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + (i ** 5)

    print("The input number is: ", No)
    print("The sum of power is: ", Sum)

    return Sum

def main():
    print(f"PID of main: {os.getpid()} PPID of main : {os.getppid()}")

    start_time = time.perf_counter()

    Value = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()

    Ret = p.map(Power, Value)

    p.close()
    p.join()

    print("The power of Value is: ", Ret)

    end_time = time.perf_counter()

    print(f"Time required is : {end_time - start_time:.4f}")

if __name__ == "__main__":
    main()