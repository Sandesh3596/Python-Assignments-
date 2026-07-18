class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder Name:", self.Name)
        print("Current Balance:", self.Amount)

    def Deposit(self):
        deposit_amount = float(input("Enter amount to deposit: "))
        self.Amount += deposit_amount
        print("Amount deposited successfully.")

    def Withdraw(self):
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount <= self.Amount:
            self.Amount -= withdraw_amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance! Withdrawal not allowed.")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


acc1 = BankAccount("Sandy", 5000)

print("Account 1")
acc1.Display()
acc1.Deposit()
acc1.Display()
acc1.Withdraw()
acc1.Display()
print("Interest =", acc1.CalculateInterest())

acc2 = BankAccount("Rutuja", 10000)

print("Account 2")
acc2.Display()
acc2.Deposit()
acc2.Display()
acc2.Withdraw()
acc2.Display()
print("Interest =", acc2.CalculateInterest())