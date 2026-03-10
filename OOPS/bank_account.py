class bank_account():
    # constructor
    def __init__(self, acc_holder, balance):
        self.acc_holder = acc_holder
        self.balance = balance

    def check_balance(self):
        return print(f"{self.acc_holder} your balance is {self.balance}")

    def deposite(self, amount):
        self.balance = self.balance+amount

    def withdraw(self, amount):
        self.balance = self.balance-amount    


john = bank_account('John', 1000)   
john.deposite(2000)
john.withdraw(100)
john.check_balance()     