'''
Create a BluePrint of Banking System
where a User can
deposit
withdraw
and Check Balance
'''

class Bank:
    def __init__(self):
        self.balance=0
      #  self.B=[]
    def deposit(self):
        self.b=int(input("Enter Balance to Deposit : "))
        self.balance=self.balance+self.b
        print("{} balance is deposited".format(self.b))

    def withdraw(self):
        self.c = int(input("Enter Amount want to Withdraw : "))
        self.balance=self.balance-self.c
        print("{} balance has been Withdrawn ".format(self.c))

class Person(Bank):
    def Check(self):
        print("Total balance = {} ".format(self.balance))

p=Person()
p.deposit()
p.withdraw()
p.Check()

