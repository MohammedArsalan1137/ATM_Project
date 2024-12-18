# Step 1: Define the Account class
class Account:
    def __init__(self, account_number, pin):
        self.account_number = account_number
        self.pin = pin
        self.balance = 0.0
        self.transaction_history = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")
        print(f"Deposit successful! {amount} added.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
            print(f"Withdrawal successful! {amount} deducted.")
        else:
            print("Insufficient funds!")

    def print_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

# Step 2: Define the ATM class
class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, pin):
      if account_number in self.accounts:
            print("Account already exists!")
      else:
            self.accounts[account_number] = Account(account_number, pin)
            print("Account created successfully!")

    def authenticate_account(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            print("Authentication successful!")
            return account
        else:
            print("Authentication failed.")
            return None

    def atm_menu(self, account):
        while True:
            print("\n--- ATM Menu ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. View Transaction History")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                print(f"Current Balance: {account.check_balance()}")
            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == '4':
                account.print_transaction_history()
            elif choice == '5':
                print("Exiting... Thank you for using the ATM!")
                break
            else:
                print("Invalid choice. Please try again.")

# Step 3: Create an instance of ATM and add accounts
atm = ATM()
atm.create_account("123456789", "1234")
atm.create_account("987654321", "4321")

# Step 4: Authenticate and show the menu
authenticated_account = atm.authenticate_account("123456789", "1234")
if authenticated_account:
    atm.atm_menu(authenticated_account)