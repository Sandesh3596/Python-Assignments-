import time
import schedule
import datetime
import os


def monitor():
    CurrentTime = datetime.datetime.now()

    FileName = "Demo.txt"
    LogFileName = "FileSizeLog.txt"

    print(FileName)

    fobj = open(LogFileName, "a")

    if os.path.exists(FileName):
        FileSize = os.path.getsize(FileName)

        fobj.write("File Path : " + os.path.abspath(FileName) + "\n")
        fobj.write("File Size : " + str(FileSize) + " bytes\n")
        fobj.write("Date : " + CurrentTime.strftime("%d/%m/%Y") + "\n")
        fobj.write("Time : " + CurrentTime.strftime("%H:%M:%S") + "\n")

    else:
        fobj.write("File does not exist : " + FileName + "\n")
        fobj.write("Date : " + CurrentTime.strftime("%d/%m/%Y") + "\n")
        fobj.write("Time : " + CurrentTime.strftime("%H:%M:%S") + "\n")
        fobj.write("----------------------------------------\n")

    fobj.close()


def main():
    schedule.every(3).seconds.do(monitor)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()