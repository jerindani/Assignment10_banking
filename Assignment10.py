class MyBankAccount:
    def __init__(self, account_number, account_holder, initial_balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited ₹", amount, "\nYour new balance is ₹", self.balance)
        else:
            print("Alert! Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print("\nWithdrew ₹", amount, "\nYour new balance is ₹", self.balance)
            else:
                print("\nYou have insufficient funds in your account.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

account = MyBankAccount("1234567890", "Jerrin Mathews", 4000.0)

account.deposit(500.0)
account.withdraw(2000.0)
account.withdraw(3500.0)

print("Your final balance is ₹", account.get_balance())
