# Q11. Create a text file with student marks, read the file and display
#      the topper, average marks, and students scoring below average.

import os

def create_student_file(filename):
    """Create a text file containing student marks."""
    print("\n--- Creating Student Marks File ---")

    try:
        num_students = int(input("Enter the number of students: "))
    except ValueError:
        print("Invalid input. Using default 5 students.")
        num_students = 5

    with open(filename, 'w') as file:
        file.write("Name,Marks\n")  # Header line
        for i in range(1, num_students + 1):
            name = input(f"  Enter name of student {i}: ")
            while True:
                try:
                    marks = float(input(f"  Enter marks of {name}: "))
                    break
                except ValueError:
                    print("  Invalid marks. Enter a numeric value.")
            file.write(f"{name},{marks}\n")

    print(f"\nFile '{filename}' created successfully!")


def read_and_analyze(filename):
    """Read the file and analyze student marks."""
    students = []

    with open(filename, 'r') as file:
        # Skip header line
        header = file.readline()

        for line in file:
            line = line.strip()
            if line:  # Skip empty lines
                parts = line.split(',')
                name = parts[0]
                marks = float(parts[1])
                students.append((name, marks))

    return students


def find_topper(students):
    """Find the student with highest marks."""
    topper = students[0]
    for student in students:
        if student[1] > topper[1]:
            topper = student
    return topper


def calculate_average(students):
    """Calculate the average marks."""
    total = 0
    for student in students:
        total += student[1]
    return total / len(students)


def find_below_average(students, average):
    """Find students scoring below average."""
    below_avg = []
    for student in students:
        if student[1] < average:
            below_avg.append(student)
    return below_avg


# --- Main Program ---
print("=" * 55)
print("   STUDENT MARKS FILE ANALYZER")
print("=" * 55)

# Define the filename
marks_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "student_marks.txt")

# Create the student marks file
create_student_file(marks_filename)

# Read and analyze the file
student_records = read_and_analyze(marks_filename)

# Display all students
print("\n" + "=" * 40)
print("   ALL STUDENT RECORDS")
print("=" * 40)
print(f"  {'Name':<20} {'Marks':>8}")
print("  " + "-" * 30)
for name, marks in student_records:
    print(f"  {name:<20} {marks:>8.1f}")

# Find and display topper
topper_student = find_topper(student_records)
print(f"\n  🏆 Topper: {topper_student[0]} with {topper_student[1]:.1f} marks")

# Calculate and display average
avg_marks = calculate_average(student_records)
print(f"  📊 Average Marks: {avg_marks:.2f}")

# Find and display students below average
below_average_students = find_below_average(student_records, avg_marks)
print(f"\n  --- Students Scoring Below Average ({avg_marks:.2f}) ---")
if below_average_students:
    for name, marks in below_average_students:
        print(f"  {name:<20} {marks:>8.1f}")
else:
    print("  No students found below average.")

# --- Expected Output ---
# =======================================================
#    STUDENT MARKS FILE ANALYZER
# =======================================================
#
# --- Creating Student Marks File ---
# Enter the number of students: 5
#   Enter name of student 1: Rahul
#   Enter marks of Rahul: 85
#   Enter name of student 2: Priya
#   Enter marks of Priya: 92
#   Enter name of student 3: Amit
#   Enter marks of Amit: 67
#   Enter name of student 4: Sneha
#   Enter marks of Sneha: 78
#   Enter name of student 5: Vikram
#   Enter marks of Vikram: 55
#
# File 'student_marks.txt' created successfully!
#
# ========================================
#    ALL STUDENT RECORDS
# ========================================
#   Name                    Marks
#   ------------------------------
#   Rahul                    85.0
#   Priya                    92.0
#   Amit                     67.0
#   Sneha                    78.0
#   Vikram                   55.0
#
#   🏆 Topper: Priya with 92.0 marks
#   📊 Average Marks: 75.40
#
#   --- Students Scoring Below Average (75.40) ---
#   Amit                     67.0
#   Vikram                   55.0
