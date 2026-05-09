# Q3. Program to generate first N prime numbers using a for loop,
#     and calculate their sum and average.

def is_prime(number):
    """Check if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_primes(n):
    """Generate the first N prime numbers using a for loop."""
    prime_list = []
    current_number = 2  # Start checking from 2

    while len(prime_list) < n:
        # Use for loop to check primality
        if is_prime(current_number):
            prime_list.append(current_number)
        current_number += 1

    return prime_list


def calculate_sum_and_average(prime_list):
    """Calculate the sum and average of prime numbers."""
    prime_sum = 0
    for prime in prime_list:
        prime_sum += prime
    prime_average = prime_sum / len(prime_list)
    return prime_sum, prime_average


# --- Main Program ---
print("=" * 50)
print("   PRIME NUMBER GENERATOR")
print("=" * 50)

# Accept N from user
while True:
    try:
        n = int(input("\nEnter the value of N (number of primes to generate): "))
        if n > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Generate first N prime numbers
primes = generate_primes(n)

# Calculate sum and average
total_sum, average = calculate_sum_and_average(primes)

# Display the results
print(f"\nFirst {n} Prime Numbers:")
print(primes)

print(f"\nSum of first {n} prime numbers     : {total_sum}")
print(f"Average of first {n} prime numbers : {average:.2f}")

# --- Expected Output ---
# ==================================================
#    PRIME NUMBER GENERATOR
# ==================================================
#
# Enter the value of N (number of primes to generate): 10
#
# First 10 Prime Numbers:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
#
# Sum of first 10 prime numbers     : 129
# Average of first 10 prime numbers : 12.90
