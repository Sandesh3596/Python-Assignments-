import time
import schedule

def Lunch():
    print("Lunch Time!")

def Wrap():
    print("Wrap Up Work")

def main():
    fobj = schedule.every().day.at("13:00").do(Lunch)
    fobj1 = schedule.every().day.at("18:00").do(Wrap)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()