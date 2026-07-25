import os
import time
import schedule

def monday():
    print("Start your weekly goals")

def wednesday():
    print("Review your weekly process")

def friday():
    print("Weekly work completed")

def main():
    schedule.every().monday.at("09:00").do(monday)
    schedule.every().wednesday.at("17:00").do(wednesday)
    schedule.every().friday.at("18:00").do(friday)
    while True:
        schedule.run_pending()
        time.sleep(10)
if __name__ == "__main__":
    main()