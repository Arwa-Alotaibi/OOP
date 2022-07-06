class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate=0.1
        self.balance=balance

    def deposit(self, amount):

        self.balance+=amount
        print(f"your deposit is : ${amount}")
        return self
    def withdraw(self, amount):
        if(self.balance < amount):
            print(f'Insufficient funds: Charging a $5 fee" and deduct $5')
            #print(f'your amount is ${amount} is more than balance')
            self.balance = self.balance - 5
        else:
            self.balance-=amount
            print(f"has been withdrawn succefully ${amount}, and the balance is: ${self.balance}")
            return self
                        
    def display_account_info(self) :
        print(f"your balance is: ${self.balance}")


    def yield_interest(self):
        if self.balance >0:
            self.balance+=self.balance*self.int_rate
            print(f"the yield interset is : {self.balance}")
            return self
        elif self.balance < 0 :

            print('the balance is negative')


    
Arwa=BankAccount(0.01,77)
Eman = BankAccount(0.01,100)
#To the first account, make 3 deposits and 1 withdrawal, 
# then yield interest and display the account's info all in one line of code (i.e. chaining)
print('Arwa')
Arwa.deposit(30).deposit(50).deposit(60).withdraw(20).yield_interest().display_account_info()
print('Eman')
#To the second account, make 2 deposits and 4 withdrawals, 
# then yield interest and display the account's info all in one line of code (i.e. chaining)
Eman.deposit(30).deposit(40).withdraw(20).withdraw(10).withdraw(5).withdraw(4).yield_interest().display_account_info()
