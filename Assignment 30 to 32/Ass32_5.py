import sys
import os
import time
import schedule


def DirectoryScanner(DirectoryPath):
    Border = "-" * 40
    timestamp = time.ctime()

    LogFileName = "Marvellous%s.log" % (timestamp)
    LogFileName = LogFileName.replace(" ", "_")
    LogFileName = LogFileName.replace(":", "_")

    Ret = False

    Ret = os.path.exists(DirectoryPath)

    if(Ret == False):
        print("Marvellous Automation error: There is no such Directory with name ", DirectoryPath)
        return

    Ret = os.path.isdir(DirectoryPath)

    if(Ret == False):
        print("Marvellous Automation error: It is not a Directory with Name ", DirectoryPath)
        return

    print("Log File get created with Name: ", LogFileName)

    fobj = open(LogFileName, "w")

    fobj.write(Border + "\n")
    fobj.write("Marvellous Automation Script \n")
    fobj.write(Border + "\n\n")

    fobj.write("Files from Directory are: \n\n")
    fobj.write(Border + "\n")

    TotalFiles = 0
    EmptyFiles = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):

        for fname in FileName:

            TotalFiles = TotalFiles + 1
            fname = os.path.join(FolderName, fname)

            try:
                FileSize = os.path.getsize(fname)

                fobj.write(f"{fname} : {FileSize} bytes\n")

                if(FileSize == 0):
                    EmptyFiles = EmptyFiles + 1

                    try:
                        os.remove(fname)
                        fobj.write(f"Deleted : {fname}\n")

                    except PermissionError:
                        fobj.write(f"Permission denied : {fname}\n")

            except PermissionError:
                fobj.write(f"Permission denied : {fname}\n")

    fobj.write(Border + "\n")
    fobj.write(f"Total Files Scanned: {TotalFiles}\n")
    fobj.write(f"Total Empty files found and deleted: {EmptyFiles}\n")

    fobj.write(Border + "\n")
    fobj.write("Log file get created at: " + timestamp)
    fobj.write("\n" + Border + "\n")

    fobj.close()


def main():
    Border = "-" * 40

    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to delete empty files")
            print("For better Usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as")
            print("Python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")

        else:
            schedule.every(1).hours.do(DirectoryScanner, sys.argv[1])

            while True:
                schedule.run_pending()
                time.sleep(1)

    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

    print(Border)
    print("Thank You for using Marvellous Automation Script")
    print(Border)


if __name__ == "__main__":
    main()