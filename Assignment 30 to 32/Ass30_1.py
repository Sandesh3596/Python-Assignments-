import time
import schedule

def Fun():
    print("Jay Ganesh...")

def main():
    fobj = schedule.every(2).seconds.do(Fun)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()