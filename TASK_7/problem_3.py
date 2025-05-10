class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposit(self, amount):
        self.balance += amount

    def Withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount

    def bankFees(self):
        self.balance -= self.balance * 0.05

    def display(self):
        print(f"Account Number : {self.accountNumber}")
        print(f"Account Name : {self.name}")
        print(f"Account Balance : {self.balance} $")

# Example usage
account = BankAccount(2178514584, "Ahmed", 3000)
account.Withdrawal(500)
account.bankFees()
account.display()