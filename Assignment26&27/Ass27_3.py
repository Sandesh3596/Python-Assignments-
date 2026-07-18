class Number:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        count = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                count += 1

        if count == 2:
            return True
        else:
            return False

    def ChkPerfect(self):
        Sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum += i

        if Sum == self.Value:
            return True
        else:
            return False

    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        Sum = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                Sum += i
        return Sum


obj1 = Number(int(input("Enter first number: ")))
obj2 = Number(int(input("Enter second number: ")))

print("\nFirst Number: ",obj1.Value)
print("Prime:", obj1.ChkPrime())
print("Perfect:", obj1.ChkPerfect())
obj1.Factors()
print("Sum of Factors:", obj1.SumFactors())

print("\nSecond Number: ",obj2.Value)
print("Prime:", obj2.ChkPrime())
print("Perfect:", obj2.ChkPerfect())
obj2.Factors()
print("Sum of Factors:", obj2.SumFactors())