 #oops
"""class Student:
    
    def __init__(self,name,marks):
        self.name= name
        self.marks= marks
        
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
            print("hi",self.name,"your core is ",sum/3)
    
s1 = Student("ali",[21,77,66])
s1.get_avg()"""


"""class Account:
    def __init__(self, acc, bal):
        self.account = acc
        self.balance = bal

    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("Total balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("Total balance =", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 12384)

acc1.debit(1000)
acc1.credit(200)
acc1.credit(400)
acc1.debit(230)"""
        

"""class Student:
    def __init__(self,name):
        self.__name=name
        
s1=Student("alish")
del s1.name
print(s1)"""

#project
# guess the random number 
import random
target = random.randint(1,100)

while True:
    userChoice = input("guess the target or Quit(Q) :")
    if( userChoice == "Q"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("your number was too small. Taking a bigger guess..")
    else:
        print("your number was too big. Take a smaller guess..")
        
    print("---GAME OVER 1234---")
    
         

