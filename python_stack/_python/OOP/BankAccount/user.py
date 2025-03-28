from bankaccount import Bankaccount

class User:
    def __init__(self, first_name, email, balance):
        self.name=first_name
        self.email=email
        self.bankaccount=Bankaccount(balance)

    def make_withdrawal(self, amount):
        self.bankaccount.balance -=amount
        return self

    def display_user_balance(self):
        print(self.name, self.bankaccount.balance)

    def transfer(self, other_user, amount):
        other_user.bankaccount.balance +=amount
        self.bankaccount.balance -=amount
        return self
        
    def make_deposit(self, amount):
        self.bankaccount.balance +=amount
        return self
        
