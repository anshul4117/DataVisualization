# Q8. Perform union, intersection, symmetric difference, and subset
#     operations on two sets entered by the user.

def get_set_from_user(set_name):
    """Accept a set of integers from the user."""
    user_input = input(f"Enter elements for {set_name} (space-separated integers): ")
    user_set = set(int(x) for x in user_input.split())
    return user_set


def perform_union(set_a, set_b):
    """Perform union of two sets."""
    return set_a | set_b


def perform_intersection(set_a, set_b):
    """Perform intersection of two sets."""
    return set_a & set_b


def perform_symmetric_difference(set_a, set_b):
    """Perform symmetric difference of two sets."""
    return set_a ^ set_b


def check_subset(set_a, set_b):
    """Check if one set is a subset of the other."""
    a_subset_b = set_a.issubset(set_b)
    b_subset_a = set_b.issubset(set_a)
    return a_subset_b, b_subset_a


# --- Main Program ---
print("=" * 55)
print("   SET OPERATIONS PROGRAM")
print("=" * 55)

# Accept two sets from the user
set_one = get_set_from_user("Set A")
set_two = get_set_from_user("Set B")

print(f"\nSet A: {set_one}")
print(f"Set B: {set_two}")

# Perform set operations
print("\n" + "-" * 45)

# 1. Union
union_result = perform_union(set_one, set_two)
print(f"Union (A ∪ B)              : {union_result}")

# 2. Intersection
intersection_result = perform_intersection(set_one, set_two)
print(f"Intersection (A ∩ B)       : {intersection_result}")

# 3. Symmetric Difference
sym_diff_result = perform_symmetric_difference(set_one, set_two)
print(f"Symmetric Difference (A △ B): {sym_diff_result}")

# 4. Difference
diff_a_b = set_one - set_two
diff_b_a = set_two - set_one
print(f"Difference (A - B)         : {diff_a_b}")
print(f"Difference (B - A)         : {diff_b_a}")

# 5. Subset check
is_a_subset_b, is_b_subset_a = check_subset(set_one, set_two)
print(f"\nIs A a subset of B?        : {is_a_subset_b}")
print(f"Is B a subset of A?        : {is_b_subset_a}")

# --- Expected Output ---
# =======================================================
#    SET OPERATIONS PROGRAM
# =======================================================
# Enter elements for Set A (space-separated integers): 1 2 3 4 5
# Enter elements for Set B (space-separated integers): 3 4 5 6 7
#
# Set A: {1, 2, 3, 4, 5}
# Set B: {3, 4, 5, 6, 7}
#
# ---------------------------------------------
# Union (A ∪ B)              : {1, 2, 3, 4, 5, 6, 7}
# Intersection (A ∩ B)       : {3, 4, 5}
# Symmetric Difference (A △ B): {1, 2, 6, 7}
# Difference (A - B)         : {1, 2}
# Difference (B - A)         : {6, 7}
#
# Is A a subset of B?        : False
# Is B a subset of A?        : False
