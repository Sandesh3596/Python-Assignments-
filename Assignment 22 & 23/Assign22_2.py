import os
import time
import multiprocessing
import math

def Factorial(no):
    print(f"The PID of Process is: {os.getpid()} PPID: {os.getppid()}")

    fact = math.factorial(no)

    print("The input Number is: ", no)
    print("Factorial of number is: ", fact)
    print()

def main():
    print(f"PID of main: {os.getpid()} PPID of main: {os.getppid()}")

    start_time = time.perf_counter()

    Value = [10, 15, 20, 25]

    with multiprocessing.Pool() as p:
        p.map(Factorial, Value)

    end_time = time.perf_counter()

    print(f"The time required for process is : {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()