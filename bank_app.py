account = {
    "owner": "Tom",
    "account": "1234",
    "balance": 100.00,
    "is_active": True,
    "transactions": []
}

def deposit(current_balance, amount):
    if amount <= 0:
        print("Invalid amount.")
        return current_balance
    account["transactions"].append(f"Deposited ${amount:.2f}")
    return current_balance + amount

def withdraw(current_balance, amount):
    if amount <=0:
        print("Invalid amount.")
        return current_balance
    elif amount <= current_balance:
        account["transactions"].append(f"Withdrew ${amount:.2f}")
        return current_balance - amount
    else:
        print("Insuficient funds.")
        return current_balance
    

def print_balance(account):
    print(f"Current balance: ${account["balance"]:.2f}")  

def print_transactions(account):
    print("\nTransactions")
    if not account["transactions"]:
        print("\tNo transactions yet.")
    for transaction in account["transactions"]:
        print("\t" + transaction)
    print()

def main():
    print(f"Welcome, {account["owner"]}! (Account #{account["account"]})")

    while True:
        print("\n--- Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. View Transactions")
        print("5. Exit")

        choice = input("Choose an option (1-5):")

        if choice == "1":
            amount = float(input("How much do you want to deposit? "))
            account["balance"] = deposit(account["balance"], amount)
            print_balance(account)
        elif choice == "2":
            amount = float(input("How much do you want to withdraw? "))
            account["balance"] = withdraw(account["balance"], amount)
            print_balance(account)
        elif choice == "3":
            print_balance(account)
        elif choice == "4":
            print_transactions(account)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()