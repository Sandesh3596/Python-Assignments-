def main():
    try:
        FileName = input("Enter a File Name: ")
        fobj =open(FileName,"r")

        Data = fobj.read()
        print("The content in File one by one: ",(Data))

    except FileNotFoundError as fobj:
       print("File is not present in current directory")
       
if __name__ == "__main__":
    main()