def main():
    try:
        FileName1 = input("Enter First File Name: ")
        FileName2 = input("Enter Second File Name: ")

        fobj1 = open(FileName1, "r")
        Data = fobj1.read()

        fobj2 = open(FileName2, "w")
        fobj2.write(Data)

        print("Contents copied successfully.")


    except FileNotFoundError:
        print("First file is not present in the current directory")

if __name__ == "__main__":
    main()