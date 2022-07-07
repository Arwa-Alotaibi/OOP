from BankAccount import BankAccount

class User:

    #attributes
    def __init__(self,name,email)  :
        pass
        self.name=name
        self.email=email
        self.account=BankAccount(int_rate=0.02 , balance=0)
        #have this method decrease the user's balance by the amount specified
    def make_withdrawal(self,amount):
        return self.account.withdraw(amount)

    def display_balance(self,amount):

        return self.account.display_account_info() 


    #specific user's account increases by the amount of the value received
    def make_deposit(self,amount):	

    	return self.account.deposit(amount)







