def main():
    File = input("Enter File Name: ")
    Word = input("Enter String: ")

    fobj = open(File, "r")
    Data = fobj.read()
    fobj.close()

    Count = Data.count(Word)

    print("Frequency of word is", Count)

if __name__ == "__main__":
    main()