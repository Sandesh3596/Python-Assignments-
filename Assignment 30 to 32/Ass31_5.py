import sys
import os
import time
import schedule
from datetime import datetime

def DirectoryCount(DirectoryPath):
    Count = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        Count = Count + len(FileName)

    CurrentTime = datetime.now()

    fobj = open("DirectoryCountLog.txt", "a")

    fobj.write("-" * 40 + "\n")
    fobj.write("Directory Path: " + DirectoryPath + "\n")
    fobj.write("Number of Files: " + str(Count) + "\n")
    fobj.write("Date and Time: " + CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
    fobj.write("-" * 40 + "\n\n")

    fobj.close()


def main():
    Border = "-" * 40

    print(Border)
    print("Marvellous Directory Automation")
    print(Border)

    if len(sys.argv) == 2:
        DirectoryPath = sys.argv[1]

        DirectoryCount(DirectoryPath)

        schedule.every(5).minutes.do(DirectoryCount, DirectoryPath)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")
        print("Please execute the script as:")
        print("python FileName.py DirectoryPath")

    print(Border)


if __name__ == "__main__":
    main()