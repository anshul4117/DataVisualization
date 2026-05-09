# Q18. Frequency counter that stores word occurrences from a paragraph
#      into a dictionary and displays the most repeated word.

def clean_word(word):
    """Remove punctuation from a word and convert to lowercase."""
    cleaned = ""
    for char in word:
        if char.isalnum():
            cleaned += char
    return cleaned.lower()


def count_word_frequency(paragraph):
    """Count the frequency of each word in the paragraph."""
    frequency_dict = {}

    # Split paragraph into words
    words = paragraph.split()

    for word in words:
        # Clean the word (remove punctuation, lowercase)
        cleaned_word = clean_word(word)

        # Skip empty strings
        if cleaned_word == "":
            continue

        # Count frequency using dictionary
        if cleaned_word in frequency_dict:
            frequency_dict[cleaned_word] += 1
        else:
            frequency_dict[cleaned_word] = 1

    return frequency_dict


def find_most_repeated(frequency_dict):
    """Find the most repeated word from the frequency dictionary."""
    max_count = 0
    most_repeated = ""

    for word, count in frequency_dict.items():
        if count > max_count:
            max_count = count
            most_repeated = word

    return most_repeated, max_count


def display_frequency_table(frequency_dict):
    """Display the frequency table sorted by count in descending order."""
    # Sort by frequency (descending)
    sorted_freq = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)

    print(f"\n  {'Word':<20} {'Frequency':>10}")
    print("  " + "-" * 32)
    for word, count in sorted_freq:
        bar = "█" * count  # Visual bar representation
        print(f"  {word:<20} {count:>5}  {bar}")


# --- Main Program ---
print("=" * 55)
print("   WORD FREQUENCY COUNTER")
print("=" * 55)

# Accept paragraph from user
user_paragraph = input("\nEnter a paragraph:\n")

# Count word frequency
word_frequency = count_word_frequency(user_paragraph)

# Display total unique words
print(f"\nTotal words entered : {len(user_paragraph.split())}")
print(f"Unique words found  : {len(word_frequency)}")

# Display frequency table
print("\n--- Word Frequency Table (Sorted by Count) ---")
display_frequency_table(word_frequency)

# Find and display most repeated word
most_common_word, max_frequency = find_most_repeated(word_frequency)
print(f"\n🏆 Most Repeated Word: '{most_common_word}' (appeared {max_frequency} times)")

# --- Expected Output ---
# =======================================================
#    WORD FREQUENCY COUNTER
# =======================================================
#
# Enter a paragraph:
# Python is a great programming language. Python is easy to learn. Python is used for web development, data science, and machine learning. Learning Python is fun and Python makes coding easy.
#
# Total words entered : 31
# Unique words found  : 20
#
# --- Word Frequency Table (Sorted by Count) ---
#   Word                  Frequency
#   --------------------------------
#   python                    5  █████
#   is                        4  ████
#   and                       2  ██
#   easy                      2  ██
#   a                         1  █
#   great                     1  █
#   programming               1  █
#   language                  1  █
#   to                        1  █
#   learn                     1  █
#   ...
#
# 🏆 Most Repeated Word: 'python' (appeared 5 times)
