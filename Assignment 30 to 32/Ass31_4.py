import sys
import time
import schedule
from datetime import datetime

def CreateLogFile(FileName):
    CurrentTime = datetime.now()

    LogFileName = FileName + "_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    print("Log File get created with Name:", LogFileName)

    fobj = open(LogFileName, "w")

    fobj.write("Log file created successfully.\n")
    fobj.write("Creation Time: " + CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))

    fobj.close()


def main():
    Border = "-" * 40

    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    if len(sys.argv) == 2:
        CreateLogFile(sys.argv[1])

        schedule.every(10).minutes.do(CreateLogFile, sys.argv[1])

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")
        print("Please execute the script as:")
        print("python FileName.py MarvellousLog")

    print(Border)


if __name__ == "__main__":
    main()