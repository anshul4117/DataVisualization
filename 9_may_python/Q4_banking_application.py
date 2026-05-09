# Q4. Menu-driven banking application using while loop with deposit,
#     withdraw, check balance, and exit functionality.

def display_menu():
    """Display the banking menu options."""
    print("\n" + "=" * 40)
    print("   BANKING APPLICATION MENU")
    print("=" * 40)
    print("  1. Deposit Money")
    print("  2. Withdraw Money")
    print("  3. Check Balance")
    print("  4. View Transaction History")
    print("  5. Exit")
    print("=" * 40)


def deposit(balance, transaction_history):
    """Deposit money into the account."""
    try:
        amount = float(input("  Enter deposit amount: Rs. "))
        if amount > 0:
            balance += amount
            transaction_history.append(f"Deposited: Rs. {amount:.2f}")
            print(f"  Successfully deposited Rs. {amount:.2f}")
            print(f"  Updated Balance: Rs. {balance:.2f}")
        else:
            print("  Deposit amount must be positive.")
    except ValueError:
        print("  Invalid input. Please enter a valid amount.")
    return balance


def withdraw(balance, transaction_history):
    """Withdraw money from the account."""
    try:
        amount = float(input("  Enter withdrawal amount: Rs. "))
        if amount <= 0:
            print("  Withdrawal amount must be positive.")
        elif amount > balance:
            print(f"  Insufficient balance! Available: Rs. {balance:.2f}")
        else:
            balance -= amount
            transaction_history.append(f"Withdrawn: Rs. {amount:.2f}")
            print(f"  Successfully withdrawn Rs. {amount:.2f}")
            print(f"  Remaining Balance: Rs. {balance:.2f}")
    except ValueError:
        print("  Invalid input. Please enter a valid amount.")
    return balance


def check_balance(balance):
    """Display the current account balance."""
    print(f"\n  Current Account Balance: Rs. {balance:.2f}")


def view_transactions(transaction_history):
    """Display the transaction history."""
    if not transaction_history:
        print("\n  No transactions yet.")
    else:
        print("\n  --- Transaction History ---")
        for index, transaction in enumerate(transaction_history, 1):
            print(f"  {index}. {transaction}")


# --- Main Program ---
print("\n" + "=" * 40)
print("   WELCOME TO PYTHON BANK")
print("=" * 40)

# Initialize account balance and transaction history
account_balance = 0.0
transactions = []

# Menu-driven loop - exits only when user chooses option 5
while True:
    display_menu()
    choice = input("  Enter your choice (1-5): ")

    if choice == '1':
        # Deposit money
        account_balance = deposit(account_balance, transactions)
    elif choice == '2':
        # Withdraw money
        account_balance = withdraw(account_balance, transactions)
    elif choice == '3':
        # Check balance
        check_balance(account_balance)
    elif choice == '4':
        # View transaction history
        view_transactions(transactions)
    elif choice == '5':
        # Exit the application
        print("\n  Thank you for using Python Bank!")
        print(f"  Final Balance: Rs. {account_balance:.2f}")
        print("  Goodbye!\n")
        break
    else:
        print("  Invalid choice! Please enter a number between 1 and 5.")

# --- Expected Output ---
# ========================================
#    WELCOME TO PYTHON BANK
# ========================================
#
# ========================================
#    BANKING APPLICATION MENU
# ========================================
#   1. Deposit Money
#   2. Withdraw Money
#   3. Check Balance
#   4. View Transaction History
#   5. Exit
# ========================================
#   Enter your choice (1-5): 1
#   Enter deposit amount: Rs. 5000
#   Successfully deposited Rs. 5000.00
#   Updated Balance: Rs. 5000.00
#
# ========================================
#    BANKING APPLICATION MENU
# ========================================
#   Enter your choice (1-5): 2
#   Enter withdrawal amount: Rs. 1500
#   Successfully withdrawn Rs. 1500.00
#   Remaining Balance: Rs. 3500.00
#
#   Enter your choice (1-5): 3
#   Current Account Balance: Rs. 3500.00
#
#   Enter your choice (1-5): 5
#   Thank you for using Python Bank!
#   Final Balance: Rs. 3500.00
#   Goodbye!
