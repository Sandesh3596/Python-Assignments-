import time
import schedule
import datetime
import os
import shutil

def Backup(SourceFile, DestinationDirectory):

    if not os.path.isfile(SourceFile):
        print("Source file does not exist.")
        return

    if not os.path.exists(DestinationDirectory):
        os.makedirs(DestinationDirectory)

    FileName = os.path.basename(SourceFile)
    Name, Extension = os.path.splitext(FileName)

    CurrentTime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    BackupFile = Name + "_" + CurrentTime + Extension

    DestinationPath = os.path.join(DestinationDirectory, BackupFile)

    shutil.copy2(SourceFile, DestinationPath)

    fobj = open("Backup_Log.txt", "a")
    fobj.write("Backup completed successfully at : ")
    fobj.write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    fobj.write("\n")
    fobj.write("Source      : " + SourceFile + "\n")
    fobj.write("Destination : " + DestinationPath + "\n")
    fobj.write("-" * 50 + "\n")
    fobj.close()

    print("Backup completed successfully.")
    print("Backup File :", BackupFile)

def main():

    SourceFile = input("Enter Source File Path : ")
    DestinationDirectory = input("Enter Destination Directory : ")

    Backup(SourceFile, DestinationDirectory)

    schedule.every(2).seconds.do(Backup, SourceFile, DestinationDirectory)

    print("Backup Scheduler Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()