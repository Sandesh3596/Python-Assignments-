import sys
import os
import time
from datetime import datetime


def DirectoryScanner(DirectoryPath):
    while True:
        FileCount = 0
        FolderCount = 0

        for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
            FileCount = FileCount + len(FileName)
            FolderCount = FolderCount + len(SubFolder)

        print("Directory Scanned:", DirectoryPath)
        print("Total Files:", FileCount)
        print("Total Subdirectories:", FolderCount)
        print("Scan Time:", datetime.now())
        print("-" * 40)

        time.sleep(60)


def main():
    Border = "-" * 40
    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    if len(sys.argv) == 2:

        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This automation script is used to scan the Directory")
            print("For better Usage please check --u flag")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Please execute the script as")
            print("Python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")

        else:
            DirectoryScanner(sys.argv[1])

    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

    print(Border)
    print("Thank You for using Marvellous Automation Script")
    print(Border)


if __name__ == "__main__":
    main()