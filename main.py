import json
import os

class BankAccount:

    def __init__(self, acc_number, name, balance=0):

        self.acc_number = acc_number
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposite(self, amount):

        if amount > 0:

            self.balance += amount
            self.transactions.append(f"Deposited : ${amount}")
            return f"Deposited : ${amount}. New Balance : ${self.balance}"
        
        return "Invalid amount to deposit !"
    
    def withdraw(self, amount):

        if 0 < amount <= self.balance:

            self.balance -= amount
            self.transactions.append(f"Withdraw : ${amount}")
            return f"Withdraw : ${amount}. New Balance : ${self.balance}"
        
        return "Insufficient balance or amount is invalid."
    
    def get_balance(self):

        return f"Account balance : ${self.balance}"
    
    def get_transaction_history(self):

        return "\n".join(self.transactions) if self.transactions else "No transactions are found."
    
class BankSystem:

    def __init__(self, db_file='accounts.json'):

        self.db_file = db_file
        self.accounts = self.load_accounts()

    def load_accounts(self):

        if os.path.exists(self.db_file):

            with open(self.db_file, "r") as file:

                return json.loads(file)
            
        return {}
    
    def save_acccounts(self):

        with open(self.db_file, "w") as file:

            json.dump(self.accounts, file, indent=4)

    
    def create_account(self, acc_number, name):

        if acc_number in self.accounts:

            return "Account is already exist."
        
        self.accounts[acc_number] = {"name":name, "balance":0, "transactions":[]}

        self.save_acccounts()

        return f"Account {acc_number} created successfully."
    
    def get_account(self, acc_number):

        if acc_number in self.accounts:

            data = self.accounts[acc_number]

            account = BankAccount(acc_number, data['name'], data['balance'])

            account.transactions = data['transactions']

            return account
        
        return None
    
    def update_account(self, account):

        self.accounts[account.acc_number] = {

            "name":account.name,
            "balance":account.balance,
            "transactions":account.transactions

        }

        self.save_acccounts()

def main():

    bank = BankSystem()

    while True:

        print("\n---Advanced Banking System---")

        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter your choice :")

        if choice == "1":

            acc_number = input("Enter Account Number: ")

            name = input("Enter Account Holder Name : ")

            print(bank.create_account(acc_number, name))

        elif choice == "2":

            acc_number = input("Enter Account Number : ")

            account = bank.get_account(acc_number)

            if account:

                amount = float(input("Enter depost amount : "))
                
                print(account.deposite(amount))

                bank.update_account(account)

            else:

                print("Account not found!")

        elif choice == "3":

            acc_number = input("Enter Account Number : ")

            account = bank.get_account(acc_number)

            if account:

                amount = float(input("Enter withdrawal amount : "))
                
                print(account.withdraw(amount))

                bank.update_account(account)

            else:

                print("Account not found!")

        elif choice == "4":

            acc_number = input("Enter Account Number : ")

            account = bank.get_account(acc_number)

            if account:

                print(account.get_balance())

            else:

                print("Account not found!")

        elif choice == "5":

            acc_number = input("Enter Account Number : ")

            account = bank.get_account(acc_number)

            if account:

                print("\nTransaction History :")
                print(account.get_transaction_history())

            else:

                print("Account not found!")  

        elif choice == "6":

            print("Thank you for using Advanced Banking System!")

            break

        else:

            print("Invalid choice! Please enter a valid option.")


if __name__ == "__main__":

    main()
