def Vowel(Chr):
    return Chr.lower () in "aeiou"

def main():
    Chr = input("Enter a character: ")

    if Vowel(Chr):
        print("This is a Vowel")
    else:
        print("This is Consonant")
        
if __name__ == "__main__":
    main()