# Q27. Create tuples containing student names and courses. Convert to
#      sets to identify students enrolled in multiple courses.

def create_student_course_tuples():
    """Create tuples of (student_name, course) from user input."""
    records = []
    try:
        num_records = int(input("Enter number of enrollment records: "))
    except ValueError:
        print("Invalid input. Using sample data instead.")
        # Return sample data if input fails
        return [
            ("Rahul", "Python"), ("Priya", "Java"), ("Amit", "Python"),
            ("Rahul", "Java"), ("Sneha", "C++"), ("Priya", "Python"),
            ("Vikram", "Java"), ("Amit", "C++"), ("Rahul", "C++"),
            ("Sneha", "Python"), ("Neha", "Java"), ("Vikram", "Python")
        ]

    for i in range(1, num_records + 1):
        print(f"\n  Record {i}:")
        name = input("    Student Name: ").strip()
        course = input("    Course Name : ").strip()
        records.append((name, course))

    return records


def find_multi_course_students(enrollment_tuples):
    """Find students enrolled in multiple courses using sets."""
    # Create a dictionary mapping student -> set of courses
    student_courses = {}

    for name, course in enrollment_tuples:
        if name not in student_courses:
            student_courses[name] = set()
        student_courses[name].add(course)

    # Filter students enrolled in more than one course
    multi_course = {}
    for student, courses in student_courses.items():
        if len(courses) > 1:
            multi_course[student] = courses

    return student_courses, multi_course


def find_common_courses(student_courses, student1, student2):
    """Find common courses between two students using set intersection."""
    if student1 in student_courses and student2 in student_courses:
        common = student_courses[student1] & student_courses[student2]
        return common
    return set()


# --- Main Program ---
print("=" * 60)
print("   STUDENT COURSE ENROLLMENT ANALYZER")
print("=" * 60)

# Create enrollment records as tuples
enrollment_records = create_student_course_tuples()

# Display all enrollment tuples
print("\n--- All Enrollment Records (Tuples) ---")
for record in enrollment_records:
    print(f"  {record}")

# Convert to sets and analyze
all_courses, multi_enrolled = find_multi_course_students(enrollment_records)

# Display student-wise courses (as sets)
print("\n" + "=" * 50)
print("   STUDENT-WISE COURSES (Sets)")
print("=" * 50)
for student, courses in all_courses.items():
    print(f"  {student:<12} : {courses}")

# Display students enrolled in multiple courses
print("\n" + "=" * 50)
print("   STUDENTS IN MULTIPLE COURSES")
print("=" * 50)
if multi_enrolled:
    for student, courses in multi_enrolled.items():
        print(f"  {student:<12} : {courses} ({len(courses)} courses)")
else:
    print("  No students enrolled in multiple courses.")

# Set operations: All unique courses
all_course_set = set()
for courses in all_courses.values():
    all_course_set = all_course_set | courses
print(f"\n  All Available Courses (Union): {all_course_set}")

# Find common courses between students
students_list = list(all_courses.keys())
if len(students_list) >= 2:
    s1, s2 = students_list[0], students_list[1]
    common = find_common_courses(all_courses, s1, s2)
    print(f"  Common courses between {s1} & {s2}: {common if common else 'None'}")

# --- Expected Output ---
# ============================================================
#    STUDENT COURSE ENROLLMENT ANALYZER
# ============================================================
# Enter number of enrollment records: abc
# Invalid input. Using sample data instead.
#
# --- All Enrollment Records (Tuples) ---
#   ('Rahul', 'Python')
#   ('Priya', 'Java')
#   ('Amit', 'Python')
#   ('Rahul', 'Java')
#   ...
#
# ==================================================
#    STUDENT-WISE COURSES (Sets)
# ==================================================
#   Rahul        : {'Python', 'Java', 'C++'}
#   Priya        : {'Java', 'Python'}
#   Amit         : {'Python', 'C++'}
#   ...
#
# ==================================================
#    STUDENTS IN MULTIPLE COURSES
# ==================================================
#   Rahul        : {'Python', 'Java', 'C++'} (3 courses)
#   Priya        : {'Java', 'Python'} (2 courses)
#   Amit         : {'Python', 'C++'} (2 courses)
#   Sneha        : {'C++', 'Python'} (2 courses)
#   Vikram       : {'Java', 'Python'} (2 courses)
#
#   All Available Courses (Union): {'Python', 'Java', 'C++'}
#   Common courses between Rahul & Priya: {'Python', 'Java'}
