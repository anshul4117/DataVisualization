# Q17. Check whether numbers entered by the user are Armstrong numbers
#      using loops and conditional statements.

def count_digits(number):
    """Count the number of digits in a number."""
    count = 0
    temp = number
    while temp > 0:
        count += 1
        temp //= 10
    return count


def is_armstrong(number):
    """Check if a number is an Armstrong number.
    An Armstrong number is a number where the sum of its digits
    raised to the power of the number of digits equals the number itself.
    Example: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    """
    if number < 0:
        return False
    if number == 0:
        return True

    # Count the number of digits
    num_digits = count_digits(number)

    # Calculate sum of digits raised to power of num_digits
    digit_power_sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        digit_power_sum += digit ** num_digits
        temp //= 10

    return digit_power_sum == number


def find_armstrong_in_range(start, end):
    """Find all Armstrong numbers in a given range."""
    armstrong_list = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            armstrong_list.append(num)
    return armstrong_list


# --- Main Program ---
print("=" * 55)
print("   ARMSTRONG NUMBER CHECKER")
print("=" * 55)
print("\n  An Armstrong number is a number where the sum of")
print("  its digits raised to the power of the number of")
print("  digits equals the number itself.")
print("  Example: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153")

# Check individual numbers
print("\n" + "-" * 55)
print("  CHECK INDIVIDUAL NUMBERS")
print("-" * 55)

while True:
    try:
        user_input = input("\nEnter a number to check (or 'done' to stop): ")
        if user_input.lower() == 'done':
            break

        number_to_check = int(user_input)
        if is_armstrong(number_to_check):
            # Show the calculation
            num_digits = count_digits(number_to_check) if number_to_check > 0 else 1
            temp = number_to_check
            calculation_parts = []
            while temp > 0:
                digit = temp % 10
                calculation_parts.append(f"{digit}^{num_digits}")
                temp //= 10
            calculation_parts.reverse()
            calculation_str = " + ".join(calculation_parts)
            print(f"  ✅ {number_to_check} IS an Armstrong number!")
            if number_to_check > 0:
                print(f"     {number_to_check} = {calculation_str} = {number_to_check}")
        else:
            print(f"  ❌ {number_to_check} is NOT an Armstrong number.")

    except ValueError:
        print("  Invalid input. Please enter a valid integer.")

# Display Armstrong numbers in a range
print("\n" + "-" * 55)
print("  ARMSTRONG NUMBERS IN RANGE 0-9999")
print("-" * 55)
armstrong_numbers = find_armstrong_in_range(0, 9999)
print(f"  Found {len(armstrong_numbers)} Armstrong numbers:")
print(f"  {armstrong_numbers}")

# --- Expected Output ---
# =======================================================
#    ARMSTRONG NUMBER CHECKER
# =======================================================
#
#   An Armstrong number is a number where the sum of
#   its digits raised to the power of the number of
#   digits equals the number itself.
#   Example: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
#
# -------------------------------------------------------
#   CHECK INDIVIDUAL NUMBERS
# -------------------------------------------------------
#
# Enter a number to check (or 'done' to stop): 153
#   ✅ 153 IS an Armstrong number!
#      153 = 1^3 + 5^3 + 3^3 = 153
#
# Enter a number to check (or 'done' to stop): 370
#   ✅ 370 IS an Armstrong number!
#      370 = 3^3 + 7^3 + 0^3 = 370
#
# Enter a number to check (or 'done' to stop): 123
#   ❌ 123 is NOT an Armstrong number.
#
# Enter a number to check (or 'done' to stop): done
#
# -------------------------------------------------------
#   ARMSTRONG NUMBERS IN RANGE 0-9999
# -------------------------------------------------------
#   Found 12 Armstrong numbers:
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474]
