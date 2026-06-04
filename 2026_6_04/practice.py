class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        if amount<0:
            return
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance<amount:
            print("余额不足")
            return
        self.balance-=amount
    def show(self):
        print(f"账户:{self.name}")
        print(f"余额:{self.balance}")
    def transfer(self,other,amount):
        if self.balance<amount:
            print("余额不足")
            return
        self.balance-=amount
        other.balance+=amount
tom=BankAccount('Tom',100)
jack=BankAccount('Jack',200)
tom.transfer(jack,50)
tom.show()
jack.show()


        
