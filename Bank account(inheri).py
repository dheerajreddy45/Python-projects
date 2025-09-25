class BankAccount:
    def __init__(self,account_user, balance = 0):
        self.account_user = account_user
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}: Current balance {self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount}: Current balance: {self.balance}")
        else:
            print("Insufficient funds")
#savings account
class SavingsAccount(BankAccount):
    def __init__(self, account_user, balance = 0, interest_rate=0.5):
        super().__init__(account_user, balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}: New balance: {self.balance}")

acc = SavingsAccount("John", 1000)
acc.deposit(500)
acc.add_interest()
acc.withdraw(200)
