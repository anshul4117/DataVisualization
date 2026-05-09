# Q36. ATM simulation program with PIN validation and account lockout
#      after three invalid attempts.

def validate_pin(correct_pin, max_attempts=3):
    """Validate PIN with a maximum number of attempts."""
    attempts = 0

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        entered_pin = input(f"  Enter your 4-digit PIN ({remaining} attempt(s) left): ").strip()

        # Check if PIN is numeric and 4 digits
        if not entered_pin.isdigit() or len(entered_pin) != 4:
            print("  ⚠️  PIN must be exactly 4 digits.")
            attempts += 1
            continue

        if entered_pin == correct_pin:
            print("  ✅ PIN verified successfully!")
            return True
        else:
            attempts += 1
            if attempts < max_attempts:
                print(f"  ❌ Incorrect PIN. {max_attempts - attempts} attempt(s) remaining.")
            else:
                print("  ❌ Incorrect PIN.")

    return False


def display_atm_menu():
    """Display ATM menu options."""
    print("\n" + "=" * 40)
    print("   ATM MENU")
    print("=" * 40)
    print("  1. Check Balance")
    print("  2. Deposit Money")
    print("  3. Withdraw Money")
    print("  4. Change PIN")
    print("  5. Mini Statement")
    print("  6. Exit")
    print("=" * 40)


def check_balance(balance):
    """Display account balance."""
    print(f"\n  💰 Your Current Balance: Rs. {balance:,.2f}")


def deposit_money(balance, transactions):
    """Deposit money into the account."""
    try:
        amount = float(input("  Enter deposit amount: Rs. "))
        if amount <= 0:
            print("  ⚠️  Amount must be positive.")
            return balance
        balance += amount
        transactions.append(f"Deposited  : +Rs. {amount:,.2f}")
        print(f"  ✅ Rs. {amount:,.2f} deposited successfully!")
        print(f"  💰 New Balance: Rs. {balance:,.2f}")
    except ValueError:
        print("  ❌ Invalid amount.")
    return balance


def withdraw_money(balance, transactions):
    """Withdraw money from the account."""
    try:
        amount = float(input("  Enter withdrawal amount: Rs. "))
        if amount <= 0:
            print("  ⚠️  Amount must be positive.")
            return balance
        if amount > balance:
            print(f"  ❌ Insufficient balance! Available: Rs. {balance:,.2f}")
            return balance
        if amount > 25000:
            print("  ⚠️  Maximum withdrawal limit is Rs. 25,000 per transaction.")
            return balance
        balance -= amount
        transactions.append(f"Withdrawn  : -Rs. {amount:,.2f}")
        print(f"  ✅ Rs. {amount:,.2f} withdrawn successfully!")
        print(f"  💰 Remaining Balance: Rs. {balance:,.2f}")
    except ValueError:
        print("  ❌ Invalid amount.")
    return balance


def change_pin(current_pin):
    """Change the ATM PIN."""
    old_pin = input("  Enter current PIN: ").strip()
    if old_pin != current_pin:
        print("  ❌ Current PIN is incorrect.")
        return current_pin

    new_pin = input("  Enter new 4-digit PIN: ").strip()
    if not new_pin.isdigit() or len(new_pin) != 4:
        print("  ⚠️  PIN must be exactly 4 digits.")
        return current_pin

    confirm_pin = input("  Confirm new PIN: ").strip()
    if new_pin != confirm_pin:
        print("  ❌ PINs do not match.")
        return current_pin

    print("  ✅ PIN changed successfully!")
    return new_pin


def mini_statement(transactions, balance):
    """Display mini statement of recent transactions."""
    print("\n  --- Mini Statement ---")
    if not transactions:
        print("  No transactions yet.")
    else:
        # Show last 5 transactions
        recent = transactions[-5:]
        for txn in recent:
            print(f"    {txn}")
    print(f"\n  Current Balance: Rs. {balance:,.2f}")


# --- Main Program ---
print("\n" + "=" * 45)
print("   🏧 WELCOME TO PYTHON ATM")
print("=" * 45)

# Initialize account details
account_pin = "1234"
account_balance = 50000.00
transaction_history = []
account_locked = False

# PIN Validation
print("\n  Please verify your identity.")
is_valid = validate_pin(account_pin)

if not is_valid:
    account_locked = True
    print("\n  🔒 ACCOUNT LOCKED!")
    print("  Your account has been locked due to 3 failed PIN attempts.")
    print("  Please visit the nearest branch to unlock your account.")
else:
    # ATM Operations
    while True:
        display_atm_menu()
        choice = input("  Enter your choice (1-6): ").strip()

        if choice == '1':
            check_balance(account_balance)
        elif choice == '2':
            account_balance = deposit_money(account_balance, transaction_history)
        elif choice == '3':
            account_balance = withdraw_money(account_balance, transaction_history)
        elif choice == '4':
            account_pin = change_pin(account_pin)
        elif choice == '5':
            mini_statement(transaction_history, account_balance)
        elif choice == '6':
            print(f"\n  💰 Final Balance: Rs. {account_balance:,.2f}")
            print("  Thank you for using Python ATM. Goodbye! 🏧")
            break
        else:
            print("  ❌ Invalid choice. Please enter 1-6.")

# --- Expected Output ---
# =============================================
#    🏧 WELCOME TO PYTHON ATM
# =============================================
#
#   Please verify your identity.
#   Enter your 4-digit PIN (3 attempt(s) left): 0000
#   ❌ Incorrect PIN. 2 attempt(s) remaining.
#   Enter your 4-digit PIN (2 attempt(s) left): 1234
#   ✅ PIN verified successfully!
#
# ========================================
#    ATM MENU
# ========================================
#   1. Check Balance
#   Enter your choice (1-6): 1
#   💰 Your Current Balance: Rs. 50,000.00
#
#   Enter your choice (1-6): 3
#   Enter withdrawal amount: Rs. 5000
#   ✅ Rs. 5,000.00 withdrawn successfully!
#   💰 Remaining Balance: Rs. 45,000.00
#
#   Enter your choice (1-6): 6
#   💰 Final Balance: Rs. 45,000.00
#   Thank you for using Python ATM. Goodbye! 🏧
