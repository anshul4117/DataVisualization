# Q1. Python program to analyze a paragraph and count uppercase, lowercase,
#     digits, spaces, and special characters. Display results in descending
#     order of frequency.

def analyze_paragraph(paragraph):
    """Accepts a paragraph and counts character categories."""
    # Initialize counters for each character category
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    space_count = 0
    special_count = 0

    # Iterate through each character in the paragraph
    for char in paragraph:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1
        else:
            special_count += 1

    # Store results in a dictionary for easy sorting
    frequency_map = {
        "Lowercase Letters": lowercase_count,
        "Uppercase Letters": uppercase_count,
        "Digits": digit_count,
        "Spaces": space_count,
        "Special Characters": special_count
    }

    # Sort dictionary by value in descending order
    sorted_frequency = sorted(frequency_map.items(), key=lambda item: item[1], reverse=True)

    return sorted_frequency


# --- Main Program ---
print("=" * 50)
print("   PARAGRAPH CHARACTER ANALYSIS")
print("=" * 50)

# Accept paragraph from the user
user_paragraph = input("\nEnter a paragraph: ")

# Analyze the paragraph
results = analyze_paragraph(user_paragraph)

# Display results in descending order of frequency
print("\n--- Character Frequency (Descending Order) ---")
print(f"{'Category':<25} {'Count':>6}")
print("-" * 35)
for category, count in results:
    print(f"{category:<25} {count:>6}")

print("\nTotal characters:", len(user_paragraph))

# --- Expected Output ---
# ==================================================
#    PARAGRAPH CHARACTER ANALYSIS
# ==================================================
#
# Enter a paragraph: Hello World! 123 Python is GREAT.
#
# --- Character Frequency (Descending Order) ---
# Category                   Count
# -----------------------------------
# Lowercase Letters             16
# Spaces                         5
# Uppercase Letters              7
# Digits                         3
# Special Characters             2
#
# Total characters: 33
