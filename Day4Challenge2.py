'''
Bonus Question:

Accept a 6 digit number from user!
Let the Computer Generate Random Numbers till the generated random number matches the user input

finally

display the total number of attempts made by computer to match the user input.
'''
'''
import random
a= int(input("Enter 6 digit Number : "))
count=0
while(1):
    r=random.randint(100000,1000000)
    print(r)
    count+=1
    if r==a:
        break
    else:
        continue
print("Total number of attempts made by computer = ",count)
'''
import random
class Checking:
    def __init__(self):
        self.count=0
    def calculation(self,a):
        while(1):
            r = random.randint(100000, 1000000)
           # print(r)
            self.count += 1

            if r == a:
                break
            else:
                continue
        self.result()
    def input(self):
        self.a = int(input("Enter 6 digit Number : "))
        self.calculation(self.a)
    def result(self):
        print("Total number of attempts made by computer = %s"%(self.count))

check=Checking()
check.input()
