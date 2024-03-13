class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} into account {self.account_number}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount} from account {self.account_number}. New balance: ${self.balance}.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_number, holder_name, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, holder_name, initial_balance)
            print(f"Account {account_number} for {holder_name} added to the bank.")
        else:
            print(f"Account {account_number} already exists.")

    def remove_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} removed from the bank.")
        else:
            print(f"Account {account_number} does not exist.")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

# Interactive usage
bank = Bank()

while True:
    print("\n1. Add Account")
    print("2. Remove Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        account_number = input("Enter account number: ")
        holder_name = input("Enter account holder name: ")
        initial_balance = float(input("Enter initial balance: "))
        bank.add_account(account_number, holder_name, initial_balance)
    elif choice == '2':
        account_number = input("Enter account number to remove: ")
        bank.remove_account(account_number)
    elif choice == '3':
        account_number = input("Enter account number to deposit into: ")
        amount = float(input("Enter amount to deposit: "))
        account = bank.get_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print(f"Account {account_number} not found.")
    elif choice == '4':
        account_number = input("Enter account number to withdraw from: ")
        amount = float(input("Enter amount to withdraw: "))
        account = bank.get_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print(f"Account {account_number} not found.")
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
