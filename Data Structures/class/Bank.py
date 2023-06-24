class BankAccount:
    

    
    def __init__(self):
        self.ac=int(input("Enter Account Number"))
        self.balance=float(input("Enter the balance"))
        self.dof=input("Enter Date of opening")
        self.cn=input("Enter customer name")

    def deposit(self):
        amount=float(input("Enter Deposit Amount"))
        self.balance += amount
        print("\n Amount Deposited:",amount)


    def withdraw(self):
        amount = float(input("Enter Withdraw Amount:"))
        if self.balance>amount:
            self.balance -= amount
            print("\n Amount withdrawn:",amount)
            print("\nTotal Amount in Account:",self.balance)
        else:
            print("\nInsufficient Balance")

            
    def check_balance(self):
        print("\nTotal Amount in Account:",self.balance)

obj = BankAccount()






        




    
