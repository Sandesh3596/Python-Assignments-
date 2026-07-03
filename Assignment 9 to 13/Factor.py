
def main():
  Ret = int(input("Enter a number: "))
  print("The factors are: ")

  for i in range(1, Ret + 1):
     if Ret % i == 0 :
        print(i)

if __name__ == "__main__":
    main()