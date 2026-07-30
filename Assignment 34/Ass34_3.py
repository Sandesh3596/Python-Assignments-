import sys
import psutil
import os
import time

def ProcessScan():

    ProcessList = []

    try:
        for proc in psutil.process_iter(["pid", "name", "username"]):
            try:
                info = {
                    "pid": proc.info["pid"],
                    "name": proc.info["name"] or "N/A",
                    "username": proc.info["username"] or "N/A"
                }
                ProcessList.append(info)

            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):
                pass

    except Exception:
        return []

    return ProcessList


def CreateLog(DirectoryName, Data):

    try:

        if not os.path.exists(DirectoryName):
            os.mkdir(DirectoryName)

        FileName = os.path.join(
            DirectoryName,
            "ProcessLog_" + time.strftime("%Y%m%d_%H%M%S") + ".txt"
        )

        with open(FileName, "w") as fobj:

            Border = "-" * 50

            fobj.write(Border + "\n")
            fobj.write("Running Process Information\n")
            fobj.write("Log Created At : " + time.ctime() + "\n")
            fobj.write(Border + "\n\n")

            for info in Data:
                fobj.write("PID       : %s\n" % info["pid"])
                fobj.write("Name      : %s\n" % info["name"])
                fobj.write("Username  : %s\n" % info["username"])
                fobj.write(Border + "\n")

    except Exception as e:
        print(e)


def main():

    DirectoryName = sys.argv[1]

    Data = ProcessScan()
    

    CreateLog(DirectoryName, Data)


if __name__ == "__main__":
    main()