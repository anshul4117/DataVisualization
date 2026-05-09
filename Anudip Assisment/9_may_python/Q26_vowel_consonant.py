# Q26. Separate vowels and consonants from a sentence and store
#      them in different lists.

def separate_vowels_consonants(sentence):
    """Separate vowels and consonants from a sentence into two lists."""
    vowel_set = "aeiouAEIOU"
    vowel_list = []
    consonant_list = []

    for char in sentence:
        if char.isalpha():  # Only process alphabetic characters
            if char in vowel_set:
                vowel_list.append(char)
            else:
                consonant_list.append(char)

    return vowel_list, consonant_list


def count_unique(char_list):
    """Count unique characters in a list."""
    unique = []
    for ch in char_list:
        if ch.lower() not in [u.lower() for u in unique]:
            unique.append(ch)
    return unique


# --- Main Program ---
print("=" * 55)
print("   VOWEL & CONSONANT SEPARATOR")
print("=" * 55)

# Accept sentence from the user
user_sentence = input("\nEnter a sentence: ")

# Separate vowels and consonants
vowels, consonants = separate_vowels_consonants(user_sentence)

# Display results
print(f"\nOriginal Sentence: '{user_sentence}'")

print(f"\n--- Vowels Found ---")
print(f"  List      : {vowels}")
print(f"  Count     : {len(vowels)}")
unique_vowels = count_unique(vowels)
print(f"  Unique    : {[v.lower() for v in unique_vowels]}")

print(f"\n--- Consonants Found ---")
print(f"  List      : {consonants}")
print(f"  Count     : {len(consonants)}")
unique_consonants = count_unique(consonants)
print(f"  Unique    : {[c.lower() for c in unique_consonants]}")

# Display frequency of each vowel
print("\n--- Vowel Frequency ---")
for v in "aeiou":
    count = sum(1 for ch in vowels if ch.lower() == v)
    if count > 0:
        print(f"  '{v}' : {count}")

# Display frequency of each consonant
print("\n--- Consonant Frequency ---")
for c_char in unique_consonants:
    count = sum(1 for ch in consonants if ch.lower() == c_char.lower())
    print(f"  '{c_char.lower()}' : {count}")

# --- Expected Output ---
# =======================================================
#    VOWEL & CONSONANT SEPARATOR
# =======================================================
#
# Enter a sentence: Python Programming is Fun and Easy
#
# Original Sentence: 'Python Programming is Fun and Easy'
#
# --- Vowels Found ---
#   List      : ['o', 'o', 'a', 'i', 'i', 'a', 'u', 'a', 'E', 'a']
#   Count     : 10
#   Unique    : ['o', 'a', 'i', 'u', 'e']
#
# --- Consonants Found ---
#   List      : ['P', 'y', 't', 'h', 'n', 'P', 'r', 'g', 'r', 'm', 'm', 'n', 'g', 's', 'F', 'n', 'n', 'd', 's', 'y']
#   Count     : 20
#   Unique    : ['p', 'y', 't', 'h', 'n', 'r', 'g', 'm', 's', 'f', 'd']
#
# --- Vowel Frequency ---
#   'a' : 4
#   'e' : 1
#   'i' : 2
#   'o' : 2
#   'u' : 1
#
# --- Consonant Frequency ---
#   'p' : 2
#   'y' : 2
#   't' : 1
#   ...
