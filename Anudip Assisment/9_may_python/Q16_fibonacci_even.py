# Q16. Generate Fibonacci numbers up to N using functions and loops,
#      and store only even Fibonacci numbers in a list.

def generate_fibonacci(n):
    """Generate Fibonacci numbers up to N."""
    fibonacci_series = []

    # First two Fibonacci numbers
    first = 0
    second = 1

    # Generate Fibonacci numbers up to N
    while first <= n:
        fibonacci_series.append(first)
        # Calculate next Fibonacci number
        first, second = second, first + second

    return fibonacci_series


def filter_even_fibonacci(fib_list):
    """Filter and return only even Fibonacci numbers."""
    even_fibonacci = []
    for num in fib_list:
        if num % 2 == 0:
            even_fibonacci.append(num)
    return even_fibonacci


def display_results(n, fib_list, even_fib_list):
    """Display the Fibonacci series and even Fibonacci numbers."""
    print(f"\nAll Fibonacci numbers up to {n}:")
    print(f"  {fib_list}")
    print(f"  Count: {len(fib_list)}")

    print(f"\nEven Fibonacci numbers up to {n}:")
    print(f"  {even_fib_list}")
    print(f"  Count: {len(even_fib_list)}")

    if even_fib_list:
        print(f"  Sum of even Fibonacci numbers: {sum(even_fib_list)}")


# --- Main Program ---
print("=" * 50)
print("   FIBONACCI NUMBER GENERATOR")
print("=" * 50)

# Accept N from the user
while True:
    try:
        limit = int(input("\nEnter the value of N (upper limit): "))
        if limit >= 0:
            break
        else:
            print("Please enter a non-negative integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Generate Fibonacci series up to N
fibonacci_numbers = generate_fibonacci(limit)

# Filter even Fibonacci numbers
even_fibonacci_numbers = filter_even_fibonacci(fibonacci_numbers)

# Display results
display_results(limit, fibonacci_numbers, even_fibonacci_numbers)

# --- Expected Output ---
# ==================================================
#    FIBONACCI NUMBER GENERATOR
# ==================================================
#
# Enter the value of N (upper limit): 100
#
# All Fibonacci numbers up to 100:
#   [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   Count: 12
#
# Even Fibonacci numbers up to 100:
#   [0, 2, 8, 34]
#   Count: 4
#   Sum of even Fibonacci numbers: 44
