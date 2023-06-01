##2 2
class BankAccount:
    def __init__(self,account_number ,balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self):
        print(self.balance + 1000)
    def withdraw(self):
        print(self.balance - 500)
babki = BankAccount("Andriy",10000)
print(babki.deposit)