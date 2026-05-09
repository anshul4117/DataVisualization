# Q37. Recursive function to calculate sum of digits and compare
#      with iterative approach.

import time

def sum_of_digits_recursive(number):
    """Calculate sum of digits using recursion."""
    # Base case: single digit number
    if number < 10:
        return number
    # Recursive case: last digit + sum of remaining digits
    return (number % 10) + sum_of_digits_recursive(number // 10)


def sum_of_digits_iterative(number):
    """Calculate sum of digits using iteration (loop)."""
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total


def trace_recursive(number, depth=0):
    """Show the recursive trace for educational purposes."""
    indent = "  " * depth
    if number < 10:
        print(f"{indent}  sum_of_digits({number}) = {number} (base case)")
        return number

    last_digit = number % 10
    remaining = number // 10
    print(f"{indent}  sum_of_digits({number}) = {last_digit} + sum_of_digits({remaining})")
    result = last_digit + trace_recursive(remaining, depth + 1)
    print(f"{indent}  = {result}")
    return result


# --- Main Program ---
print("=" * 60)
print("   SUM OF DIGITS: RECURSIVE vs ITERATIVE")
print("=" * 60)

while True:
    try:
        user_input = input("\nEnter a positive integer (or 'quit' to exit): ").strip()
        if user_input.lower() == 'quit':
            print("\n  Goodbye!")
            break

        number = int(user_input)
        if number < 0:
            number = abs(number)
            print(f"  Using absolute value: {number}")

    except ValueError:
        print("  ❌ Invalid input. Please enter a valid integer.")
        continue

    # Method 1: Recursive Approach
    print(f"\n--- Recursive Approach ---")
    start_time = time.perf_counter()
    recursive_result = sum_of_digits_recursive(number)
    recursive_time = time.perf_counter() - start_time

    # Show recursive trace for small numbers
    if number < 100000:
        print("  Trace:")
        trace_recursive(number)

    print(f"  Result: {recursive_result}")
    print(f"  Time  : {recursive_time:.8f} seconds")

    # Method 2: Iterative Approach
    print(f"\n--- Iterative Approach ---")
    start_time = time.perf_counter()
    iterative_result = sum_of_digits_iterative(number)
    iterative_time = time.perf_counter() - start_time

    print(f"  Steps:")
    temp = number
    steps = []
    while temp > 0:
        steps.append(str(temp % 10))
        temp //= 10
    steps.reverse()
    print(f"  {' + '.join(steps)} = {iterative_result}")
    print(f"  Result: {iterative_result}")
    print(f"  Time  : {iterative_time:.8f} seconds")

    # Comparison
    print(f"\n--- Comparison ---")
    print(f"  Number          : {number}")
    print(f"  Recursive Result: {recursive_result}")
    print(f"  Iterative Result: {iterative_result}")
    print(f"  Results Match   : {'✅ Yes' if recursive_result == iterative_result else '❌ No'}")
    print(f"  Recursive Time  : {recursive_time:.8f}s")
    print(f"  Iterative Time  : {iterative_time:.8f}s")

    if recursive_time > 0 and iterative_time > 0:
        if recursive_time < iterative_time:
            print(f"  Faster Method   : Recursive")
        else:
            print(f"  Faster Method   : Iterative")

# --- Expected Output ---
# ============================================================
#    SUM OF DIGITS: RECURSIVE vs ITERATIVE
# ============================================================
#
# Enter a positive integer (or 'quit' to exit): 12345
#
# --- Recursive Approach ---
#   Trace:
#   sum_of_digits(12345) = 5 + sum_of_digits(1234)
#     sum_of_digits(1234) = 4 + sum_of_digits(123)
#       sum_of_digits(123) = 3 + sum_of_digits(12)
#         sum_of_digits(12) = 2 + sum_of_digits(1)
#           sum_of_digits(1) = 1 (base case)
#         = 3
#       = 6
#     = 10
#   = 15
#   Result: 15
#   Time  : 0.00001200 seconds
#
# --- Iterative Approach ---
#   Steps:
#   1 + 2 + 3 + 4 + 5 = 15
#   Result: 15
#   Time  : 0.00000400 seconds
#
# --- Comparison ---
#   Number          : 12345
#   Recursive Result: 15
#   Iterative Result: 15
#   Results Match   : ✅ Yes
#   Faster Method   : Iterative
