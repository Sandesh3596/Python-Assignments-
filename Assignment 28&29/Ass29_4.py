import sys

def main():
    File1 = sys.argv[1]
    File2 = sys.argv[2]

    fobj1 = open(File1, "r")
    fobj2 = open(File2, "r")

    Data1 = fobj1.read()
    Data2 = fobj2.read()

    fobj1.close()
    fobj2.close()

    if Data1 == Data2:
        print("Success")
    else:
        print("Failure")

if __name__ == "__main__":
    main()