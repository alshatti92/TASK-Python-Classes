class Wallet:
    def __init__(self, money=0):
        self.money = money
    

    def credit(self, amount):
        self.money = amount + self.money

        # we can print for testing perpose ... print("f credit: the new amount of money is {self.money}")

    def debit(self, amount):
        self.money = self.money - amount

    def __str__(self):
        return f"this wallet has {self.money}"
        # we use this to test print.


wallet = Wallet(6)
wallet = Wallet()  # This should default money inside the wallet to 0
print(Wallet)


class Person:
    def __init__(self, name, location, money):
        self.name = name
        self.location = location
        self.wallet = wallet (money)
        
    def __str__(self):
        return f"this person is {self.name} is {self.location}"

    def move_to(self, point):
        self.location = point
        print(f"the new location for {self.name} is {self.location}")
    


person = Person("Moh", 5, 50)


class Vendor(Person):
    range = 5
    price = 1

    def __init__(self, name, location, money):
        super().__init__(name, location. money)




vendor = Vendor("Abdallah", 3, 6)


class Customer(Person):
   def __init__(self, name, location, money):
       super().__init__(name, location, money)

    
    def is_in_range(self, vendor):
        distance = abs(self.location - vendor.location)
        if distance <= vendor.range:
            print(f"this vendor {vendor.name} is within {self.name} range")
            return True
        else:
            print(f"this vendor {vendor.name} is NOT within {slef.name} range")
            return False

vendor_one = Vendor("talal", 3, 60)
vendor_two = Vendor ("lateefa", 81, 500)
customer = Customer("Abdallah", 3, 6)
