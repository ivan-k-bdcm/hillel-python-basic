class BankAccount:
    def __init__(self, balance = 0):
        self._balance = balance


    @property
    def balance(self):
        return self._balance


    def deposit(self, amount: int | float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount


    def withdraw(self, amount: int | float):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        self._balance = max(0, self._balance - amount)


bank = BankAccount(100)

print(bank.balance)
bank.deposit(200)
print(bank.balance)
bank.withdraw(1000)
print(bank.balance)