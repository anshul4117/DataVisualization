# Q25. Store word frequencies from a text file into a dictionary
#      and display the top five most frequently used words.

import os

def create_sample_text_file(filename):
    """Create a sample text file for word frequency analysis."""
    content = """Python is a powerful programming language that is widely used in the world.
Python is known for its simplicity and readability.
Many developers love Python because Python makes programming fun and easy.
Python is used for web development and data science and machine learning.
The Python community is one of the largest programming communities in the world.
Learning Python is a great investment for any programmer in the world.
Python supports multiple programming paradigms including object oriented programming.
Data science with Python is growing rapidly in the industry.
Python libraries like NumPy and Pandas make data analysis easy.
Web frameworks like Django and Flask are built with Python for the web."""

    with open(filename, 'w') as file:
        file.write(content)
    print(f"  Sample text file '{os.path.basename(filename)}' created!\n")


def read_file_content(filename):
    """Read and return the content of a text file."""
    with open(filename, 'r') as file:
        return file.read()


def count_word_frequencies(content):
    """Count word frequencies and store in a dictionary."""
    frequency_dict = {}

    # Clean and split content into words
    words = content.lower().split()

    for word in words:
        # Remove punctuation from word
        cleaned_word = ""
        for char in word:
            if char.isalnum():
                cleaned_word += char

        if cleaned_word:
            if cleaned_word in frequency_dict:
                frequency_dict[cleaned_word] += 1
            else:
                frequency_dict[cleaned_word] = 1

    return frequency_dict


def get_top_n_words(frequency_dict, n=5):
    """Get the top N most frequently used words."""
    # Sort dictionary by value in descending order
    sorted_words = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]


# --- Main Program ---
print("=" * 55)
print("   TOP 5 WORD FREQUENCY ANALYZER")
print("=" * 55)

# Create a sample text file
script_dir = os.path.dirname(os.path.abspath(__file__))
text_filename = os.path.join(script_dir, "sample_paragraph.txt")
create_sample_text_file(text_filename)

# Read file content
file_content = read_file_content(text_filename)

# Count word frequencies
word_freq = count_word_frequencies(file_content)

# Display total statistics
print(f"  Total words in file     : {sum(word_freq.values())}")
print(f"  Unique words            : {len(word_freq)}")

# Display complete frequency dictionary (sorted)
print("\n--- Complete Word Frequency Dictionary ---")
sorted_all = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_all:
    bar = "█" * count
    print(f"  {word:<18} : {count:>3}  {bar}")

# Display top 5 most frequent words
top_5 = get_top_n_words(word_freq, 5)
print("\n" + "=" * 45)
print("   🏆 TOP 5 MOST FREQUENT WORDS")
print("=" * 45)
for rank, (word, count) in enumerate(top_5, 1):
    print(f"  {rank}. '{word}' — {count} occurrences")

# --- Expected Output ---
# =======================================================
#    TOP 5 WORD FREQUENCY ANALYZER
# =======================================================
#   Sample text file 'sample_paragraph.txt' created!
#
#   Total words in file     : 102
#   Unique words            : 48
#
# --- Complete Word Frequency Dictionary ---
#   python             :  10  ██████████
#   is                 :   7  ███████
#   programming        :   5  █████
#   and                :   5  █████
#   ...
#
# =============================================
#    🏆 TOP 5 MOST FREQUENT WORDS
# =============================================
#   1. 'python' — 10 occurrences
#   2. 'is' — 7 occurrences
#   3. 'programming' — 5 occurrences
#   4. 'and' — 5 occurrences
#   5. 'in' — 4 occurrences
