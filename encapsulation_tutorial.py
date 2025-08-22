# Example of Encapsulation in Python

class BankAccount:
    # Public variable: can be accessed from anywhere
    bank_name = "Global Bank"

    def __init__(self, owner, initial_balance):
        # Protected variable (by convention): should not be accessed directly outside the class or subclass
        self._owner = owner
        # Private variable: name mangling prevents accidental access from outside the class
        self.__balance = initial_balance

    # Public method to display account details
    def display_info(self):
        print(f"Account owner: {self._owner}")
        print(f"Bank: {self.bank_name}")

    # Getter method for the private variable (__balance)
    def get_balance(self):
        return self.__balance

    # Setter method for the private variable (__balance)
    # Only allows positive values to be set, demonstrating validation logic
    def set_balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative!")
        else:
            self.__balance = amount

    # Deposit method—operates on the private balance variable
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Invalid deposit amount!")

    # Withdraw method—also encapsulates logic to avoid negative balance
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Invalid withdrawal!")

# Usage example:
account = BankAccount("Alice ♥", 1000)
account.display_info()          # Accessing public method

print("Current balance:", account.get_balance())   # Using getter

account.deposit(500)            # Deposit money safely
account.withdraw(200)           # Withdraw money safely

account.set_balance(-300)       # Attempt to set an invalid balance
account.set_balance(1200)       # Properly use setter to update balance

print("Updated balance:", account.get_balance())
