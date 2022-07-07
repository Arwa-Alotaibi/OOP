from user import User
from BankAccount import BankAccount


user_1=User('arwa','arwa@gmail.com')

user_2=User('eman','eman@gmail.com')



user_1.account.deposit(44).deposit(33).withdraw(24).display_account_info()
user_2.account.deposit(24).deposit(13).withdraw(24).display_account_info()