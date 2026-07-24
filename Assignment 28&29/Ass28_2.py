def main():
    try:
        FileName = input("Enter a File Name: ")
        fobj =open(FileName,"r")

        Data = fobj.read()
        Words = Data.split()
        print("The words in File: ",len(Words))

    except FileNotFoundError as fobj:
       print("File is not present in current directory")
       
if __name__ == "__main__":
    main()