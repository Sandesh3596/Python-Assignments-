import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for i in range(100000):
        lock.acquire()
        counter += 1
        lock.release()

def main():
    threads = []

    for i in range(5):
        t = threading.Thread(target=increment)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Final Counter Value:", counter)

if __name__ == "__main__":
    main()
    