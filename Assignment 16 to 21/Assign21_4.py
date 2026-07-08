import threading

sum_result = 0
result = 1

def find_sum(lst):
    global sum_result
    sum_result = sum(lst)

def find_product(lst):
    global result
    result = 1
    for i in lst:
        result *= i

def main():
    No = int(input("Enter the number of elements: "))
    lst = []

    for i in range(No):
        lst.append(int(input()))

    t1 = threading.Thread(target=find_sum, args=(lst,))
    t2 = threading.Thread(target=find_product, args=(lst,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements:", sum_result)
    print("Product of elements:", result)

if __name__ == "__main__":
    main()