import sys
import os
import shutil
import time
import schedule
import datetime


def CopyFiles(Source, Destination):
    
    Ret = False

    Ret = os.path.exists(Source)

    if Ret == False:
        print("Source path is Invalid")
        return

    Ret = os.path.isdir(Source)

    if Ret == False:
        print("Source is not Directory")
        return

    Ret = os.path.exists(Destination)

    if Ret == False:
        print("Destination path is Invalid")
        return

    Ret = os.path.isdir(Destination)

    if Ret == False:
        print("Destination is not Directory")
        return

    LogFile = open("CopyLog.txt", "a")

    for FolderName, Subfolder, FileName in os.walk(Source):

        for Fname in FileName:

            if Fname.endswith(".txt"):

                SourceFile = os.path.join(FolderName, Fname)

                DestinationFile = os.path.join(Destination, Fname)

                try:
                    shutil.copy(SourceFile, DestinationFile)

                    CurrentTime = datetime.datetime.now()

                    LogFile.write(
                        Fname + " copied at " +
                        CurrentTime.strftime("%d/%m/%Y %H:%M:%S") + "\n"
                    )

                    print(Fname, "copied successfully")

                except Exception as e:
                    print("Unable to copy :", Fname)
                    print("Error :", e)

    LogFile.close()


def main():

    Source = input("Enter source directory : ")
    Destination = input("Enter destination directory : ")

    CopyFiles(Source, Destination)

    schedule.every(10).minutes.do(CopyFiles, Source, Destination)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()