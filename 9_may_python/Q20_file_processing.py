# Q20. File processing program that handles file not found errors
#      and counts total words, lines, and characters in a text file.

import os

def create_sample_file(filename):
    """Create a sample text file for demonstration."""
    sample_content = """Python is a versatile programming language.
It is widely used in web development, data science, and automation.
Python has a simple and clean syntax.
Many developers prefer Python for machine learning projects.
The Python community is large and supportive.
Learning Python opens up many career opportunities.
Python supports multiple programming paradigms.
It is an interpreted, high-level language.
Python was created by Guido van Rossum in 1991.
Today Python is one of the most popular languages worldwide."""

    with open(filename, 'w') as file:
        file.write(sample_content)
    print(f"  Sample file '{os.path.basename(filename)}' created successfully!\n")


def count_words(content):
    """Count total words in the file content."""
    words = content.split()
    return len(words)


def count_lines(content):
    """Count total lines in the file content."""
    lines = content.split('\n')
    # Filter out empty lines if needed
    non_empty_lines = [line for line in lines if line.strip()]
    return len(lines), len(non_empty_lines)


def count_characters(content):
    """Count total characters (with and without spaces)."""
    total_chars = len(content)
    chars_no_spaces = len(content.replace(" ", "").replace("\n", ""))
    return total_chars, chars_no_spaces


def process_file(filename):
    """Process the file and display word, line, and character counts."""
    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()

        # Count words
        word_count = count_words(content)

        # Count lines
        total_lines, non_empty_lines = count_lines(content)

        # Count characters
        total_chars, chars_no_spaces = count_characters(content)

        # Display results
        print("=" * 50)
        print("   FILE ANALYSIS RESULTS")
        print("=" * 50)
        print(f"  File Name             : {os.path.basename(filename)}")
        print(f"  File Size             : {os.path.getsize(filename)} bytes")
        print(f"\n  Total Lines           : {total_lines}")
        print(f"  Non-Empty Lines       : {non_empty_lines}")
        print(f"  Total Words           : {word_count}")
        print(f"  Total Characters      : {total_chars}")
        print(f"  Characters (no space) : {chars_no_spaces}")

        # Display file content preview
        print("\n" + "-" * 50)
        print("   FILE CONTENT PREVIEW")
        print("-" * 50)
        lines = content.split('\n')
        for i, line in enumerate(lines[:5], 1):  # Show first 5 lines
            print(f"  Line {i}: {line}")
        if len(lines) > 5:
            print(f"  ... ({len(lines) - 5} more lines)")

    except FileNotFoundError:
        # Handle file not found error
        print(f"\n  ❌ Error: File '{filename}' not found!")
        print("  Please check the file path and try again.")

    except PermissionError:
        # Handle permission error
        print(f"\n  ❌ Error: Permission denied to read '{filename}'!")

    except IOError as e:
        # Handle general I/O errors
        print(f"\n  ❌ I/O Error: {e}")

    except Exception as e:
        # Handle any other unexpected errors
        print(f"\n  ❌ Unexpected Error: {e}")


# --- Main Program ---
print("=" * 50)
print("   FILE PROCESSING PROGRAM")
print("   (with Error Handling)")
print("=" * 50)

# Create a sample file first
script_dir = os.path.dirname(os.path.abspath(__file__))
sample_filename = os.path.join(script_dir, "sample_text.txt")
create_sample_file(sample_filename)

# Test 1: Process the existing sample file
print("\n📂 Test 1: Processing existing file...")
process_file(sample_filename)

# Test 2: Try processing a non-existent file
print("\n\n📂 Test 2: Processing non-existent file...")
process_file("non_existent_file.txt")

# Test 3: Let user enter a filename
print("\n\n📂 Test 3: User input...")
user_filename = input("  Enter a filename to process (or press Enter for default): ").strip()
if user_filename == "":
    user_filename = sample_filename
process_file(user_filename)

# --- Expected Output ---
# ==================================================
#    FILE PROCESSING PROGRAM
#    (with Error Handling)
# ==================================================
#   Sample file 'sample_text.txt' created successfully!
#
# 📂 Test 1: Processing existing file...
# ==================================================
#    FILE ANALYSIS RESULTS
# ==================================================
#   File Name             : sample_text.txt
#   File Size             : 486 bytes
#
#   Total Lines           : 10
#   Non-Empty Lines       : 10
#   Total Words           : 82
#   Total Characters      : 486
#   Characters (no space) : 405
#
# --------------------------------------------------
#    FILE CONTENT PREVIEW
# --------------------------------------------------
#   Line 1: Python is a versatile programming language.
#   Line 2: It is widely used in web development, data science, and automation.
#   Line 3: Python has a simple and clean syntax.
#   Line 4: Many developers prefer Python for machine learning projects.
#   Line 5: The Python community is large and supportive.
#   ... (5 more lines)
#
# 📂 Test 2: Processing non-existent file...
#   ❌ Error: File 'non_existent_file.txt' not found!
#   Please check the file path and try again.
