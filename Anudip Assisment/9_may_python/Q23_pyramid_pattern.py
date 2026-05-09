# Q23. Print a pyramid pattern of numbers and calculate the sum
#      of all numbers printed in the pattern.

def print_pyramid_pattern(num_rows):
    """Print a pyramid pattern of numbers and return total sum."""
    total_sum = 0

    print(f"\n--- Number Pyramid Pattern (Rows: {num_rows}) ---\n")

    for i in range(1, num_rows + 1):
        # Print leading spaces for pyramid shape
        spaces = " " * ((num_rows - i) * 2)
        print(spaces, end="")

        # Print numbers in ascending order
        row_numbers = []
        for j in range(1, i + 1):
            row_numbers.append(j)
            total_sum += j

        # Print numbers in descending order (mirror)
        for j in range(i - 1, 0, -1):
            row_numbers.append(j)
            total_sum += j

        # Display the row
        print("  ".join(str(n) for n in row_numbers))

    return total_sum


def print_simple_number_pyramid(num_rows):
    """Print a simple number pyramid pattern."""
    total_sum = 0
    current_num = 1

    print(f"\n--- Sequential Number Pyramid (Rows: {num_rows}) ---\n")

    for i in range(1, num_rows + 1):
        # Print leading spaces
        spaces = " " * ((num_rows - i) * 3)
        print(spaces, end="")

        # Print numbers in the row
        row_nums = []
        for j in range(i):
            row_nums.append(current_num)
            total_sum += current_num
            current_num += 1

        print("   ".join(f"{n:>2}" for n in row_nums))

    return total_sum


# --- Main Program ---
print("=" * 50)
print("   PYRAMID NUMBER PATTERN GENERATOR")
print("=" * 50)

# Accept number of rows from user
while True:
    try:
        rows = int(input("\nEnter the number of rows: "))
        if rows > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Pattern 1: Diamond-style number pyramid
sum_pattern1 = print_pyramid_pattern(rows)
print(f"\nSum of all numbers in Pattern 1: {sum_pattern1}")

# Pattern 2: Sequential number pyramid
sum_pattern2 = print_simple_number_pyramid(rows)
print(f"\nSum of all numbers in Pattern 2: {sum_pattern2}")

# --- Expected Output ---
# ==================================================
#    PYRAMID NUMBER PATTERN GENERATOR
# ==================================================
#
# Enter the number of rows: 5
#
# --- Number Pyramid Pattern (Rows: 5) ---
#
#         1
#       1  2  1
#     1  2  3  2  1
#   1  2  3  4  3  2  1
# 1  2  3  4  5  4  3  2  1
#
# Sum of all numbers in Pattern 1: 55
#
# --- Sequential Number Pyramid (Rows: 5) ---
#
#              1
#           2   3
#        4   5   6
#     7   8   9  10
#  11  12  13  14  15
#
# Sum of all numbers in Pattern 2: 120
