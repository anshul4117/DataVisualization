# Q24. Function for division of two numbers with exception handling
#      to validate inputs and avoid runtime errors.

def get_valid_number(prompt):
    """Get a valid numeric input from the user with error handling."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("  ❌ Invalid input! Please enter a numeric value.")


def divide_numbers(numerator, denominator):
    """Divide two numbers with proper exception handling."""
    try:
        # Check if denominator is zero
        if denominator == 0:
            raise ZeroDivisionError("Division by zero is not allowed!")

        # Check for very large results
        result = numerator / denominator

        # Check for infinity
        if result == float('inf') or result == float('-inf'):
            raise OverflowError("Result is too large (infinity).")

        return result

    except ZeroDivisionError as zde:
        print(f"  ❌ ZeroDivisionError: {zde}")
        return None

    except OverflowError as oe:
        print(f"  ❌ OverflowError: {oe}")
        return None

    except TypeError as te:
        print(f"  ❌ TypeError: {te}")
        return None

    except Exception as e:
        print(f"  ❌ Unexpected Error: {e}")
        return None


# --- Main Program ---
print("=" * 50)
print("   DIVISION CALCULATOR")
print("   (with Exception Handling)")
print("=" * 50)

while True:
    print("\n" + "-" * 40)

    # Get numerator with validation
    num1 = get_valid_number("  Enter the numerator: ")

    # Get denominator with validation
    num2 = get_valid_number("  Enter the denominator: ")

    # Perform division
    result = divide_numbers(num1, num2)

    # Display result
    if result is not None:
        print(f"\n  ✅ {num1} / {num2} = {result:.4f}")

        # Show integer division and remainder as well
        if num2 != 0:
            int_div = int(num1 // num2)
            remainder = num1 % num2
            print(f"  📌 Integer Division: {num1} // {num2} = {int_div}")
            print(f"  📌 Remainder       : {num1} %  {num2} = {remainder:.4f}")

    # Ask to continue
    again = input("\n  Perform another division? (yes/no): ").strip().lower()
    if again not in ['yes', 'y']:
        print("\n  Thank you! Exiting the Division Calculator.")
        break

# --- Expected Output ---
# ==================================================
#    DIVISION CALCULATOR
#    (with Exception Handling)
# ==================================================
#
# ----------------------------------------
#   Enter the numerator: 100
#   Enter the denominator: 3
#
#   ✅ 100.0 / 3.0 = 33.3333
#   📌 Integer Division: 100.0 // 3.0 = 33
#   📌 Remainder       : 100.0 %  3.0 = 1.0000
#
#   Perform another division? (yes/no): yes
#
# ----------------------------------------
#   Enter the numerator: 50
#   Enter the denominator: 0
#   ❌ ZeroDivisionError: Division by zero is not allowed!
#
#   Perform another division? (yes/no): yes
#
# ----------------------------------------
#   Enter the numerator: abc
#   ❌ Invalid input! Please enter a numeric value.
#   Enter the numerator: 25
#   Enter the denominator: 5
#
#   ✅ 25.0 / 5.0 = 5.0000
#
#   Perform another division? (yes/no): no
#   Thank you! Exiting the Division Calculator.
