import time
import schedule
import datetime

def Fun():
    obj = open("Marvellous.txt", "a") 
    obj.write(str(datetime.datetime.now()) + "\n")
    print("Task Executed at: ",datetime.datetime.now())
    obj.close()
    

def main():
    fobj = schedule.every(5).minutes.do(Fun)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()