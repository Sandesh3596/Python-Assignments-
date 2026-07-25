import time
import schedule

def Fun():
    print("Namskar")

def main():
    fobj = schedule.every().day.at("09:00").do(Fun)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()