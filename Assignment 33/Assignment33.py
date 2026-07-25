import os
import sys
import time
from datetime import datetime
from Marvellous import *


def CreateLogDirectory():

    if not os.path.exists("Marvellous"):
        os.mkdir("Marvellous")


def CreateLogFile():

    Current = datetime.now()

    Name = "DuplicateRemovalLog_"
    Name = Name + Current.strftime("%d_%m_%Y_%H_%M_%S")
    Name = Name + ".log"

    return os.path.join("Marvellous", Name)


def RemoveDuplicates(Path, LogFile):

    Data = FindDuplicates(Path)

    TotalFiles = 0
    DeletedFiles = 0

    fobj = open(LogFile, "w")

    fobj.write("Directory : " + Path + "\n")
    fobj.write("Starting Time : " + str(datetime.now()) + "\n\n")

    for Key in Data:

        if len(Data[Key]) > 1:

            TotalFiles += len(Data[Key])

            for Name in Data[Key][1:]:

                try:

                    os.remove(Name)

                    DeletedFiles += 1

                    fobj.write("Deleted : " + Name + "\n")

                except:

                    fobj.write("Unable to delete : " + Name + "\n")

    fobj.write("\nTotal Duplicate Files : ")
    fobj.write(str(TotalFiles))

    fobj.write("\nDuplicate Files Deleted : ")
    fobj.write(str(DeletedFiles))

    fobj.write("\nCompletion Time : ")
    fobj.write(str(datetime.now()))

    fobj.close()


def main():

    if len(sys.argv) != 4:

        print("Usage :")
        print("python DuplicateFileRemoval.py Directory Interval Email")
        sys.exit()

    Directory = sys.argv[1]
    Interval = int(sys.argv[2])
    Email = sys.argv[3]

    while True:

        CreateLogDirectory()

        LogFile = CreateLogFile()

        RemoveDuplicates(Directory, LogFile)

        time.sleep(Interval * 60)


if __name__ == "__main__":
    main()