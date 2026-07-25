import time
import schedule

def Fun():
    print("Coding Kar")

def main():
    fobj = schedule.every(30).minutes.do(Fun)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()