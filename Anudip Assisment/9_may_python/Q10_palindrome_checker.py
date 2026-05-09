# Q10. Check if a string is a palindrome after removing spaces,
#      punctuation marks, and converting to lowercase.

import string

def clean_string(input_string):
    """Remove spaces, punctuation and convert to lowercase."""
    cleaned = ""
    for char in input_string:
        # Keep only alphanumeric characters
        if char.isalnum():
            cleaned += char.lower()
    return cleaned


def is_palindrome(text):
    """Check if the cleaned text is a palindrome."""
    length = len(text)
    for i in range(length // 2):
        if text[i] != text[length - 1 - i]:
            return False
    return True


# --- Main Program ---
print("=" * 50)
print("   PALINDROME CHECKER")
print("=" * 50)

# Accept string from user
user_string = input("\nEnter a string: ")

# Clean the string
cleaned_string = clean_string(user_string)

# Check if palindrome
result = is_palindrome(cleaned_string)

# Display results
print(f"\nOriginal String  : '{user_string}'")
print(f"Cleaned String   : '{cleaned_string}'")
print(f"Reversed Cleaned : '{cleaned_string[::-1]}'")

if result:
    print(f"\n✅ '{user_string}' IS a palindrome!")
else:
    print(f"\n❌ '{user_string}' is NOT a palindrome.")

# Additional test cases for demonstration
print("\n" + "-" * 50)
print("   Additional Test Cases:")
print("-" * 50)
test_strings = [
    "A man, a plan, a canal: Panama",
    "race a car",
    "Was it a car or a cat I saw?",
    "hello world",
    "Madam, I'm Adam"
]

for test in test_strings:
    cleaned = clean_string(test)
    palindrome_check = is_palindrome(cleaned)
    status = "✅ Palindrome" if palindrome_check else "❌ Not Palindrome"
    print(f"  '{test}' -> {status}")

# --- Expected Output ---
# ==================================================
#    PALINDROME CHECKER
# ==================================================
#
# Enter a string: A man, a plan, a canal: Panama
#
# Original String  : 'A man, a plan, a canal: Panama'
# Cleaned String   : 'amanaplanacanalpanama'
# Reversed Cleaned : 'amanaplanacanalpanama'
#
# ✅ 'A man, a plan, a canal: Panama' IS a palindrome!
#
# --------------------------------------------------
#    Additional Test Cases:
# --------------------------------------------------
#   'A man, a plan, a canal: Panama' -> ✅ Palindrome
#   'race a car' -> ❌ Not Palindrome
#   'Was it a car or a cat I saw?' -> ✅ Palindrome
#   'hello world' -> ❌ Not Palindrome
#   'Madam, I'm Adam' -> ✅ Palindrome
