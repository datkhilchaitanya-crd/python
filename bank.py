class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self):
        amt = float(input("Enter amount to deposit:"))
        self.balance = self.balance + amt 
        print("deposited:",amt)
        
    def withdraw(self):
        amt = float(input("Enter amount to withdraw"))
        if amt <= self.balance:
            self.balance = self.balance - amt
            print("withdraw:",amt)
        else:
            print("Not enough balance")
            
    def check_balance(self):
        print("current balance:",self.balance)
        
account = input("Enter Account Number:")
balance = float(input("Enter Intial balance:"))

obj = BankAccount(account,balance)

while True:
    print("\n1 Deposit")
    print("2 withdraw")
    print("3 check balance")
    print("4 exit")
    
    ch = input("Enter choice")
    
    if ch == "1":
        obj.deposit()
    elif ch == "2":
        obj.withdraw()
    elif ch == "3":
        obj.check_balance()
    elif ch == "4":
        print("Thank you")
        break
    else:
        print("wrong choice")