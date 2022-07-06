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
            print(f'your amount is ${amount} is more than balance')
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

                