def main():
    try:
        FileName = input("Enter File Name: ")
        fobj = open(FileName,"r")

        Data = fobj.read()

        print(Data)

    except FileNotFoundError as fobj:
       print("File is not present in current directory")
       
if __name__ == "__main__":
    main()