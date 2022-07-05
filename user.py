class user:
    pass
    def __init__(self, name, email_address):
        self.name = name			
        self.email = email_address		
        self.account_balance = 0
    def make_deposit(self, amount):	
        self.account_balance += amount

    def make_withdrawal(self,amount):
        self.account_balance-=amount

    def display_user_balance(self):
        print(f" user: {self.name} ,  account balance: {self.account_balance}$")

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)

#Create 3 instances of the User class

#1-user1
#Have the first user make 3 deposits and 1 withdrawal and then display their balance

print('--instances 1--')
user_1= user('arwa', 'arwa@gmail.com')
user_1.make_deposit(300)
user_1.make_deposit(400)
user_1.make_deposit(500)
user_1.make_withdrawal(200)
user_1.display_user_balance()


#Have the second user make 2 deposits and 2 withdrawals and then display their balance
#2-user2
print('--instances 2--')

user_2=user('eman','eman@gmail.com')
user_2.make_deposit(600)
user_2.make_deposit(700)
user_2.make_withdrawal(400)
user_2.make_withdrawal(200)
user_2.display_user_balance()

#Have the third user make 1 deposits and 3 withdrawals and then display their balance
print('--instances 3--')
user_3= user('anoud', 'anoud@gmail.com')
user_3.make_deposit(1000)
user_3.make_withdrawal(200)
user_3.make_withdrawal(300)
user_3.make_withdrawal(100)
user_3.display_user_balance()

print('transfer money ')
user_1.transfer_money(user_3,200)
user_3.display_user_balance()
user_1.display_user_balance()