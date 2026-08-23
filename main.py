from datetime import datetime


# ==========================================
# ACCOUNT CLASS
# ==========================================

class Account:

    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self._balance = balance
        self.transactions = []

    # --------------------------------------
    # Deposit Money
    # --------------------------------------

    def deposit(self, amount):

        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return False

        self._balance += amount

        self.transactions.append({
            "type": "Deposit",
            "amount": amount,
            "balance": self._balance,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "description": "Money deposited"
        })

        print(f"₹{amount:.2f} deposited successfully.")
        print(f"Updated Balance: ₹{self._balance:.2f}")

        return True

    # --------------------------------------
    # Withdraw Money
    # --------------------------------------

    def withdraw(self, amount):

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return False

        if amount > self._balance:
            print("Insufficient balance.")
            return False

        self._balance -= amount

        self.transactions.append({
            "type": "Withdrawal",
            "amount": amount,
            "balance": self._balance,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "description": "Money withdrawn"
        })

        print(f"₹{amount:.2f} withdrawn successfully.")
        print(f"Updated Balance: ₹{self._balance:.2f}")

        return True

    # --------------------------------------
    # Get Balance
    # --------------------------------------

    def get_balance(self):
        return self._balance

    # --------------------------------------
    # Display Account
    # --------------------------------------

    def display_account(self):

        print("\n========== ACCOUNT DETAILS ==========")
        print("Account Number:", self.account_number)
        print("Account Holder:", self.name)
        print("Account Type:", self.account_type)
        print("Balance: ₹", f"{self._balance:.2f}")

    # --------------------------------------
    # Transaction History
    # --------------------------------------

    def show_transaction_history(self):

        print("\n========== TRANSACTION HISTORY ==========")

        if not self.transactions:
            print("No transactions found.")
            return

        for index, transaction in enumerate(
            self.transactions,
            start=1
        ):

            print(f"\nTransaction {index}")
            print("Date:", transaction["date"])
            print("Type:", transaction["type"])
            print("Amount: ₹", f"{transaction['amount']:.2f}")
            print(
                "Balance After Transaction: ₹",
                f"{transaction['balance']:.2f}"
            )
            print("Description:", transaction["description"])


# ==========================================
# SAVINGS ACCOUNT
# ==========================================

class SavingsAccount(Account):

    def __init__(
        self,
        account_number,
        name,
        balance=0
    ):

        super().__init__(
            account_number,
            name,
            balance
        )

        self.account_type = "Savings"
        self.interest_rate = 5.0

    def calculate_interest(self):

        return self._balance * self.interest_rate / 100


# ==========================================
# CURRENT ACCOUNT
# ==========================================

class CurrentAccount(Account):

    def __init__(
        self,
        account_number,
        name,
        balance=0
    ):

        super().__init__(
            account_number,
            name,
            balance
        )

        self.account_type = "Current"
        self.interest_rate = 2.0

    def calculate_interest(self):

        return self._balance * self.interest_rate / 100


# ==========================================
# BANK CLASS
# ==========================================

class Bank:

    def __init__(self):

        self.accounts = {}

    # --------------------------------------
    # Create Account
    # --------------------------------------

    def create_account(
        self,
        account_number,
        name,
        account_type,
        initial_deposit
    ):

        if account_number in self.accounts:

            print("Account number already exists.")
            return False

        if not name.strip():

            print("Account holder name cannot be empty.")
            return False

        if initial_deposit < 0:

            print("Initial deposit cannot be negative.")
            return False

        if account_type.lower() == "savings":

            account = SavingsAccount(
                account_number,
                name,
                initial_deposit
            )

        elif account_type.lower() == "current":

            account = CurrentAccount(
                account_number,
                name,
                initial_deposit
            )

        else:

            print("Invalid account type.")
            return False

        self.accounts[account_number] = account

        print("\nAccount created successfully!")
        print("Account Number:", account_number)

        return True

    # --------------------------------------
    # Find Account
    # --------------------------------------

    def find_account(self, account_number):

        return self.accounts.get(account_number)

    # --------------------------------------
    # Deposit Money
    # --------------------------------------

    def deposit_money(
        self,
        account_number,
        amount
    ):

        account = self.find_account(account_number)

        if account is None:

            print("Account not found.")
            return

        account.deposit(amount)

    # --------------------------------------
    # Withdraw Money
    # --------------------------------------

    def withdraw_money(
        self,
        account_number,
        amount
    ):

        account = self.find_account(account_number)

        if account is None:

            print("Account not found.")
            return

        account.withdraw(amount)

    # --------------------------------------
    # Display Account
    # --------------------------------------

    def display_account(self, account_number):

        account = self.find_account(account_number)

        if account is None:

            print("Account not found.")
            return

        account.display_account()

    # --------------------------------------
    # Transaction History
    # --------------------------------------

    def show_transaction_history(
        self,
        account_number
    ):

        account = self.find_account(account_number)

        if account is None:

            print("Account not found.")
            return

        account.show_transaction_history()

    # --------------------------------------
    # Show All Accounts
    # --------------------------------------

    def show_all_accounts(self):

        print("\n========== ALL ACCOUNTS ==========")

        if not self.accounts:

            print("No accounts available.")
            return

        for account in self.accounts.values():

            print(
                f"Account: {account.account_number} | "
                f"Name: {account.name} | "
                f"Type: {account.account_type} | "
                f"Balance: ₹{account.get_balance():.2f}"
            )


# ==========================================
# INPUT VALIDATION
# ==========================================

def get_amount(message):

    try:

        amount = float(input(message))

        if amount < 0:

            print("Amount cannot be negative.")
            return None

        return amount

    except ValueError:

        print("Please enter a valid number.")
        return None


# ==========================================
# CREATE ACCOUNT MENU
# ==========================================

def create_account_menu(bank):

    print("\n========== CREATE ACCOUNT ==========")

    account_number = input(
        "Enter Account Number: "
    ).strip()

    name = input(
        "Enter Account Holder Name: "
    ).strip()

    account_type = input(
        "Enter Account Type (Savings/Current): "
    ).strip()

    initial_deposit = get_amount(
        "Enter Initial Deposit: ₹"
    )

    if initial_deposit is None:
        return

    bank.create_account(
        account_number,
        name,
        account_type,
        initial_deposit
    )


# ==========================================
# MAIN MENU
# ==========================================

def main():

    bank = Bank()

    while True:

        print("\n")
        print("=" * 50)
        print("        PYTHON BANKING SYSTEM")
        print("=" * 50)

        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance")
        print("6. Transaction History")
        print("7. View All Accounts")
        print("8. Calculate Interest")
        print("9. Exit")

        print("=" * 50)

        choice = input(
            "Enter your choice (1-9): "
        ).strip()

        # ----------------------------------
        # Create Account
        # ----------------------------------

        if choice == "1":

            create_account_menu(bank)

        # ----------------------------------
        # View Account
        # ----------------------------------

        elif choice == "2":

            account_number = input(
                "Enter Account Number: "
            ).strip()

            bank.display_account(account_number)

        # ----------------------------------
        # Deposit
        # ----------------------------------

        elif choice == "3":

            account_number = input(
                "Enter Account Number: "
            ).strip()

            amount = get_amount(
                "Enter Deposit Amount: ₹"
            )

            if amount is not None:

                bank.deposit_money(
                    account_number,
                    amount
                )

        # ----------------------------------
        # Withdraw
        # ----------------------------------

        elif choice == "4":

            account_number = input(
                "Enter Account Number: "
            ).strip()

            amount = get_amount(
                "Enter Withdrawal Amount: ₹"
            )

            if amount is not None:

                bank.withdraw_money(
                    account_number,
                    amount
                )

        # ----------------------------------
        # Check Balance
        # ----------------------------------

        elif choice == "5":

            account_number = input(
                "Enter Account Number: "
            ).strip()

            account = bank.find_account(
                account_number
            )

            if account:

                print(
                    f"\nCurrent Balance: "
                    f"₹{account.get_balance():.2f}"
                )

            else:

                print("Account not found.")

        # ----------------------------------
        # Transaction History
        # ----------------------------------

        elif choice == "6":

            account_number = input(
                "Enter Account Number: "
            ).strip()

            bank.show_transaction_history(
                account_number
            )

        # ----------------------------------
        # View All Accounts
        # ----------------------------------

        elif choice == "7":

            bank.show_all_accounts()

        # ----------------------------------
        # Calculate Interest
        # ----------------------------------

        elif choice == "8":

            account_number = input(
                "Enter Account Number: "
            ).strip()

            account = bank.find_account(
                account_number
            )

            if account:

                interest = account.calculate_interest()

                print(
                    f"\nInterest for "
                    f"{account.account_type} Account: "
                    f"₹{interest:.2f}"
                )

            else:

                print("Account not found.")

        # ----------------------------------
        # Exit
        # ----------------------------------

        elif choice == "9":

            print(
                "\nThank you for using "
                "Python Banking System!"
            )

            break

        else:

            print(
                "\nInvalid choice. "
                "Please enter a number between 1 and 9."
            )


# ==========================================
# PROGRAM START
# ==========================================

if __name__ == "__main__":
    main()
