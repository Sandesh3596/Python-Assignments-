import os

def main():
    SourceFile = "ABC.txt"

    if os.path.exists(SourceFile):
        fobj1 = open(SourceFile, "r")
        Data = fobj1.read()
        fobj1.close()

        fobj2 = open("Demo.txt", "w")
        fobj2.write(Data)
        fobj2.close()

        print("Contents copied successfully into Demo.txt")
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()