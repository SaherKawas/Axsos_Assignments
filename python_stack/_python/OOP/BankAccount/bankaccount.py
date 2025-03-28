class Bankaccount:
    def __init__(self, balance=1000, interest_rate=0.01):
        self.balance=balance
        self.interest_rate=interest_rate

    def deposit(self, amount):
        self.balance +=amount
    
    def withdraw(self, amount):
        if self.balance>= amount:
            self.balance -=amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -=5

    def display_account_info(self):
        
        print(f"Balance: ${self.balance}")
    
    
    def yield_interest(self):
        if self.balance>0:
            self.balance +=self.balance*self.interest_rate
