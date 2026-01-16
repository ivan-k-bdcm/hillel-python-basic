"""
class BankAccount:
    bank_name = "PrivatBank"



    def __init__(self, balance = 0):
        self.balance = balance


    def deposit(self, amount: int | float) -> int | float:
        self.balance += amount

        return self.balance

    def withdraw(self, amount: int | float) -> int | float:
        self.balance = max(0, self.balance - amount)

        return self.balance



bank1 = BankAccount()
print(bank1.bank_name)

bank1.deposit(200)
bank1.withdraw(50)
print(bank1.balance)

bank2 = BankAccount()
print(bank2.bank_name)

bank2.deposit(100)
bank2.withdraw(200)
print(bank2.balance)
"""

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value >= -273.15:
            self._celsius = value
        else:
            print('Celsius cannot be lower than -273.15')





temp = Temperature(100)

temp.celsius = 200
print(temp.celsius)

temp.celsius = -300
print(temp.celsius)