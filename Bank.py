class Bank_account:
    def __init__(self,name,opening_balance):
        self.name=name
        self.balance=opening_balance

    def deposit(self,ammount):
        self.balance += ammount

    def withdraw(self,ammount):
        self.balance-=ammount

    def get_balance(self):
        print("Hi {} your balance is {}".format(self.name, self.balance))

user = Bank_account("Ramesh",0)
user.deposit(100)
user.deposit(200)
user.deposit(500)

user.withdraw(50)
user.get_balance()