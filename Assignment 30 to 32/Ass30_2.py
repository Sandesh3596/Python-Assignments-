import time
import schedule
import datetime

def Display():
    print("Current Date and Time: ",datetime.datetime.now())

def main():
    fobj = schedule.every(1).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(50)

if __name__ == "__main__":
    main()