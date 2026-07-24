def main():
        FileName = input("Enter File Name: ")
        Word = input("Enter a Word: ")

        fobj = open(FileName, "r")

        Data = fobj.read()

        if Word in Data:
            print("The word is found in the file.")
        else:
            print("The word is not found in the file.")

        fobj.close()

if __name__ == "__main__":
    main()