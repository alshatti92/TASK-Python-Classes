class Wallet:
    def __init__(self, money):
        self.money = money
       


    def credit(self, amount):
        self.money = amount + self.money

    def debit(self, amount):
        self.money = self.money - amount


wallet = Wallet(6)
wallet = Wallet(0)  # This should default money inside the wallet to 0
print(Wallet)

wallet ():
amount = 5
credit = 
class Person:
    def __init__(self, name, location, wallet, moveto):
        self.name = name
        self.location = location
        self.wallet = wallet
        self.moveto = moveto
        pass
    # Implement the code here
    pass


person = Person("Moh", 5, 50)


class Vendor:
    # implement Vendor!
    pass


vendor = Vendor("Abdallah", 3, 6)


class Customer:
    # implement Customer!
    pass


customer = Customer("Abdallah", 3, 6)
