import os
import time
import multiprocessing

def SumSquare(no):
    
    Sum = no * (no + 1) * (2 * no + 1) // 6

    return Sum

def main():

    start_time = time.perf_counter()

    Value = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()

    Ret = p.map(SumSquare, Value)

    p.close()
    p.join()

    print("Output :", Ret)

    end_time = time.perf_counter()

    print(f"Time required is : {end_time - start_time:.4f}")

if __name__ == "__main__":
    main()