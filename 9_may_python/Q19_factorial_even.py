# Q19. Function that accepts a list of integers and returns a new list
#      containing factorial of only even numbers.

def calculate_factorial(number):
    """Calculate the factorial of a given number using a loop."""
    if number == 0 or number == 1:
        return 1

    factorial_result = 1
    for i in range(2, number + 1):
        factorial_result *= i
    return factorial_result


def factorial_of_evens(integer_list):
    """Accept a list of integers and return factorials of even numbers."""
    even_factorial_list = []

    for num in integer_list:
        # Check if the number is even
        if num % 2 == 0:
            fact = calculate_factorial(num)
            even_factorial_list.append((num, fact))

    return even_factorial_list


def get_integer_list():
    """Accept a list of integers from the user."""
    while True:
        try:
            user_input = input("Enter integers separated by spaces: ")
            int_list = [int(x) for x in user_input.split()]
            if len(int_list) == 0:
                print("Please enter at least one integer.")
                continue
            return int_list
        except ValueError:
            print("Invalid input. Please enter valid integers.")


# --- Main Program ---
print("=" * 55)
print("   FACTORIAL OF EVEN NUMBERS")
print("=" * 55)

# Accept list of integers from user
numbers_list = get_integer_list()

print(f"\nInput List: {numbers_list}")

# Separate even and odd numbers for display
even_numbers = [n for n in numbers_list if n % 2 == 0]
odd_numbers = [n for n in numbers_list if n % 2 != 0]

print(f"Even Numbers: {even_numbers}")
print(f"Odd Numbers (skipped): {odd_numbers}")

# Calculate factorials of even numbers
result = factorial_of_evens(numbers_list)

# Display results
print(f"\n--- Factorials of Even Numbers ---")
print(f"  {'Number':>8}  {'Factorial':>15}")
print("  " + "-" * 28)
for number, factorial in result:
    print(f"  {number:>8}  {factorial:>15}")

# Extract just the factorial values
factorial_values = [fact for _, fact in result]
print(f"\nFactorial List: {factorial_values}")

# --- Expected Output ---
# =======================================================
#    FACTORIAL OF EVEN NUMBERS
# =======================================================
# Enter integers separated by spaces: 1 2 3 4 5 6 7 8
#
# Input List: [1, 2, 3, 4, 5, 6, 7, 8]
# Even Numbers: [2, 4, 6, 8]
# Odd Numbers (skipped): [1, 3, 5, 7]
#
# --- Factorials of Even Numbers ---
#     Number        Factorial
#   ----------------------------
#          2                2
#          4               24
#          6              720
#          8            40320
#
# Factorial List: [2, 24, 720, 40320]
