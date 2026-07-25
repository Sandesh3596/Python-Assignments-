import time
import schedule

def Display(Message):
    print(Message)

def main():
    Input = input("Enter message: ")
    Data = int(input("Enter interval in seconds: "))

    if Data <= 0:
        print("Interval must be greater than zero.")
        return

    schedule.every(Data).seconds.do(Display, Input)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()