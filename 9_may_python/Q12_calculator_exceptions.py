# Q12. Calculator program with exception handling for division by zero,
#      invalid inputs, and incorrect operations.

def add(num1, num2):
    """Perform addition."""
    return num1 + num2


def subtract(num1, num2):
    """Perform subtraction."""
    return num1 - num2


def multiply(num1, num2):
    """Perform multiplication."""
    return num1 * num2


def divide(num1, num2):
    """Perform division with zero check."""
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return num1 / num2


def modulus(num1, num2):
    """Perform modulus operation."""
    if num2 == 0:
        raise ZeroDivisionError("Cannot perform modulus with zero!")
    return num1 % num2


def power(num1, num2):
    """Perform exponentiation."""
    return num1 ** num2


def display_calculator_menu():
    """Display calculator menu."""
    print("\n" + "=" * 40)
    print("   CALCULATOR MENU")
    print("=" * 40)
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (/)")
    print("  5. Modulus (%)")
    print("  6. Power (**)")
    print("  7. Exit")
    print("=" * 40)


# --- Main Program ---
print("\n" + "=" * 40)
print("   PYTHON CALCULATOR")
print("   (with Exception Handling)")
print("=" * 40)

# Calculator loop
while True:
    display_calculator_menu()

    try:
        # Get user choice
        choice = input("  Enter your choice (1-7): ").strip()

        # Exit condition
        if choice == '7':
            print("\n  Thank you for using the Calculator. Goodbye!")
            break

        # Validate operation choice
        if choice not in ['1', '2', '3', '4', '5', '6']:
            raise ValueError(f"Invalid operation '{choice}'. Please choose 1-7.")

        # Get numbers from user
        try:
            first_number = float(input("  Enter first number: "))
        except ValueError:
            raise TypeError("Invalid input for first number. Please enter a numeric value.")

        try:
            second_number = float(input("  Enter second number: "))
        except ValueError:
            raise TypeError("Invalid input for second number. Please enter a numeric value.")

        # Perform the selected operation
        if choice == '1':
            result = add(first_number, second_number)
            operator = '+'
        elif choice == '2':
            result = subtract(first_number, second_number)
            operator = '-'
        elif choice == '3':
            result = multiply(first_number, second_number)
            operator = '*'
        elif choice == '4':
            result = divide(first_number, second_number)
            operator = '/'
        elif choice == '5':
            result = modulus(first_number, second_number)
            operator = '%'
        elif choice == '6':
            result = power(first_number, second_number)
            operator = '**'

        # Display the result
        print(f"\n  ✅ Result: {first_number} {operator} {second_number} = {result}")

    except ZeroDivisionError as zde:
        # Handle division by zero
        print(f"\n  ❌ Math Error: {zde}")

    except TypeError as te:
        # Handle invalid input types
        print(f"\n  ❌ Input Error: {te}")

    except ValueError as ve:
        # Handle incorrect operations
        print(f"\n  ❌ Operation Error: {ve}")

    except OverflowError:
        # Handle number too large
        print("\n  ❌ Overflow Error: Result is too large to compute.")

    except Exception as e:
        # Handle any other unexpected errors
        print(f"\n  ❌ Unexpected Error: {e}")

# --- Expected Output ---
# ========================================
#    PYTHON CALCULATOR
#    (with Exception Handling)
# ========================================
#
# ========================================
#    CALCULATOR MENU
# ========================================
#   1. Addition (+)
#   2. Subtraction (-)
#   3. Multiplication (*)
#   4. Division (/)
#   5. Modulus (%)
#   6. Power (**)
#   7. Exit
# ========================================
#   Enter your choice (1-7): 1
#   Enter first number: 25
#   Enter second number: 15
#
#   ✅ Result: 25.0 + 15.0 = 40.0
#
#   Enter your choice (1-7): 4
#   Enter first number: 10
#   Enter second number: 0
#
#   ❌ Math Error: Cannot divide by zero!
#
#   Enter your choice (1-7): 1
#   Enter first number: abc
#
#   ❌ Input Error: Invalid input for first number. Please enter a numeric value.
#
#   Enter your choice (1-7): 9
#
#   ❌ Operation Error: Invalid operation '9'. Please choose 1-7.
#
#   Enter your choice (1-7): 7
#   Thank you for using the Calculator. Goodbye!
