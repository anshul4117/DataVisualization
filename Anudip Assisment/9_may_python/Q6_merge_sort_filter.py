# Q6. Merge two lists, remove duplicates, sort in descending order,
#     and display numbers divisible by both 3 and 5.

def merge_lists(list1, list2):
    """Merge two lists into one."""
    merged = list1 + list2
    return merged


def remove_duplicates(input_list):
    """Remove duplicate values from the list."""
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


def sort_descending(input_list):
    """Sort the list in descending order using bubble sort (no built-in sort)."""
    sorted_list = input_list.copy()
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j] < sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    return sorted_list


def divisible_by_3_and_5(input_list):
    """Filter numbers divisible by both 3 and 5 (i.e., divisible by 15)."""
    result = []
    for num in input_list:
        if num % 3 == 0 and num % 5 == 0:
            result.append(num)
    return result


# --- Main Program ---
print("=" * 55)
print("   MERGE, DEDUPLICATE, SORT & FILTER PROGRAM")
print("=" * 55)

# Accept two lists from the user
input1 = input("\nEnter first list of integers (space-separated): ")
list_one = [int(x) for x in input1.split()]

input2 = input("Enter second list of integers (space-separated): ")
list_two = [int(x) for x in input2.split()]

print(f"\nList 1: {list_one}")
print(f"List 2: {list_two}")

# Step 1: Merge two lists
merged_list = merge_lists(list_one, list_two)
print(f"\nMerged List          : {merged_list}")

# Step 2: Remove duplicates
unique_list = remove_duplicates(merged_list)
print(f"After Removing Dupes : {unique_list}")

# Step 3: Sort in descending order
sorted_list = sort_descending(unique_list)
print(f"Sorted (Descending)  : {sorted_list}")

# Step 4: Filter numbers divisible by both 3 and 5
divisible_list = divisible_by_3_and_5(sorted_list)
if divisible_list:
    print(f"\nNumbers divisible by both 3 and 5: {divisible_list}")
else:
    print("\nNo numbers found that are divisible by both 3 and 5.")

# --- Expected Output ---
# =======================================================
#    MERGE, DEDUPLICATE, SORT & FILTER PROGRAM
# =======================================================
#
# Enter first list of integers (space-separated): 15 30 7 45 10 3
# Enter second list of integers (space-separated): 30 60 7 90 5 15
#
# List 1: [15, 30, 7, 45, 10, 3]
# List 2: [30, 60, 7, 90, 5, 15]
#
# Merged List          : [15, 30, 7, 45, 10, 3, 30, 60, 7, 90, 5, 15]
# After Removing Dupes : [15, 30, 7, 45, 10, 3, 60, 90, 5]
# Sorted (Descending)  : [90, 60, 45, 30, 15, 10, 7, 5, 3]
#
# Numbers divisible by both 3 and 5: [90, 60, 45, 30, 15]
