class BankAccount:
    def __init__(self, name, amount, interest_rate):
        self.name = name
        self.amount = amount
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.amount *= (1 + self.interest_rate / 100)

account = BankAccount('Juan De Hattatime', 1000, 3)
account.apply_interest()
print(account.amount)
account.interest_rate = 2
account.apply_interest()
print(account.amount)