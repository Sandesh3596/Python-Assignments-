import schedule
import datetime
import time


def file():
    CurrentTime = datetime.datetime.now()

    FileName = "File_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    print(FileName)

    fobj = open(FileName, "w")

    fobj.write("Filename : " + FileName + "\n")
    fobj.write("Creation Date : " + CurrentTime.strftime("%d/%m/%Y") + "\n")
    fobj.write("Creation Time : " + CurrentTime.strftime("%H:%M:%S") + "\n")

    fobj.close()

def main():
    schedule.every(1).minutes.do(file)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()