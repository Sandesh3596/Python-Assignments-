import time
import schedule
import datetime


def monitor():
    CurrentTime = datetime.datetime.now()

    FileName = "Demo.txt"

    print("Reading File :", FileName)

    try:
        fobj = open(FileName, "r")

        Data = fobj.read()

        if Data == "":
            print("File is empty")

        else:
            print("File Contents :")
            print(Data)

        fobj.close()

    except FileNotFoundError:
        print("File does not exist")

    except PermissionError:
        print("Permission denied")

    except OSError:
        print("File cannot be opened")


def main():
    schedule.every(1).minutes.do(monitor)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()