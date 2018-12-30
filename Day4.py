'''
Bonus Question:
Generate a four digit random number
Accept 4 Digit No from User

if the corresponding digits Matches increament Cow by 1
if not matches increament Bull by 1

for eg.
Random No : 4481
UserInput : 4281

Output:
3 Cows
1 Bull
'''
'''
import random

generate=random.randint(1000,10000)
a=int(input("Enter 4 digit number : "))
print(generate)
count=0
cows=0
bulls=0
while(count<4):
    r=int(generate%10)
    p=int(a%10)
    if r==p:
        cows+=1
    else:
        bulls+=1
    generate=(int(generate/10))
    a=(int(a/10))
    count+=1
print("{} Cows".format(cows))
print("%s Bulls"%(bulls))
'''
import random
class Cows:
    def __init__(self):
        self.cows=0
class Bulls:
    def __init__(self):
        self.bulls=0
class Calc(Cows,Bulls):
    def __init__(self):

        Cows.__init__(self)
        Bulls.__init__(self)
    def cow(self):
        self.cows+=1
    def bull(self):
        self.bulls+=1
    def calculation(self,a,b):
        print("Current Generate ", b)
        while(b>0):
            r=int(a%10)
            p=int(b%10)

            if r==p:
                self.cow()
            else:
                self.bull()
            a=int(a/10)
            b = int(b/ 10)
        print("{} Cows".format(self.cows))
        print("%s Bulls"%(self.bulls))
    def input(self):
        self.user=int(input("Enter 4 Digit Number : "))
        self.generate=random.randint(1000,10000)
        self.calculation(self.user,self.generate)


calc=Calc()
calc.input()



