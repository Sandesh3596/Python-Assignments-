import os

def main():
    A = input("Enter File Name: ")

    if(os.path.exists(A)):
        print("File is present in current directory")

    else:
        print("There is no such file")
if __name__ == "__main__":
    main()
    