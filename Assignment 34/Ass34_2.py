import sys
import psutil
import time

def ProcessScan(ProcessName):

    ProcessList = []

    try:
        for proc in psutil.process_iter(["pid", "name", "username"]):
            try:
                if proc.info["name"] and proc.info["name"].lower() == ProcessName.lower():

                    info = {
                        "pid": proc.info["pid"],
                        "name": proc.info["name"],
                        "username": proc.info["username"] or "N/A"
                    }

                    ProcessList.append(info)

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess
            ):
                pass

    except Exception:
        return []

    return ProcessList


def CreateLog(FileName, ProcessName, Data):

    try:
        with open(FileName, "w") as fobj:

            Border = "-" * 50

            fobj.write(Border + "\n")
            fobj.write("Process Information\n")
            fobj.write("Log Created At : " + time.ctime() + "\n")
            fobj.write(Border + "\n\n")

            if len(Data) == 0:
                fobj.write("Process '" + ProcessName + "' is not running.\n")

            else:
                fobj.write("Process '" + ProcessName + "' is running.\n\n")

                for info in Data:
                    fobj.write("PID       : %s\n" % info["pid"])
                    fobj.write("Name      : %s\n" % info["name"])
                    fobj.write("Username  : %s\n" % info["username"])
                    fobj.write(Border + "\n")

    except Exception as e:
        print("Unable to create log file :", e)


def main():

    if len(sys.argv) != 3:
        sys.exit()

    ProcessName = sys.argv[1]
    FileName = "ProcessLog.txt"

    Data = ProcessScan(ProcessName)

    CreateLog(FileName, ProcessName, Data)


if __name__ == "__main__":
    main()