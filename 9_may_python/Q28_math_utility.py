# Q28. Menu-driven mathematical utility program using functions for
#      factorial, prime checking, and Armstrong number checking.

def calculate_factorial(n):
    """Calculate factorial of a number using loop."""
    if n < 0:
        return "Factorial not defined for negative numbers"
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    if n < 0:
        return False
    num_digits = len(str(n))
    digit_sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        digit_sum += digit ** num_digits
        temp //= 10
    return digit_sum == n


def display_menu():
    """Display the mathematical utility menu."""
    print("\n" + "=" * 45)
    print("   MATHEMATICAL UTILITY PROGRAM")
    print("=" * 45)
    print("  1. Calculate Factorial")
    print("  2. Check Prime Number")
    print("  3. Check Armstrong Number")
    print("  4. All Three Checks at Once")
    print("  5. Exit")
    print("=" * 45)


# --- Main Program ---
print("\n" + "=" * 45)
print("   WELCOME TO MATH UTILITY")
print("=" * 45)

while True:
    display_menu()
    choice = input("  Enter your choice (1-5): ").strip()

    if choice == '1':
        # Factorial
        try:
            num = int(input("  Enter a non-negative integer: "))
            result = calculate_factorial(num)
            print(f"\n  ✅ Factorial of {num} = {result}")
        except ValueError:
            print("  ❌ Invalid input. Please enter an integer.")

    elif choice == '2':
        # Prime Check
        try:
            num = int(input("  Enter a number: "))
            if is_prime(num):
                print(f"\n  ✅ {num} IS a prime number.")
            else:
                print(f"\n  ❌ {num} is NOT a prime number.")

            # Show primes up to that number
            if num > 2:
                primes_list = [i for i in range(2, num + 1) if is_prime(i)]
                print(f"  📌 Prime numbers up to {num}: {primes_list}")
        except ValueError:
            print("  ❌ Invalid input. Please enter an integer.")

    elif choice == '3':
        # Armstrong Check
        try:
            num = int(input("  Enter a number: "))
            if is_armstrong(num):
                digits = len(str(num))
                parts = [f"{d}^{digits}" for d in str(num)]
                print(f"\n  ✅ {num} IS an Armstrong number!")
                print(f"     {num} = {' + '.join(parts)} = {num}")
            else:
                print(f"\n  ❌ {num} is NOT an Armstrong number.")
        except ValueError:
            print("  ❌ Invalid input. Please enter an integer.")

    elif choice == '4':
        # All three checks
        try:
            num = int(input("  Enter a number: "))
            print(f"\n  --- Analysis of {num} ---")
            print(f"  Factorial  : {calculate_factorial(num) if num >= 0 else 'N/A (negative)'}")
            print(f"  Prime      : {'Yes ✅' if is_prime(num) else 'No ❌'}")
            print(f"  Armstrong  : {'Yes ✅' if is_armstrong(num) else 'No ❌'}")
        except ValueError:
            print("  ❌ Invalid input. Please enter an integer.")

    elif choice == '5':
        print("\n  Thank you for using Math Utility! Goodbye!")
        break

    else:
        print("  ❌ Invalid choice. Please enter 1-5.")

# --- Expected Output ---
# =============================================
#    WELCOME TO MATH UTILITY
# =============================================
#
# =============================================
#    MATHEMATICAL UTILITY PROGRAM
# =============================================
#   1. Calculate Factorial
#   2. Check Prime Number
#   3. Check Armstrong Number
#   4. All Three Checks at Once
#   5. Exit
# =============================================
#   Enter your choice (1-5): 1
#   Enter a non-negative integer: 5
#
#   ✅ Factorial of 5 = 120
#
#   Enter your choice (1-5): 2
#   Enter a number: 17
#
#   ✅ 17 IS a prime number.
#   📌 Prime numbers up to 17: [2, 3, 5, 7, 11, 13, 17]
#
#   Enter your choice (1-5): 3
#   Enter a number: 153
#
#   ✅ 153 IS an Armstrong number!
#      153 = 1^3 + 5^3 + 3^3 = 153
#
#   Enter your choice (1-5): 4
#   Enter a number: 7
#
#   --- Analysis of 7 ---
#   Factorial  : 5040
#   Prime      : Yes ✅
#   Armstrong  : No ❌
#
#   Enter your choice (1-5): 5
#   Thank you for using Math Utility! Goodbye!
