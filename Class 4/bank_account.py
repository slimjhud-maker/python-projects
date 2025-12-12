class Bank:
    def __init__(self, acc_numX, acc_nameX, balanceX):
        self.acc_num = acc_numX
        self.acc_name = acc_nameX
        self.balance = balanceX
    def __del__(self):
        print("Destructor was called to clean the RAM")
    def deposit(self):
        money_add = int(input("How much money would you like to deposit? "))
        self.balance += money_add
        print(f"Your updated balance is: {self.balance}")
    def withdraw(self):
        money_minus = int(input("How much money would you like to withdraw? "))
        if money_minus <= self.balance:
            self.balance -= money_minus
            print(f"Your updated balance is: {self.balance}")
        else:
            print("Insufficient Funds")
    def display(self):
        print(f"""
------------------------------------
Account Number: {self.acc_num}

Account Holder Name: {self.acc_name}

Account Balance: {self.balance}
------------------------------------
""")
        



jhud = Bank(123456, "Jhud", 500)
jhud.display()
jhud.deposit()
jhud.withdraw()
akash = Bank(12345, "Akash", 1000)
akash.display()
akash.deposit()
akash.withdraw()

     
        










"""
**1. Bank Account Simulation**

**Problem:**

Design a `BankAccount` class with attributes like:

- Account Number
- Account Holder Name
- Balance

Add methods to:

1. Deposit money.
2. Withdraw money (ensure sufficient balance).
3. Display account details.

 **Hint:** Use encapsulation and implement appropriate validations.
"""