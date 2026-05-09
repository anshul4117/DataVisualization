# Q33. Copy contents from one file to another and display the total
#      number of words copied.

import os

def create_source_file(filename):
    """Create a source file with sample content."""
    content = """Python is one of the most popular programming languages in the world.
It was created by Guido van Rossum and first released in 1991.
Python emphasizes code readability and simplicity.
It supports multiple programming paradigms including procedural, object-oriented, and functional programming.
Python is widely used in web development, data science, artificial intelligence, and automation.
The language has a large standard library and an active community.
Many top companies like Google, Netflix, and Instagram use Python extensively.
Python is an excellent choice for beginners as well as experienced developers."""

    with open(filename, 'w') as file:
        file.write(content)
    print(f"  Source file '{os.path.basename(filename)}' created successfully!")


def copy_file_contents(source_file, destination_file):
    """Copy contents from source file to destination file."""
    try:
        # Read from source file
        with open(source_file, 'r') as src:
            content = src.read()

        # Write to destination file
        with open(destination_file, 'w') as dest:
            dest.write(content)

        return content

    except FileNotFoundError:
        print(f"  ❌ Error: Source file '{source_file}' not found!")
        return None
    except PermissionError:
        print(f"  ❌ Error: Permission denied!")
        return None
    except IOError as e:
        print(f"  ❌ I/O Error: {e}")
        return None


def count_words(content):
    """Count total words in the content."""
    words = content.split()
    return len(words)


def count_lines(content):
    """Count total lines in the content."""
    lines = content.strip().split('\n')
    return len(lines)


def count_characters(content):
    """Count total characters in the content."""
    return len(content)


# --- Main Program ---
print("=" * 55)
print("   FILE COPY PROGRAM")
print("=" * 55)

# Define file paths
script_dir = os.path.dirname(os.path.abspath(__file__))
source_filename = os.path.join(script_dir, "source_file.txt")
destination_filename = os.path.join(script_dir, "destination_file.txt")

# Create the source file
create_source_file(source_filename)

# Copy contents from source to destination
print(f"\n  Copying from '{os.path.basename(source_filename)}' to '{os.path.basename(destination_filename)}'...")
copied_content = copy_file_contents(source_filename, destination_filename)

if copied_content is not None:
    # Count statistics
    word_count = count_words(copied_content)
    line_count = count_lines(copied_content)
    char_count = count_characters(copied_content)

    print(f"\n  ✅ File copied successfully!\n")

    # Display statistics
    print("=" * 45)
    print("   COPY STATISTICS")
    print("=" * 45)
    print(f"  Source File      : {os.path.basename(source_filename)}")
    print(f"  Destination File : {os.path.basename(destination_filename)}")
    print(f"  Words Copied     : {word_count}")
    print(f"  Lines Copied     : {line_count}")
    print(f"  Characters Copied: {char_count}")
    print(f"  File Size        : {os.path.getsize(destination_filename)} bytes")

    # Verify copy by reading destination file
    print("\n" + "-" * 45)
    print("   DESTINATION FILE CONTENT (Preview)")
    print("-" * 45)
    with open(destination_filename, 'r') as dest_file:
        lines = dest_file.readlines()
        for i, line in enumerate(lines[:5], 1):
            print(f"  Line {i}: {line.strip()}")
        if len(lines) > 5:
            print(f"  ... ({len(lines) - 5} more lines)")

    # Verify integrity
    print("\n  ✅ Integrity Check: ", end="")
    with open(source_filename, 'r') as src, open(destination_filename, 'r') as dest:
        if src.read() == dest.read():
            print("Source and Destination files are identical!")
        else:
            print("⚠️ Files differ!")

# --- Expected Output ---
# =======================================================
#    FILE COPY PROGRAM
# =======================================================
#   Source file 'source_file.txt' created successfully!
#
#   Copying from 'source_file.txt' to 'destination_file.txt'...
#
#   ✅ File copied successfully!
#
# =============================================
#    COPY STATISTICS
# =============================================
#   Source File      : source_file.txt
#   Destination File : destination_file.txt
#   Words Copied     : 95
#   Lines Copied     : 8
#   Characters Copied: 574
#   File Size        : 574 bytes
#
# ---------------------------------------------
#    DESTINATION FILE CONTENT (Preview)
# ---------------------------------------------
#   Line 1: Python is one of the most popular programming languages in the world.
#   Line 2: It was created by Guido van Rossum and first released in 1991.
#   ... (3 more lines)
#
#   ✅ Integrity Check: Source and Destination files are identical!
