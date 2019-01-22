#filename:class_bank.py (in chap3)
#function: using the class and _init_ and some method to process the bank operation
#_init_: the purpose of the self is that it refers to the specific object created from class like Account class

class Account:
    def __init__(self, acct_number, name):
        print("\t_init_ contstructor is processing")
        self.acct_number = acct_number
        self.name = name
        self.balance = 100
                
    def deposit(self, amount):
        print("Deposit amount is ", amount)
        if amount <= 0:
            raise ValueError('should be positive amount')
        self.balance += amount
        
    def withdraw(self, amount):
        print("Withdraw amount is ", amount)
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise RuntimeError('Your account balance is not enough!!!')

#when you use your ATM card to withdraw momey,you must pass the password first
#the while loop is used to check the password
        
while True:
    print("\nPlease key in your Card password!!!")
    passwrd=input()
    if passwrd == "222222":
        acct1 = Account("0081038000111", 'Johnny Hsu')
        break
    else:
        continue
print("your current balance of card is:", acct1.balance)

print("\n start to prcocess the class object acct1")
deposit1 = acct1.deposit
withdraw1 = acct1.withdraw
acct1.deposit(2000)
deposit1(10000)
withdraw1(5000)
print("the bank balaance is ",acct1.balance)
      
print("\n start to prcocess the class object acct2")
acct2 = Account('00810380000222', 'Sean Pan ')
deposit2 = acct2.deposit
withdraw2 = acct2.withdraw
deposit2(3000)
withdraw2(2000)
print("the bank balance is ",acct2.balance)

