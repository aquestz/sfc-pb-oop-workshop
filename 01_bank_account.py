"""

You are tasked with developing a system to manage bank accounts.
The system should allow for the following operations:
  Deposit Money: Add a specified amount of money to a bank account.
  Withdraw Money: Subtract a specified amount of money from a bank account,
  but ensure that the account balance does not become negative.
  Check Balance: Retrieve the current balance of a bank account.
See example:

account = BankAccount(100)
account.deposit(50)
print(account.check_balance())  # Prints 150

account.withdraw(30)
print(account.check_balance())  # Prints 120

account.withdraw(100)
print(account.check_balance())  # Prints 20

account.withdraw(50)  # Prints "Insufficient funds"
print(account.check_balance())  # Prints 20


Once your classes are complete, copy and paste the above example below them in order to test their functionality
"""



"""
Write a class that meets these requirements.

Name:       BankAccount

Required state:
   * balance

Behavior:
   * check_balance()      # returns the current balance
   * deposit(amount)      # adds the new amount to the balance
   * withdraw(amount)     # removes the amount from the balance, but does not allow the balance to go negative

"""

class BankAccount:
    def __init__(self, owner, balance=100):
        self.owner = owner
        self.__balance = balance  # Private attribute (name mangling)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)
print(account.get_balance())  # Prints 150

account.withdraw(30)
print(account.get_balance())  # Prints 120

account.withdraw(100)
print(account.get_balance())  # Prints 20

account.withdraw(50)  # Prints "Insufficient funds"
print(account.get_balance())  # Prints 20