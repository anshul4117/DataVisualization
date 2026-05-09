# Q5. Function to find the second largest and second smallest elements
#     from a list of integers without using built-in sorting functions.

def find_second_largest(numbers):
    """Find the second largest element without using built-in sort."""
    # Initialize largest and second_largest
    largest = numbers[0]
    second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return None  # All elements are the same
    return second_largest


def find_second_smallest(numbers):
    """Find the second smallest element without using built-in sort."""
    # Initialize smallest and second_smallest
    smallest = numbers[0]
    second_smallest = float('inf')

    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    if second_smallest == float('inf'):
        return None  # All elements are the same
    return second_smallest


def get_integer_list():
    """Accept a list of integers from the user."""
    while True:
        try:
            user_input = input("Enter integers separated by spaces: ")
            int_list = [int(x) for x in user_input.split()]
            if len(int_list) < 2:
                print("Please enter at least 2 integers.")
                continue
            return int_list
        except ValueError:
            print("Invalid input. Please enter valid integers.")


# --- Main Program ---
print("=" * 50)
print("   SECOND LARGEST & SECOND SMALLEST FINDER")
print("=" * 50)

# Accept list of integers from user
integer_list = get_integer_list()

print(f"\nInput List: {integer_list}")

# Find second largest
second_max = find_second_largest(integer_list)
if second_max is not None:
    print(f"Second Largest Element  : {second_max}")
else:
    print("Second Largest Element  : Not found (all elements are same)")

# Find second smallest
second_min = find_second_smallest(integer_list)
if second_min is not None:
    print(f"Second Smallest Element : {second_min}")
else:
    print("Second Smallest Element : Not found (all elements are same)")

# --- Expected Output ---
# ==================================================
#    SECOND LARGEST & SECOND SMALLEST FINDER
# ==================================================
# Enter integers separated by spaces: 12 45 7 23 89 56 3 67
#
# Input List: [12, 45, 7, 23, 89, 56, 3, 67]
# Second Largest Element  : 67
# Second Smallest Element : 7
