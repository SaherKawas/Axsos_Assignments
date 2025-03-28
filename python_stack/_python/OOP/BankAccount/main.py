from user import User
from bankaccount import Bankaccount

Tom=User("Tom", "tom@gmail.com", 0)
Brad=User("Brad", "brad@gmail.com", 0)
Ron=User("Ron", "ron@gmail.com", 0)

Tom.make_deposit(1500).make_deposit(2000).make_deposit(4000).make_withdrawal(1000).transfer(Ron,1000).display_user_balance()

Brad.make_deposit(20000).make_deposit(3000).make_withdrawal(4000).make_withdrawal(1000).display_user_balance()

Ron.make_deposit(10000).make_withdrawal(1500).make_withdrawal(500).make_withdrawal(500).display_user_balance()


